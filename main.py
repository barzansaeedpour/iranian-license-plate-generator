import argparse
import json
import os
import random
from typing import List, Tuple

import cv2
import numpy as np
from PIL import Image

from remove_background import remove_background


# ============================================================
# CLI
# ============================================================
def parse_args():
    parser = argparse.ArgumentParser("Synthetic License Plate Generator")

    # Dataset
    parser.add_argument("--num-images", type=int, default=10)
    parser.add_argument("--output-dir", type=str, default="output")
    parser.add_argument("--config", type=str, default="config.json")
    parser.add_argument("--seed", type=int, default=None)

    # Perspective
    parser.add_argument("--perspective-prob", type=float, default=1.0)
    parser.add_argument("--perspective-max-offset", type=float, default=0.08)

    # Rotation / Shear
    parser.add_argument("--rotate-prob", type=float, default=0.7)
    parser.add_argument("--rotate-max-deg", type=float, default=7.0)
    parser.add_argument("--shear-max", type=float, default=0.08)

    # Motion blur
    parser.add_argument("--motion-blur-prob", type=float, default=0.6)
    parser.add_argument("--motion-blur-kernels", nargs="+", type=int, default=[3, 5, 7])

    # Illumination
    parser.add_argument("--illumination-alpha-min", type=float, default=0.8)
    parser.add_argument("--illumination-alpha-max", type=float, default=1.3)
    parser.add_argument("--illumination-beta-min", type=int, default=-25)
    parser.add_argument("--illumination-beta-max", type=int, default=25)

    return parser.parse_args()


# ============================================================
# Utils
# ============================================================
def generate_yolo_yaml(output_dir: str, class_names: list):
    """
    Generate YOLO-compatible data.yaml file.
    """
    yaml_path = os.path.join(output_dir, "data.yaml")

    with open(yaml_path, "w") as f:
        f.write(f"path: {output_dir}\n")
        f.write("train: images\n")
        f.write("val: images\n\n")

        f.write(f"nc: {len(class_names)}\n\n")
        f.write("names:\n")

        for i, name in enumerate(class_names):
            f.write(f"  {i}: '{name}'\n")

    print(f"[INFO] YOLO data.yaml generated at: {yaml_path}")

def load_config(path):
    with open(path) as f:
        return json.load(f)


def yolo_line(box, iw, ih):
    x, y, w, h, cls = box
    return f"{cls} {(x+w/2)/iw:.6f} {(y+h/2)/ih:.6f} {w/iw:.6f} {h/ih:.6f}"


def transform_boxes_affine(boxes, M):
    new_boxes = []

    for (x, y, w, h, cls) in boxes:
        pts = np.float32([
            [x, y],
            [x + w, y],
            [x + w, y + h],
            [x, y + h]
        ]).reshape(-1, 1, 2)

        tpts = cv2.transform(pts, M)
        xs, ys = tpts[:, 0, 0], tpts[:, 0, 1]

        nx, ny = xs.min(), ys.min()
        nw, nh = xs.max() - nx, ys.max() - ny

        new_boxes.append((nx, ny, nw, nh, cls))

    return new_boxes


# ============================================================
# Augmentations
# ============================================================
def perspective_warp(img, boxes, max_offset):
    h, w = img.shape[:2]

    src = np.float32([[0, 0], [w, 0], [w, h], [0, h]])
    dst = src.copy()

    for i in range(4):
        dst[i][0] += random.uniform(-max_offset, max_offset) * w
        dst[i][1] += random.uniform(-max_offset, max_offset) * h

    M = cv2.getPerspectiveTransform(src, dst)
    warped = cv2.warpPerspective(img, M, (w, h), borderValue=(0, 0, 0, 0))

    new_boxes = []
    for (x, y, bw, bh, cls) in boxes:
        pts = np.float32([
            [x, y],
            [x + bw, y],
            [x + bw, y + bh],
            [x, y + bh]
        ]).reshape(-1, 1, 2)

        tpts = cv2.perspectiveTransform(pts, M)
        xs, ys = tpts[:, 0, 0], tpts[:, 0, 1]
        nx, ny = xs.min(), ys.min()
        nw, nh = xs.max() - nx, ys.max() - ny
        new_boxes.append((nx, ny, nw, nh, cls))

    return warped, new_boxes


def rotate_and_shear(img, boxes, max_deg, max_shear):
    h, w = img.shape[:2]
    angle = random.uniform(-max_deg, max_deg)
    shear = random.uniform(-max_shear, max_shear)

    M_rot = cv2.getRotationMatrix2D((w / 2, h / 2), angle, 1.0)
    M_rot[0, 1] += shear

    img = cv2.warpAffine(img, M_rot, (w, h), borderValue=(0, 0, 0, 0))
    boxes = transform_boxes_affine(boxes, M_rot)

    return img, boxes


def motion_blur(img, kernels):
    k = random.choice(kernels)
    kernel = np.zeros((k, k))
    kernel[k // 2, :] = 1.0
    kernel /= k
    return cv2.filter2D(img, -1, kernel)


def illumination(img, amin, amax, bmin, bmax):
    alpha = random.uniform(amin, amax)
    beta = random.randint(bmin, bmax)
    return cv2.convertScaleAbs(img, alpha=alpha, beta=beta)


# ============================================================
# Generation
# ============================================================
def generate_plate(i, args, numbers, mini_numbers, chars, class_map, img_dir, lbl_dir):
    r = [random.choice(numbers) for _ in range(5)]
    rc = random.choice(chars)
    m1 = random.choice([m for m in mini_numbers if m["ch"] != "0"])
    m2 = random.choice(mini_numbers)

    plate_text = f"{r[0]['ch']}{r[1]['ch']}-{rc['ch']}-{r[2]['ch']}{r[3]['ch']}{r[4]['ch']}-{m1['ch']}{m2['ch']}"

    char_color = "white" if rc["ch"] in ["P", "TH", "A", "Z"] else "black"

    template_map = {
        "T": "taxi.png",
        "EIN": "taxi.png",
        "P": "police.png",
        "TH": "police.png",
        "A": "gov.png",
        "Z": "blue.png",
        "SH": "artesh.png",
    }

    bg = Image.open(f"templates/{template_map.get(rc['ch'], 'savari.png')}").convert("RGBA")
    fg = Image.new("RGBA", bg.size)
    boxes = []

    def paste(ch, size, pos):
        img = remove_background(Image.open(f"chars/{ch}.png"), char_color)
        img = img.resize(size)
        fg.paste(img, pos, img)
        boxes.append((pos[0], pos[1], size[0], size[1], class_map[ch]))

    paste(r[0]["ch"], r[0]["size"], (100, r[0]["position"][1]))
    paste(r[1]["ch"], r[1]["size"], (180, r[1]["position"][1]))
    paste(rc["ch"], rc["size"], tuple(rc["position"]))
    paste(r[2]["ch"], r[2]["size"], (390, r[2]["position"][1]))
    paste(r[3]["ch"], r[3]["size"], (470, r[3]["position"][1]))
    paste(r[4]["ch"], r[4]["size"], (550, r[4]["position"][1]))
    paste(m1["ch"], m1["size"], (655, m1["position"][1]))
    paste(m2["ch"], m2["size"], (720, m2["position"][1]))

    final = Image.alpha_composite(bg, fg)
    cv_img = cv2.cvtColor(np.array(final), cv2.COLOR_RGBA2BGRA)

    if random.random() < args.perspective_prob:
        cv_img, boxes = perspective_warp(cv_img, boxes, args.perspective_max_offset)

    if random.random() < args.rotate_prob:
        cv_img, boxes = rotate_and_shear(
            cv_img, boxes, args.rotate_max_deg, args.shear_max
        )

    if random.random() < args.motion_blur_prob:
        cv_img = motion_blur(cv_img, args.motion_blur_kernels)

    cv_img = illumination(
        cv_img,
        args.illumination_alpha_min,
        args.illumination_alpha_max,
        args.illumination_beta_min,
        args.illumination_beta_max,
    )

    final = Image.fromarray(cv2.cvtColor(cv_img, cv2.COLOR_BGRA2RGBA))
    iw, ih = final.size

    final.save(f"{img_dir}/{i}_{plate_text}.png")
    with open(f"{lbl_dir}/{i}_{plate_text}.txt", "w") as f:
        for b in boxes:
            f.write(yolo_line(b, iw, ih) + "\n")


# ============================================================
# Main
# ============================================================
def main():
    args = parse_args()

    if args.seed:
        random.seed(args.seed)
        np.random.seed(args.seed)

    os.makedirs(f"{args.output_dir}/images", exist_ok=True)
    os.makedirs(f"{args.output_dir}/labels", exist_ok=True)

    cfg = load_config(args.config)
    numbers, mini_numbers, chars = cfg["numbers"], cfg["mini_numbers"], cfg["chars"]
    class_names = [c["ch"] for c in mini_numbers + chars]
    class_map = {c["ch"]: i for i, c in enumerate(mini_numbers + chars)}

    generate_yolo_yaml(args.output_dir, class_names)


    for i in range(args.num_images):
        generate_plate(
            i, args, numbers, mini_numbers, chars,
            class_map,
            f"{args.output_dir}/images",
            f"{args.output_dir}/labels",
        )


if __name__ == "__main__":
    main()


# python main.py --num-images 100 --motion-blur-prob 0.3 --perspective-max-offset 0.12 --illumination-alpha-max 1.5
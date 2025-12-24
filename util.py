import os
import random
import json
import cv2


def visualize_random_sample(
    dataset_dir="output",
    config_path="config.json",
    save_dir="files",
):
    img_dir = os.path.join(dataset_dir, "images")
    lbl_dir = os.path.join(dataset_dir, "labels")
    os.makedirs(save_dir, exist_ok=True)

    with open(config_path) as f:
        cfg = json.load(f)

    classes = [c["ch"] for c in cfg["numbers"] + cfg["mini_numbers"] + cfg["chars"]]

    img_name = random.choice(os.listdir(img_dir))
    base = os.path.splitext(img_name)[0]

    img = cv2.imread(os.path.join(img_dir, img_name))
    h, w = img.shape[:2]

    with open(os.path.join(lbl_dir, base + ".txt")) as f:
        for line in f:
            cls, xc, yc, bw, bh = map(float, line.split())
            cls = int(cls)

            x = int((xc - bw / 2) * w)
            y = int((yc - bh / 2) * h)
            bw = int(bw * w)
            bh = int(bh * h)

            cv2.rectangle(img, (x, y), (x + bw, y + bh), (0, 255, 0), 2)
            cv2.putText(
                img,
                classes[cls],
                (x, y - 5),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.6,
                (0, 0, 0),
                2,
            )

    out = os.path.join(save_dir, f"viz_{img_name}")
    cv2.imwrite(out, img)
    print(f"Saved visualization to {out}")


if __name__ == "__main__":
    visualize_random_sample()

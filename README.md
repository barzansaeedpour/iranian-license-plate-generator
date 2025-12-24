# Iranian-license-plate-generator

You can use this project to produce quality Iranian license plates.

از این پروژه برای تولید پلاک های ایرانی با کیفیت می توانید استفاده کنید.

## Samples


samples of generated images

نمونه پلاک های تولید شده بدون پارامتر:

<html>
<body>
    <table>
        <tr>
            <td><img src="./files/1.png" width="100%" height="100%"></td>
            <td><img src="./files/2.png" width="100%" height="100%"> </td>
        </tr>
        <tr>
            <td><img src="./files/3.png" width="100%" height="100%"></td>
            <td><img src="./files/4.png" width="100%" height="100%"></td>
        </tr>
        <tr>
            <td><img src="./files/5.png" width="100%" height="100%"></td>
            <td><img src="./files/6.png" width="100%" height="100%"></td>
        </tr>
    </table>
</body>
</html>

نمونه پلاک های تولید شده با پارامترهای (چرخش، تغییر پرسپکتیو، اشباع رنگ و غیره):


<html>
<body>
    <table>
        <tr>
            <td><img src="./files/7.png" width="100%" height="100%"></td>
            <td><img src="./files/8.png" width="100%" height="100%"> </td>
        </tr>
        <tr>
            <td><img src="./files/9.png" width="100%" height="100%"></td>
            <td><img src="./files/10.png" width="100%" height="100%"></td>
        </tr>
        <tr>
            <td><img src="./files/11.png" width="100%" height="100%"></td>
            <td><img src="./files/12.png" width="100%" height="100%"></td>
        </tr>
    </table>
</body>
</html>

نمونه پلاک های تولید شده به همراه برچسب فرمت YOLO:


<html>
<body>
    <table>
        <tr>
            <td><img src="./files/13.png" width="100%" height="100%"></td>
            <td><img src="./files/14.png" width="100%" height="100%"> </td>
        </tr>
        <tr>
            <td><img src="./files/15.png" width="100%" height="100%"></td>
            <td><img src="./files/16.png" width="100%" height="100%"></td>
        </tr>
        <tr>
            <td><img src="./files/17.png" width="100%" height="100%"></td>
            <td><img src="./files/18.png" width="100%" height="100%"></td>
        </tr>
    </table>
</body>
</html>

## How to use (Python 3.10.0 is recommended)

- ```
    pip install -r requirements.txt
    ```
- ```
    python main.py 
    ```

- With arguments (با پارامترهای چرخش، تغییر پرسپکتیو، اشباع رنگ و غیره):
- ```
    python main.py --num-images 100 --motion-blur-prob 0.3 --perspective-max-offset 0.12 --illumination-alpha-max 1.5
```

## Chars and Numbers

| Persian | English | Image | Persian | English | Image |
|----------|----------|----------|----------|----------|----------|
| 0 | 0 | <img src="./resized_chars/0.png" width="50%" height="50%" style="background-color: white;"> | ب | B | <img src="./resized_chars/B.png" width="50%" height="50%" style="background-color: white;"> |
| 1 | 1 | <img src="./resized_chars/1.png" width="50%" height="50%" style="background-color: white;"> | پ | P | <img src="./resized_chars/P.png" width="50%" height="50%" style="background-color: white;"> |
| 2 | 2 | <img src="./resized_chars/2.png" width="50%" height="50%" style="background-color: white;"> | ت | T | <img src="./resized_chars/T.png" width="50%" height="50%" style="background-color: white;"> |
| 3 | 3 | <img src="./resized_chars/3.png" width="50%" height="50%" style="background-color: white;"> | ج | J | <img src="./resized_chars/J.png" width="50%" height="50%" style="background-color: white;"> |
| 4 | 4 | <img src="./resized_chars/4.png" width="50%" height="50%" style="background-color: white;"> | ح | HE | <img src="./resized_chars/HE.png" width="50%" height="50%" style="background-color: white;"> |
| 5 | 5 | <img src="./resized_chars/5.png" width="50%" height="50%" style="background-color: white;"> | د | D | <img src="./resized_chars/D.png" width="50%" height="50%" style="background-color: white;"> |
| 6 | 6 | <img src="./resized_chars/6.png" width="50%" height="50%" style="background-color: white;"> | س | SIN | <img src="./resized_chars/SIN.png" width="50%" height="50%" style="background-color: white;"> |
| 7 | 7 | <img src="./resized_chars/7.png" width="50%" height="50%" style="background-color: white;"> | ص | SAD | <img src="./resized_chars/SAD.png" width="50%" height="50%" style="background-color: white;"> |
| 8 | 8 | <img src="./resized_chars/8.png" width="50%" height="50%" style="background-color: white;"> | ط | TA | <img src="./resized_chars/TA.png" width="50%" height="50%" style="background-color: white;"> |
| 9 | 9 | <img src="./resized_chars/9.png" width="50%" height="50%" style="background-color: white;"> | ع | EIN | <img src="./resized_chars/EIN.png" width="50%" height="50%" style="background-color: white;"> |
| ق | Q | <img src="./resized_chars/Q.png" width="50%" height="50%" style="background-color: white;"> | ن | N | <img src="./resized_chars/N.png" width="50%" height="50%" style="background-color: white;"> 
| م | M | <img src="./resized_chars/M.png" width="50%" height="50%" style="background-color: white;"> |و | V | <img src="./resized_chars/V.png" width="50%" height="50%" style="background-color: white;"> |
| ی | Y | <img src="./resized_chars/Y.png" width="50%" height="50%" style="background-color: white;"> | ه | H | <img src="./resized_chars/H.png" width="50%" height="50%" style="background-color: white;"> |


## Label Mapping (راهنمای برچسب ها)

This dataset uses YOLO-format annotations.

Each label is encoded as:
<class_id> <x_center> <y_center> <width> <height>

### Class IDs

| ID | Label | Description |
|----|-------|------------|
| 0  | 0     | Digit zero (عدد صفر) |
| 1  | 1     | Digit one (عدد یک)|
| ...| ...   | ... |
| 9  | 9     | Digit nine (عدد نه) |
| 10 | A     | Government plate (دولتی)|
| 11 | P     | Police (پلیس)|
| 12 | T     | Taxi (تاکسی)|
| 13 | TH    | Sepah (سپاه)|
| 14 | Z     | Blue plate (دیپلمات)|
| 15 | SH    | Military (ارتش)|
| 16 | EIN   | Public (عمومی)|

- در کنار خروجی، راهنمای برچسب ها نیز اتماتیک ایجاد می شود
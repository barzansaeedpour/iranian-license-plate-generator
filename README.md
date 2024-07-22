# Iranina-license-plate-generator

You can use this project to produce quality Iranian license plates.

از این پروژه برای تولید پلاک های ایرانی با کیفیت می توانید استفاده کنید.

## Samples


samples of generated images

نمونه پلاک های تولید شده

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
    </table>
</body>
</html>

## How to use

- ```
    pip install -r requirements.txt
    ```
- ```
    python main.py [options]
    ```
- -o <output_dir>: Specify the output directory. Default is ./output/.
- -n <number>: Specify the number of iterations. Default is 100.

Note: Both -o and -n are optional. If not specified, the defaults are ./output/ for -o and 100 for -n.

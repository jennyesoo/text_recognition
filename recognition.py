# -*- coding: utf-8 -*-
"""
Created on Thu May 12 11:00:03 2022

@author: hebe.chuang
"""


from PIL import Image,ImageEnhance
import pytesseract


pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

#數字辨識
def convert_img(img,threshold):
        img = img.convert("L")  # 處理灰白
        pixels = img.load()
        for x in range(img.width):
            for y in range(img.height):
                if pixels[x, y] > threshold:
                    pixels[x, y] = 255
                else:
                    pixels[x, y] = 0
        return img

img = Image.open(r'./data/captcha_login.png')
result = convert_img(img,150)
result = pytesseract.image_to_string(result)


#文字辨識
img_name = './data/number+black.png'  #number+black.png , captcha_login.png , number.png
img = Image.open(img_name)
text = pytesseract.image_to_string(img, lang='eng')
print(text)


#文字辨識
img_name = './data/1_HMtYtaaAeV8pBWU2jAXjMg.jpeg' #number+black.png , captcha_login.png , number.png
img = Image.open(img_name)
img = convert_img(img,150)
text = pytesseract.image_to_string(img, lang='chi_tra+eng')
print(text)


#文字辨識
img_name = './data/color.png' #number+black.png , captcha_login.png , number.png
img = Image.open(img_name)
text = pytesseract.image_to_string(img)
print(text)


result = convert_img(img,150)
#
img = img.convert('L')
img
# 對比度增強
sharpness = ImageEnhance.Contrast(img)
sharp_img = sharpness.enhance(5.0)
content = pytesseract.image_to_string(sharp_img, lang='chi_tra+eng')
print(content)
import pytesseract
from PIL import Image
import cv2

# 開啟圖片
image = Image.open("lab13英文字.png")

text = pytesseract.image_to_string(image, lang='eng', config='--psm 6')

print("OCR 辨識結果:")
print("-" * 40)
print(text)
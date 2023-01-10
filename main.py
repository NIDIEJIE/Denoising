import pywt
import numpy as np
import cv2
from PIL import Image

# ==============固定阈值、预设小波=====================
img = cv2.imread("origin.bmp", 0)
# img是数组
w = 'sym4'  # 定义小波基的类型
l = 3  # 变换层次为3
coeffs = pywt.wavedec2(data=img, wavelet=w, level=l)  # 对图像进行小波分解
threshold = 0.04

list_coeffs = []
for i in range(1, len(coeffs)):
    list_coeffs_ = list(coeffs[i])
    list_coeffs.append(list_coeffs_)

for r1 in range(len(list_coeffs)):
    for r2 in range(len(list_coeffs[r1])):
        # 对噪声滤波(软阈值)
        list_coeffs[r1][r2] = pywt.threshold(list_coeffs[r1][r2], threshold * np.max(list_coeffs[r1][r2]))

rec_coeffs = []  # 重构系数
rec_coeffs.append(coeffs[0])  # 将原图像的低尺度系数保留进来

for j in range(len(list_coeffs)):
    rec_coeffs_ = tuple(list_coeffs[j])
    rec_coeffs.append(rec_coeffs_)

denoised_img = pywt.waverec2(rec_coeffs, 'sym4')
denoised_img = Image.fromarray(np.uint8(denoised_img))
denoised_img.save("result.bmp")

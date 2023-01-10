import pywt
import numpy as np
import cv2
from PIL import Image

# ==============固定阈值、预设小波=====================
# 原理：小波阈值去噪的实质为抑制信号中无用部分、增强有用部分的过程。小波阈值去噪过程为：(1)分解过程，即选定一种小波对信号进行n层小波分解；
# (2)阈值处理过程，即对分解的各层系数进行阈值处理，获得估计小波系数；(3)重构过程，据去噪后的小波系数进行小波重构，获得去噪后的信号。
# 影响效果的因素：分解层数、阈值、小波基的选择、阈值函数的选择

img = cv2.imread("origin.bmp", 0)
# img是数组
w = 'sym4'  # 定义小波基的类型
l = 3  # 变换层次为3
coeffs = pywt.wavedec2(data=img, wavelet=w, level=l)  # 对图像进行小波分解
# coeffs是个列表，主要有两个东西：
# 1）低频系数，以数组形式存放。
# 2）高频系数，每一层的（水平、垂直、对角线）高频系数构成一个 3 维元组，所以有几层小波分解就有几个元组
threshold = 0.04 # 阈值
list_coeffs = []

# 处理高频系数，用list存起来
for i in range(1, len(coeffs)):
    list_coeffs_ = list(coeffs[i])
    list_coeffs.append(list_coeffs_)

for r1 in range(len(list_coeffs)):
    for r2 in range(len(list_coeffs[r1])):
        # 对噪声滤波(软阈值)，list_coeffs[r1][r2]也是个二维数组
        list_coeffs[r1][r2] = pywt.threshold(list_coeffs[r1][r2], threshold * np.max(list_coeffs[r1][r2]))

rec_coeffs = []  # 重构系数
rec_coeffs.append(coeffs[0])  # 将原图像的低尺度系数保留进来

for j in range(len(list_coeffs)):
    rec_coeffs_ = tuple(list_coeffs[j])
    rec_coeffs.append(rec_coeffs_)

# 小波重构
denoised_img = pywt.waverec2(rec_coeffs, w)
denoised_img = Image.fromarray(np.uint8(denoised_img))
denoised_img.save("result_wavelet.bmp")

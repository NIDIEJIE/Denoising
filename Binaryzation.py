import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
from PIL import Image
import os

# 图片输入路径
path_input_low = './picture/input/low/'
path_input_mid = './picture/input/mid/'
path_input_high = './picture/input/high/'

# 图片输出路径
path_output_low = './picture/output/low/'
path_output_mid = './picture/output/mid/'
path_output_high = './picture/output/high/'

# 不同质量图片的阈值
threshl = 155
threshh = 143
threshm = 148

files = os.listdir(path_input_mid)
# files = os.listdir('E:\研究生项目\软管图像处理\去噪\picture\input')
print(len(files))

# imread路径中不能出现中文
# img = cv.imread('./picture/input/low/221101-1-0-0.jpg', 0)

for i in range (len(files)):
    img = cv.imread(path_input_mid + files[i], 0)
    ret, thresh1 = cv.threshold(img, threshm, 255, cv.THRESH_BINARY)
    denoised_img = Image.fromarray(thresh1)
    denoised_img.save(path_output_mid + files[i])

# ret, thresh1 = cv.threshold(img, 140, 255, cv.THRESH_BINARY)
# ret, thresh2 = cv.threshold(img, 140, 255, cv.THRESH_BINARY_INV)
# ret, thresh3 = cv.threshold(img, 140, 255, cv.THRESH_TRUNC)
# ret, thresh4 = cv.threshold(img, 140, 255, cv.THRESH_TOZERO)
# ret, thresh5 = cv.threshold(img, 140, 255, cv.THRESH_TOZERO_INV)
# titles = ['Original Image', 'BINARY', 'BINARY_INV', 'TRUNC', 'TOZERO', 'TOZERO_INV']
# images = [img, thresh1, thresh2, thresh3, thresh4, thresh5]
# for i in range(6):
#     plt.subplot(2, 3, i + 1), plt.imshow(images[i], 'gray', vmin=0, vmax=255)
#     plt.title(titles[i])
#     plt.xticks([]), plt.yticks([])
# plt.show()

# denoised_img = Image.fromarray(thresh1)
# denoised_img.save("result_binary_hose_2.jpg")

import numpy as np
from PIL import Image
# from MedianFilter import border

# @均值滤波
def deNoise(img, x, y):
    num = d / 2
    # 这里默认的是3*3模版故 length = 9，
    maskLength = 9
    start = int(num)
    end = int(maskLength - num)
    L = []
    xl = [x - 1, x, x + 1]
    yl = [y - 1, y, y + 1]
    for i in xl:
        for j in yl:
            gray = img.getpixel((i, j))  # 取出灰度值
            L.append(gray)
    L.sort()
    c = np.mean(L[start:end])
    print(c)
    return int(c)


def solve(path1, path2):
    img1 = Image.open(path1)  # 图像1
    w, h = img1.size
    img2 = Image.new('L', (w, h), 'white')  # 图像2
    for x in range(1, w - 1):
        for y in range(1, h - 1):
            c = deNoise(img1, x, y)  # 求中值
            img2.putpixel((x, y), c)  # 将灰度设置为中值
    b = 0
    print("end")
    # borderPixelList = border(img1, w, h)
    # 将边缘像素原样输出
    # for i in range(h):
    #     if i == 0 or i == h - 1:
    #         for j in range(w):
    #             img2.putpixel((j, i), borderPixelList[b])
    #             b += 1
    #     else:
    #         img2.putpixel((0, i), borderPixelList[b])
    #         b += 1
    #         img2.putpixel((w - 1, i), borderPixelList[b])
    #         b += 1
    img2.save(path2)


path1 = '221101-1-0-0.jpg'  # 带噪声的图像
path2 = 'result_alphameanfilter_hose.jpg'  # 降噪后的图像
d = 6  # 去除d/2个小值和d/2个大值
solve(path1, path2)

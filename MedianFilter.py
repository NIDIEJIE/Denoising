from PIL import Image


# 求图像img中(x,y)处像素的中值c
def median(img, x, y):
    L = []
    xl = [x - 1, x, x + 1]
    yl = [y - 1, y, y + 1]
    for i in xl:
        for j in yl:
            gray = img.getpixel((i, j))  # 取出灰度值
            L.append(gray)
    L.sort()
    c = L[4]
    return c

# 获取边缘像素值
def border(img, w, h):
    borderPixelList = []
    for i in range(h):
        if i == 0 or i == h - 1:
            for j in range(w):
                gray = img.getpixel((i, j))
                borderPixelList.append(gray)
        else:
            gray1 = img.getpixel((i, 0))
            gray2 = img.getpixel((i, w - 1))
            borderPixelList.append(gray1)
            borderPixelList.append(gray2)
    # print(len(borderPixelList))
    return borderPixelList


# 对图像文件1进行降噪，并将结果保存为图像文件2
# 图像文件1和2的路径分别为path1和path2
def denoise(path1, path2):
    img1 = Image.open(path1)  # 图像1
    img1 = img1.convert('L')  # 将图像1转换为灰度图
    w, h = img1.size
    img2 = Image.new('L', (w, h), 'white')  # 图像2
    for x in range(1, w - 1):
        for y in range(1, h - 1):
            c = median(img1, x, y)  # 求中值
            img2.putpixel((x, y), c)  # 将灰度设置为中值
    b = 0
    borderPixelList = border(img1, w, h)
    # 将边缘像素原样输出
    for i in range(h):
        if i == 0 or i == h - 1:
            for j in range(w):
                img2.putpixel((i, j), borderPixelList[b])
                b += 1
        else:
            img2.putpixel((i, 0), borderPixelList[b])
            b += 1
            img2.putpixel((i, w - 1), borderPixelList[b])
            b += 1
    img2.save(path2)


path1 = 'origin.bmp'  # 带噪声的图像
path2 = 'result_medianfilter.bmp'  # 降噪后的图像
denoise(path1, path2)

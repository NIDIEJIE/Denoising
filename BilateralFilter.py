import cv2
from PIL import Image
img = cv2.imread("221101-1-0-0.jpg", 0)

imgResult = cv2.bilateralFilter(img, 3, 100, 50)
imgResult = Image.fromarray(imgResult)
imgResult.save("result_bilateralFilter_hose.jpg")
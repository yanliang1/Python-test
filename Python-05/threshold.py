#简单图形轮廓识别与绘制
import cv2 as cv

img = cv.imread("1.jpg")
cv.imshow("image",img)
print(img.shape)

#灰度图
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
# cv.imshow("gray",gray)
print(gray.shape)

#阈值分割，把灰度图转成二值图
ret,bin_img = cv.threshold(gray,127,255,cv.THRESH_BINARY_INV)
print("ret =",ret)
# cv.imshow("bin",bin_img)

#在二值图中查找对象的轮廓，轮廓其实就是一个优点组成的列表
contours,hierarchy = cv.findContours(bin_img,cv.RETR_EXTERNAL,cv.CHAIN_APPROX_SIMPLE)
print(type(contours))
print(len(contours[0]))

#在原图中绘制轮廓，-1表示绘制所有的点
ResourceWarning = cv.drawContours(img,contours,-1,(0,255,255),10)
cv.imshow("ret",bin_img)

cv.waitKey(0)
cv.destroyAllWindows()
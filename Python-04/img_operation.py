#图像的基本操作
import cv2

#加载图像
img = cv2.imread("1.jpg")
print(type(img))

#显示到窗体中
cv2.imshow("image",img)

#读取像素点的值
pix = img[100,20]
print(type(pix))
print(pix)

#等待操作
cv2.waitKey(0)

#销毁窗体
cv2.destroyAllWindows()

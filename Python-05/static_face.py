import cv2 as cv

#创建人脸分类器
casc = cv.CascadeClassifier("haarcascade_frontalface_alt2.xml")
print(type(casc))

#打开图片
img = cv.imread("1.jpg")

#灰度化
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)

#检测人脸
faces_rect = casc.detectMultiScale(gray)
print(type(faces_rect))
print(faces_rect)   #返回的是一个矩形信息  起始点  宽和高  [[166 158 144 144]]
x,y,w,h = faces_rect[0]
print(x,y,w,h)

#绘制脸部区域
#cv.rectangle(img,pt1,pt2,color) #pt1:矩形的左上角，pt2右下角（255,0,0）
# cv.rectangle(img,(x,y),(x + w,y + h),(0,0,255))
cv.circle(img,((x + x + w) / 2,(y + y + h) / 2),w // 2,(0,255,0))

#显示图像
cv.imshow("img",img)

#等待用户操作
key = cv.waitKey(0)
if key == ord('q'):
    print("key =",key)

#销毁所有窗体
cv.destroyAllWindows()
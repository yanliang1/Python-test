import cv2 as cv

img = cv.imread("1.jpg")
cv.imshow("image",img)
print(img.shape)

gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow("gray",gray)
print(gray.shape) # 行 和 列
row,col = gray.shape

pix = gray[0,0]
print(pix)
pix = img[1,1]
print(pix)
for i in range(row - 1):
    for j in range(col - 1):
        pix = gray[i:j]
        if gray[i,j] > 128:
                gray[i,j] = 255
        else:
                gray[i,j] = 0
        print(pix)
        print()
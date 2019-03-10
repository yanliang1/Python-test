import cv2 as cv

cv.namedWindow("video")  
cap = cv.VideoCapture(0) #加载摄像头录制  
ret, frame = cap.read()  

casc = cv.CascadeClassifier("haarcascade_frontalface_alt2.xml")
count=0
while ret:
    ret,frame = cap.read()

    image = cv.cvtColor(frame,cv.COLOR_BGR2GRAY)

    faces_rect = casc.detectMultiScale(image, 1.2, 2, cv.CASCADE_SCALE_IMAGE)  
    if len(faces_rect) > 0:  
        for faceRect in faces_rect:  
            x, y, w, h = faceRect  
            cv.rectangle(frame,(x,y),(x+h,y+w),(0,0,255),2)
        cv.imshow("video", frame)  
    key = cv.waitKey(2)
    if(key == ord('q')):
        break
    elif(key == ord('p')):
        cv.imwrite("{}.jpg".format(count), frame)
        count += 1


cv.destroyWindow("video")  

'''
    key = cv.waitKey(1)   
    if key == ord("p"): 
        cv.imwrite("11.jpg",frame)  
        '''
  #  key = cv.waitKey(1)  

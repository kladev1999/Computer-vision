"""
ผู้จัดทำ 
    นายภูผา ไชยดี 63172310444-1
    นายวัฒนา นามมา 6317310369-7
    นายณัฐพงศ์ เสาวพันธ์ 63172310241-3
    นายกวี นวลสุธา 63172310242-3
    นายอนันตภพ โค่นถอน 63172310156-1
"""


from cmath import cos, sin
from itertools import count
import math
import cv2
from cv2 import edgePreservingFilter
import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt
from scipy import ndimage  

imgpa = '1233.png'


def robert(imgpa): #ประกาศชื่อ ฟังก์ชั่นชื่อว่า robert แล้วรับค่าพารมิเตอร์ imgpa
    count = 0 # ประกาศตัวแปร count เพื่อมารอนับเส้น

    img = cv2.imread(imgpa) # ประกาศตัวแปร img  แล้วเรียกใช้ cv2.imread เพื่ออ่านค่า path ของรูปภาพ
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # แปลงรูปภาพเป็น gray scale  แล้วนำไปเก็บที่ตัวแปร gray 
    img_gaussian = cv2.GaussianBlur(gray,(3,3),0) # ใช้ GaussianBlur เพื่อทำการเบลอภาพแล้วเก็บค่าที่ img_gaussian

    
    roberts_cross_v = np.array( [[1,0],[0,-1]] ) #ทำตามอัลกอริทึม robert ประกาศอาเรย์ แนวตั้ง 
    roberts_cross_h = np.array( [[0,1],[-1,0]]  )#ทำตามอัลกอริทึม robert ประกาศอาเรย์ แนวนอน

    img_robertx = cv2.filter2D(img_gaussian, -1, roberts_cross_v) # ใช้ 2d filter โดยนำภาพที่ใช้ guassianBlur มา แล้วกำหนด kernel ให้มีค่า ตามที่ประกาศข้างบน 
    img_roberty = cv2.filter2D(img_gaussian, -1, roberts_cross_h)
    imgrobert = (img_robertx + img_roberty) # นำค่า แกนx และ แกนy มาบวกกัน

    lines_list =[] #ประกาศตัวแปร lines_list
    # เรียกใช้  Library HoughLinesP ส่งค่า imgrobert ที่นำค่า  แกนx และ แกนy มาบวกกัน ส่งไป พร้อมค่า rho, theta ,threshold, ค่า min และค่า max
    lines = cv2.HoughLinesP(imgrobert,1, np.pi/180, threshold=100, minLineLength=5,maxLineGap=10)
    # loop for point ตามข้อมูลใน ตัวแปร lines
    for points in lines:
        #นำค่าที่ loop ได้จาก pointsตำแหน่งที่ [0] มาเก็บไว้ตามตัวแปร x1,y1,x2,y2
        x1,y1,x2,y2=points[0] 
        # ทำการวาดเส้น ลงในภาพ img ตามจุด x1,y1 และ x2,y2 แล้วกำหนด สี กำหนดความเข้มของเส้น
        cv2.line(img,(x1,y1),(x2,y2),(255,0,0),2)
        #เพิ่มเส้นเข้าไปในตัวแปร lines_list
        lines_list.append([(x1,y1),(x2,y2)])
        #เพิ่มค่า count 
        count += 1
    
    print('Robert Count = ',int(count/4))
    return cv2.line(img,(x1,y1),(x2,y2),(255,0,0),2)

def sobel(imgpa):
    count = 0

    img = cv2.imread(imgpa)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img_gaussian = cv2.GaussianBlur(gray,(3,3),0)

    sobel_cross_v = np.array( [[1,0,-1],
                             [2,0,-2 ],
                             [1,0,-1]] )

    sobel_cross_h = np.array( [[1, 2, 1 ],
                             [ 0, 0, 0 ],
                             [-1,-2,-1]] )

    img_sobelx = cv2.filter2D(img_gaussian, -1, sobel_cross_v)
    img_sobely = cv2.filter2D(img_gaussian, -1, sobel_cross_h)
    imgsobel = (img_sobelx + img_sobely)

    lines_list =[]
    lines = cv2.HoughLinesP(imgsobel,1, np.pi/180, threshold=100, minLineLength=5,maxLineGap=10)

    for points in lines:
        x1,y1,x2,y2=points[0] 
        cv2.line(img,(x1,y1),(x2,y2),(255,0,0),2)
        lines_list.append([(x1,y1),(x2,y2)])
        count += 1
        
    
    print('Sobel Count = ',int(count/4))

    return cv2.line(img,(x1,y1),(x2,y2),(255,0,0),2)

def prewitt(imgpa):
    count = 0

    img = cv2.imread(imgpa)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img_gaussian = cv2.GaussianBlur(gray,(3,3),0)

    prewitt_cross_v = np.array( [[1,0,-1],
                             [1,0,-1 ],
                             [1,0,-1]] )

    prewitt_cross_h = np.array( [[1, 1, 1 ],
                             [ 0, 0, 0 ],
                             [-1,-1,-1]] )
    
    img_prewittx = cv2.filter2D(img_gaussian, -1, prewitt_cross_v)
    img_prewitty = cv2.filter2D(img_gaussian, -1, prewitt_cross_h)
    imgpree = (img_prewittx + img_prewitty)

    lines_list =[]
    lines = cv2.HoughLinesP(imgpree,1, np.pi/180, threshold=100, minLineLength=5,maxLineGap=10)

    for points in lines:
        x1,y1,x2,y2=points[0] 
        cv2.line(img,(x1,y1),(x2,y2),(255,0,0),2)
        lines_list.append([(x1,y1),(x2,y2)])
        count += 1
    
    print('Prewitt Count = ',int(count/4))

    return cv2.line(img,(x1,y1),(x2,y2),(255,0,0),2)

def canny(imgpa):
    count = 0
    img = cv2.imread(imgpa)
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    edgesCanny = cv2.Canny(gray,300,400,apertureSize=3)
    # print(type(img))
    # print(img.ndim)
    # print(img.shape[0]*img.shape[1])
    # print(img.size)
    # print(np.amin(edgesCanny))
    # print(np.amax(edgesCanny))
    lines_list =[]
    lines = cv2.HoughLinesP(edgesCanny,1,np.pi/180, threshold=100, minLineLength=5,maxLineGap=10)
   
    for points in lines:
        x1,y1,x2,y2=points[0] 
        cv2.line(img,(x1,y1),(x2,y2),(255,0,0),2)
        lines_list.append([(x1,y1),(x2,y2)])
        count+=1
    #     for i in range(360):
    #         i+=i
    # print(math.sqrt((img.shape[0]*img.shape[0])+(img.shape[1]*img.shape[1])))
    print('Canny Count = ',int(count/2))

    return cv2.line(img,(x1,y1),(x2,y2),(255,0,0),2)

def showImg(imgpa):
    robertim = robert(imgpa)
    sobelim = sobel(imgpa)
    prewittim = prewitt(imgpa)
    cannyim = canny(imgpa)
    
    img = cv.imread(imgpa,0)

    cv2.imwrite('circanny.jpg',cannyim)
    cv2.imwrite('cirrobert.jpg',robertim)
    cv2.imwrite('cirprewitt.jpg',prewittim)
    cv2.imwrite('cirsobel.jpg',sobelim)

    plt.subplot(231),plt.imshow(img,cmap = 'gray')
    plt.title('Original Image'), plt.xticks([]), plt.yticks([])

    plt.subplot(232),plt.imshow(cannyim,cmap = 'gray')
    plt.title('Canny'), plt.xticks([]), plt.yticks([])

    plt.subplot(233),plt.imshow(robertim,cmap = 'gray')
    plt.title('Robert'), plt.xticks([]), plt.yticks([])

    plt.subplot(234),plt.imshow(prewittim,cmap = 'gray')
    plt.title('Prewitt'), plt.xticks([]), plt.yticks([])

    plt.subplot(235),plt.imshow(sobelim,cmap = 'gray')
    plt.title('Sobel'), plt.xticks([]), plt.yticks([])
    
    plt.show()


showImg(imgpa)



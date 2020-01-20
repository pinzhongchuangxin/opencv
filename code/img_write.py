import numpy as np
import cv2
import time

# # 使用Numpy创建一张A4(2105×1487)纸
# img = np.zeros((16,16,3), np.uint8)
# # 使用白色填充图片区域,默认为黑色
# img.fill(255)
# font=cv2.FONT_HERSHEY_COMPLEX
# cv2.putText(img,'1',(1,1), font, 1,(0,0,0),2)
# # cv2.putText(img,'SunFounder',(30,70), font, 1,(0,0,0),2)
# img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# img_array = np.asarray(img)
# for i in img_array:
#     print(i)
#     time.sleep(0.5)
# cv2.imwrite("sun.jpeg", img)

import cv2 as cv
def inverse(img):
    img = cv.bitwise_not(img)   #函数cv.bitwise_not可以实现像素点各通道值取反
    cv.imshow("second_image", img)

src=cv.imread('E:\imageload\example.png')   #blue, green, red
cv.namedWindow('first_image', cv.WINDOW_AUTOSIZE)
cv.imshow('first_image', src)
t1 = cv.getTickCount()    #GetTickcount函数返回从操作系统启动到当前所经过的毫秒数
inverse(src)
t2 = cv.getTickCount()
time = (t2-t1)/cv.getTickFrequency()  #getTickFrequency函数返回CPU的频率,就是每秒的计时周期数
print("time : %s ms"%(time*1000) )    #输出运行时间
cv.waitKey(0)
cv.destroyAllWindows()


#自定义一张三通道图片
import cv2 as cv
import numpy as np
def creat_image():
    img = np.zeros([400, 400, 3], np.uint8)   #将所有像素点的各通道数值赋0
    img[:, :, 0] = np.ones([400, 400]) * 255   #0通道代表B
    # img[:, :, 1] = np.ones([400, 400]) * 255   #1通道代表G
    # img[:, :, 2] = np.ones([400, 400]) * 255   #2通道代表R
    cv.imshow("new_image",img)
creat_image()
cv.waitKey(0)
cv.destroyAllWindows()
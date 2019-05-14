#!/usr/bin/env python
# coding: utf-8

# In[6]:


import cv2 as cv
import numpy
import random

# 随机字母:
def rndChar():
    return chr(random.randint(65, 90))

# 随机颜色1:
def rndColor():
    return (random.randint(64, 255), random.randint(64, 255), random.randint(64, 255))

# 随机颜色2:
def rndColor2():
    return (random.randint(32, 127), random.randint(32, 127), random.randint(32, 127))

for i in range(10):
    # 240 x 60:
    width = 60
    height = 60 * 4
    I=numpy.zeros((width,height),dtype=numpy.uint8)
    image = cv.cvtColor(I,cv.COLOR_GRAY2BGR)
    # 创建Font对象:
    font = cv.FONT_HERSHEY_SIMPLEX  
    # 填充每个像素:
    for x in range(width):
        for y in range(height):
            image[x, y]=rndColor()
    # 输出文字:
    for t in range(4):
        cv.putText(image,rndChar(),(60 * t + 10, 50),font,2,rndColor2(),2)
    # 模糊:
    image = cv.medianBlur(image, 5)
    #保存显示
    cv.imwrite('code.jpg',image)
    cv.imshow('code',image)
    cv.waitKey(1500)
cv.destroyAllWindows()


# In[ ]:





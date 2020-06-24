#!/usr/bin/env python
# coding: utf-8

# In[1]:


from multiprocessing import Process, Queue
import os
import cv2 as cv
import numpy as np
import time

# 创建一个VideoCapture对象
capture = cv.VideoCapture(0)         

#退出计数
exit_time = 0

while(True):
    # 一帧一帧读取视频
    ret, frame = capture.read()                     
    
    # 显示结果，按q停止
    cv.imshow('frame', frame)  
    cv.waitKey(1)
    
    exit_time += 1
    if exit_time > 400:
        break
        
# 释放cap,销毁窗口
capture.release()                                   
cv.destroyAllWindows()


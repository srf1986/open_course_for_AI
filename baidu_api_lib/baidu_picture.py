#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#!/usr/bin/env python
# coding: utf-8

# In[22]:


#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (c) 2020 Taste all Pi.
#
# Licensed under the GNU General Public License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#   http://www.gnu.org/licenses/gpl-2.0.html
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

#########  百度图像处理库使用说明  #################
# baidu_picture_2_msg：初始化方法和获取图像信息
# init初始化方法：
#        需要传入百度AI应用提供的api_key和secret_key
# pic_2_msg获取图像方法： 
#        对输入的图片进行人工智能分析，并获取分析结果
#################################################

#########  调用方式举例  #################
# #导入标准库
# import sys
# from playsound import playsound
# import cv2 as cv

# #导入自定义库
# sys.path.append('../baidu_api_lib')
# from baidu_picture import baidu_picture_2_msg
# 
# #传入参数
# baidu_request_url = "https://aip.baidubce.com/rest/2.0/image-classify/v1/body_analysis"
# baidu_api_key = 'EtVQHk3Oq3ZQDfNzGbW7sZLd'
# baidu_api_secret = 'OjFeIol5wRCGRyjrk4YRUM07BN1qomBk'
# 
# if __name__ == "__main__":
#     try:
#         # 打开摄像头
#         capture = cv.VideoCapture(0) 
#         
#         # 传入百度AI的参数
#         pic_msg = baidu_picture_2_msg(baidu_api_id, baidu_api_key, baidu_api_secret)
#         
#         while True:
#             # 一帧一帧读取视频
#             ret, frame = capture.read()
#             
#             # 写入图片
#             cv.imwrite('camera_pic.jpg',frame)  
#             #time.sleep(1)
#             
#             response = pic_msg.pic_2_msg(baidu_request_url, 'camera_pic.jpg')
#             print(response.json())
#             
#             # 本地显示视频图像
#             cv.imshow('screen', frame) 
#             cv.waitKey(1)  
#                
#     except KeyboardInterrupt:             
#         # 释放cap,销毁窗口
#         capture.release()                                   
#         cv.destroyAllWindows()                                  
#         print("任务被终止")
#################################################      

from aip import AipSpeech
import requests
import base64
import re

class baidu_picture_2_msg(object):
    
    #百度AI应用提供参数
    REQUEST_URL = None
    API_ID      = None
    API_KEY     = None
    SECRET_KEY  = None
    response    = None
    
    def __init__(self, api_id, api_key, secret_key):
        #获取提供的百度AI接口参数
        self.API_ID = api_id
        self.API_KEY = api_key
        self.SECRET_KEY = secret_key
        
        #获取access_token值
        main_host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id='
        host = main_host + api_key + '&client_secret=' + secret_key
        self.response = requests.get(host)
        
    def pic_2_msg(self, request_url, pic_name):
        #获取应用的调用接口
        self.REQUEST_URL = request_url 
        
        if self.response:
            #打开待处理的图片
            f = open(pic_name, 'rb')
            img = base64.b64encode(f.read())
            params = {"image":img, 'image_type':'BASE64', \
                      'face_field':'age,mask,expression,emotion', \
                      'max_face_num':10}

            #获取access_token值
            access_token = self.response.json()['access_token']
            self.REQUEST_URL = self.REQUEST_URL + "?access_token=" + access_token
            headers = {'content-type': 'application/x-www-form-urlencoded'}

            #获得请求后，进行信息输出
            response = requests.post(self.REQUEST_URL, data=params, headers=headers)
            if response:
                return response
        return None


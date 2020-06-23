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

#########  百度春联库使用说明  #################
# baidu_couplets：初始化方法和获取对联方法
# init初始化方法：
#        需要传入百度AI应用提供的APP_ID、API_KEY和SECRET_KEY
# get_couplets：获取对联方法方法
#        request_url:百度api的链接
#        word:对联命题关键字，以双引号括起来
#################################################

#########  调用方式举例  #################
# #导入标准库
# import sys
# import os

# #传入参数
# baidu_app_id = '20217336'
# baidu_api_key = 'cGIn10y839IumZjhUSu0CQ9W'
# baidu_api_secret = 'FaZDHtAGYFurNtXZoPHso7PbjL7vTsUP'

# baidu_request_url = 'https://aip.baidubce.com/rpc/2.0/creation/v1/couplets'

# if __name__ == "__main__":
#     try:
#         couplets = baidu_couplets(baidu_app_id, baidu_api_key, baidu_api_secret)
        
#         word = couplets.get_couplets(baidu_request_url, "春天")
        
#         print(word.json())
                       
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
import json

class baidu_couplets_create(object):
    
    #百度AI应用提供参数
    APP_ID      = None
    API_KEY     = None
    SECRET_KEY  = None
    access_token      = None
    
    def __init__(self, app_id, api_key, secret_key):
        #获取提供的百度AI接口参数
        self.APP_ID = app_id
        self.API_KEY = api_key
        self.SECRET_KEY = secret_key
        
        #获取access_token值
        main_host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id='
        host = main_host + self.API_KEY + '&client_secret=' + self.SECRET_KEY
        response = requests.get(host)
        self.access_token = response.json()['access_token']
        
    def get_couplets(self, request_url, word):
        #对要文字进行格式转化
        params = dict()
        params['index'] = 0
        params['text'] = word
        params = json.dumps(params).encode('utf-8')
        
        #填充请求对联格式，进行获取对联
        request_url = request_url + "?access_token=" + self.access_token
        headers = {'content-type': 'application/x-www-form-urlencoded'}
        response = requests.post(request_url, data=params, headers=headers)

        #返回获取到的春联
        return response


# In[ ]:





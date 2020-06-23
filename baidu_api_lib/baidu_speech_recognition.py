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

#########  百度语音识别库使用说明  #################
# baidu_speech_2_word类提供：初始化方法和语音识别方法
# init初始化方法：
#        需要传入百度AI应用提供的APP_ID、API_KEY和SECRET_KEY
# speech_2_word语音识别方法： 
#        识别的音频文件名，格式为.mp3
#################################################

#########  调用方式举例  #################
# #导入标准库
# import sys
# from playsound import playsound

# #导入自定义库
# sys.path.append('../../baidu_api_lib')
# from baidu_speech_recognition import baidu_speech_2_word

# """ 我的 APPID AK SK """
# APP_ID = '20114704'
# API_KEY = 'Lwd56jic7ZvTon8PsYyZ5DfG'
# SECRET_KEY = 'EnNdR4Vr0HgATxz7LiHEDx3dKfLkWFGj'

# if __name__ == "__main__":
#     try:
#         #传入百度AI的参数
#         sp_2_wd = baidu_speech_2_word(APP_ID, API_KEY, SECRET_KEY)
        
#         #对音频文件进行分析
#         msg = sp_2_wd.speech_2_word('ppp1.mp3')
        
#         #输出分析结果
#         print(msg)

#     except KeyboardInterrupt:
#         print("任务被终止了")
#################################################    

from aip import AipSpeech

class baidu_speech_2_word(object):
    
    #百度AI应用提供参数
    APP_ID      = None
    API_KEY     = None
    SECRET_KEY  = None
    client      = None
    
    def __init__(self, app_id, api_key, secret_key):
        #获取提供的百度AI接口参数
        self.APP_ID = app_id
        self.API_KEY = api_key
        self.SECRET_KEY = secret_key
        
        #获取授权
        self.client = AipSpeech(self.APP_ID, self.API_KEY, self.SECRET_KEY)
        
    def speech_2_word(self, sound_file, rate = 16000, dev_pid = 1537):
        with open(sound_file, 'rb') as fp:
            # 识别本地文件
            return self.client.asr(fp.read(), 'pcm', rate, {'dev_pid': dev_pid,})
        
        return None


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

#########  百度语音合成库使用说明  #################
# baidu_word_2_sound类提供：初始化方法和文字语音合成方法
# init初始化方法：
#        需要传入百度AI应用提供的APP_ID、API_KEY和SECRET_KEY
# trans_word_to_sound语音合成方法： 
#        待合成的文字，注意用用单引号包裹文字，例如：'要合成的文字'
#        合成后语音保存文件名，注意用用单引号包裹文字，例如：'auido.mp3'
#################################################

#########  调用方式举例  #################
# from playsound import playsound
# 
# """ 我的 APPID AK SK """
# APP_ID = '20114704'
# API_KEY = 'Lwd56jic7ZvTon8PsYyZ5DfG'
# SECRET_KEY = 'EnNdR4Vr0HgATxz7LiHEDx3dKfLkWFGj'
# 
# if __name__ == "__main__":
#   try:
#         baidu_word_2_sound(APP_ID, API_KEY, SECRET_KEY)
#         baidu_word_2_sound.trans_word_to_sound('淘淘，要听奶奶的话','sound.mp3')
#        
#       playsound('sound.mp3')
#     except KeyboardInterrupt:
#        print("任务被终止了")
#################################################        

from aip import AipSpeech

class baidu_word_2_sound(object):
    
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
        
    def trans_word_to_sound(self, word, sound_file, sound_speed = 5, \
                            sound_tune = 5, sound_volume = 5, sound_type = 0):
        #进行语音合成
        result  = self.client.synthesis(word, 'zh', 1, {
            'spd' : sound_speed,'pit':sound_tune,'vol': sound_volume,'per':sound_type
        })

        # 识别正确返回语音二进制 错误则返回dict 参照下面错误码
        if not isinstance(result, dict):
            with open(sound_file, 'wb') as f:
                f.write(result)


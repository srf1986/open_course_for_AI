#!/usr/bin/env python
# coding: utf-8

# In[2]:


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

#导入标准库
import sys
import os

#导入自定义库
sys.path.append('../../baidu_api_lib')
from baidu_sound import baidu_word_2_sound

""" 公开课的语音合成+人脸识别，可选更改为自己的api接口 """
APP_ID = '20558036'
API_KEY = 'u3L19UyWw6Tmx8fvnkqufP4y'
SECRET_KEY = '7VjAOyufSVY3IjlM6WV79xrhtivGwO8O'

#阅读的内容
rd_poem = ["李白诗集","早发白帝城。朝辞白帝彩云间，千里江陵一日还。两岸猿声啼不住，轻舟已过万重山。"]
 
if __name__ == "__main__":
    try:
        #传入百度AI的参数
        word_2_sound = baidu_word_2_sound(APP_ID, API_KEY, SECRET_KEY)
            
        #以迭代方式阅读
        for one_poem in rd_poem:
            #进行语音合成
            word_2_sound.trans_word_to_sound(one_poem,'tst_sound.mp3')

            #播放合成的语音
            os.system('mplayer ' + 'tst_sound.mp3')
        
        #删除临时文件    
        os.remove('tst_sound.mp3')
        
    except KeyboardInterrupt:
        print("任务被终止了")

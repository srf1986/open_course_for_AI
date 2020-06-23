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
from playsound import playsound

#导入自定义库
sys.path.append('../../baidu_api_lib')
import voice_record

if __name__ == "__main__":
    try:
        #进行麦克风录音
        voice_record.recording("voice_test.mp3", 5)
        
        #播放录制的声音
        os.system('mplayer ' + 'voice_test.mp3')
    
        #删除临时文件
        os.remove("voice_test.mp3")
        
    except KeyboardInterrupt:
        print("任务被终止了")


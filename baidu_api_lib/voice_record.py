#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# -*- coding: utf-8 -*-
# @Time    : 18-10-16 下午12:20
# @Author  : Felix Wang

import pyaudio
import numpy as np
from scipy import fftpack
import wave
from playsound import playsound
import time

###############  MAC录音功能说明  ################
# recording方法包含3个参数，
#     filename : 录音后，声音存储到的文件名
#     time     : 录音的时间，0为不限定时间，根据声音是否结束来停止
#                          不为0的值，录制x秒
#     threshold: 麦克风停止录音的门限值，默认为7000
# init初始化方法：
#        需要传入百度AI应用提供的APP_ID、API_KEY和SECRET_KEY
# speech_2_word语音识别方法： 
#        识别的音频文件名，格式为.mp3
#################################################

#########  调用方式举例  #################
#导入标准库
# import sys
# import os
# from playsound import playsound

# #导入自定义库
# sys.path.append('../../baidu_api_lib')
# import voice_record

# if __name__ == "__main__":
#     try:
#         #进行麦克风录音
#         voice_record.recording("voice_test.mp3", 0, 8000)
        
#         #播放录制的声音
#         playsound("voice_test.mp3")
    
#         #删除临时文件
#         os.remove("voice_test.mp3")
        
#     except KeyboardInterrupt:
#         print("任务被终止了")
#################################################

# 录音
# 录音必须安装portaudio模块，否则会报错
# http://portaudio.com/docs/v19-doxydocs/compile_linux.html
def recording(filename, time=0, threshold=7000):
    """
    :param filename: 文件名
    :param time: 录音时间,如果指定时间，按时间来录音，默认为自动识别是否结束录音
    :param threshold: 判断录音结束的阈值
    :return:
    """
    CHUNK = 512  # 块大小
    FORMAT = pyaudio.paInt16  # 每次采集的位数
    CHANNELS = 1  # 声道数
    RATE = 44100  # 采样率：每秒采集数据的次数
    RECORD_SECONDS = time  # 录音时间
    WAVE_OUTPUT_FILENAME = filename  # 文件存放位置
    p = pyaudio.PyAudio()
    stream = p.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True, frames_per_buffer=CHUNK)
    print("* 录音中...")
    frames = []
    if time > 0:
        for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
            data = stream.read(CHUNK)
            frames.append(data)
    else:
        stopflag = 0
        stopflag2 = 0
        while True:
            data = stream.read(CHUNK)
            rt_data = np.frombuffer(data, np.dtype('<i2'))
            # print(rt_data*10)
            # 傅里叶变换
            fft_temp_data = fftpack.fft(rt_data, rt_data.size, overwrite_x=True)
            fft_data = np.abs(fft_temp_data)[0:fft_temp_data.size // 2 + 1]

            # 测试阈值，输出值用来判断阈值
            # print(sum(fft_data) // len(fft_data))

            # 判断麦克风是否停止，判断说话是否结束，# 麦克风阈值，默认7000
            if sum(fft_data) // len(fft_data) > threshold:
                stopflag += 1
            else:
                stopflag2 += 1
            oneSecond = int(RATE / CHUNK)
            if stopflag2 + stopflag > oneSecond:
                if stopflag2 > oneSecond // 3 * 2:
                    break
                else:
                    stopflag2 = 0
                    stopflag = 0
            frames.append(data)
    print("* 录音结束")
    stream.stop_stream()
    stream.close()
    p.terminate()
    with wave.open(WAVE_OUTPUT_FILENAME, 'wb') as wf:
        wf.setnchannels(CHANNELS)
        wf.setsampwidth(p.get_sample_size(FORMAT))
        wf.setframerate(RATE)
        wf.writeframes(b''.join(frames))


#!/usr/bin/env python
# coding: utf-8

# In[11]:


#使用的模块
import os
import sys

#发送测试命令
cmd = "ping www.baidu.com -c 3"
rst = os.system(cmd)

#输出测试结果
if rst == 0:
    print("网络连接正常")
    return 0
else:
    print("!!!网络异常，请检查无线wifi连接")
    
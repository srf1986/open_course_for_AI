#!/bin/sh

chmod +x  ./word_2_sound_prog.py

echo 
echo "进行网络测试"
echo 
./word_2_sound_prog.py "进行网络测试"
sudo ping www.baidu.com -c 3
if [ $? -eq 0 ]
then
    ./word_2_sound_prog.py "网络测试成功"
fi

echo 
echo 
echo "进行喇叭测试"
echo 
echo 
./word_2_sound_prog.py "开始喇叭测试，确认是否能听到声音"
cd 2.喇叭测试
chmod +x ./speaker_test.py
./speaker_test.py
cd ..

echo 
echo 
echo "进行摄像头测试"
echo 
echo 
./word_2_sound_prog.py "进行摄像头测试，是否能看到摄像头图像，10s后摄像头自动关闭"
chmod +x ./3.摄像头测试/camera_test.py
./3.摄像头测试/camera_test.py

echo 
echo 
echo "进行麦克风测试"
echo 
echo 
./word_2_sound_prog.py "进行麦克风测试，请说一句话"
cd 4.麦克风测试/
chmod +x ./microphone_test.py
sleep 1
./microphone_test.py
cd ..

echo 
echo 
echo "全部测试完成"
echo 
echo 
./word_2_sound_prog.py "全部测试完成"

#删除临时文件
rm *.mp3

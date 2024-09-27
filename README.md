# ClubK

## 说明

ClubK是基于python编写的简易xss测试平台，本项目仅供学习交流使用，不得用于任何非法用途。

## 配置

1. clone到本地后使用`pip install -r requirements.txt`安装所需的库。

2. 在config更改HOST，也就是接受地址，**必须加上http协议头**。

3. 默认端口为5000，可根据需要自行更改。

## 使用

直接运行ClubK即可，接受到的cookie会下载到cookies目录下，文件名即为目标地址。
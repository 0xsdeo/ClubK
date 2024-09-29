# ClubK

```markdown
 _____   _           ___   _____   _   _   
/  ___| | |         /   | |  _  \ | | / /  
| |     | |        / /| | | |_| | | |/ /   
| |     | |       / / | | |  _  { | |\ \   
| |___  | |___   / /  | | | |_| | | | \ \  
\_____| |_____| /_/   |_| |_____/ |_|  \_\ 
```

## 说明

ClubK是基于python3编写的简易xss测试平台。

**该工具仅供学习、学术研究、合法渗透测试和网络安全教育使用，在任何情况下，不得用于任何非法目的，造成的任何问题皆与本库开发者无关。**

## 配置

1. clone到本地后使用`pip install -r requirements.txt`安装所需的库。

2. 在config更改HOST，也就是接受地址，**必须加上协议头**。

3. 默认端口为5000，可根据需要自行更改。

4. 如有配置ssl需求，需在根目录创建ssl文件夹，然后将ssl证书下载至此，接着在config填充pem和key文件地址，例如：`r'ssl/xxx.online_bundle.pem'`、`r'ssl/xxx.online.key'`。

5. 如有配置钉钉机器人需求，请先查阅钉钉官方文档查看如何创建机器人：`https://open.dingtalk.com/document/orgapp/custom-robot-access`，需要注意的是创建机器人时安全设置需要设置为**加签**模式，然后将机器人的Webhook和secret填充到config即可。
## 使用

直接运行ClubK即可，接受到的cookie会下载到cookies目录下，文件名即为目标地址。

>配置ssl后启用https

```shell
python ClubK.py -s 或 python ClubK.py --ssl
```

>启用钉钉机器人

```shell
python ClubK.py --ding
```

## 效果

![1727613129369](image/README/1727613129369.png)
![1727613168635](image/README/1727613168635.png)

## Tips

如果启用了钉钉机器人，需要注意的是**每个机器人每分钟最多发送20条消息到群里**，超过20条不会继续发送。
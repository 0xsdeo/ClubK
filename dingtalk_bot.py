# -*- coding: UTF-8 -*-
# @Project ：Tools 
# @File    ：dingtalk_bot.py
# Author   ：0xsdeo
# Date     ：2024/9/29 16:02
from dingtalkchatbot.chatbot import DingtalkChatbot
from config import dingtalk_bot_Webhook, dingtalk_bot_secret


def boot(msg):
    try:
        # 初始化机器人小丁
        bot = DingtalkChatbot(dingtalk_bot_Webhook, secret=dingtalk_bot_secret)
        # Text消息@所有人
        bot.send_text(msg=msg, is_at_all=True)
    except:
        print("钉钉机器人配置错误")
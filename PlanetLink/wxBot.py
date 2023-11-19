#!/usr/bin python
# -*- coding: utf-8 -*-

######
#	Filename: wxBot.py
#	Created by vu1nex on 2022/09/23 21:20:09
#   Description: To send content message to wechat
#   Version: 0.0.1
#
######

# import modules
import requests
from PlanetLink.wxMessage import wxMessage

class wxBot:
    # define variable
    corpid = ""
    corpsecret = ""
    token = ""
    wxMessageDemo = ""
    agentid = ""

    # init veriable
    def initBot(self,corpid,corpsecret,agentid,title,sign):
        self.corpid = corpid
        self.corpsecret = corpsecret
        self.agentid = agentid
        self.wxMessageDemo = wxMessage(title,sign)

    # define function
    # get send message token
    def getToken(self):
        # function variable
        # get request url
        url = "https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid="+self.corpid+"&corpsecret="+self.corpsecret

        # get token and save it to global variable token
        r = requests.get(url)
        if (r.status_code == 200):
            self.token = r.json()['access_token']
            print("get token success")
        else:
            print("error")

    # send message
    def sendMessage(self):
        # function variable
        url = "https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token="+self.token
        data = {
            "touser": "@all",
            "toparty": "@all",
            "totag": "@all",
            "msgtype": "text",
            "agentid": self.agentid,
            "text": {
                "content": self.wxMessageDemo.getSendMessage()
            },
            "safe": 0,
            "enable_id_trans": 0,
            "enable_duplicate_check": 0
        }

        print("Message:",self.wxMessageDemo.getSendMessage())

        # send message to wxRobot 
        r = requests.post(url, json=data)

        if (r.json().get("errcode") == 0):
            print("send message success")
        else:
            print("error")

    # get token, format message and send message
    def send(self):
        self.getToken()
        self.wxMessageDemo.formatMessage()
        self.sendMessage()

    # add content
    def addContent(self,content):
        self.wxMessageDemo.addContent(content)

    # get send message
    def getSendMessage(self):
        return self.wxMessageDemo.getSendMessage()
    
    # clear content
    def clearContent(self):
        self.wxMessageDemo.clearContent()
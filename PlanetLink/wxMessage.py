#!/usr/bin python
# -*- coding: utf-8 -*-

######
#	Filename: wxMessage.py
#	Created by vu1nex on 2022/09/24 13:43:31
#   Description: weChat message class
#
######

# import modules
import time

# define class
class wxMessage:
    # define variable
    message = {
        "time": "",
        "title": "",
        "sign": "",
        "remark":"",
        "content": [],
        "sendMessage": ""
    }

    # define function
    # defaule constructor
    def __init__(self,title = "INFO",sign = "INFO"):
        self.message["time"] = self.generateTime()
        self.setTitle(title)
        self.setSign(sign)

    # add time to message.time
    def generateTime(self):
        #get current time in format of yyyy-mm-dd hh:mm:ss
        return time.strftime("[%Y-%m-%d %H:%M:%S]", time.localtime())

    # set message's title
    def setTitle(self, title):
        self.message["title"] = title

    # set message's sign
    def setSign(self, sign):
        if sign =="WARNING":
            self.message["sign"] = "⚠️"
        elif sign =="ERROR":
            self.message["sign"] = "❌"
        elif sign =="COMPLETE":
            self.message["sign"] = "✅"
        elif sign =="INFO":
            self.message["sign"] = "ℹ️"
        else:
            self.message["sign"] = "⛔"

    # add content to message.content[]
    def addContent(self, content):
        self.message["content"].append(content)

    # function to generate message
    def formatMessage(self):
        # different delimiter for different platform
        delimiter = "-------------------------------------"
        delimiter2 = "========================"
        delimiter3 = "********************************"
        delimiter4 = "#####################"

        # format message's front part
        self.message["sendMessage"] = self.message["sign"]+" "+self.message["title"]+"\n"+self.message["time"]+"\n"
        self.message["sendMessage"] += delimiter2 + "\n"
        
        # format content in list
        for i in range(len(self.message["content"])):
            self.message["sendMessage"] += self.message["content"][i]+"\n"
            self.message["sendMessage"] += delimiter+"\n"

        # delete last newline
        self.message["sendMessage"] = self.message["sendMessage"][:-1]
    
    # get sendMessage
    def getSendMessage(self):
        return self.message["sendMessage"]
    
    # clear content
    def clearContent(self):
        self.message["content"] = []

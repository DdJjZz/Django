# -*- coding: utf-8 -*-
# @Time    : 2018/6/28 10:13
# @Author  : DJZ
# @Site    : 
# @File    : ModAccessHttpHandler.py
# @Software: PyCharm
import time
import sys
import os
import django
sys.path.append('../DjoSiteDba2')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "DjoSiteDba2.settings")
django.setup()
from DjoSiteDba import views
import json
from http.server import BaseHTTPRequestHandler
class ClassEnrtyHttpHandler:
    def __init__(self):
        pass
class ClassHttpRequestGenernalHandler(BaseHTTPRequestHandler):
    def _writeheaders(self):
        self.send_response(200)
        self.send_header('Content-type','text/html')
        self.end_headers()
    def do_Head(self):
        self._writeheaders()
    def do_GET(self):
        self._writeheaders()
        self.wfile.write(bytes("""<!DOCTYPE HTML>
        <html lang="en-US">
        <head>
        <meta charset="UTF-8">
        <title>HUIREST SERVICE - GET</title>
        </head>
        <body>
        <p>this is get!</p>
        </body>
        </html>"""+str(self.headers), "UTF-8"))
    def do_POST(self):
        self._writeheaders()
        length=self.headers.get('content-length')
        nbytes=int(length)
        inputData=self.rfile.read(nbytes)
        jsonInput=json.loads(inputData)
        # aa=views.login(jsonInput)
        print("[", time.asctime(time.localtime(time.time())), "HUIREST]: Receiving Post Data Buf = ", jsonInput)
        # return aa
        m=[]
        ret = {'key': '123456'}
        m.append(ret)
        ss=json.dumps(m)
        self.wfile.write(bytes(ss, "UTF-8"))

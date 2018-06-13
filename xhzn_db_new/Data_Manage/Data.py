# -*- coding: utf-8 -*-
def Hello_world():
    print("HELLO WORLD")
def aaa(aa):
    action = aa.POST.get('action')
    user = aa.POST.get('body[username]')
    pwd = aa.POST.get('body[password]')
    print(action,user,pwd)
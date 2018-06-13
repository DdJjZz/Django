# -*- coding: utf-8 -*-
from django.shortcuts import render,HttpResponse
import json
from Data_Manage import Data
# Create your views here.
def login(request):
    return render(request,'Login.html')
def ajax(request):
    if request.method =='POST':
        ret={'status':False,'msg':''}
        Data.aaa(request)
        print(request.body)
        action=request.POST.get('action')
        user=request.POST.get('body[username]')
        pwd=request.POST.get('body[password]')
        if user == 'root' and pwd == '123456ding':
            ret['status'] = True
            ret['msg']='用户登录成功'
        else:
            ret['msg']='用户名或密码错误'
        return  HttpResponse(json.dumps(ret))
    return render(request,'Login.html')
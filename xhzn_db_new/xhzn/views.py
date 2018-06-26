# -*- coding: utf-8 -*-
from django.shortcuts import render,HttpResponse
import json
from Data_Manage import Data
import hashlib
from xhzn.models import t_l3f1sym_menu_code_mapping as menu,t_l3f1sym_account_primary as account
# Create your views here.
def login(request):
    return render(request,'Login.html')
def ajax1(request):
    if request.method =='POST':
        ret={'status':False,'msg':''}
        Data.aaa(request)
        print(request.body)
        # action=request.POST.get('action')
        user=request.POST.get('body[username]')
        pwd=request.POST.get('body[password]')
        hl = hashlib.md5()
        hl.update(pwd.encode(encoding='utf-8'))
        pwd=hl.hexdigest()
        user_login=account.objects.filter(login_name=user,pass_word=pwd)
        if user_login.exists():
            ret['status'] = True
            ret['msg'] = '用户登录成功'
        else:
            ret['msg']='用户名或密码错误'
        return  HttpResponse(json.dumps(ret))
    return render(request,'Login.html')
def ajax(request):
    if request.method=='POST':
        menu=Data.code()
        ret={'status':menu,'ret':True}
        return HttpResponse(json.dumps(ret))
    return render(request,"Management.html")

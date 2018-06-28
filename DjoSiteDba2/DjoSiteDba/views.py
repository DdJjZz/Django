from django.shortcuts import render,HttpResponse
import json

# Create your views here.
def login(request):
    ret = {'key': '123456'}
    return HttpResponse(json.dumps(ret))
    # return render(request, "Login.html")
def request(request):
    ret={'key':'123456'}
    back={'status':'true','ret':ret,'msg':'Hello World'}
    if request.method == "GET":
        action=request.GET['action']
        if(action=='login'):
            print("Hello World")
        print(request)
        print(request.GET)
        print('--------------')
        print(request.GET['action'])
        print('--------------')
        print(json.dumps(back))
        return HttpResponse(json.dumps(back))
    if request.method=='POST':
        action=request.POST.get["action"]
    return render(request, "LostPassword.html")
def loss(request):
    if request.method == "GET":
        print(request)
        print(request.GET)
    return render(request, "LostPassword.html")
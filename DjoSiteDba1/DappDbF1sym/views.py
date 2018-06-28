from django.shortcuts import render
import datetime
import time
# Create your views here.
def show():
    print(int(time.time()))
if __name__=="__main__":
    show()
from django.shortcuts import render
from DappDbF1sym.models import dct_t_l3f1sym_user_login_session
import random
import datetime
import time
# Create your views here.
def __dft_getRandomsid(strlen):
    str_array=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y']
    sid=''.join(random.sample(str_array,strlen))
    return sid
def __dft_getRandomUid(strlen):
    str_array=['0','1','2','3','4','5','6','7','8','9']
    uid=''.join(random.sample(str_array,strlen))
    return uid
def __dft_updateSession(uid,sessionid):
    now_time=int(time.time())
    result=dct_t_l3f1sym_user_login_session.objects.filter(uid=uid)
    if result.exists():
        result=dct_t_l3f1sym_user_login_session.objects.filter(uid=uid).update(session_id=sessionid,timestamp=now_time)
    else:
        result=dct_t_l3f1sym_user_login_session(uid=uid,session_id=sessionid,timestamp=now_time)
        result.save()
    return result
def dft_dbi_session_check(sessionid):
    result=dct_t_l3f1sym_user_login_session.objects.filter(session_id=sessionid)
    return 
print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
print(int(time.time()))
    
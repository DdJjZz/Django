# -*- coding: utf-8 -*-
# @Time    : 2018/6/15 10:12
# @Author  : DJZ
# @Site    : 
# @File    : DataInsert.py
# @Software: PyCharm
faam1={
    'menu':{
        0x0101:"UserManage",
        0x0102:"ParaManage",
        0x0103:"menu_user_profile",
        0x0104:"ExportTableManage",
        0x0105:"SoftwareLoadManage",

        0x0201:"PGManage",
        0x0202:'ProjManage',
        0x0203:'MPManage',
        0x0204:'DevManage',
        0x0205:'KeyManage',
        0x0206:'KeyAuth',
        0x0207:'KeyHistory',

        0x0301:"MPMonitor",
        0x0302:"MPStaticMonitorTable",
        0x0303:"MPMonitorCard",

        0x0401:"InstConf",
        0x0402:"InstRead",
        0x0403:"InstDesign",
        0x0404:"InstControl",
        0x0405:"InstSnapshot",
        0x0406:"InstVideo",

        0x0501:"WarningCheck",
        0x0502:"WarningHandle",
        0x0503:"WarningLimit",

        0x0601:"AuditTarget",
        0x0602:"AuditStability",
        0x0603:"AuditAvailability",
        0x0604:"AuditError",
        0x0605:"AuditQuality",

        0x0701:"ADConf",
        0x0702:"ADManage",
        0x0703:"WEBConf",

        0x0901:"GeoInfoQuery",
        0x0902:"GeoTrendAnalysis",
        0x0903:"GeoDisaterForecast",
        0x0904:"GeoEmergencyDirect",
        0x0905:"GeoDiffusionAnalysis",

        0x0A01:"SoftwareLoadManage",
        0x0A02:"AttendanceManage",
        0x0A03:"FactoryManage",
        0x0A04:"SpecificationManage",
        0x0A05:"AssembleManage",
        0x0A06:"AssembleAudit",
        0x0A07:"AttendanceAudit",
        0x0A08:"KPIAudit",
        0x0A09:"ConsumablesManage",
        0x0A0A:"ConsumablesHistory",
        0x0A0B:"ProductStorageManage",
        0x0A0C:"ProductDeliveryManage",
        0x0A0D:"MaterialStorageManage",
        0x0A0E:"MaterialDeliveryManage",
        0x0A0F:"SeafoodInfo",
        0x0A10:"SeafoodAudit",
    },
    'action':{
        0x0101:'login',
        0x0102:'Get_user_auth_code',
        0x0103:'Reset_password',
        0x0120:'UserInfo',
        0x0121:'UserNew',
        0x0122:'UserMod',
        0x0123:'UserDel',
        0x0124:	'UserTable',

        0x0201:	'PGNew',
        0x0202:	'PGMod',
        0x0203:	'PGDel',
        0x0204:	'PGTable',
        0x0205:	'PGProj',
        0x0206:	'ProjectPGList',
        0x0220:	'ProjectList',
        0x0221:	'UserProj',
        0x0222:	'ProjTable',
        0x0223:	'ProjPoint',
        0x0224:	'ProjNew',
        0x0225:	'ProjMod',
        0x0226:	'ProjDel',
        0x0240:	'PointProj',
        0x0241:	'PointTable',
        0x0242:	'PointNew',
        0x0243:'PointMod',
        0x0244:	'PointDel',
        0x0245:	'PointDev',
        0x0260:	'DevTable',
        0x0261:	'DevNew',
        0x0262:	'DevMod',
        0x0263:	'DevDel',
        0x0264:	'GetStationActiveInfo',
        0x0265:	'StationActive',
        0x0266:	'TableQuery',
        0x0267:	'ProductModel',

        0x0268:	'PointConf',
        0x0269:	'PointLogin',
        0x02A0:	'UserKey',
        0x02A1:	'ProjKeyList',
        0x02A2:	'ProjKey',
        0x02A3:	'ProjUserList',
        0x02A4:	'KeyTable',
        0x02A5:	 'KeyNew',
        0x02A6:	 'KeyMod',
        0x02A7:	 'KeyDel',
        0x02A8:	'DomainAuthlist',
        0x02A9:	'KeyAuthlist',
        0x02AA:	'KeyGrant',
        0x02AB:	 'KeyAuthNew',
        0x02AC:	'KeyAuthDel',

        0x0301:	 'DevSensor',
        0x0302:	 'SensorList',
        0x0303:	'MonitorList',
        0x0304:	'FakeMonitorList',
        0x0305:	'Favourite_list',
        0x0306:	'Favourite_count',
        0x0307:	'GetStaticMonitorTable',
        0x0308:	'PointPicture',
        0x0320:	'KeyHistory',
        0x0321:	'GetOpenImg',

        0x0401:	'SensorUpdate',
        0x0401:	'GetVideoCameraWeb',
        0x0401:	'GetVideoList',
        0x0401:	'GetVideo',
        0x0401:	'GetCameraStatus',
        0x0401:	'GetCameraUnit',
        0x0401:	'CameraVAdj',
        0x0401:	'CameraHAdj',
        0x0401:	'CameraZAdj',
        0x0401:	'CameraReset',
        0x0401:	'GetCameraStatus',
        0x0401:	'OpenLock',

        0x0501:	'MonitorAlarmList',
        0x0502:	'DevAlarm',
        0x0503:	'AlarmType',
        0x0504:	'AlarmQuery',
        0x0505:	'AlarmQueryRealtime',
        0x0506:	'GetWarningHandleListTable',
        0x0507:	'GetWarningImg',
        0x0508:	'AlarmHandle',
        0x0509:	'AlarmClose',
        0x050A:	'GetHistoryRTSP',

        0x0601:	'GetAuditStabilityTable',

        0x0701:	'SetUserMsg',
        0x0702:	'GetUserMsg',
        0x0703:	'ShowUserMsg',
        0x0704:	'GetUserImg',
        0x0705:	'ClearUserImg',

        0x0A01:	'AttendanceAudit',
        0x0A02:	'AttendanceMod',
        0x0A03:	'KPIAudit',
        0x0A04:	'StaffDel',
        0x0A05:	'ConsumablesPurchaseNew',
        0x0A06:	'ConsumablesTable',
        0x0A07:	'ConsumablesHistory',
        0x0A08:	'GetConsumablesPurchase',
        0x0A09:	'ConsumablesPurchaseMod',
        0x0A0A:	'ConsumablesPurchaseDel',
        0x0A0B:	'ProductStockNew',
        0x0A0C:	'GetProductWeightAndSize',
        0x0A0D:	'GetProductStockList',
        0x0A0E:	'GetProductEmptyStock',
        0x0A0F:	'ProductStockTable',
        0x0A10:	'ProductStockDel',
        0x0A11:	'GetProductStockDetail',
        0x0A12:	'ProductStockTransfer',
        0x0A13:	'ProductStockHistory',
        0x0A14:	'MaterialStockNew',
        0x0A15:	'GetMaterialStockList',
        0x0A16:	'GetMaterialEmptyStock',
        0x0A17:	'MaterialStockDel',
        0x0A18:	'MaterialStockTable',
        0x0A19:	'GetMaterialStockDetail',
        0x0A1A:	'MaterialStockIncomeNew',
        0x0A1B:	'MaterialStockRemovalNew',
        0x0A1C:	'MaterialStockHistory',
        0x0A1D:	'GetMaterialStockHistoryDetail',
        0x0A1E:	'MaterialStockIncomeMod',
        0x0A1F:	'MaterialStockRemovalMod',
        0x0A20:	'MaterialStockRemovalDel',
        0x0A21:	'GetProductStockHistoryDetail',
        0x0A22:	'ProductStockRemovalMod',
        0x0A23:	'ProductStockRemovalDel',
        0x0A24:	'ProductStockRemovalNew',
        0x0A30:	'SeafoodInfo',
        0x0A31:	'SeafoodAudit',
    }
}
# print(len(faam1))
# print(len(faam1['menu']))
# print(len(faam1['action']))
# for key in faam1['menu']:
#     print(key)
#     print(faam1['menu'][key])
import os
import hashlib
os.environ['DJANGO_SETTINGS_MODULE']='xhzn_db_new.settings'
import django
django.setup()
from xhzn.models import t_l3f1sym_menu_code_mapping as map,t_l3f1sym_account_primary as account,t_l3f1sym_user_right_menu as right_menu
def insert_map(code,name):
    Map=map(menu_code=code,menu_name=name)
    Map.save()
    return
def delete_map():
    Map=map.objects.filter().delete()
    return
def insert_user():
    h1=hashlib.md5()
    name='admin'
    str='admin'
    h1.update(str.encode(encoding='utf-8'))
    pwd=h1.hexdigest()
    uid='MID0000002'
    email='111@qq.com'
    grade_level=1
    Account=account(uid=uid,login_name=name,pass_word=pwd,email=email,grade_lever=grade_level)
    Account.save()
def update_user():
    Account=account.objects.get(uid='MID0000001')
    Account.menu_group=1
    Account.save()
def select_menu():
    menu=map.objects.filter().all()
    return menu
def auth_menu(line,group):
    Auth=right_menu(menu_name=line.menu_name,menu_code=line,menu_group=group)
    Auth.save()
if __name__ == '__main__':
    print('Work Start')
    a="admin123"
    hl=hashlib.md5()
    hl.update(a.encode(encoding='utf-8'))
    print(hl.hexdigest())
    # delete_map()
    # for key in faam1['menu']:
    #     print(faam1['menu'][key])
    #     print(key)
    #     insert_map(faam1['menu'][key],key)

    # insert_user()

    # update_user()

    # menu=select_menu()
    # for line in menu:
    #     auth_menu(line,1)
    print('Work End')

# import threading
# from time import ctime,sleep
#
#
# def music(func):
#     for i in range(2):
#         print ("I was listening to %s. %s" %(func,ctime()))
#         sleep(1)
#
# def move(func):
#     for i in range(2):
#         print("I was at the %s! %s" %(func,ctime()))
#         sleep(5)
#
# threads = []
# t1 = threading.Thread(target=music,args=(u'爱情买卖',))
# threads.append(t1)
# t2 = threading.Thread(target=move,args=(u'阿凡达',))
# threads.append(t2)
#
# if __name__ == '__main__':
#     for t in threads:
#         t.setDaemon(True)
#         t.start()
#
#     print ("all over %s" %ctime())
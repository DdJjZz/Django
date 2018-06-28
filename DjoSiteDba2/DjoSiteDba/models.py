from django.db import models
import time
# Create your models here.
class dct_t_l3f1sym_account_primary(models.Model):
    uid=models.CharField(max_length=15,primary_key=True)
    login_name=models.CharField(max_length=20,db_index=True)
    pass_word=models.CharField(max_length=100)
    email=models.EmailField(null=True,blank=True)
    menu_group=models.IntegerField(default=0)
    grade_lever=models.IntegerField(null=True,blank=True)
    red_date=models.DateTimeField(auto_now_add=True)
class dct_t_l3f1sym_account_secondary(models.Model):
    CHOICES=((1,'男'),(2,'女'),(3,'第三人'))
    uid=models.OneToOneField(dct_t_l3f1sym_account_primary,on_delete=models.CASCADE,primary_key=True)
    nick_name=models.CharField(max_length=20,null=True,blank=True)
    true_name=models.CharField(max_length=20,null=True,blank=True)
    gender=models.IntegerField(choices=CHOICES)
    age=models.IntegerField(null=True,blank=True)
    telephone=models.CharField(max_length=11,null=True,blank=True)
    city=models.CharField(max_length=20,null=True,blank=True)
class dct_t_l3f1sym_menu_code_mapping(models.Model):
    menu_code=models.IntegerField(primary_key=True)
    menu_name=models.CharField(max_length=20)
class dct_t_l3f1sym_user_right_menu(models.Model):
    sid=models.AutoField(primary_key=True)
    menu_group=models.IntegerField(default=0)
    menu_code=models.ForeignKey(dct_t_l3f1sym_menu_code_mapping,on_delete=models.CASCADE)
    menu_name=models.CharField(max_length=20)
class dct_t_l3f1sym_user_right_action(models.Model):
    sid=models.AutoField(primary_key=True)
    action_code = models.IntegerField(unique=True)
    action_name=models.CharField(max_length=20)
    l1_auth = models.BooleanField(default=0,blank=True)
    l2_auth = models.BooleanField(default=0,blank=True)
    l3_auth = models.BooleanField(default=0,blank=True)
    l4_auth = models.BooleanField(default=0,blank=True)
    l5_auth = models.BooleanField(default=0,blank=True)
class dct_t_l3f1sym_user_right_project(models.Model):
    sid=models.AutoField(primary_key=True)
    uid=models.ForeignKey(dct_t_l3f1sym_account_primary,on_delete=models.CASCADE)
    auth_type=models.IntegerField(default=0)
    auth_code=models.IntegerField(default=0)
class dct_t_l3f1sym_user_login_session(models.Model):
    uid=models.OneToOneField(dct_t_l3f1sym_account_primary,primary_key=True,on_delete=models.CASCADE)
    session_id=models.CharField(max_length=10)
    timestamp = models.IntegerField(verbose_name="更新时间戳", default=time.time())

class dct_t_l3f2cm_pg_common(models.Model):
    pg_code = models.AutoField(primary_key=True)
    pg_name = models.CharField(max_length=20)
    pg_creator = models.CharField(max_length=10)
    create_date = models.DateTimeField(auto_now=True, blank=True)
    superintendent = models.CharField(max_length=20, null=True, blank=True)
    telephone = models.CharField(max_length=15, null=True, blank=True)
    department = models.CharField(max_length=50, null=True, blank=True)
    address = models.CharField(max_length=50, null=True, blank=True)
    comments = models.TextField(null=True)


class dct_t_l3f2cm_project_common(models.Model):
    prj_code = models.AutoField(primary_key=True)
    prj_name = models.CharField(max_length=20)
    pg_code = models.ForeignKey(dct_t_l3f2cm_pg_common, on_delete=models.CASCADE)
    prj_creator = models.CharField(max_length=10)
    create_date = models.DateTimeField(auto_now=True)
    superintendent = models.CharField(max_length=20, null=True, blank=True)
    telephone = models.CharField(max_length=15, null=True, blank=True)
    department = models.CharField(max_length=50, null=True, blank=True)
    address = models.CharField(max_length=50, null=True, blank=True)
    comments = models.TextField(null=True)


class dct_t_l3f2cm_site_common(models.Model):
    site_code = models.AutoField(primary_key=True)
    site_name = models.CharField(max_length=20)
    prj_code = models.ForeignKey(dct_t_l3f2cm_project_common, on_delete=models.CASCADE)
    site_creator = models.CharField(max_length=10)
    create_date = models.DateTimeField(auto_now=True)
    superintendent = models.CharField(max_length=20, null=True, blank=True)
    telephone = models.CharField(max_length=15, null=True, blank=True)
    address = models.CharField(max_length=50, null=True, blank=True)
    longitude = models.DecimalField(max_digits=10, decimal_places=6)
    latitude = models.DecimalField(max_digits=10, decimal_places=6)
    comments = models.TextField(null=True, blank=True)


class dct_t_l3f2cm_device_common(models.Model):
    # null=true显示的是数据库中该字段可以为空，blank=true表示在admin后台管理界面上该字段可以不填
    dev_code = models.CharField(max_length=20, primary_key=True)
    site_code = models.ForeignKey(dct_t_l3f2cm_site_common, on_delete=models.CASCADE)
    create_date = models.DateTimeField(auto_now=True)
    socket_id = models.IntegerField(null=True, blank=True)
    hw_type = models.IntegerField(null=True, blank=True)
    hw_ver = models.IntegerField(null=True, blank=True)
    sw_rel = models.IntegerField(null=True, blank=True)
    sw_ver = models.IntegerField(null=True, blank=True)


class dct_t_l3f2cm_favour_site(models.Model):
    sid = models.AutoField(primary_key=True)
    uid = models.ForeignKey(dct_t_l3f1sym_account_primary, on_delete=models.CASCADE)
    site_code = models.ForeignKey(dct_t_l3f2cm_site_common, on_delete=models.CASCADE)
    create_time = models.DateTimeField(auto_now=True)


class dct_t_l3f2cm_project_aqyc(models.Model):
    prj_code = models.OneToOneField(dct_t_l3f2cm_project_common, on_delete=models.CASCADE, primary_key=True)
    eng_code = models.CharField(max_length=50)
    eng_name = models.CharField(max_length=50, null=True, blank=True)
    prj_type = models.IntegerField
    prj_category = models.IntegerField
    prj_period = models.IntegerField
    district = models.CharField(max_length=5)
    region = models.IntegerField
    street = models.CharField(max_length=50, null=True, blank=True)
    longitude = models.DecimalField(max_digits=10, decimal_places=6)
    latitude = models.DecimalField(max_digits=10, decimal_places=6)
    contractors = models.CharField(max_length=50, null=True, blank=True)
    eng_addr = models.CharField(max_length=50, null=True, blank=True)
    site_area = models.FloatField(null=True, blank=True)
    building_area = models.FloatField(null=True, blank=True)
    start_date = models.DateTimeField(null=True, blank=True)
    end_date = models.DateTimeField(null=True, blank=True)
    stage = models.CharField(max_length=2, null=True, blank=True)
    is_completed = models.BooleanField(default=0, blank=True)
    eng_status = models.BooleanField(default=1, blank=True)


class dct_t_l3f2cm_device_aqyc(models.Model):
    dev_code = models.ForeignKey(dct_t_l3f2cm_device_common, on_delete=models.CASCADE, primary_key=True)
    ip_addr = models.IPAddressField
    mac_addr = models.CharField(max_length=20)
    cam_url = models.CharField(max_length=100)
    ctrl_url = models.CharField(max_length=100)
    ctrl_port = models.IntegerField
    rtsp_port = models.IntegerField
    service_port = models.IntegerField
    ssh_port = models.IntegerField
    vnc_port = models.IntegerField
    nvr_web_port = models.IntegerField
    nvr_rstp_port = models.IntegerField


class dct_t_l3f2cm_project_fstt(models.Model):
    prj_code = models.OneToOneField(dct_t_l3f2cm_project_common, primary_key=True, on_delete=models.CASCADE)


class dct_t_l3f2cm_site_fstt(models.Model):
    site_code = models.OneToOneField(dct_t_l3f2cm_site_common, primary_key=True, on_delete=models.CASCADE)
    order_no = models.CharField(max_length=10)
    tower_sn = models.CharField(max_length=10)
    tower_code = models.CharField(max_length=15)
    tower_type = models.IntegerField(default=0, blank=True)
    tower_conf = models.IntegerField(default=0, blank=True)
    tower_date = models.DateTimeField(default=0, blank=True)
    install_date = models.DateTimeField(default=0, blank=True)


class dct_t_l3f2cm_device_fstt(models.Model):
    dev_code = models.OneToOneField(dct_t_l3f2cm_device_common, primary_key=True, on_delete=models.CASCADE)
    cam_url = models.CharField(max_length=100)
    ctrl_url = models.CharField(max_length=100)
    ctrl1_port = models.IntegerField
    rtsp1_port = models.IntegerField
    service_port = models.IntegerField
    ssh_port = models.IntegerField
    vnc_port = models.IntegerField
    ctrl2_port = models.IntegerField(null=True, blank=True)
    rtsp2_port = models.IntegerField(null=True, blank=True)
    ctrl3_port = models.IntegerField(null=True, blank=True)
    rtsp3_port = models.IntegerField(null=True, blank=True)

class dct_t_l3f3dm_current_report_aqyc(models.Model):
    sid = models.AutoField(primary_key=True)
    dev_code = models.ForeignKey(dct_t_l3f2cm_device_common, on_delete=models.CASCADE)
    site_code = models.ForeignKey(dct_t_l3f2cm_site_common, on_delete=models.CASCADE)
    report_time = models.DateTimeField(auto_now=True)
    tsp = models.FloatField(default=0,verbose_name="TSP")
    pm01 = models.FloatField(default=0,verbose_name="PM0.1")
    pm25 = models.FloatField(default=0,verbose_name="PM2.5")
    pm10 = models.FloatField(default=0,verbose_name="PM10")
    noise = models.FloatField(default=0,verbose_name="噪声")
    temperature = models.FloatField(default=0, verbose_name="温度")
    humidity = models.FloatField(default=0, verbose_name="湿度")
    winddir = models.FloatField(default=0, verbose_name="风向")
    windspd = models.FloatField(default=0, verbose_name="风速")
    rain = models.FloatField(default=0, verbose_name="雨量")
    airpresure = models.FloatField(default=0, verbose_name="气压")


class dct_t_l3f3dm_minute_report_aqyc(models.Model):
    sid = models.AutoField(primary_key=True)
    dev_code = models.ForeignKey(dct_t_l3f2cm_device_common, on_delete=models.CASCADE)
    site_code = models.ForeignKey(dct_t_l3f2cm_site_common, on_delete=models.CASCADE)
    report_date = models.DateTimeField(auto_now=True)
    hourminindex = models.IntegerField
    tsp = models.FloatField(default=0, verbose_name="TSP")
    pm01 = models.FloatField(default=0, verbose_name="PM0.1")
    pm25 = models.FloatField(default=0, verbose_name="PM2.5")
    pm10 = models.FloatField(default=0, verbose_name="PM10")
    noise = models.FloatField(default=0, verbose_name="噪声")
    temperature = models.FloatField(default=0, verbose_name="温度")
    humidity = models.FloatField(default=0, verbose_name="湿度")
    winddir = models.FloatField(default=0, verbose_name="风向")
    windspd = models.FloatField(default=0, verbose_name="风速")
    rain = models.FloatField(default=0, verbose_name="雨量")
    airpresure = models.FloatField(default=0, verbose_name="气压")


class dct_t_l3f3dm_alarm_report_aqyc(models.Model):
    sid = models.AutoField(primary_key=True)
    dev_code = models.ForeignKey(dct_t_l3f2cm_device_common, on_delete=models.CASCADE)
    site_code = models.ForeignKey(dct_t_l3f2cm_site_common, on_delete=models.CASCADE)
    alarmflag = models.CharField(max_length=1)
    alarmseverity = models.IntegerField(default=0,blank=True)
    alarmcontent = models.IntegerField(default=0,blank=True)
    alarmtype = models.IntegerField(default=0,blank=True)
    clearflag = models.IntegerField(default=0,blank=True)
    causeid = models.IntegerField(default=0,blank=True)
    tsgen = models.DateTimeField(auto_now_add=True)
    tsclose = models.DateTimeField(null=True, blank=True)
    alarmpic = models.CharField(max_length=100)
    alarmproc = models.TextField(max_length=200)


class dct_t_l3f3dm_current_report_fhys(models.Model):
    sid = models.AutoField(primary_key=True)
    dev_code = models.ForeignKey(dct_t_l3f2cm_device_common, on_delete=models.CASCADE)
    site_code = models.ForeignKey(dct_t_l3f2cm_site_common, on_delete=models.CASCADE)
    report_time = models.DateTimeField(auto_now=True)
    door_1 = models.IntegerField
    door_2 = models.IntegerField
    door_3 = models.IntegerField
    door_4 = models.IntegerField
    lock_1 = models.IntegerField
    lock_2 = models.IntegerField
    lock_3 = models.IntegerField
    lock_4 = models.IntegerField
    battstate = models.IntegerField
    waterstate = models.IntegerField
    shakestate = models.IntegerField
    fallstate = models.IntegerField
    smokestate = models.IntegerField
    door_1 = models.IntegerField
    door_1 = models.IntegerField
    door_1 = models.IntegerField
    door_1 = models.IntegerField
    door_1 = models.IntegerField
    door_1 = models.IntegerField
    battvalue = models.FloatField(default=0,blank=True, verbose_name="电池电量值")
    fallvalue = models.FloatField(default=0,blank=True, verbose_name="倾斜角度值")
    tempvalue = models.FloatField(default=0,blank=True, verbose_name="温度值")
    humidvalue = models.FloatField(default=0,blank=True, verbose_name="湿度值")
    rssivalue = models.FloatField(default=0,blank=True, verbose_name="信号强度值")


class dct_t_l3f3dm_minute_report_fhys(models.Model):
    sid = models.AutoField(primary_key=True)
    dev_code = models.ForeignKey(dct_t_l3f2cm_device_common, on_delete=models.CASCADE)
    site_code = models.ForeignKey(dct_t_l3f2cm_site_common, on_delete=models.CASCADE)
    report_date = models.DateTimeField(auto_now=True)
    hourminindex = models.IntegerField
    door_1 = models.IntegerField
    door_2 = models.IntegerField
    door_3 = models.IntegerField
    door_4 = models.IntegerField
    lock_1 = models.IntegerField
    lock_2 = models.IntegerField
    lock_3 = models.IntegerField
    lock_4 = models.IntegerField
    battstate = models.IntegerField
    waterstate = models.IntegerField
    shakestate = models.IntegerField
    fallstate = models.IntegerField
    smokestate = models.IntegerField
    door_1 = models.IntegerField
    door_1 = models.IntegerField
    door_1 = models.IntegerField
    door_1 = models.IntegerField
    door_1 = models.IntegerField
    door_1 = models.IntegerField
    battvalue = models.FloatField(default=0,blank=True, verbose_name="电池电量值")
    fallvalue = models.FloatField(default=0,blank=True, verbose_name="倾斜角度值")
    tempvalue = models.FloatField(default=0,blank=True, verbose_name="温度值")
    humidvalue = models.FloatField(default=0,blank=True, verbose_name="湿度值")
    rssivalue = models.FloatField(default=0,blank=True, verbose_name="信号强度值")

class dct_t_l2snr_sensor_type(models.Model):
    snr_code = models.CharField(max_length=10, primary_key=True)
    snr_name = models.CharField(max_length=15)
    value_min = models.FloatField(default=0,blank=True,  verbose_name="量程最小值")
    value_max = models.FloatField(default=0,blank=True,  verbose_name="量程最大值")
    snr_model = models.CharField(max_length=20)
    snr_vendor = models.CharField(max_length=20)


class dct_t_l2snr_dust(models.Model):
    sid = models.AutoField(primary_key=True)
    dev_code = models.ForeignKey(dct_t_l3f2cm_device_common, on_delete=models.CASCADE)
    tsp = models.FloatField(default=0,blank=True, verbose_name="TSP")
    pm01 = models.FloatField(default=0,blank=True, verbose_name="PM0.1")
    pm25 = models.FloatField(default=0,blank=True, verbose_name="PM2.5")
    pm10 = models.FloatField(default=0,blank=True, verbose_name="PM10")
    dataflag = models.CharField(max_length=1)
    report_data = models.DateTimeField(auto_now=True)
    hourminindex = models.IntegerField


class dct_t_l2snr_noise(models.Model):
    sid = models.AutoField(primary_key=True)
    dev_code = models.ForeignKey(dct_t_l3f2cm_device_common, on_delete=models.CASCADE)
    noise = models.FloatField(default=0,blank=True, verbose_name="噪声")
    dataflag = models.CharField(max_length=1)
    report_data = models.DateTimeField(auto_now=True)
    hourminindex = models.IntegerField


class dct_t_l2snr_temperature(models.Model):
    sid = models.AutoField(primary_key=True)
    dev_code = models.ForeignKey(dct_t_l3f2cm_device_common, on_delete=models.CASCADE)
    temperature = models.FloatField(default=0,blank=True, verbose_name="温度值")
    dataflag = models.CharField(max_length=1)
    report_data = models.DateTimeField(auto_now=True)
    hourminindex = models.IntegerField


class dct_t_l2snr_humidity(models.Model):
    sid = models.AutoField(primary_key=True)
    dev_code = models.ForeignKey(dct_t_l3f2cm_device_common, on_delete=models.CASCADE)
    humidity = models.FloatField(default=0,blank=True, verbose_name="湿度值")
    #     pm01=models.FloatField(max_digits=10,decimal_places=4,verbose_name="PM0.1")
    #     pm25=models.FloatField(max_digits=10,decimal_places=4,verbose_name="PM2.5")
    #     pm10=models.FloatField(max_digits=10,decimal_places=4,verbose_name="PM10")
    dataflag = models.CharField(max_length=1)
    report_data = models.DateTimeField(auto_now=True)
    hourminindex = models.IntegerField


class dct_t_l2snr_winddir(models.Model):
    sid = models.AutoField(primary_key=True)
    dev_code = models.ForeignKey(dct_t_l3f2cm_device_common, on_delete=models.CASCADE)
    windir = models.FloatField(default=0,blank=True, verbose_name="风向")
    #     pm01=models.FloatField(max_digits=10,decimal_places=4,verbose_name="PM0.1")
    #     pm25=models.FloatField(max_digits=10,decimal_places=4,verbose_name="PM2.5")
    #     pm10=models.FloatField(max_digits=10,decimal_places=4,verbose_name="PM10")
    dataflag = models.CharField(max_length=1)
    report_data = models.DateTimeField(auto_now=True)
    hourminindex = models.IntegerField


class dct_t_l2snr_windspd(models.Model):
    sid = models.AutoField(primary_key=True)
    dev_code = models.ForeignKey(dct_t_l3f2cm_device_common, on_delete=models.CASCADE)
    windspd = models.FloatField(default=0,blank=True,  verbose_name="风速")
    #     pm01=models.FloatField(max_digits=10,decimal_places=4,verbose_name="PM0.1")
    #     pm25=models.FloatField(max_digits=10,decimal_places=4,verbose_name="PM2.5")
    #     pm10=models.FloatField(max_digits=10,decimal_places=4,verbose_name="PM10")
    dataflag = models.CharField(max_length=1)
    report_data = models.DateTimeField(auto_now=True)
    hourminindex = models.IntegerField


class dct_t_l2snr_picture(models.Model):
    sid = models.AutoField(primary_key=True)
    site_code = models.ForeignKey(dct_t_l3f2cm_site_common, on_delete=models.CASCADE)
    file_name = models.TextField(max_length=100)
    file_size = models.IntegerField
    description = models.TextField(max_length=100)
    dataflag = models.CharField(max_length=1)
    report_data = models.DateTimeField(auto_now=True)
    hourminindex = models.IntegerField
# -*- coding: utf-8 -*-
from django.db import models

# Create your models here.
class t_l3f1sym_menu_code_mapping(models.Model):
    menu_code=models.IntegerField(primary_key=True)
    menu_name=models.CharField(max_length=20)
    # def __unicode__(self):
    #     return self.menu_name,self.menu_code
class t_l3f1sym_user_right_menu(models.Model):
    sid=models.AutoField(primary_key=True)
    menu_group=models.IntegerField(default=0)
    menu_code=models.ForeignKey(t_l3f1sym_menu_code_mapping,on_delete=models.CASCADE)
    menu_name=models.CharField(max_length=20)
class t_l3f1sym_user_action(models.Model):
    sid=models.AutoField(primary_key=True)
    action_code = models.IntegerField(unique=True)
    action_name=models.CharField(max_length=20)
    l1_auth = models.BooleanField(default=0)
    l2_auth = models.BooleanField(default=0)
    l3_auth = models.BooleanField(default=0)
    l4_auth = models.BooleanField(default=0)
    l5_auth = models.BooleanField(default=0)
    l6_auth = models.BooleanField(default=0)
class t_l3f1sym_account_primary(models.Model):
    uid=models.CharField(max_length=10,primary_key=True)
    login_name=models.CharField(max_length=20,db_index=True)
    pass_word=models.CharField(max_length=100)
    email=models.EmailField(null=True)
    menu_group=models.IntegerField(default=0)
    grade_lever=models.IntegerField(null=True)
    red_date=models.DateTimeField(auto_now_add=True)
class t_l3f1sym_account_secondary(models.Model):
    CHOICES=((1,'男'),(2,'女'),(3,'第三人'))
    uid=models.OneToOneField(t_l3f1sym_account_primary,on_delete=models.CASCADE,primary_key=True)
    nick_name=models.CharField(max_length=20,null=True)
    true_name=models.CharField(max_length=20,null=True)
    gender=models.IntegerField(null=True,choices=CHOICES)
    age=models.IntegerField(null=True)
    telephone=models.CharField(max_length=11,null=True)
    city=models.CharField(max_length=20,null=True)
class t_l3f1sym_user_right_project(models.Model):
    sid=models.AutoField(primary_key=True)
    uid=models.ForeignKey(t_l3f1sym_account_primary,on_delete=models.CASCADE)
    auth_type=models.IntegerField(default=0)
    auth_code=models.IntegerField(default=0)
class t_l3f2cm_pg_common(models.Model):
    pg_code=models.IntegerField(primary_key=True)
    pg_name=models.CharField(max_length=20)
    pg_creator=models.CharField(max_length=10)
    create_date=models.DateTimeField(auto_now=True)
    superintendent=models.CharField(max_length=20,null=True)
    telephone=models.CharField(max_length=15,null=True)
    department=models.CharField(max_length=50,null=True)
    address=models.CharField(max_length=50,null=True)
    comments=models.TextField(null=True)
class t_l3f2cm_project_common(models.Model):
    prj_code=models.CharField(max_length=10,primary_key=True)
    prj_name=models.CharField(max_length=20)
    pg_code=models.ForeignKey(t_l3f2cm_pg_common,on_delete=models.CASCADE)
    prj_creator=models.CharField(max_length=10)
    create_date=models.DateTimeField(auto_now=True)
    superintendent = models.CharField(max_length=20, null=True)
    telephone = models.CharField(max_length=15, null=True)
    department = models.CharField(max_length=50, null=True)
    address = models.CharField(max_length=50, null=True)
    comments = models.TextField(null=True)
class t_l3f2cm_site_common(models.Model):
    site_code = models.CharField(max_length=10, primary_key=True)
    site_name = models.CharField(max_length=20)
    prj_code = models.ForeignKey(t_l3f2cm_project_common, on_delete=models.CASCADE)
    site_creator = models.CharField(max_length=10)
    create_date = models.DateTimeField(auto_now=True)
    superintendent = models.CharField(max_length=20, null=True)
    telephone = models.CharField(max_length=15, null=True)
    address = models.CharField(max_length=50, null=True)
    longitude = models.DecimalField(max_digits=10, decimal_places=6)
    latitude = models.DecimalField(max_digits=10, decimal_places=6)
    comments = models.TextField(null=True)
class t_l3f2cm_device_common(models.Model):
    dev_code=models.CharField(max_length=20,primary_key=True)
    site_code=models.ForeignKey(t_l3f2cm_site_common,on_delete=models.CASCADE)
    create_date=models.DateTimeField(auto_now=True)
    socket_id=models.IntegerField(null=True)
    hw_type=models.IntegerField(null=True)
    hw_ver=models.IntegerField(null=True)
    sw_rel=models.IntegerField(null=True)
    sw_ver=models.IntegerField(null=True)
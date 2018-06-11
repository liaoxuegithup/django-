from django.contrib import admin

# Register your models here.
from .models import PeopleInfo,BookInfo

# 注册模型让后台操作数据库
admin.site.register(BookInfo)
admin.site.register(PeopleInfo)
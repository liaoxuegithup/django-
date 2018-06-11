from django.db import models

# Create your models here.

class BookInfo(models.Model):
    name = models.CharField(max_length=20)
    # 输的名字
    pub_date = models.DateField(null=True)
    #
    readcount = models.IntegerField(default=0)
    # 读的次数
    commentcount = models.IntegerField(default=0)

    is_delete = models.BooleanField(default=False)
    def __str__(self):
        return self.name
#     字段不能是python,mysql

# /关键字名不能有来个__
class Meta():
    db_table = "bookinfo"
#     这个是固定写法还是自己定义的.
# 为什么没有返回值
class PeopleInfo(models.Model):
    GENDER_CHOICES = (
        (0, 'male'),
        (1, 'female')
    )
    # 啥意思不知道
    name = models.CharField(max_length=20,verbose_name="名称")
    gender = models.SmallIntegerField(choices=GENDER_CHOICES,default=0,verbose_name="性别")
    description  = models.CharField(max_length=200,verbose_name="描述信息")
    book = models.ForeignKey(BookInfo,on_delete=models.CASCADE,verbose_name="图书")
    is_delete = models.BooleanField(default=0,verbose_name="删除信息")
    class Meta:
        db_table = "peopleinfo"
        verbose_name = "人物信息"
    def __str__(self):
        return self.name
    # 数据库的表名是Student,StudentProject,将表明给了admin在admin中设置表
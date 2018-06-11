from django.shortcuts import render
from .models import PeopleInfo
# Create your views here.


def index(request):
    people_name = PeopleInfo.objects.all()
    context={
        "people_name":people_name,
        "name":'name'
    }
    return render(request,"index.html",context)

# def model():
#         # 数据库的增删改查
from student.models import PeopleInfo,BookInfo
    # book = BookInfo.objects.a
    # 增加数据
# book = BookInfo.objects.create(
#     name = "三国演绎",
#     pub_date = '2011-2-3',
#     readcount =100,
#     commentcount = 100,
#     is_delete = False
# )
# 上面方式直接添加
# book = BookInfo(
# name = "水浒传",
#     pub_date = '1980-2-3',
#     readcount =89,
#     commentcount = 78,
#     is_delete = False
# )
# book.save()
# 修改
# book = BookInfo()
# book.name = "西游记"
# book.save()
# book = BookInfo.objects.filter(id=3).update(name="鲁迅")
# 删除
# book = BookInfo.objects.filter(id=2).delete()
# 删除首先获取该条件下的语句,删除
# book = BookInfo.objects.get(name="鲁迅").update(name="hahj")
# update针对的是QuerySet的对象
# 不行那个
# book.delete()
# 查询 基础查询 get all count
# book = BookInfo.objects.get(id=4)
# book = BookInfo.objects.all()
# BookInfo.objects.count()
# book = BookInfo.objects.get(pk=2)
# 过滤查询
# 1\get只有一条数据
# 2\filter    过滤
# 3\exclude 除了选项以外的都显示
# id_exact表示等于
# book = BookInfo.objects.get(id__exact = 1)
# book = BookInfo.objects.filter(id__exact=3)


# BookInfo.objects.filter(name__contains = "义")
# BookInfo.objects.filter(name__endswith="狐")
# BookInfo.objects.filter(name__startswith="雪")
# 空查询,isnull是否为null
# in范围查询
# gt表示大于,gte表示大于等于,lt表示小于,lte表示小于等于
# 不等于运算符用exclude()过滤器
# 日期查询 year,month,day,week_day,hour,minute,second
# PeopleInfo.objects.all().update(name="鲁迅")
# 查询编号为1的图书
# BookInfo.objects.filter(id__exact=1)
# BookInfo.objects.get(id=1)
# BookInfo.objects.get(pk=1)
# # 查询书名包含'湖'的图书
# BookInfo.objects.filter(name__contains="湖")
# #   查询书名以'部'结尾的图书
# BookInfo.objects.filter(name__endswith = "部")
# # 查询书名为空的图书
# BookInfo.objects.filter(name__isnull=True)
# #   查询编号为1或3或5的图书
# BookInfo.objects.filter(id__in = {1,3,5})
# # 查询编号大于3的图书
# BookInfo.objects.filter(id__gt=3)
# BookInfo.objects.filter(id__lt=7)
# BookInfo.objects.filter(id__gte=3)
# BookInfo.objects.filter(id__lte=7)
# #   查询1980年发表的图书
# BookInfo.objects.filter(pub_date__year='1980')
# # 查询1990年1月1日后发表的图书
# BookInfo.objects.filter(name="水浒传").update(name="西游记")
# BookInfo.objects.filter(pub_date__gt="1990-1-1")
  # 在运算符前面加上i表示不去分大小写
  # F对象表示跨字段进行比较操作
# Q对象是|
# from django.db.models import F
# BookInfo.objects.filter(readcount__gt=F('commentcount'))
# BookInfo.objects.filter(readcount__gt=F('commentcount')*2)
  # 表示阅读数量大于评论数量的2陪
  # 这个比较是一行中两个字段进行比较
# from django.db.models import Q
# BookInfo.objects.filter(Q(readcount__gt=30)|Q(commentcount__gt=60))
# # Q中的|表示或的含义
# BookInfo.objects.filter(readcount__gt=30).filter(commentcount__gt=60)
# BookInfo.objects.filter(Q(readcount__gt=30)& Q(commentcount__gt=60) )
#   # 表示在满足readcount大于30的基础上,在过滤出大于60的
#   # not还可以~Q
# books = BookInfo.objects.filter(~Q(id=3))
# BookInfo.objects.exclude(id=3)
  # Q中的not和exclude效果相同,区别是exclude是过滤器,而~Q表示过滤条件
  # 聚合函数
  # Avg(),Sum(),Count(),Max(),Min()
#
# BookInfo.objects.aggregate(Sum('readcount'))
# from django.db.models import Sum,Avg
# BookInfo.objects.aggregate(Avg('readcount'))
# from django.db.models import Count
# BookInfo.objects.aggregate(Count('readcount'))
# from django.db.models import Max
# BookInfo.objects.aggregate(Max('readcount'))
# from django.db.models import Min
# BookInfo.objects.aggregate(Min('readcount'))
# 在查询聚合函数时使用过滤器是aggregate
# 排序order_by
# BookInfo.objects.filter(readcount__gt=30).order_by('commentcount')
# # 倒叙
# # BookInfo.objects.filter(readcount__gt=30).order_by('-commentcount')
# book = BookInfo.objects.get(id=1)
# book.peopleinfo_set.all()
# book = BookInfo.objects.get(id=6)
# book.peopleinfo_set.all()
#获取的是BookInfo中id=1的 对象因为有外建约束
# 可以找到book对应的People中的值
# people = PeopleInfo.objects.get(id=72)
# people. book
# 通过外建的属性可以找到book的对应属性
# book = BookInfo.objects.filter(id__exact=3)
# book.peopleinfo_set.all()
book = BookInfo.objects.get(id=4)
book.peopleinfo_set.all()
# 通过没有外建的找有外建的使用以上方式

people = PeopleInfo.objects.get(id=75)
people.book.name
# book是给People的属性()关于BookInfo的属性



















# return renr('index.html')
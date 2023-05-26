from django.db import models

# Create your models here.
class Student(models.Model):
    """
    创建数据模型，相当于数据库里的一张表
    """
    stu_id = models.CharField(primary_key=True,max_length=20)
    stu_name = models.CharField(max_length=20)
    stu_psw = models.CharField(max_length=20)




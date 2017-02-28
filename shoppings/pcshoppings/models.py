from django.db import models
from  django.apps  import AppConfig


class  Category(models.Model):
    name=models.CharField(max_length=20)

    def __str__(self):
        return self.name



class item(models.Model):
    category = models.ForeignKey(Category, verbose_name='商品分類', null=True, blank=True)
    #category = models.TextField(max_length=100, default=None)
    item_name = models.CharField(verbose_name='商品名稱', max_length=20)
    item_description = models.TextField(verbose_name='商品描述',max_length=100)
    item_price = models.PositiveIntegerField(verbose_name='商品價格',default=None)
    created_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)
    item_img=models.ImageField(upload_to='upload', null=True,blank=True)
    item_url=models.CharField(verbose_name='商品相關連結', max_length=200,default=None)


    def __str__(self):
        return self.item_name

class member(models.Model):
    member_name=models.CharField(max_length=20,default=None)
    member_account = models.CharField(verbose_name='登入帳號',max_length=8,default=None)
    member_homephone = models.PositiveIntegerField(verbose_name='市內電話',default=None)
    member_phone=models.PositiveIntegerField(verbose_name='手機',blank=True,default=None)
    member_email=models.CharField(verbose_name='email',max_length=20,default=None)
    def __str__(self):
        return self.member_name

class  comment(models.Model):
    content=models.CharField(max_length=255)
    visitor=models.ForeignKey(member)


#class item_information(models.Model):

# Create your models here.

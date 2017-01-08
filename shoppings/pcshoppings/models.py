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
    item_price = models.PositiveIntegerField(verbose_name='商品價格',default=0)
    created_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.item_name

class member(models.Model):
    member_name=models.CharField(max_length=20)
    member_account = models.CharField(max_length=8,blank=True)
    member_phone=models.PositiveIntegerField(blank=True,default=None)

    def __str__(self):
        return self.member_name




#class item_information(models.Model):

# Create your models here.

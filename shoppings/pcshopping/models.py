from django.db import models
from  django.apps  import AppConfig


class  Category(models.Model):
    name=models.CharField(max_length=100)

    def __str__(self):
        return self.name



class shopping_cpu(models.Model):

    item_title = models.CharField(verbose_name='我',max_length=20)
    item_description=models.TextField(max_length=100)
    content = models.TextField(blank=True)
    item_photo = models.URLField(blank=True)
    item_price=models.PositiveIntegerField(default=0)#if price =0   alert
    item_location = models.CharField(max_length=100)
    created_time = models.DateTimeField(auto_now_add=True)
    update_time=models.DateTimeField(auto_now=True)

class member(models.Model):
    member_name=models.CharField(max_length=20)
    member_account = models.CharField(max_length=8,blank=True)
    member_phone=models.PositiveIntegerField(blank=True,default=None)

#class item_information(models.Model):

# Create your models here.

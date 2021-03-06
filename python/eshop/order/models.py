# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8') 
from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Product(models.Model):
    name=models.CharField('product name',max_length=30)
    price=models.FloatField('price',default=10)
    ptype=models.ForeignKey('Ptype')
    img=models.ImageField('img',upload_to="product",max_length=100)
    def __unicode__(self):
        return "%s -->%f" % (self.name,self.price)

class Ptype(models.Model):
    name=models.CharField('type',max_length=10)
    def __unicode__(self):
            return "%s" % self.name  
        
class Order(models.Model):
    odate=models.DateTimeField("order date",auto_now=True)
    product=models.ForeignKey("Product")
    user=models.ForeignKey(User)
    
class UserProfile(models.Model):
    SEX_CHOICES=(('1',u'男'),('2',u'女'),)
    
    user=models.OneToOneField(User)
    nickname=models.CharField(u"昵称",max_length=30)
    sex=models.CharField(u"性别",max_length=1,choices=SEX_CHOICES,default='1')
    address=models.CharField(u"地址",max_length=100,null=True)
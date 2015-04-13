# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
from django.contrib import admin
from models import Product,Ptype,Order,UserProfile
admin.site.register(Product)
admin.site.register(Ptype)
admin.site.register(Order)
admin.site.register(UserProfile)



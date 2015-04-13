# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render_to_response
from models import Product,Ptype,Order,UserProfile
from django.core.paginator import Paginator
from django.template import RequestContext
def index(request):
    pagenum=1
    if request.REQUEST.has_key('pid'):
        pagenum=request.REQUEST['pid']
    products=Product.objects.all()
    p=Paginator(products,5)
    page=p.page(pagenum)
    return render_to_response("index.html",{"user":request.user,"p":p,"page":page},context_instance=RequestContext(request))
def query(request):
    pagenum=1
    if request.REQUEST.has_key('pid'):
        pagenum=request.REQUEST['pid']
    if request.POST.has_key("productname"):
        products=Product.objects.filter(name__contains=request.POST["productname"])
    else:
        products=Product.objects.all()
    
    p=Paginator(products,2)
    page=p.page(pagenum)   
    return render_to_response("index.html",{"user":request.user,"p":p,"page":page},context_instance=RequestContext(request))
def order(request):
    orderObj=None
    if request.GET.has_key("pid"):
        product=Product.objects.get(id=request.GET['pid'])
        orderObj=Order.objects.create(product=product,user=request.user)
    return render_to_response("order.html",{"order":orderObj},context_istance=RequestContext(request))
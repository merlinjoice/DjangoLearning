# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
# Create your views here.
from django.http import HttpResponse

from Apptwo.models import User

def users(request):
    users_list=User.objects.order_by(FirstName)
    date_dict={'user_record':users_list}
    return render(request,'Apptwofolder/user.html',context=date_dict)

def index(request):
    #return HttpResponse("<em>Hello </em>")
    return render(request,'Apptwofolder/index.html')

def help(request):
    my_Dict={'code2':'New code inserted'}
    return render(request,'Apptwofolder/HelpPage.html',context=my_Dict)

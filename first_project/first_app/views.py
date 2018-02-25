# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

from first_app.models import Topic,Webpage,AccessRecord

def index(request):
    #return HttpResponse("Hello World")
    #my_Dict={'insert_me':"Hello I am from views.py hello merlin"}

    webpages_list=AccessRecord.objects.order_by('date')
    date_dict={'access_record':webpages_list}
    return render(request,'first_app/index.html',context=date_dict)

from django.conf.urls import url
from Apptwo import views


urlpatterns=[

    url(r'^$',views.help,name='help'),
    url(r'^$',views.User,name='users'),


]

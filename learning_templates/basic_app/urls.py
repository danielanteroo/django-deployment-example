from django.urls import path as url
from basic_app import views

#TEMPLATE TAGGING (IMPORTANTE MEU AMIGO!!!!!!!!!! NAO ESQUECA )
app_name = 'basic_app'
########################################################
urlpatterns= [
    url('relative/', views.relative,name='relative'),
    url('other/', views.other,name='other'),
    url('index/', views.index,name='index'),
]
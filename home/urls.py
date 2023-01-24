
from django.contrib import admin
from django.urls import path,include
from . import views
from rest_framework.routers import DefaultRouter
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('clearSession', views.clearSession, name='clearSession'),

    path('com', views.comper, name='com'),

    path('cheak/', views.sc, name='store'),

    path('store/', views.store, name='store'),

    path('store/<int:id>', views.storefilter, name='storefilter'),


    path('cart/', views.cart, name='cart'),

    path('checkout/', views.checkout, name='checkout'),

    path('', views.First, name='first'),

    path('update_item/', views.updateItem, name='updateItem'),

]

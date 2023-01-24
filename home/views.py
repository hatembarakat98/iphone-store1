from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
import json
from .models import Product
from .models import Land
from .models import Category, Product, Order, OrderItem, Search
from django.http import HttpResponseRedirect, request
import os
from project2 import settings
from pprint import pprint

from django.http import HttpResponse
from django.http import JsonResponse

from django.contrib.auth.decorators import login_required
from django.contrib import messages

from django.core.paginator import Paginator

from django.core import serializers

import uuid


def clearSession(request):
    # if request.method == 'POST':
    del request.session['uuid']
    # request.session.pop('uuid')
    return redirect('store')


def First(request):
     cat =Category.objects.all()
     product=Product.objects.all().filter(Cat=13)
     product=product[0]
     product2=Product.objects.all().latest('id')

     return render(request,"index.html",{"cat":cat,"product":product,"product2":product2  })

def sc(request):
    if 'uuid' in request.session:
        user_id = request.session['uuid']
        order = Order.objects.filter(user_id=user_id, complete=False)
        forder = order[0]
        items = OrderItem.objects.filter(order=forder)
    else:
        items = []
        order={"get_cart_total":0, "get_cart_items":0}
        forder={}
    context = {
        'items':items,
        'forder':forder,
    }

    return render(request,"store/index.html",context)



def storefilter(request,id):
    if request.method == 'POST':
        myStopWords = stopwords.words('english')
        searched = request.POST['searched']
        splitSearch = searched.split()
        print(splitSearch)
        products1 = Product.objects.all().filter(Cat=id)
        listName = []
        for product1 in products1:
            nameSplit = product1.name.split()
            for sS in splitSearch:
                if sS in myStopWords:
                    break
                else:        
                    for nS in nameSplit:
                        if sS == nS:
                            print(nS)
                            listName.append(product1.name)
                            break
        for l in listName:
            print(l)
        products2 = Product.objects.filter(name__in = listName)
        print("GOOD")
        print(products2)
        products = Product.objects.filter(name__in = listName)
        for sS in splitSearch:
            allSearchs = Search.objects.filter(name = sS)
            length = len(allSearchs)
            if length > 0:
                search = Search.objects.filter(name=sS)
                for s in search:
                    s.count += 1
                    s.save()
    else: 
        products = Product.objects.all().filter(Cat=id)
        searched = ''
    if 'uuid' in request.session:
        user_id = request.session['uuid']
        order = Order.objects.filter(user_id=user_id, complete=False)
        forder = order[0]
        items = OrderItem.objects.filter(order=forder)
    else:
        items = []
        order={"get_cart_total":0, "get_cart_items":0}
        forder = {}
    print(Search.objects.order_by('-count')[:2])
    categories = Category.objects.all()
    context = {'categories':categories, 'products':products,'forder':forder ,'items':items, 'searched':searched}
    return render(request, 'store/store.html', context)


















def store(request):
    if request.method == 'POST':
        myStopWords = stopwords.words('english')
        searched = request.POST['searched']
        splitSearch = searched.split()
        print(splitSearch)
        products1 = Product.objects.all()
        listName = []
        for product1 in products1:
            nameSplit = product1.name.split()
            for sS in splitSearch:
                if sS in myStopWords:
                    break
                else:        
                    for nS in nameSplit:
                        if sS == nS:
                            print(nS)
                            listName.append(product1.name)
                            break
        for l in listName:
            print(l)
        products2 = Product.objects.filter(name__in = listName)
        print("GOOD")
        print(products2)
        products = Product.objects.filter(name__in = listName)
        for sS in splitSearch:
            allSearchs = Search.objects.filter(name = sS)
            length = len(allSearchs)
            if length > 0:
                search = Search.objects.filter(name=sS)
                for s in search:
                    s.count += 1
                    s.save()
    else: 
        products = Product.objects.all()
        searched = ''
    if 'uuid' in request.session:
        user_id = request.session['uuid']
        order = Order.objects.filter(user_id=user_id, complete=False)
        forder = order[0]
        items = OrderItem.objects.filter(order=forder)
    else:
        items = []
        order={"get_cart_total":0, "get_cart_items":0}
        forder = {}
    print(Search.objects.order_by('-count')[:2])
    categories = Category.objects.all()
    context = {'categories':categories, 'products':products,'forder':forder ,'items':items, 'searched':searched}
    return render(request, 'store/store.html', context)

def cart(request):
    if 'uuid' in request.session:
        user_id = request.session['uuid']
        order = Order.objects.filter(user_id=user_id, complete=False)
        forder = order[0]
        items = OrderItem.objects.filter(order=forder)
    else:
        items = []
        order={"get_cart_total":0, "get_cart_items":0}
        forder={}
    context = {
        'items':items,
        'forder':forder
    }
    # for orderr in order:
    #     print(orderr.transaction_id)
    return render(request, 'store/cart.html',  context)


def checkout(request):
    if 'uuid' in request.session:
        user_id = request.session['uuid']
        order = Order.objects.filter(user_id=user_id, complete=False)
        forder = order[0]
        items = OrderItem.objects.all()
    else:
        items = []
        order={"get_cart_total":0, "get_cart_items":0}
        forder={}
    context = {
        'items':items,
        'forder':forder
    }
    return render(request, 'store/checkout.html', context)


def comper(request):

    id=request.POST.get('id',None)
    products=Product.objects.filter(Cat=id)
    product=products[0]
    com_product = {
        'name': product.name,
        'size': product.size,
        'description': product.description,
        #'price': product.price,
        'image':str( product.image),
        'screan': product.screan,
        'core': product.core,
        'coverage': product.coverage,
        'camera': product.camera,
        'battery': product.battery,
        'front': product.front,
        'Covergimage': str(product.Covergimage),
        'Battrayimage':str( product.Battrayimage),
        'Frontimage': str(product.Frontimage),
        'Cameraimage':str(product.Cameraimage),
        'coreimage':str(product.Coreimage),


    }
    return  JsonResponse(com_product, safe=True)




import requests

def send_to_telegram(message):

    apiToken = '5850535001:AAGaeeFzh0V4_7oit7Jbjilt359EtLe0RLU'
    chatID = '727117894'
    apiURL = f'https://api.telegram.org/bot{apiToken}/sendMessage'

    try:
        response = requests.post(apiURL, json={'chat_id': chatID, 'text': message})
        print(response.text)
    except Exception as e:
        print(e)




def updateItem(request):
    if 'uuid' in request.session:
        user_id = request.session['uuid']
    else:
        user_id = uuid.uuid4()
        request.session['uuid'] = str(user_id)
    data = json.loads(request.body)

    productId = data['productId']
    action = data['action']
    # print(str(user_id))
    # customer = request.user
    product = Product.objects.get(id=productId)
    order, created = Order.objects.get_or_create(user_id=user_id, complete=False)

    orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)

    if action == 'add':
        orderItem.quantity = (orderItem.quantity + 1)
    elif action == 'remove':
        orderItem.quantity = (orderItem.quantity - 1)
    
    orderItem.save()

    if orderItem.quantity <= 0:
        orderItem.delete()

    return JsonResponse("Item was added",  safe=False)





from os import name
#from posix import PRIO_PROCESS
from django.conf import settings
from django.db import models
from django.db.models.base import Model
from django.db.models.fields import CharField
from django.contrib.auth.models import User
from colorfield.fields import ColorField

# Create your models here.



class Category(models.Model):
  name = models.CharField(max_length=250)
  def __str__(self):
    return self.name



class Name_stor():
  name=models.CharField(max_length=200)
  def __str__(self):
    return self.name





class Product(models.Model):
  name = models.CharField(max_length=250)
  size=models.FloatField(default=None)
  color=models.CharField(max_length=250,default=None)
  description = models.TextField()
  price = models.FloatField()
  placeToUpload = 'products'
  image = models.ImageField(upload_to=placeToUpload, null=True)
  Cat=models.ForeignKey(Category ,on_delete=models.CASCADE ,default=None)

  screan = models.CharField(max_length=250,blank=True , null=True )
  mobile_color = ColorField(default='#FF0000')
  mobile_color2 = ColorField(default='#FC0000')
  mobile_color3 = ColorField(default='#FB0000')
  mobile_color4 = ColorField(default='#FA0000')
  coverage = models.TextField(max_length=250,blank=True , null=True )
  camera = models.TextField(max_length=250,blank=True , null=True )
  core = models.TextField(max_length=250,blank=True , null=True )
  battery = models.CharField(max_length=250,blank=True , null=True )
  front = models.CharField(max_length=250,blank=True , null=True )

  Covergimage = models.ImageField(upload_to='placeToUpload', null=True ,blank=True)
  Battrayimage = models.ImageField(upload_to='placeToUpload', null=True,blank=True)
  Coreimage = models.ImageField(upload_to='placeToUpload', null=True,blank=True)
  Frontimage = models.ImageField(upload_to='placeToUpload', null=True,blank=True)
  Cameraimage = models.ImageField(upload_to='placeToUpload', null=True,blank=True)
  
  def __str__(self):
    return self.name

class ProductsImages(models.Model):
    Covergimage = models.ImageField(upload_to='placeToUpload', null=True)
    Battrayimage = models.ImageField(upload_to='placeToUpload', null=True)
    Coreimage = models.ImageField(upload_to='placeToUpload', null=True)
    Frontimage = models.ImageField(upload_to='placeToUpload', null=True)
    Cameraimage = models.ImageField(upload_to='placeToUpload', null=True)
    ProductImage = models.ForeignKey(Product, on_delete=models.CASCADE, default=None)


  # @property
  # def get_products(self):
  #    return Product.objects.filter(categories__name=self.category)







@property
def image_url(self):
  try:
    url = self.image.url
  except:
    url=""
  return url



class Order(models.Model):
  # customer=models.ForeignKey(User ,on_delete=models.SET_NULL,blank=True,null=True)
  user_id = models.CharField(max_length=100, default="0")
  data_orderd=models.DateTimeField(auto_now_add=True)
  complete=models.BooleanField(default=False,null=True,blank=False)
  transaction_id=models.CharField(max_length=300,null=True)

  def str(self):
      return str(self.id)

  @property
  def get_cart_total(self):
    orderitems = OrderItem.objects.filter(order = self.id)
    total = sum([item.get_total for item in orderitems])
    return total

  @property
  def get_cart_items(self):
    orderitems = OrderItem.objects.filter(order = self.id)
    total= sum([item.quantity for item in orderitems])
    return total

class OrderItem(models.Model):
  product =models.ForeignKey(Product ,on_delete=models.SET_NULL,blank=True,null=True )
  order = models.ForeignKey(Order, on_delete=models.SET_NULL, blank=True, null=True)
  quantity=models.IntegerField(default=0,null=True,blank=True)
  data_added = models.DateTimeField(auto_now_add=True)

  @property
  def get_total(self):
      total=self.product.price * self.quantity
      return  total



class ShippingAdderss(models.Model):
  customer=models.ForeignKey(User ,on_delete=models.SET_NULL,blank=True,null=True )
  order = models.ForeignKey(Order, on_delete=models.SET_NULL, blank=True, null=True)
  address = models.CharField(max_length=300, null=True)
  city = models.CharField(max_length=300, null=True)
  state = models.CharField(max_length=300, null=True)
  zipcode = models.CharField(max_length=300, null=True)
  data_added = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return self.address




class Land(models.Model):
  owner = models.ForeignKey(
      settings.AUTH_USER_MODEL,
      on_delete=models.CASCADE,
    )
  location = models.CharField(max_length=150)
  plants=(
    ("Apple" ,"Apple"),
    ('Tomato','Tomato'),
    ('Strawberry','Strawberry'),
    ('Squash','Squash'),
    ('Soybean','Soybean'),
    ('Raspberry','Raspberry'),
    ('Potato','Potato'),
    ('Pepper','Pepper'),
    ('Peach', 'Peach'),
    ('Orange', 'Orange'),
    ('Grape', 'Grape'),
    ('Corn', 'Corn'),
    ('Cherry', 'Cherry'),
    ('Blueberry', 'Blueberry'),
  )
  plant = models.CharField(max_length=200,choices=plants)

class Search(models.Model):
  lands = models.CharField(max_length=250, null=True)
  name = models.CharField(max_length=250)
  count = models.IntegerField(default=0)

  def __str__(self):
    return self.name
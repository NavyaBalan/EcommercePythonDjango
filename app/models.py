from django.db import models
from django.contrib.auth.models import User
# Create your models here.

category_choices=(
    ('vg','Vegetables'),
    ('ft','Fruits')
)

state_choices =(
    ('Kerala','Kerala'),
    ('Karnataka','Karnataka'),
    ('Delhi','Delhi'),
    ('TamilNadu','TamilNadu'),
    ('AndhraPredhesh','AndhraPradhesh'),
    ('Rajasthan','Rajasthan')
   

)

status_choice =(
    ('Pending','Pending'),
    ('Accepted','Accepted'),
    ('Shipped','Shipped'),
    ('Cancel','Cancel'),
    ('Delivered','Delivered'),
    ('On The Way','On The Way'),

)

class Product(models.Model):
    name= models.CharField(max_length=100)
    price=models.FloatField()
    description= models.TextField()
    category = models.CharField(choices=category_choices,max_length=100)
    product_image=models.ImageField(upload_to='product')

    def __str__(self) :
        return self.name
    

    


class Customer(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    locality=models.CharField(max_length=100)
    city=models.CharField(max_length=100)
    mobile = models.IntegerField(default=0)
    zip_code = models.IntegerField()
    state =models.CharField(choices=state_choices,max_length=100)
    
    def __str__(self) :
        return self.name
    

class Cart(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    product =models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    @property
    def total(self):
        return self.quantity * self.product.price

class Payment (models.Model):
      user = models.ForeignKey(User,on_delete=models.CASCADE)
      amount =models.FloatField()
      razorpay_order_id = models.CharField(max_length=200,blank=True,null=True)
      razorpay_payment_status = models.CharField(max_length=200,blank=True,null=True)
      razorpay_payment_id= models.CharField(max_length=200,blank=True,null=True)
      paid= models.BooleanField(default=False)

      
class Order(models.Model):
      user = models.ForeignKey(User,on_delete=models.CASCADE)
      customer = models.ForeignKey(Customer,on_delete=models.CASCADE)
      product = models.ForeignKey(Product,on_delete=models.CASCADE)
      quantity = models.PositiveIntegerField(default=1)
      order_date = models.DateField(auto_now_add=True)
      status = models.CharField(choices=status_choice, default='pending', max_length=200)
      payment = models.ForeignKey(Payment,on_delete=models.CASCADE)
      
      
      @property
      def totalCost(self):
           return self.quantity * self.product.price
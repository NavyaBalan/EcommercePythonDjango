from django.contrib import admin
from .models import  Cart, Customer, Order, Payment,  Product


# Register your models here.



@admin.register(Product)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = ['id','name','price','category','product_image']



@admin.register(Customer)
class CustomerModelAdmin(admin.ModelAdmin):
    list_display = [ 'id','user','locality','state','zip_code']

@admin.register(Cart)
class CartModelAdmin(admin.ModelAdmin):
    list_display = [ 'id','user','product','quantity']

admin.register(Payment)
# class PaymentModelAdmin(admin.ModelAdmin):
#     list_display = [ 'id','user','amount',' razorpay_order_id',' razorpay_payment_status',' razorpay_payment_id','paid']

@admin.register(Order)
class OrderModelAdmin(admin.ModelAdmin):
    list_display = [ 'id','user','product','quantity','order_date','status']
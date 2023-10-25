
from django.conf import settings
from django.http import JsonResponse
from django.shortcuts import  render,redirect

from app.forms import CustomerProfileForm, UserRegistrationForm, MyPasswordResetForm


from django.contrib import messages

from .models import   Customer, Product, Cart,Order

from django.db.models import  Q
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail

# Create your views here.

def home(request):
    products=Product.objects.all()
    return render(request,'index.html',{'products': products})

def about(request):
    return render(request,'about.html')

def vegetable_category(request):
    vegetables = Product.objects.filter(category='vg')
    return render(request, 'vegetable_category.html', {'vegetables': vegetables})

def fruit_category(request):

    fruits = Product.objects.filter(category='ft')
    return render(request, 'fruit_category.html', {'fruits': fruits})

def product_details(request, product_id):
    product = Product.objects.get(pk=product_id)
    return render(request, 'product_details.html', {'product': product})


def searchProduct(request):
    query= request.GET.get('search')

    
    if query is not None and query != "":
      
        products = Product.objects.filter(Q(name__icontains=query) | Q(description__icontains=query))
    else:
       
        products = []
 
    return render (request,'search.html',{'products': products})

   
 

@login_required
def addtocart(request,prod_id):
    user= request.user
  
    product = Product.objects.get(id=prod_id)
    Cart(user=user,product=product).save()
    return redirect('/')



def showCart(request):
    user=request.user
    cart = Cart.objects.filter(user=user)
    amount=0
    for p in cart:
        value = p.quantity * p.product.price
        amount += value
    totalamount= amount + 40
    return render(request,'cart.html',locals())

def viewOrder(request):
    user=request.user
    orderPlaced = Order.objects.filter(user=user)
    return render(request,'order.html',{'orderPlaced' : orderPlaced})

def pluscart(request):
    if request.method == 'GET':
        product_id=request.GET['prod_id']
        c=Cart.objects.get(Q(product=product_id)& (Q(user=request.user)))
      
        c.quantity+=1
        c.save()
        user = request.user
        cart =Cart.objects.filter(user=user)
        amount = 0
        for p in cart:
            value = p.quantity * p.product.price
            amount = amount + value
        totalamount = amount + 40
        data ={
            'quantity' : c.quantity,
            'amount': amount,
            'totalamount': totalamount
        }
        return JsonResponse(data)

def minuscart(request):
    if request.method == 'GET':
        prod_id=request.GET['prod_id']
        c=Cart.objects.get(Q(product=prod_id)& (Q(user=request.user)))
        c.quantity-=1
        c.save()
        user = request.user
        cart =Cart.objects.filter(user=user)
        amount = 0
        for p in cart:
            value = p.quantity * p.product.price
            amount = amount + value
        totalamount =amount+40
        data ={
            'quantity' : c.quantity,
            'amount': amount,
            'totalamount': totalamount
        }
        return JsonResponse(data)
    
def removecart(request):
    if request.method == 'GET':
        prod_id=request.GET['prod_id']
        c=Cart.objects.get(Q(product=prod_id)& (Q(user=request.user)))
        
        c.delete()
        user = request.user
        cart =Cart.objects.filter(user=user)
        amount = 0
        for p in cart:
            value = p.quantity * p.product.price
            amount = amount + value
        totalamount =amount+40
        data ={
           
            'amount': amount,
            'totalamount': totalamount
        }
        return JsonResponse(data)

def placeorder(request):
    user=request.user
    add=Customer.objects.filter(user=user)
    cartitems=Cart.objects.filter(user=user)
    amount=0
    for p in cartitems:
            value = p.quantity * p.product.price
            amount +=value
    totalamount =amount+40
    return render(request,'PlaceOrder.html',locals())
    

def registers(request):
  
    form = UserRegistrationForm(request.POST)
    if form.is_valid():
        form.save()
        redirect('login')
        # messages.success(request,"Congratualtions User register successfully")
    else:
        messages.warning(request,"invalid input data")
    
    
    return render(request, 'register.html',{'form': form})

def LoginView(request):
     return render(request, 'login.html')




def profileview(request):
    if request.method == 'POST':
        form = CustomerProfileForm(request.POST)
        if form.is_valid():
      
            user = request.user
            name = form.cleaned_data['name']
            locality = form.cleaned_data['locality']
            city = form.cleaned_data['city']
            mobile = form.cleaned_data['mobile']
            state = form.cleaned_data['state']
            zip_code = form.cleaned_data['zip_code']
            
            reg = Customer(user=user, name=name, locality=locality, mobile=mobile, city=city, state=state, zip_code=zip_code)
            reg.save()
            messages.success(request, 'Congratulations! Profile saved successfully')

    else:
    
        form = CustomerProfileForm()

    return render(request, 'profile.html', {'form': form})


def address(request):

     add=Customer.objects.filter( user = request.user)
     return render (request,'address.html',{'add': add})

def updateAddress(request, pk):
    customer = Customer.objects.get(pk=pk) 

    if request.method == 'POST':
        form = CustomerProfileForm(request.POST, instance=customer)   
        if form.is_valid():
            form.save() 
            messages.success(request, 'Congratulations! Profile Updated successfully')

            return redirect('address')  
        
    else:
        form = CustomerProfileForm(instance=customer)
    
    return render(request, 'updateAddress.html', {'form': form})
    

def EmailSend(request):
    form = MyPasswordResetForm()
    if request.method == 'POST': 
        form = MyPasswordResetForm(request.POST)
        if form.is_valid():
           
            subject = 'Reset The Password'
            message = 'Sending Email through Gmail'
            recipient = form.cleaned_data.get('email')
            send_mail(subject,
                      message,settings.Email_HOST_USER, [recipient],fail_silently=False)
            
            return redirect('password_reset/done/')
        
    return render(request,'resetpasswordconfirm.html',{'form':form})  

def searchBar(request):
    if request.method == 'GET':
       query = request.GET.get('query')
       if query:
           products = Product.objects.filter(name__icontains=query)
           return render(request,'searchBar.html',{'products':products})
       else:
           print('no products available')
           return render(request,'searchBar.html',{})
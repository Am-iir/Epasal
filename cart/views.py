from django.shortcuts import render ,redirect

from accounts.forms import LoginForm
from billing.models import BillingProfile
from products.models import Product
from orders.models import Order

from .models import Cart

# Create your views here.

def cart_home(request):
    # del request.session['cart_id'] 
    cart_obj, new_obj = Cart.objects.new_or_get(request)
    return render(request,"carts/home.html",{"cart":cart_obj})

def cart_update(request):  
    product_id = request.POST.get('product_id')
    print (request.POST)
    print(product_id) 
    if product_id is not None:
        try:           
            product_obj = Product.objects.get(id=product_id)
        except Product.DoesNotExist:
            print("error message")
            return redirect("cart:cart_home")            
        cart_obj ,new_obj = Cart.objects.new_or_get(request)
        if product_obj in cart_obj.products.all():
            cart_obj.products.remove(product_obj)
        else:
            cart_obj.products.add(product_obj)
        request.session['cart_items']=cart_obj.products.count() # to return number of items in cart

    return redirect("cart:cart_home")

def checkout_home(request):
    cart_obj , cart_created = Cart.objects.new_or_get(request)
    
    if cart_created or cart_obj.products.count() ==0: # if not creatd new or products is empty
        return redirect("cart:cart_home")
    else:        
        order_obj , obj_created = Order.objects.get_or_create(cart=cart_obj)
    user = request.user

    billing_profile = None
    login_form = LoginForm()
    if user.is_authenticated():
        billing_profile , billing_profile_created = BillingProfile.objects.get_or_create(user=user , email=user.email)
    context={
        "object":order_obj,
        "billing_profile":billing_profile,
        "login_form":login_form

    }

    return render (request , "carts/checkout.html",context)


    


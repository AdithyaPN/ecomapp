from django.shortcuts import render,redirect
from seller.models import Product
from common.models import Customer
from customer.models import Cart

# Create your views here.
def customer_home(request):
    product_list = Product.objects.all() # all() is used to get every sellers products from the database.
    return render(request, 'customer/customer_home.html',{'products':product_list})

def change_password(request):
    msg = ''
    if request.method == 'POST':
        customer = Customer.objects.get(id = request.session['customer'])

        customer_password = request.POST['current_password']
        new_pass = request.POST['new_password']
        confirm_pass = request.POST['confirm_password']

        if customer.customer_password == customer_password:

            if new_pass == confirm_pass:
                customer.customer_password = new_pass
                customer.save()
                msg = 'Password changed successfully'
            else:
                msg = 'Password Does not Match'
        else:
            msg = 'Incorrect password'
    return render(request, 'customer/change_password.html',{'msg':msg})

def prod_details(request,pid):
    msg = ''
    product_details = Product.objects.get(id = pid)

    if request.method == 'POST':
        # checking if the user has added the same product in cart
        # exists() method returns boolean value, true if data exists
        product_exist = Cart.objects.filter(product_details = pid,customer = request.session['customer']).exists()

        if not product_exist:
            cart = Cart(customer_id = request.session['customer'], product_details_id = pid)
            cart.save()
        else:
            msg = 'item already in cart'

      # data we pass views to templete is called context data
    context = {
        'details':product_details,
        'msg':msg
    }
    return render(request, 'customer/product_details.html', context)
    # return render(request, 'customer/product_details.html',{'details':product_details,'msg':msg})

def customer_cart(request):
    cart = Cart.objects.filter(customer = request.session['customer'])
    return render(request, 'customer/cart.html',{'customer_cart' : cart})

def customer_orders(request):
    return render(request, 'customer/orders.html')

def profile(request):
    profile = Customer.objects.get(id = request.session['customer'])

    return render(request, 'customer/profile.html',{'customer' : profile})

# to logout and remove item from cart have no html. these are two functions to do the task.
# remove item has url, it is done by using id
def remove_item_from_cart(request,pid):
    cart_item = Cart.objects.get(product_details = pid, customer = request.session['customer'])
    cart_item.delete()
    return redirect('customer:cart')

def logout(request):
    del request.session['customer']
    request.session.flush() # to remove session data from django_session table
    return redirect('common:customerlogin')


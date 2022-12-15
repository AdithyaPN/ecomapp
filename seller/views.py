from django.shortcuts import render,redirect
from common.models import Seller
from .models import Product
from django.http import JsonResponse

# Create your views here.
def seller_home(request):
    seller_data = Seller.objects.get(id = request.session['seller'])
    return render(request, 'seller/seller_home.html',{'data':seller_data})

def add_product(request):
    msg = ''
    if request.method == 'POST':
            product_name = request.POST['product_name']
            product_description = request.POST['product_description']
            product_number = request.POST['product_number']
            product_price = request.POST['product_price']
            current_stock = request.POST['current_stock']
            product_image = request.FILES['product_image']

            product = Product(product_name=product_name,
            product_description=product_description,
            product_number=product_number,
            product_price=product_price,
            current_stock=current_stock,
            product_image=product_image,
            seller_id=request.session['seller'])

            product.save()
            msg = 'Product added successfully'

    return render(request, 'seller/add_product.html',{'msg':msg})

def change_password(request):
    msg = ''
    if request.method == 'POST':
        seller = Seller.objects.get(id = request.session['seller'])

        seller_password = request.POST['current_password']
        new_password = request.POST['new_password']
        confirm_password = request.POST['confirm_password']

        if seller.seller_password == seller_password:
            if new_password == confirm_password:
                seller.seller_password = new_password
                seller.save()
                msg = 'Password changed successfully'
            else:
                msg = 'Password Does not Match'
        else:
            msg = 'Incorrect password'
            
    return render(request, 'seller/change_password.html',{'msg':msg})

def catalogue(request):
    seller_products = Product.objects.filter(seller = request.session['seller'])
    return render(request, 'seller/catalogue.html',{'products':seller_products})

def seller_profile(request):
    profile = Seller.objects.get(id = request.session['seller'])
    return render(request, 'seller/seller_profile.html',{'seller':profile})

def update_stock(request):

    update_stock = Product.objects.filter(seller = request.session['seller'])

    if request.method =='POST':
        new_stock = request.POST['NewStock']
        product_id = request.POST['product_id']

        product = Product.objects.get(id = product_id)
        product.current_stock = product.current_stock + int(new_stock)
        product.save()
    return render(request, 'seller/update_stock.html', {'products':update_stock})

def recent_order(request):
    return render(request, 'seller/recent_order.html')

def dash_board(request):
    return render(request, 'seller/dashboard.html')

def order_history(request):
    return render(request, 'seller/order_history.html')

def logout(request):
    del request.session['seller']
    request.session.flush() # to remove session data from django_session table
    return redirect('common:sellerlogin')

def get_stock(request):
    id = request.POST['id']
    product = Product.objects.get(id=id)
    product_name = product.product_name
    current_stock = product.current_stock
    p_id = product.id
    return JsonResponse({'p_name':product_name, 'stock':current_stock,'p_id':p_id})

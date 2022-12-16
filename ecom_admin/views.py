from django.shortcuts import render,redirect
from common.models import Customer,Seller
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.
def admin_home(request):
    return render(request, 'ecom_admin/home_admin.html')

def approve_customer(request):
    customers = Customer.objects.all()# every objects in customer class stores here.
    return render(request, 'ecom_admin/approve_customer.html', {'customer_list' : customers})

def approve_seller(request):
    seller = Seller.objects.all()
    return render(request, 'ecom_admin/approve_seller.html',{'seller_list':seller})

def view_customer(request):
    return render(request, 'ecom_admin/view_customer.html')

def view_seller(request):
    return render(request, 'ecom_admin/view_seller.html')

def approve(request,sid):

    seller = Seller.objects.get(id=sid)
    email = Seller.objects.filter(seller_email = request.session['seller'])
    message = 'You are approved to login'
    send_mail(
        'Approved',
        message,
        settings.EMAIL_HOST_USER,
        [seller.seller_email,],
        
    )
    seller.approved = True
    seller.save()
    return redirect('ecom_admin:viewSeller')

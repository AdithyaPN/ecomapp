from django.shortcuts import render
from common.models import Customer,Seller

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
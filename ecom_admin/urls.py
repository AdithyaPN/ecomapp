from django.urls import path
from . import views

app_name = 'ecom_admin'
urlpatterns=[
    path('adminhome', views.admin_home, name='adminhome'),
    path('approveCustomer', views.approve_customer, name='approveCustomer'),
    path('approveSeller', views.approve_seller,name='approveSeller'),
    path('viewCustomer', views.view_customer, name='viewCustomer'),
    path('viewSeller', views.view_seller, name='viewSeller'),
    path('approve/<int:sid>', views.approve, name='approve'),

]
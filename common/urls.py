from django.urls import path
from . import views

app_name = 'common'
urlpatterns = [
    path('projecthome', views.project_home, name='projecthome'),
    path('customerlogin', views.customer_login, name='customerlogin'),
    path('sellerlogin', views.seller_login, name='sellerlogin'),
    path('customer_reg', views.customer_registration, name='customer_reg'),
    path('seller_reg', views.seller_registration, name='seller_reg'),                                                                       
    path('email_exist', views.email_exist, name='email_exist'),                                                       
]
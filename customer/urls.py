from django.urls import path
from . import views
app_name= 'customer'
urlpatterns=[
    path('customerhome', views.customer_home, name='customerhome'),
    path('changePassword', views.change_password, name='changePassword'),
    path('productDetails/<int:pid>', views.prod_details, name='productDetails'),
    path('cart', views.customer_cart, name='cart'),
    path('orders', views.customer_orders, name='orders'),
    path('profile', views.profile, name='profile'),
    path('remove_cart/<int:pid>', views.remove_item_from_cart, name='remove_cart'),
]
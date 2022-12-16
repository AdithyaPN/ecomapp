from django.urls import path
from . import views

app_name='seller'
urlpatterns=[
    path('sellerhome', views.seller_home, name='sellerhome'),
    path('addproduct', views.add_product, name='addproduct'),
    path('changePassword', views.change_password, name='changePassword'),
    path('catalogue', views.catalogue, name='catalogue'),
    path('dashboard', views.dash_board, name='dashboard'),
    path('profile', views.seller_profile, name='profile'),
    path('updateStock', views.update_stock, name='updateStock'),
    path('recentOrder', views.recent_order, name='recentOrder'),
    path('orderHistory', views.order_history, name='orderHistory'),
    path('get_stock', views.get_stock, name='get_stock'),   # url in which Ajax call is made, to update stock
]
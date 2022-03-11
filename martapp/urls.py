from django.urls import path
from.import views
urlpatterns=[
    path('index3',views.index3,name='index3'),
    path('contact',views.contact,name='contact'),
    path('condata',views.condata,name='condata'),
    path('contable',views.contable,name='contable'),
    path('register',views.register,name='register'),
    path('regi',views.regi,name='regi'),
    path('registration',views.registration,name='registration'),
    path('userlogin',views.userlogin,name='userlogin'),
    path('userin',views.userin,name='userin'),
    path('logout',views.logout,name='logout'),
    path('products/<str:cat>/',views.products,name='products'),
    path('single/<int:pid>',views.single,name='single'),
    path('cart',views.cart,name='cart'),
    path('check',views.check,name='check'),
    path('cart1/<int:pid>/',views.cart1,name='cart1'),
    path('deletec/<int:cid>/',views.deletec,name='deletec'),
    path('checkout',views.checkout,name='checkout'),
    path('cart_update',views.cart_update,name='cart_update'),
    path('orders',views.orders,name='orders'),
    path('getorder',views.getorder,name='getorder')






]
from django.urls import path
from.import views
urlpatterns=[
    path('index',views.index,name='index'),
    path('addcategory',views.addcategory,name='addcategory'),
    path('viewcategory',views.viewcategory,name='viewcategory'),
    path('getdata',views.getdata,name='getdata'),
    path('edit/<int:martid>/',views.edit,name='edit'),
    path('update/<int:martid>/',views.update,name='update'),
    path('delete/<int:martid>/',views.delete,name='delete'),

    path('addproduct',views.addproduct,name='addproduct'),
    path('viewproduct',views.viewproduct,name='viewproduct'),
    path('getdata1',views.getdata1,name='getdata1'),
    path('edit1/<int:productid>/',views.edit1,name='edit1'),
    path('update1/<int:productid>/',views.update1,name='update1'),
    path('delete1/<int:productid>/',views.delete1,name='delete1'),
    path('',views.adminlogin,name='adminlogin'),
    path('adlogin',views.adlogin,name='adlogin')


]
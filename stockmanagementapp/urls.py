from django.urls import path
from .import views

urlpatterns =[
    path('dashboard/',views.dashboard,name="dashboard.html"),
    path('addadmin/',views.addadmin,name="addadmin.html"),
    path('editadmin/<int:id>',views.editadmin,name="editadmin.html"),
    path('deleteadmin/<int:id>',views.deleteadmin,name="deleteadmin.html"), 
    path('addcategory/',views.addcategory,name="addcategory.html"),
    path('editcategory/<int:id>',views.editcategory,name="editcategory.html"),
    path('deletecategory/<int:id>',views.deletecategory,name="deletecategory "),
    path('addsubcategory/',views.addsubcategory,name="addsubcategory.html"),
    path('editsubcategory/<int:id>',views.editsubcategory,name="editsubcategory.html"),
    path('deletesubcategory/<int:id>',views.deletesubcategory,name="deletesubcategory "),
    path('addproduct/',views.addproduct,name="addproduct.html"),
    path('editproduct/<int:id>',views.editproduct,name="editproduct.html"),
    path('deleteproduct/<int:id>',views.deleteproduct,name="deleteproduct.html"),
    path('addcustomer/', views.addcustomer, name='addcustomer'),
    path('editcustomer/<int:id>', views.editcustomer, name='editcustomer'),
    path('deletecustomer/<int:id>/', views.deletecustomer, name='deletecustomer'),
    path('purchase/', views.purchase, name='purchase'),
    path('deletepurchase/<str:id>/<str:billno>/', views.deletepurchase, name='deletepurchase'),
    path('finalpurchase/<str:billno>', views.finalpurchase, name='finalpurchase'),
    path('purchasecomplete/<str:billno>', views.purchasecomplete, name='purchasecomplete'),
    path('sale/', views.sale, name='sale'),
    path('finalsale/<str:billno>', views.finalsale, name='finalsale'),
    path('salecomplete/<str:billno>', views.salecomplete, name='salecomplete'),
    path('deletesale/<str:id>/<str:billno>/', views.deletesale, name='deletesale'),
    path('allstock/', views.allstock, name='allstock'),
    path('allpurchase/', views.allpurchase, name='allpurchase'),
    path('allsale/', views.allsale, name='allsale'),
    path('allaccount/', views.allaccount, name='allaccount'),
    path('adminlogin/', views.adminlogin, name='adminlogin'),
    path('deletetemppurchase/<str:billno>', views.deletetemppurchase, name='deletetemppurchase'),
     path('deletetempsale/<str:billno>', views.deletetempsale, name='deletetempsale'),




]
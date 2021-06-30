from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.registerPage, name="register"),
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('userSettings/', views.userPage, name="user-page"),

    path('', views.home, name="home"),

    path('products/', views.products, name="products"),
    path('create_product/', views.createProduct, name="create_product"),
    path('update_product/<str:pk>/', views.updateProduct, name="update_product"),
    path('delete_product/<str:pk>/', views.deleteProduct, name="delete_product"),



    path('customerlist/', views.customerlist, name="customerlist"),
    path('customerDetail/<str:pk>/', views.customerDetail, name="customerdetail"),
    path('create_customer/', views.createCustomer, name="create_customer"),
    path('update_customer/<str:pk>/',
         views.updateCustomer, name="update_customer"),
    path('delete_customer/<str:pk>/',
         views.deleteCustomer, name="delete_customer"),

    path('orderslist/', views.orderlist, name="orderslist"),
    path('create_order/', views.createOrder, name="create_order"),
    path('update_order/<str:pk>/', views.updateOrder, name="update_order"),
    path('delete_order/<str:pk>/', views.deleteOrder, name="delete_order"),

    path('stafflist/', views.stafflist, name="stafflist"),
]

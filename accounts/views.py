from django.db.models.query import QuerySet
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from .models import *
from .forms import *
from .decorators import unauthenticated_user, allowed_users, admin_only
from .filters import ProductFilter, CustomerFilter, OrderFilter, StaffFilter


@unauthenticated_user
def registerPage(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')

            messages.success(
                request, 'Account was created for ' + username)
            return redirect('login')

    context = {'form': form}
    return render(request, 'accounts/register.html', context)


@unauthenticated_user
def loginPage(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'username or password is incorrect')
    context = {}
    return render(request, 'accounts/login.html', context)


def logoutUser(request):
    logout(request)
    return redirect('login')


@login_required(login_url='login')
def home(request):
    orders = Order.objects.all()
    customers = Customer.objects.all()
    total_customers = customers.count()
    total_orders = orders.count()
    delivered = orders.filter(status='Delivered').count()
    pending = orders.filter(status='Pending').count()

    context = {'orders': orders, 'customers': customers, 'total_customers': total_customers,
               'total_orders': total_orders, 'delivered': delivered, 'pending': pending}
    return render(request, 'accounts/dashboard.html', context)


@login_required(login_url='login')
def userPage(request):
    staff = request.user.staff
    form = StaffForm(instance=staff)

    if request.method == 'POST':
        form = StaffForm(request.POST, request.FILES, instance=staff)
        if form.is_valid():
            form.save()

    context = {'form': form}
    return render(request, 'accounts/userSettings.html', context)


# ---------- Product related-----------------------
@login_required(login_url='login')
def products(request):
    products = Product.objects.all()

    myFilter = ProductFilter(request.GET, queryset=products)
    products = myFilter.qs

    context = {'products': products, 'myFilter': myFilter}
    return render(request, 'accounts/products.html', context)


@allowed_users(allowed_roles=['admin', 'manager'])
def createProduct(request):
    form = ProductForm()
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/products')
    context = {'form': form}
    return render(request, 'accounts/product_form.html', context)


@allowed_users(allowed_roles=['admin', 'manager'])
def updateProduct(request, pk):
    product = Product.objects.get(id=pk)
    form = ProductForm(instance=product)

    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form}
    return render(request, 'accounts/product_form.html', context)


@allowed_users(allowed_roles=['admin', 'manager'])
def deleteProduct(request, pk):
    product = Product.objects.get(id=pk)
    context = {'item': product}
    return render(request, 'accounts/delete_product.html', context)


# -------------Customer Related ---------
@login_required(login_url='login')
def customerlist(request):
    customer = Customer.objects.all()

    myFilter = CustomerFilter(request.GET, queryset=customer)
    customer = myFilter.qs

    context = {'customer': customer, 'myFilter': myFilter}
    return render(request, 'accounts/customerlist.html', context)


@allowed_users(allowed_roles=['admin', 'manager'])
def customerDetail(request, pk):
    customer = Customer.objects.get(id=pk)
    orders = customer.order_set.all()
    order_count = orders.count()
    context = {'customer': customer,
               'orders': orders, 'order_count': order_count}
    return render(request, 'accounts/customer_detail.html', context)


def createCustomer(request):
    form = CustomerForm()
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/customerlist')

    context = {'form': form}
    return render(request, 'accounts/customer_form.html', context)


def updateCustomer(request, pk):
    customer = Customer.objects.get(id=pk)
    form = CustomerForm(instance=customer)
    if request.method == 'POST':
        form = CustomerForm(request.POST, instance=customer)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form': form}
    return render(request, 'accounts/customer_form.html', context)


@allowed_users(allowed_roles=['admin', 'manager'])
def deleteCustomer(request, pk):
    customer = Customer.objects.get(id=pk)
    if request.method == "POST":
        customer.delete()
        return redirect('/')
    context = {'item': customer}
    return render(request, 'accounts/delete_customer.html', context)


# ------------ Order Related --------------------


@login_required(login_url='login')
def orderlist(request):
    orderlist = Order.objects.all()

    myFilter = OrderFilter(request.GET, queryset=orderlist)
    orderlist = myFilter.qs

    context = {'orderlist': orderlist, 'myFilter': myFilter}
    return render(request, 'accounts/ordersList.html', context)


def createOrder(request):
    form = OrderForm()
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/orderslist')

    context = {'form': form}
    return render(request, 'accounts/order_form.html', context)


def updateOrder(request, pk):
    order = Order.objects.get(id=pk)
    form = OrderForm(instance=order)
    if request.method == 'POST':
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form': form}
    return render(request, 'accounts/order_form.html', context)


@allowed_users(allowed_roles=['admin', 'manager'])
def deleteOrder(request, pk):
    order = Order.objects.get(id=pk)
    if request.method == "POST":
        order.delete()
        return redirect('/')
    context = {'item': order}
    return render(request, 'accounts/delete.html', context)


# -------Staff Related -----

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin', 'manager'])
def stafflist(request):
    stafflist = Staff.objects.all()

    myFilter = StaffFilter(request.GET, queryset=stafflist)
    stafflist = myFilter.qs

    context = {'stafflist': stafflist, 'myFilter': myFilter}
    return render(request, 'accounts/staffList.html', context)

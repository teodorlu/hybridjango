from django.shortcuts import render
from .models import Product, Order


def index(request):
    return render(request, "kiltshop/info.html")

def info2(request):
    return render(request, "kiltshop/info2.html")


def order(request):
    if not request.user.is_authenticated():
        return render(request, 'registration/login.html')
    else:
        user = request.user
        return render(request, "kiltshop/bestilling.html", {'products':Product.objects.filter(order=Order.objects.filter(user=user))})


def shop(request):
    user = request.user
    if request.method == 'POST':
        products = request.POST.getlist('product', None)
        if products is not None:
            if Order.objects.filter(user=user).exists():
                order = Order.objects.filter(user=user).first()
                order.products.add(*products)
                print(order)
                order.save()
            else:
                order = Order.objects.create(user=user)
                order.products.add(*products)
                order.save()
    return render(request, "kiltshop/shop.html", {"products": Product.objects.all(), "kilts": Product.objects.filter(type="k")})


def admin(request):

    if not request.user.is_staff:
        return render(request, 'registration/login.html')
    else:
        user = request.user
        orders = Order.objects.all()
        return render(request, "kiltshop/admin.html", {'orders': orders})
from django.shortcuts import redirect
from .models import Cart
from store.models import Product

def add_to_cart(request,id):
    product = Product.objects.get(id=id)
    Cart.objects.create(user=request.user, product=product)
    return redirect("/")

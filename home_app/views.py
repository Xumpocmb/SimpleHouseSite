from django.shortcuts import render
from .models import Product, Category


def index(request, category_id=None):
    context = {
        'title': 'SimpleHouse',
        'products': Product.objects.filter(category_id=category_id) if category_id else Product.objects.all(),
        'categories': Category.objects.all()
    }
    return render(request, 'home_app/index.html', context)

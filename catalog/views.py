from django.shortcuts import render

from .models import  Products

def product_list(request):
    context = {
        'product_list': Products.objects.all()
         }
    return render(request, 'catalog/product_list.html', context)

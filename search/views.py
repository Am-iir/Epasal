from django.db.models import Q
from django.shortcuts import render
from products.models import Product
# Create your views here.

def search_products_list(request):

    query= request.GET.get('q')
    print(query)
    if query is not None:
        lookups = (Q( title__icontains=query)| Q(description__icontains=query))
        qs= Product.objects.filter(lookups).distinct()    
    
    context={
        'query':query,
        'obj_list':qs
    }

    return render (request,'search.html',context)
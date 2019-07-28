from django.shortcuts import render,get_object_or_404 
from django.http import Http404
from django.views.generic import DetailView

# Create your views here.

from .models import Product
from cart.models import Cart

def products_list(request):
    qs= Product.objects.all()
    context={
        'obj_list':qs
    }

    return render (request,'product_list.html',context)

def products_detail(request ,pk=None, *args ,**kwargs):
    instance = get_object_or_404(Product, pk=pk)
    context = {
        'object':instance
    }

    return render(request,'product_detail.html',context)

class products_detail_slug(DetailView):
    queryset = Product.objects.all()
    template_name = 'product_detail.html'

    def get_context_data(self , *args, **kwargs):
        context = super(products_detail_slug ,self).get_context_data(*args , **kwargs)
        cart_obj , new_obj = Cart.objects.new_or_get(self.request)
        context['cart']=cart_obj
        return context


    def get_object(self, *args , **kwargs):
        request = self.request
        slug = self.kwargs.get('slug')
        # instance = get_object_or_404(Product, slug=slug)
        try:
            instance = Product.objects.get(slug= slug)
        except Product.DoesNotExist:
            raise Http404("Not Found ..")
        except Product.MultipleObjectsReturned:
            qs = Product.objects.filter(slug=slug)
            instance = qs.first()

        return instance
    


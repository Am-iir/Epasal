from django.conf.urls import url
from .views import (
    search_products_list,
    
    )

urlpatterns = [    
    url(r'^$',search_products_list,name='search'),     
]



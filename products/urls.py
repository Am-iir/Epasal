from django.conf.urls import url
from .views import (
    products_list,
    products_detail_slug
    )

urlpatterns = [    
    url(r'^$',products_list,name='list'),
    # url(r'^product/(?P<pk>\d+)/$',products_detail),
    url(r'^(?P<slug>[\w-]+)/$',products_detail_slug.as_view(),name='detail')    
]



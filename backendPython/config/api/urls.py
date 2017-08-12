from . import apiviews
from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    url(r'products/(?P<key>[0-9]+)/$', apiviews.Products.as_view(), name='produtos'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
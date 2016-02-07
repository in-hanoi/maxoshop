# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.conf.urls import patterns, url
from shop.search.views import SearchView
from maxoshop.models.commodity import Commodity
from maxoshop.serializers import ProductSearchSerializer


autocomplete_options = dict(
    serializer_class=ProductSearchSerializer,
    index_models=[Commodity],
)
urlpatterns = patterns('',
    url(r'^', SearchView.as_view(**autocomplete_options)),
)

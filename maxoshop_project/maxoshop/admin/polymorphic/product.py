# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from django.db.models import Max
from django.template.context import Context
from django.template.loader import get_template
from django.utils.translation import ugettext_lazy as _
from adminsortable2.admin import SortableAdminMixin
from cms.admin.placeholderadmin import PlaceholderAdminMixin, FrontendEditableAdminMixin
from parler.admin import TranslatableAdmin
from polymorphic.admin import (PolymorphicParentModelAdmin, PolymorphicChildModelAdmin,
    PolymorphicChildModelFilter)
from shop.admin.product import CMSPageAsCategoryMixin, ProductImageInline
# go up to app_module maxoshop: /maxoshop/admin/polymorphic/product.py
from ...models.polymorphic.product import Product
from ...models.polymorphic.smartcard import SmartCard
from ...models.polymorphic.smartphone import OperatingSystem, SmartPhone, SmartPhoneModel


class SmartCardAdmin(SortableAdminMixin, TranslatableAdmin, FrontendEditableAdminMixin,
                     CMSPageAsCategoryMixin, PlaceholderAdminMixin, PolymorphicChildModelAdmin):
    base_model = Product
    fieldsets = (
        (None, {
            'fields': ('name', 'slug', 'product_code', 'unit_price', 'active',),
        }),
        (_("Translatable Fields"), {
            'fields': ('description',)
        }),
        (_("Properties"), {
            'fields': ('manufacturer', 'storage', 'card_type', 'speed',)
        }),
    )
    filter_horizontal = ('cms_pages',)
    inlines = (ProductImageInline,)
    prepopulated_fields = {'slug': ('name',)}


@admin.register(OperatingSystem)
class OperatingSystemAdmin(admin.ModelAdmin):
    pass


class SmartPhoneInline(admin.TabularInline):
    model = SmartPhone
    extra = 0


class SmartPhoneAdmin(TranslatableAdmin, FrontendEditableAdminMixin,
                      CMSPageAsCategoryMixin, PlaceholderAdminMixin, PolymorphicChildModelAdmin):
    base_model = Product
    fieldsets = (
        (None, {
            'fields': ('name', 'slug', 'active',),
        }),
        (_("Translatable Fields"), {
            'fields': ('description',)
        }),
        (_("Properties"), {
            'fields': ('manufacturer', 'battery_type', 'battery_capacity', 'ram_storage',
                'wifi_connectivity', 'bluetooth', 'gps', 'operating_system',
                ('width', 'height', 'weight',), 'screen_size'),
        }),
    )
    filter_horizontal = ('cms_pages',)
    inlines = (ProductImageInline, SmartPhoneInline,)
    prepopulated_fields = {'slug': ('name',)}

    def save_model(self, request, obj, form, change):
        if not change:
            # since SortableAdminMixin is missing on this class, ordering has to be computed by hand
            max_order = self.base_model.objects.aggregate(max_order=Max('order'))['max_order']
            obj.order = max_order + 1 if max_order else 1
        super(SmartPhoneAdmin, self).save_model(request, obj, form, change)

    def render_text_index(self, instance):
        template = get_template('search/indexes/maxoshop/commodity_text.txt')
        return template.render(Context({'object': instance}))
    render_text_index.short_description = _("Text Index")


@admin.register(Product)
class ProductAdmin(SortableAdminMixin, PolymorphicParentModelAdmin):
    base_model = Product
    child_models = ((SmartPhoneModel, SmartPhoneAdmin), (SmartCard, SmartCardAdmin),)
    list_display = ('name', 'get_price', 'product_type', 'active',)
    list_display_links = ('name',)
    search_fields = ('name',)
    list_filter = (PolymorphicChildModelFilter,)
    list_per_page = 250
    list_max_show_all = 1000

    def get_price(self, obj):
        return obj.get_real_instance().get_price(None)
    get_price.short_description = _("Price starting at")

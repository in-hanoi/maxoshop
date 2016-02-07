# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
# go up to app_module
from ..models.properties import Manufacturer


@admin.register(Manufacturer)
class ManufacturerAdmin(admin.ModelAdmin):
    pass

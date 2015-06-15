#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.contrib import admin
# from django.contrib.admin.sites import AdminSite


# Register your models here.

from examples import models
from django.apps import AppConfig


class ExamplesConfig(AppConfig):
    name = u'examples'
    verbose_name = u"文章应用模块管理"


class CommentInline(admin.TabularInline):
    model = models.Comment


class DocumentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'create_time')
    search_fields = ('name', 'text')

    def change_view(self, request, object_id, form_url='', extra_context=None):
        result = super(DocumentAdmin, self).change_view(
            request, object_id,
            form_url=form_url,
            extra_context=extra_context)

        document = models.Document.objects.get(id__exact=object_id)

        if '_addanother' not in request.POST and \
                '_continue' not in request.POST:
            result['Location'] = document.get_absolute_url()
        return result


class CommentAdmin(admin.ModelAdmin):
    pass



# site_obj = AdminSite(name="文章模块")
admin.site.register(models.Document, DocumentAdmin)
admin.site.register(models.Comment, CommentAdmin)
admin.site.register(models.Tag)

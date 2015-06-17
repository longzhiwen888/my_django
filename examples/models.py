#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.db import models
from django.core.urlresolvers import reverse


class Document(models.Model):
    """A Document is a blog post or wiki entry with some text content"""
    name = models.CharField(u'文章标题', max_length=255)
    text = models.TextField(u'正文')
    create_time = models.DateTimeField(u'创建时间')

    def get_absolute_url(self):
        return reverse('document_preview', args=[self.id])

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = '文章'   # 修改从管理级'产品中心'进入后的页面显示，显示为'产品'
        verbose_name_plural = '文章管理'  # 修改管理级页面显示
        app_label = 'examples'


class Comment(models.Model):
    """A Comment is some text about a given Document"""
    document = models.ForeignKey(Document, related_name='comments')
    text = models.TextField()

    def get_absolute_url(self):
        return reverse('comment_preview', args=[self.id])

    class Meta:
        verbose_name = '评论'  # 修改从管理级'产品中心'进入后的页面显示，显示为'产品'
        verbose_name_plural = '评论管理'   # 修改管理级页面显示
        app_label = 'examples'


class Tag(models.Model):
    """
    The Tags with the document.
    """
    document = models.ForeignKey(Document, related_name='tags')
    name = models.CharField(max_length=255)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = '标签'  # 修改从管理级'产品中心'进入后的页面显示，显示为'产品'
        verbose_name_plural = '标签管理'   # 修改管理级页面显示
        app_label = 'examples'

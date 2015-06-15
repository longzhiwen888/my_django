#!/usr/bin/env python
# -*- coding: utf-8 -*-

from haystack import indexes
from examples.models import Document


class DocumentIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    name = indexes.CharField(model_attr='name')
    create_time = indexes.DateTimeField(model_attr='create_time')

    def get_model(self):
        return Document

    def index_queryset(self):
        """Used when the entire index for model is updated."""
        return self.get_model().objects.all()

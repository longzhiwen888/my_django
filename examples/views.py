from django.shortcuts import render
from django.http import HttpResponse

from examples.models import Document, Comment, Tag


def document_preview(request, doc_id):
    doc = Document.objects.get(id=doc_id)
    tags = Tag.objects.filter(document__id=doc_id).all()
    comments = Comment.objects.filter(document__id=doc_id).all()

    prev_doc = Document.objects.filter(id__lt=doc_id).order_by("-id").first()
    prev_doc_url = prev_doc.get_absolute_url() if prev_doc else ''
    next_doc = Document.objects.filter(id__gt=doc_id).order_by("id").first()
    next_doc_url = next_doc.get_absolute_url() if next_doc else ''

    context = {'doc': doc, 'tags': tags, 'comments': comments,
               'prev_doc_url': prev_doc_url, 'next_doc_url': next_doc_url}

    return render(request, 'admin/examples/document/document.html', context)


def comment_preview(request, doc_id):
    comment = Comment.objects.get(id=doc_id)
    output = str(comment)
    return HttpResponse(output)

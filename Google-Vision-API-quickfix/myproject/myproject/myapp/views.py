# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from myproject.myapp.models import Document
from myproject.myapp.forms import DocumentForm
from myproject.myapp.visionary import googleapiremote
import json
from vis import main, DETECTION_TYPES

def list(request):
    # Handle file upload
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            if '_googleapiclient' in request.POST:
                print("Google Api Client Test")
                print(googleapiremote("a"))
            elif '_upload' in request.POST:
                newdoc = Document(docfile=request.FILES['docfile'])
                newdoc.save()
                # Redirect to the document list after POST
                return HttpResponseRedirect(reverse('list'))
    else:
        form = DocumentForm()  # A empty, unbound form

    # Load documents for the list page
    documents = Document.objects.all()

    # Render list page with the documents and the form
    return render(
        request,
        'list.html',
        {'documents': documents, 'form': form}
    )

def api(request):
    context = dict()
    documents = Document.objects.all()
    context['documents'] = documents

    if request.method == 'POST':
        data = request.POST.dict()

        pictures = data["input"]
        pictures = json.loads(pictures)

        for picture in pictures:
            print(picture)
            # Call API here
            main(picture, DETECTION_TYPES, 4, "output")

    return render(
        request,
        'api.html',
        context
    )

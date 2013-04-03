# Create your views here.
from django.http import HttpResponse
from django.template import loader, Context
from django.shortcuts import render_to_response
from django.contrib.flatpages.models import FlatPage

def search(request):
    query = request.GET['q']
    return render_to_response('search/search.html',
                       {'query': query,
                        'results': FlatPage.objects.filter(content_icontains=query)})

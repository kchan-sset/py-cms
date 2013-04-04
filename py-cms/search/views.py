# Create your views here.
from django.http import HttpResponse
from django.template import loader, Context
from django.shortcuts import render_to_response
from django.contrib.flatpages.models import FlatPage

"""content__icontains looks for the content field in the Flatpage table -
   there are two underscores """
def search(request):
    query = request.GET.get('q', '')
    results = []
    if query:
        results = FlatPage.objects.filter(content__icontains=query)

    return render_to_response('search/search.html',
                       {'query': query,
                        'results': results})

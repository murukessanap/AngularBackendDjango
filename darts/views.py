from django.http import HttpResponse
#from django.template import loader
from django.template.loader import render_to_string


def index(request):
    rendered = render_to_string('index.html', {'foo': 'bar'})
    #context = {'list': ['1','2','3']}
    #template = loader.get_template('index.html')
    return HttpResponse(rendered)
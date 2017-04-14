from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template import RequestContext

def Portada(request):
    return render_to_response('portada/index.html')

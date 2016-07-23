from django.shortcuts import render
from django.shortcuts import render_to_response

# Create your views here.
from django.http import HttpResponse
from django.template import loader

def index(request):
    template = loader.get_template("home.html")
    return HttpResponse(template.render())

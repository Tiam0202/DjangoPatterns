from django.shortcuts import render_to_response
from patterns import *


def index(request):
    return render_to_response('index.html')
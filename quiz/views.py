from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.urls import reverse
from django.views import generic

def IndexView(request):
    return HttpResponse("Hello, world. You're at the polls index.")



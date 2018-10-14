"""Project views."""
from django.views.generic import TemplateView
# from django.http import HttpResponse
# from django.shortcuts import render


# Create your views here.
# def index(request):
#     """Home page."""
#     return HttpResponse("Hello, world. You're at the project index.")

class IndexView(TemplateView):
    """Home page."""

    template_name = "index.html"

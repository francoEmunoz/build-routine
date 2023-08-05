from django.views.generic.base import TemplateView
from django.shortcuts import render

class HomePageView( TemplateView ):
    template_name = "core/home.html"

def handler404(request, exception):
    return render(request, "core/notFound.html", status=404)
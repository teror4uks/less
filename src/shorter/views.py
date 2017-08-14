from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.views import View
from .models import LessUrl

# Create your views here.

def less_redirect_view(request, shortcode=None ,*args, **kwargs):
    obj = get_object_or_404(LessUrl, shortcode=shortcode)
    return HttpResponseRedirect(obj.url)

class LessBasedView(View):
    def get(self, request, shortcode=None, *args, **kwargs):
        obj = get_object_or_404(LessUrl, shortcode=shortcode)
        return HttpResponseRedirect(obj.url)


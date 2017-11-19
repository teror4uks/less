from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.views import View
from .models import LessUrl
from .forms import SubmitUrlForm
# Create your views here.


class HomeView(View):

    def get(self, request, *args, **kwargs):
        the_form = SubmitUrlForm()
        context = {
            "title": "Less.tk",
            "form": the_form
        }
        return render(request, "templates/shorter/home.html", context=context)

    def post(self, request, *args, **kwargs):
        form = SubmitUrlForm(request.POST)
        context = {
            "title": "Less.tk",
            "form": form
        }
        template = "shorter/home.html"
        if form.is_valid():
            new_url = form.cleaned_data.get('url')
            obj, created = LessUrl.objects.get_or_create(url=new_url)
            context = {
                "object": obj,
                "created": created
            }
            if created:
                template = "shorter/success.html"
            else:
                template = "shorter/already-exists.html"

        return render(request, template, context)


class LessBasedView(View):
    def get(self, request, shortcode=None, *args, **kwargs):
        obj = get_object_or_404(LessUrl, shortcode=shortcode)
        return HttpResponseRedirect(obj.url)


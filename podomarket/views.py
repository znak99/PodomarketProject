from django.shortcuts import render
from django.urls import reverse
from django.views.generic import ListView
from allauth.account.views import PasswordChangeView
from podomarket.models import Post

class IndexView(ListView):
    model = Post
    template_name = "podomarket/index.html"
    context_object_name = "posts"
    paginate_by = 8
    ordering = ["-dt_updated"]

class CustomPasswordChangeView(PasswordChangeView):
    def get_success_url(self):
        return reverse('index')
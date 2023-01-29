from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from podomarket.views import CustomPasswordChangeView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('podomarket.urls')),
    path(
        'email-confirmation-done/',
        TemplateView.as_view(template_name='podomarket/email_confirmation_done.html'),
        name='account_email_confirmation_done',
    ),
    path('password/change/', CustomPasswordChangeView.as_view(), name='account_change_password'),
    path('', include('allauth.urls')),
]

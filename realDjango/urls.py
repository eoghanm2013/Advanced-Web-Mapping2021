
from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('world.urls')),
    #path('registration/signup/', TemplateView.as_view(template_name='signup.html'), name='signup'),
    path('map/', TemplateView.as_view(template_name='map.html'), name='home'),
    path('', TemplateView.as_view(template_name='loggedout.html'), name='loggedout'),

]

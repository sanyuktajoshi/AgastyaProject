from django.contrib import admin
from django.urls import path,include
from ideavault import views
from django.views.generic.base import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path("login/",views.user_login, name="login"),
    path("logout/",views.user_logout, name="logout"),
    path("upload/",views.upload_project,name="uploadForm"),
    path("explore/",views.explore,name="explore"),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),         
]
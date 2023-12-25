from django.contrib import admin
from django.urls import path,include
from ideavault import views
from django.views.generic.base import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path("login/",views.user_login, name="login"),
    path("logout/",views.user_logout, name="logout"),
    path("upload/",views.upload_project,name="uploadForm"),
    path("explore",views.explore,name="explore"),
    path('projectDetails/<int:pk>/',views.projectDetails, name="projectDetails"),
    path('project/<int:pk>/become-mentor/', views.become_mentor, name='become_mentor'),
    path('project/<int:pk>/become-sponsor/', views.become_sponsor, name='become_sponsor'),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),         
]
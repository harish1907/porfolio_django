from django.urls import path
from home import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('skills', views.skills, name='skills'),
    path('hire', views.hire, name='hire'),
    path('contact', views.contact, name='contact')
]

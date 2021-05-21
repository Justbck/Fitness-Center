from django.urls import path
from base.views import personalClass_views as views


urlpatterns = [
    path('', views.getPersonalClasses, name="personal-classes"),
    path('<str:pk>', views.getPersonalClass, name="personal-class"),
]
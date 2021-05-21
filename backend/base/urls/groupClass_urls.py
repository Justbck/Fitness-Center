from django.urls import path
from base.views import groupClass_views as views


urlpatterns = [
    path('', views.getGroupClasses, name="group-classes"),
    path('<str:pk>', views.getGroupClass, name="group-class"),
]
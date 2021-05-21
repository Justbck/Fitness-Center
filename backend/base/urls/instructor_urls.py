from django.urls import path
from base.views import instructor_views as views


urlpatterns = [
    path('', views.getInstructors, name="instructors"),
    path('<str:pk>', views.getInstructor, name="instructor"),
]
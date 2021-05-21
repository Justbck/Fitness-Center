from django.urls import path
from base.views import user_views as views


urlpatterns = [
    path('login/', views.MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('register/', views.registerUser, name = 'register'),
    path('profile/', views.getUser, name="user"),
    path('profile/update/', views.updateUser, name="user-update"),
    path('', views.getUsers, name="users"),
]
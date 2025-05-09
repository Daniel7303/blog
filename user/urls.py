from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView



app_name = 'user'

urlpatterns = [
    path('register/', views.register_view, name='user_register'),
    path('login/', views.login_view, name='login'),
    path('logout/', LogoutView.as_view(next_page='posts:hero'), name='logout'),
]
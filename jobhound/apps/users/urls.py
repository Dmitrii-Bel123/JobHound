from django.contrib.auth.views import LogoutView
from django.urls import path
from . import views

app_name='users' # Пространство имен

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),

    # Это не allauth
    # path('signup/', views.signup_view, name='signup'),
    # path('login/', views.login_view, name='login'),
    # # URL для выхода использует LOGIN_REDIRECT_URL из settings.py
    # path('logout/', LogoutView.as_view(), name='logout'),
]


# s govno228@mail.ru
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LogoutView, LoginView
from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import CustomUserCreationForm


# def signup_view(request):
#     if request.method == 'POST':
#         form = CustomUserCreationForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             login(request, user)
#             return redirect('dashboard')
#     else:
#         form = CustomUserCreationForm()
#     return render(request, 'users/sign_up.html', {'form':form})


# def login_view(request):
#     # Используем стандартный LoginView, но со своим шаблоном
#     # Для простоты можно и свою функцию написать, но так правильнее
#     view = LoginView.as_view(template_name='users/login.html')
#     return view(request)


@login_required
def dashboard(request):
    return render(request, 'users/dashboard.html')


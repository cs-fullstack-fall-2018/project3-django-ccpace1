from django.contrib.auth.decorators import login_required
from django.urls import path
from . import views
from django.contrib.auth.views import login

urlpatterns = [
    path('', views.index, name='base'),
    path('list/', views.list, name='transactions'),
    path('login/', login, {'template_name': 'expense_app/login.html'}, name='login'),
    path('logout/', views.logout, name='logout'),
    path('register/', views.register, name='register'),
    path('profile/', views.logout),

]
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('expenses/', include('expense_app.urls')),
    path('accounts/', include('expense_app.urls'))
]

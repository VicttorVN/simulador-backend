from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('simulador.urls')),  # 🔥 Este é o que faltava!
]
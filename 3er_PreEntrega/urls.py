from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('EscuelaApp.urls')),  # Ruta raíz que incluye las URLs de EscuelaApp
]
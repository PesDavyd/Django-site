from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('mainApp.urls')),
    path('news/', include('news.urls')),
    path('profile/', include('mainpage.urls')),
    path('auth/', include('authentication.urls'))
]

from django.contrib import admin
from django.urls import path, include





urlpatterns = [
    path('admin/', admin.site.urls),

    # api paths
    path('profile/', include('user_profile.urls', namespace='user_profile')),
]

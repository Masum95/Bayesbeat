from django.contrib import admin
from django.urls import path, include


import os
# from dotenv import load_dotenv
# load_dotenv()


urlpatterns = [
    # path(os.getenv('ADMIN_URL')+'/', admin.site.urls),

    path('profile/', include('user_profile.urls', namespace='user_profile')),
]

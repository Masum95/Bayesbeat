from django.urls import path
# from user_profile.views import (
#
# )
from user_profile import views
from django.urls import path
from .views import *

app_name = 'user_profile'


urlpatterns = [

    path('upload/', MyFileView.as_view(), name='home'),
    path('ack/', file_ack_view, name='ack'),
    path('isValidPhone/', isValidPHone, name='isValidPhone')

]

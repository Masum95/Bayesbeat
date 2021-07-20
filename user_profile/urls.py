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
    path('watch_id/', get_watch_id, name='isValidPhone'),
    path('medical_profile/', MedicalProfileView.as_view(), name='medical_profile'),
    path('pdf/', pdfGenerate, name='pdf'),

]

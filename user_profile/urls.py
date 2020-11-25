from django.urls import path
# from user_profile.views import (
#
# )
from user_profile import views
from django.urls import path


app_name = 'workplace_feedback'


urlpatterns = [
    # path('feedbacks/', feedback.FeedbackListCreateAPIView.as_view() , name='workplace_feedback_list' ),
    # path('feedbacks/myfeedbacks/', feedback.MyFeedbackListAPIView.as_view(), name='my_workplace_feedback_list'),
    #
    # path('feedbacks/<str:uuid>/', feedback.FeedbackRetrieveUpdateDestroyAPIView.as_view(), name='workplace_feedback_manipulate'),
    # path('reacts/<str:uuid>/', reaction.ReactionListCreateAPIView.as_view(), name='reaction_list_create'),
    # path('choices/reaction', choices.ReactionChoiceListView.as_view(), name='reaction choices'),
    path('', views.home, name='home')
]

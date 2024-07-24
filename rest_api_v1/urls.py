from django.urls import path
import rest_api_v1.polls.views as poll_views

urlpatterns = [
    path('polls/create', poll_views.CreatePoll.as_view(), name='create-poll'),
    path('polls/create-async', poll_views.CreateAsyncPoll.as_view(), name='create-poll-async'),
    path('polls/list', poll_views.ReadPolls.as_view(), name='read-polls'),
]
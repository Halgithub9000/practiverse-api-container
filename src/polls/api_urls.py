from django.urls import path

from .api_views import PollDetail, PollList

urlpatterns = [
    path("", PollList.as_view(), name="poll-list"),
    path("<int:pk>/", PollDetail.as_view(), name="detail"),
]

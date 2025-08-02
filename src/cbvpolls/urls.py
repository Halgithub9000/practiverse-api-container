from django.urls import path

from cbvpolls.views import DetailView, IndexView, ResultsView, vote

app_name = "cbvpolls"
urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("<int:pk>/", DetailView.as_view(), name="detail"),
    path("<int:pk>/results/", ResultsView.as_view(), name="results"),
    path("<int:question_id>/vote/", vote, name="vote"),
]

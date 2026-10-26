from django.urls import path
from .views import AssessmentRecommendView, ChatView
urlpatterns = [
    path("recommendations/", AssessmentRecommendView.as_view(), name="recommendations"),
    path("chat/", ChatView.as_view(), name="chat"),
]

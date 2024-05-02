from django.urls import path
from .views import AttachmentView


urlpatterns = [
    path("attachment/", AttachmentView.as_view()),
]

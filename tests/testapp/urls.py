from django import forms
from django.urls import include, path
from django.contrib import admin
from django.views.generic import FormView

from trix.widgets import TrixEditor


class EditorForm(forms.Form):
    content = forms.CharField(widget=TrixEditor)


class EditorView(FormView):
    form_class = EditorForm
    template_name = "index.html"


urlpatterns = [
    path("admin/", admin.site.urls),
    path("trix/", include("trix.urls")),
    path("", EditorView.as_view()),
]

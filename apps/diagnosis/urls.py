from django.urls import path

from .views.diagnosis import DiagnosisView
from .views.diagnosis_list import DiagnosisListView
from .views.diagnosis_detail import DiagnosisDetailView


urlpatterns = [
    path(
        "",
        DiagnosisView.as_view(),
        name="diagnosis",
    ),
    path(
        "history/",
        DiagnosisListView.as_view(),
        name="diagnosis-history",
    ),
    path(
        "<int:pk>/",
        DiagnosisDetailView.as_view(),
        name="diagnosis-detail",
    ),
]
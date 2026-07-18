from django.urls import path

from .views.disease import (
    DiseaseDetailView,
    DiseaseListCreateView,
)
from .views.symptom import (
    SymptomDetailView,
    SymptomListCreateView,
)

urlpatterns = [
    # Disease
    path(
        "diseases/",
        DiseaseListCreateView.as_view(),
        name="disease-list-create",
    ),
    path(
        "diseases/<int:id>/",
        DiseaseDetailView.as_view(),
        name="disease-detail",
    ),

    # Symptom
    path(
        "symptoms/",
        SymptomListCreateView.as_view(),
        name="symptom-list-create",
    ),
    path(
        "symptoms/<int:id>/",
        SymptomDetailView.as_view(),
        name="symptom-detail",
    ),
]
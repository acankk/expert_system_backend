from django.urls import path

from .views.disease import DiseaseDetailView, DiseaseListCreateView
from .views.recommendation import (
    RecommendationDetailView,
    RecommendationListCreateView,
)
from .views.rule import RuleDetailView, RuleListCreateView
from .views.symptom import SymptomDetailView, SymptomListCreateView


urlpatterns = [
    # Disease
    path(
        "diseases/",
        DiseaseListCreateView.as_view(),
        name="disease-list-create",
    ),
    path(
        "diseases/<int:pk>/",
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
        "symptoms/<int:pk>/",
        SymptomDetailView.as_view(),
        name="symptom-detail",
    ),

    # Rule
    path(
        "rules/",
        RuleListCreateView.as_view(),
        name="rule-list-create",
    ),
    path(
        "rules/<int:pk>/",
        RuleDetailView.as_view(),
        name="rule-detail",
    ),

    # Recommendation
    path(
        "recommendation/",
        RecommendationListCreateView.as_view(),
        name="recommendation-list-create",
    ),
    path(
        "recommendation/<int:pk>/",
        RecommendationDetailView.as_view(),
        name="recommendation-detail",
    ),
]
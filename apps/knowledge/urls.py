from django.urls import path

from .views.disease import DiseaseListCreateView, DiseaseDetailView
from .views.symptom import SymptomListCreateView, SymptomDetailView
from .views.rule import RuleListCreateView, RuleDetailView


urlpatterns = [
    # Disease
    path("diseases/", DiseaseListCreateView.as_view()),
    path("diseases/<int:id>/", DiseaseDetailView.as_view()),

    # Symptom
    path("symptoms/", SymptomListCreateView.as_view()),
    path("symptoms/<int:id>/", SymptomDetailView.as_view()),

    # Rule
    path("rules/", RuleListCreateView.as_view()),
    path("rules/<int:id>/", RuleDetailView.as_view()),
]
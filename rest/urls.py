from django.urls import path
from .views import (ElementListView, MolarMassView, CalcPHView,
                    GasLawView, CalcStoichiometryView)

urlpatterns = [
    path('elements/', ElementListView.as_view(), name='element-list'),
    path('calculate/molar_mass/', MolarMassView.as_view(), name='molar-mass'),
    path('calculate/ph/', CalcPHView.as_view(), name='ph-calculator'),
    path('calculate/gas_law/', GasLawView.as_view(), name='gas-law'),
    path('calculate/stoichiometry/', CalcStoichiometryView.as_view(), name='stoichiometry')
]

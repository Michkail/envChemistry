from django.urls import path
from .views import (ElementListView, MolarMassView, CalcPHView, GasLawView, StoichiometryReactantProductView,
                    StoichiometryLomonosovLavoisierView, StoichiometryMoleRatioView, VanDerWaalsView,
                    EquilibriumConstantView, GibbsFreeEnergyView, CellPotentialView, RateLawView, HenryLawView,
                    TitrationEquivalenceView, RaoultLawView, EnthalpyEntropyView, BufferPHView, HessLawView,
                    NernstEquationView, FreezingBoilingPointView, HalfLifeView, MoleFractionView,
                    HeatCapacityView, GasDiffusionView)

urlpatterns = [
    path('elements/', ElementListView.as_view(), name='element-list'),
    path('calculate/gas/diffusion/', GasDiffusionView.as_view(), name='gas-diffusion'),
    path('calculate/gas-law/', GasLawView.as_view(), name='gas-law'),
    path('calculate/gas-law/van-der-waals/', VanDerWaalsView.as_view(), name='van-der-waals'),
    path('calculate/stoichiometry/mole-ratio/', StoichiometryMoleRatioView.as_view(), name='reactant-prod'),
    path('calculate/stoichiometry/conservation-mass/', StoichiometryLomonosovLavoisierView.as_view(), name='lavoisier'),
    path('calculate/stoichiometry/reactant-product/', StoichiometryReactantProductView.as_view(), name='mole-ratio'),
    path('calculate/electrochemistry/cell-potential/', CellPotentialView.as_view(), name='cell-potential'),
    path('calculate/electrochemistry/nernst-equation/', NernstEquationView.as_view(), name='nernst-equation'),
    path('calculate/thermodynamics/heat-capacity/', HeatCapacityView.as_view(), name='heat-capacity'),
    path('calculate/thermodynamics/enthalpy-entropy/', EnthalpyEntropyView.as_view(), name='enthalpy-entropy'),
    path('calculate/thermodynamics/hess-law/', HessLawView.as_view(), name='hess-law'),
    path('calculate/kinetics/rate-law/', RateLawView.as_view(), name='rate-law'),
    path('calculate/kinetics/half-life/', HalfLifeView.as_view(), name='half-life'),
    path('calculate/solution/freezing-boiling-point/', FreezingBoilingPointView.as_view(), name='freezing-boiling'),
    path('calculate/solution/mole-fraction/', MoleFractionView.as_view(), name='mole-fraction'),
    path('calculate/ph/', CalcPHView.as_view(), name='ph-calculator'),
    path('calculate/ph/buffer-solution/', BufferPHView.as_view(), name='buffer-ph'),
    path('calculate/henry-law/', HenryLawView.as_view(), name='henry-law'),
    path('calculate/raoult-law/', RaoultLawView.as_view(), name='raoult-law'),
    path('calculate/titration/equivalence-point/', TitrationEquivalenceView.as_view(), name='titration-equivalence'),
    path('calculate/equilibrium/constant/', EquilibriumConstantView.as_view(), name='equilibrium-constant'),
    path('calculate/gibbs-free-energy/', GibbsFreeEnergyView.as_view(), name='gibbs-free-energy'),
    path('calculate/molar-mass/', MolarMassView.as_view(), name='molar-mass')
]

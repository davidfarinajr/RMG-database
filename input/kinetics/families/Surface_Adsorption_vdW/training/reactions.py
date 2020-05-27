#!/usr/bin/env python
# encoding: utf-8

name = "Surface_Adsorption_vdW/training"
shortDesc = u"Reaction kinetics used to generate rate rules"
longDesc = u"""
Put kinetic parameters for specific reactions in this file to use as a
training set for generating rate rules to populate this kinetics family.
"""

entry(
    index = 1,
    label = "H2O + Pt <=> H2OX",
    kinetics = StickingCoefficientBEP(
        A = 7.5E-1,
        n = 0,
        Ea=(0, 'J/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Deutschmann_Pt""",
    longDesc = u"""R6.Deutschmann_Pt."""
)

entry(
    index = 2,
    label = "CO2 + Pt <=> CO2X",
    kinetics = StickingCoefficientBEP(
        A = 5.0E-3,
        n = 0,
        Ea=(0, 'J/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Default""",
    longDesc = u"""R7. Deutschmann_Pt."""
)

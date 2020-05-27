#!/usr/bin/env python
# encoding: utf-8

name = "Surface_Adsorption_vdW/groups"
shortDesc = u""
longDesc = u"""
Physisorption of a gas-phase species onto the surface.

  *1:         *1
      ---->   :
 ~*2~       ~*2~~

The rate, which should be in mol/m2/s,
will be given by k * (mol/m2) * (mol/m3)
so k should be in (m3/mol/s). We will use sticking coefficients.
"""

template(reactants=["Adsorbate", "VacantSite"], products=["Adsorbed"], ownReverse=False)

reverse = "Surface_Desorption_vdW"

reactantNum=2
productNum=1

recipe(actions=[
    ['FORM_BOND', '*1', 0, '*2']
])

entry(
    index = 1,
    label = "Adsorbate",
    group =
"""
multiplicity [1]
1 *1 R u0 p[1,2,3] cx
""",
    kinetics = None,
)

entry(
    index = 2,
    label = "O",
    group =
"""
multiplicity [1]
1 *1 O u0 p[1,2,3] cx
""",
    kinetics = None,
)

entry(
    index = 3,
    label = "Os",
    group =
"""
multiplicity [1]
1 *1 O u0 p[2,3] cx {2,S}
2    R u0 px cx {1,S}
""",
    kinetics = None,
)

entry(
    index = 4,
    label = "Od",
    group =
"""
multiplicity [1]
1 *1 O u0 p2 c0 {2,D}
2    R u0 px cx {1,D}
""",
    kinetics = None,
)

entry(
    index = 5,
    label = "N",
    group =
"""
multiplicity [1]
1 *1 N u0 p[1,2] cx
""",
    kinetics = None,
)

entry(
    index = 6,
    label = "N3s",
    group =
"""
multiplicity [1]
1 *1 N3s u0 p1
""",
    kinetics = None,
)

entry(
    index = 7,
    label = "N3d",
    group =
"""
multiplicity [1]
1 *1 N3d u0 p1
""",
    kinetics = None,
)

entry(
    index = 8,
    label = "N3t",
    group =
"""
multiplicity [1]
1 *1 N3t u0 p1
""",
    kinetics = None,
)

entry(
    index = 9,
    label = "C",
    group =
"""
multiplicity [1]
1 *1 C u0 p1
""",
    kinetics = None,
)

entry(
    index = 10,
    label="VacantSite",
    group =
"""
1 *2 Xv u0 p0 c0
""",
    kinetics = None,
)


tree(
"""
L1: Adsorbate
    L2: O
        L3: Os
        L3: Od
    L2: N
        L3: N3s
        L3: N3d
        L3: N3t
    L2: C
L1: VacantSite
"""
)

# forbidden(
#     label = "charge",
#     group =
# """
# 1 R ux c[+1,-1]
# """,
#     shortDesc = u"""Charges not allowed""",
#     longDesc =
# u"""
# """,
# )

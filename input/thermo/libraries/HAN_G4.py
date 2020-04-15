#!/usr/bin/env python
# encoding: utf-8

name = "HAN_G4"
shortDesc = ""
longDesc = """

"""
entry(
    index = 0,
    label = "[O-][NH2+]CDO",
    molecule = 
"""
1 O u0 p3 c-1 {3,S}
2 O u0 p2 c0 {4,D}
3 N u0 p0 c+1 {1,S} {4,S} {5,S} {6,S}
4 C u0 p0 c0 {2,D} {3,S} {7,S}
5 H u0 p0 c0 {3,S}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.9782,0.00140796,6.63597e-05,-1.28041e-07,8.09037e-11,-7111.93,8.39002], Tmin=(10,'K'), Tmax=(406.432,'K')),
            NASAPolynomial(coeffs=[1.76086,0.023239,-1.42425e-05,4.22217e-09,-4.84123e-13,-6931.76,17.0902], Tmin=(406.432,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-32.4082,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (157.975,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob G4 calculation with 1D Hindered Rotors',
    referenceType = "Theory",
    shortDesc = """G4/1D HR""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 1,
    label = "OCDNNDO",
    molecule = 
"""
1 O u0 p2 c0 {5,S} {7,S}
2 O u0 p2 c0 {4,D}
3 N u0 p1 c0 {4,S} {5,D}
4 N u0 p1 c0 {2,D} {3,S}
5 C u0 p0 c0 {1,S} {3,D} {6,S}
6 H u0 p0 c0 {5,S}
7 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.923,0.00435463,8.50106e-05,-1.62057e-07,9.07417e-11,-1687.79,8.90468], Tmin=(10,'K'), Tmax=(601.358,'K')),
            NASAPolynomial(coeffs=[3.045,0.0286672,-2.17104e-05,7.33469e-09,-9.14527e-13,-1916.2,9.91686], Tmin=(601.358,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (12.9867,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (149.66,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob G4 calculation with 1D Hindered Rotors',
    referenceType = "Theory",
    shortDesc = """G4/1D HR""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 2,
    label = "ONDCO",
    molecule = 
"""
1 O u0 p2 c0 {4,S} {6,S}
2 O u0 p2 c0 {3,S} {7,S}
3 N u0 p1 c0 {2,S} {4,D}
4 C u0 p0 c0 {1,S} {3,D} {5,S}
5 H u0 p0 c0 {4,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.01207,-0.00165947,8.47963e-05,-1.44738e-07,7.75766e-11,-24152.3,8.13041], Tmin=(10,'K'), Tmax=(587.765,'K')),
            NASAPolynomial(coeffs=[1.50558,0.0270158,-1.80323e-05,5.52246e-09,-6.38652e-13,-24058.3,17.1837], Tmin=(587.765,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-173.993,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (149.66,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob G4 calculation with 1D Hindered Rotors',
    referenceType = "Theory",
    shortDesc = """G4/1D HR""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 3,
    label = "[O]NCDO",
    molecule = 
"""
multiplicity 2
1 O u1 p2 c0 {3,S}
2 O u0 p2 c0 {4,D}
3 N u0 p1 c0 {1,S} {4,S} {5,S}
4 C u0 p0 c0 {2,D} {3,S} {6,S}
5 H u0 p0 c0 {3,S}
6 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.97606,0.00160913,6.0595e-05,-1.27569e-07,8.67053e-11,-11532.4,8.618], Tmin=(10,'K'), Tmax=(430.863,'K')),
            NASAPolynomial(coeffs=[2.49296,0.0189041,-1.18919e-05,3.58379e-09,-4.15065e-13,-11437.4,14.1445], Tmin=(430.863,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-73.3166,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (133.032,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob G4 calculation with 1D Hindered Rotors',
    referenceType = "Theory",
    shortDesc = """G4/1D HR""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 4,
    label = "[O-][NH+](O)O",
    molecule = 
"""
1 O u0 p2 c0 {4,S} {6,S}
2 O u0 p2 c0 {4,S} {7,S}
3 O u0 p3 c-1 {4,S}
4 N u0 p0 c+1 {1,S} {2,S} {3,S} {5,S}
5 H u0 p0 c0 {4,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.89202,0.00677108,8.59265e-05,-2.04464e-07,1.38837e-10,-17596.1,8.21794], Tmin=(10,'K'), Tmax=(523.481,'K')),
            NASAPolynomial(coeffs=[5.36155,0.0183405,-1.25521e-05,4.14705e-09,-5.21362e-13,-18062.3,-0.90417], Tmin=(523.481,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-116,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (149.66,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob G4 calculation with 1D Hindered Rotors',
    referenceType = "Theory",
    shortDesc = """G4/1D HR""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 5,
    label = "NC(O)(N)N",
    molecule = 
"""
1  O u0 p2 c0 {5,S} {12,S}
2  N u0 p1 c0 {5,S} {6,S} {7,S}
3  N u0 p1 c0 {5,S} {8,S} {9,S}
4  N u0 p1 c0 {5,S} {10,S} {11,S}
5  C u0 p0 c0 {1,S} {2,S} {3,S} {4,S}
6  H u0 p0 c0 {2,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.7958,0.0118194,0.000157435,-3.35885e-07,2.0289e-10,-28998.4,10.2696], Tmin=(10,'K'), Tmax=(592.212,'K')),
            NASAPolynomial(coeffs=[7.41722,0.0358707,-2.63585e-05,9.33749e-09,-1.23635e-12,-30278,-12.4867], Tmin=(592.212,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-192.478,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (266.063,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob G4 calculation with 1D Hindered Rotors',
    referenceType = "Theory",
    shortDesc = """G4/1D HR""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 6,
    label = "O[N-][N+](DO)O",
    molecule = 
"""
1 O u0 p2 c0 {4,S} {6,S}
2 O u0 p2 c0 {5,S} {7,S}
3 O u0 p2 c0 {4,D}
4 N u0 p0 c+1 {1,S} {3,D} {5,S}
5 N u0 p2 c-1 {2,S} {4,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.88432,0.00688085,9.28599e-05,-2.04342e-07,1.27605e-10,-3311.92,9.14922], Tmin=(10,'K'), Tmax=(567.298,'K')),
            NASAPolynomial(coeffs=[5.37429,0.0224379,-1.71874e-05,5.96472e-09,-7.62636e-13,-3900.36,-0.890762], Tmin=(567.298,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (2.8117,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (149.66,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob G4 calculation with 1D Hindered Rotors',
    referenceType = "Theory",
    shortDesc = """G4/1D HR""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 7,
    label = "[O-][NH+]CDO",
    molecule = 
"""
multiplicity 2
1 O u0 p3 c-1 {3,S}
2 O u0 p2 c0 {4,D}
3 N u1 p0 c+1 {1,S} {4,S} {5,S}
4 C u0 p0 c0 {2,D} {3,S} {6,S}
5 H u0 p0 c0 {3,S}
6 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.97607,0.00160837,6.06005e-05,-1.27592e-07,8.67338e-11,-11532,8.61801], Tmin=(10,'K'), Tmax=(430.736,'K')),
            NASAPolynomial(coeffs=[2.49271,0.0189043,-1.18919e-05,3.58374e-09,-4.15054e-13,-11436.8,14.1459], Tmin=(430.736,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-73.3127,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (133.032,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob G4 calculation with 1D Hindered Rotors',
    referenceType = "Theory",
    shortDesc = """G4/1D HR""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 8,
    label = "[NH][O]",
    molecule = 
"""
multiplicity 3
1 O u1 p2 c0 {2,S}
2 N u1 p1 c0 {1,S} {3,S}
3 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.0254,-0.0015145,9.81487e-06,-9.90808e-09,3.26777e-12,20888.8,4.75601], Tmin=(10,'K'), Tmax=(912.974,'K')),
            NASAPolynomial(coeffs=[2.99621,0.00439361,-2.19043e-06,5.36669e-10,-5.1891e-14,21018.4,9.30828], Tmin=(912.974,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (186.599,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (58.2013,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob G4 calculation with 1D Hindered Rotors',
    referenceType = "Theory",
    shortDesc = """G4/1D HR""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 9,
    label = "[O-][NH2+]CO",
    molecule = 
"""
1 O u0 p2 c0 {4,S} {9,S}
2 O u0 p3 c-1 {3,S}
3 N u0 p0 c+1 {2,S} {4,S} {7,S} {8,S}
4 C u0 p0 c0 {1,S} {3,S} {5,S} {6,S}
5 H u0 p0 c0 {4,S}
6 H u0 p0 c0 {4,S}
7 H u0 p0 c0 {3,S}
8 H u0 p0 c0 {3,S}
9 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.01291,-0.00119485,8.1724e-05,-1.26675e-07,6.37911e-11,-19430.6,8.64438], Tmin=(10,'K'), Tmax=(552.434,'K')),
            NASAPolynomial(coeffs=[-0.287192,0.0330156,-1.95148e-05,5.5733e-09,-6.16201e-13,-19002.5,26.4135], Tmin=(552.434,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-126.397,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (207.862,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob G4 calculation with 1D Hindered Rotors',
    referenceType = "Theory",
    shortDesc = """G4/1D HR""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 10,
    label = "NC(O)N",
    molecule = 
"""
1  O u0 p2 c0 {4,S} {10,S}
2  N u0 p1 c0 {4,S} {6,S} {7,S}
3  N u0 p1 c0 {4,S} {8,S} {9,S}
4  C u0 p0 c0 {1,S} {2,S} {3,S} {5,S}
5  H u0 p0 c0 {4,S}
6  H u0 p0 c0 {2,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.8988,0.0053599,0.000110753,-1.93378e-07,9.8426e-11,-27676.4,7.71965], Tmin=(10,'K'), Tmax=(664.973,'K')),
            NASAPolynomial(coeffs=[2.10193,0.0428848,-3.4158e-05,1.23195e-08,-1.62162e-12,-28028.1,11.214], Tmin=(664.973,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-189.603,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (220.334,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob G4 calculation with 1D Hindered Rotors',
    referenceType = "Theory",
    shortDesc = """G4/1D HR""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 11,
    label = "OCD[N+](O)[O-]",
    molecule = 
"""
1 O u0 p2 c0 {5,S} {7,S}
2 O u0 p2 c0 {4,S} {8,S}
3 O u0 p3 c-1 {4,S}
4 N u0 p0 c+1 {2,S} {3,S} {5,D}
5 C u0 p0 c0 {1,S} {4,D} {6,S}
6 H u0 p0 c0 {5,S}
7 H u0 p0 c0 {1,S}
8 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.91324,0.00542832,0.000103793,-2.21364e-07,1.41783e-10,-25697.5,9.3552], Tmin=(10,'K'), Tmax=(514.667,'K')),
            NASAPolynomial(coeffs=[2.77249,0.0315258,-2.24894e-05,7.26803e-09,-8.75151e-13,-25808.3,11.8838], Tmin=(514.667,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-182.592,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (174.604,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob G4 calculation with 1D Hindered Rotors',
    referenceType = "Theory",
    shortDesc = """G4/1D HR""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 12,
    label = "ONCDO",
    molecule = 
"""
1 O u0 p2 c0 {3,S} {7,S}
2 O u0 p2 c0 {4,D}
3 N u0 p1 c0 {1,S} {4,S} {5,S}
4 C u0 p0 c0 {2,D} {3,S} {6,S}
5 H u0 p0 c0 {3,S}
6 H u0 p0 c0 {4,S}
7 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.93879,0.00383868,7.4799e-05,-1.60124e-07,1.03961e-10,-24591.6,8.01675], Tmin=(10,'K'), Tmax=(510.612,'K')),
            NASAPolynomial(coeffs=[3.37087,0.0210815,-1.34383e-05,4.15109e-09,-4.94632e-13,-24700.4,8.74173], Tmin=(510.612,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-177.522,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (153.818,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob G4 calculation with 1D Hindered Rotors',
    referenceType = "Theory",
    shortDesc = """G4/1D HR""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 13,
    label = "[O-][NH+](O)[O]",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {4,S} {6,S}
2 O u1 p2 c0 {4,S}
3 O u0 p3 c-1 {4,S}
4 N u0 p0 c+1 {1,S} {2,S} {3,S} {5,S}
5 H u0 p0 c0 {4,S}
6 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.95968,0.00227247,5.79917e-05,-1.04266e-07,5.65968e-11,8381.66,8.74368], Tmin=(10,'K'), Tmax=(594.475,'K')),
            NASAPolynomial(coeffs=[2.3971,0.0221843,-1.59636e-05,5.26321e-09,-6.47563e-13,8401.38,14.0729], Tmin=(594.475,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (95.8209,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (128.874,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob G4 calculation with 1D Hindered Rotors',
    referenceType = "Theory",
    shortDesc = """G4/1D HR""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 14,
    label = "[O-][NH3+]",
    molecule = 
"""
1 O u0 p3 c-1 {2,S}
2 N u0 p0 c+1 {1,S} {3,S} {4,S} {5,S}
3 H u0 p0 c0 {2,S}
4 H u0 p0 c0 {2,S}
5 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.04823,-0.00311859,1.70121e-05,-8.47949e-11,-1.17354e-11,6206.9,3.70758], Tmin=(10,'K'), Tmax=(549.166,'K')),
            NASAPolynomial(coeffs=[0.616641,0.0137062,-6.62727e-06,1.52173e-09,-1.34032e-13,6707,19.328], Tmin=(549.166,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (72.9407,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (108.088,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob G4 calculation with 1D Hindered Rotors',
    referenceType = "Theory",
    shortDesc = """G4/1D HR""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 15,
    label = "ODNCDO",
    molecule = 
"""
1 O u0 p2 c0 {4,D}
2 O u0 p2 c0 {3,D}
3 N u0 p1 c0 {2,D} {4,S}
4 C u0 p0 c0 {1,D} {3,S} {5,S}
5 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.93765,0.00379515,5.31499e-05,-1.18805e-07,7.63506e-11,-1008.16,8.05969], Tmin=(10,'K'), Tmax=(546.107,'K')),
            NASAPolynomial(coeffs=[4.55998,0.0128748,-9.24874e-06,3.09783e-09,-3.89013e-13,-1279.49,3.57183], Tmin=(546.107,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (9.9377,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (103.931,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob G4 calculation with 1D Hindered Rotors',
    referenceType = "Theory",
    shortDesc = """G4/1D HR""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 16,
    label = "OCNDO",
    molecule = 
"""
1 O u0 p2 c0 {4,S} {7,S}
2 O u0 p2 c0 {3,D}
3 N u0 p1 c0 {2,D} {4,S}
4 C u0 p0 c0 {1,S} {3,S} {5,S} {6,S}
5 H u0 p0 c0 {4,S}
6 H u0 p0 c0 {4,S}
7 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.97783,0.00122619,7.11693e-05,-1.18675e-07,6.23189e-11,-13317.2,8.2624], Tmin=(10,'K'), Tmax=(497.885,'K')),
            NASAPolynomial(coeffs=[0.0974268,0.0323988,-2.27381e-05,7.05666e-09,-8.08886e-13,-12930.8,24.2773], Tmin=(497.885,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-84.0274,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (149.66,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob G4 calculation with 1D Hindered Rotors',
    referenceType = "Theory",
    shortDesc = """G4/1D HR""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 17,
    label = "[N-]([N+](DO)N)[O]",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {3,D}
2 O u1 p2 c0 {5,S}
3 N u0 p0 c+1 {1,D} {4,S} {5,S}
4 N u0 p1 c0 {3,S} {6,S} {7,S}
5 N u0 p2 c-1 {2,S} {3,S}
6 H u0 p0 c0 {4,S}
7 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.91086,0.00542096,8.49229e-05,-1.84116e-07,1.16848e-10,27911.7,9.59517], Tmin=(10,'K'), Tmax=(543.427,'K')),
            NASAPolynomial(coeffs=[4.29889,0.0221292,-1.5199e-05,4.96181e-09,-6.13955e-13,27580.6,5.30183], Tmin=(543.427,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (262.555,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (157.975,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob G4 calculation with 1D Hindered Rotors',
    referenceType = "Theory",
    shortDesc = """G4/1D HR""",
    longDesc = 
"""

""",
    rank = 5,
)


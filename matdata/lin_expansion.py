from math import log10, fabs, floor, erf, exp
'''
Linear Thermal expansion functions

'''
def Inconel_718:
    #Inconel (UNS N107718)
    #Data Range: 6-275
    #Equation Range: 4-300
    #Curve Fit % Error Relative to Data: 2
    #[m/m]
    a=-2.368E2
    b=-2.120E-1
    c=5.497E-3
    d=-6.882E-6
    e=0

    T_low =20
    f =-238.87

    if T <= T_low:
        ans = f
    else:
        ans = a + (b*T) + (c*(T**(2))) + (d*(T**(3))) + (e*(T**(4)))
    return ans

def AL_ALY_3003F(T):
    #3003F Aluminum (UNS A93003)
    #Data Range: 4-300
    #Equation Range: 4-300
    #Curve Fit % Error Relative to Data: 4
    #[m/m] 
    a=-4.1277E2
    b=-3.0389E-1
    c=8.7696E-3
    d=-9.9821E-6
    e=0

    T_low =18.0
    f =-415.45

    if T <= T_low:
        ans = f
    else:
        ans = a + (b*T) + (c*(T**(2))) + (d*(T**(3))) + (e*(T**(4)))
    return ans

def AL_ALY_5083(T):
    # Annealed (-O) UNS A95083
    #Data Range: 4-300
    #Equation Range: 4-300
    #Curve Fit % Error Relative to Data: 4
    #[m/m]
    a=-4.1277E2
    b=-3.0389E-1
    c=8.7696E-3
    d=-9.9821E-6

    T_low = 18
    f =-415.45

    if T <= T_low:
        ans = f
    else:
        ans = a + (b*T) + (c*(T**(2))) + (d*(T**(3)))
    return ans

def AL_ALY_6061(T):
    # Heat treated (-T6) UNS A96061
    #Data Range: 4-300
    #Equation Range: 4-300
    #Curve Fit % Error Relative to Data: 4
    #[m/m]
    a=-4.1277E2
    b=-3.0389E-1
    c=8.7696E-3
    d=-9.9821E-6
    e=0

    T_low =18
    f =-415.45

    if T <= T_low:
        ans = f
    else:
        ans = a + (b*T) + (c*(T**(2))) + (d*(T**(3))) + (e*(T**(4)))
    return ans

def Beechwood_Phenolic_90(T):
    # (cross-laminate [0/90], grain direction)
    #Data Range: 77-293
    #Equation Range: 77-293
    #Curve Fit % Error Relative to Data: 0.89
    #[m/m]
    a=-944.081
    b=2.909782
    c=0.002971
    d=-1E-05
    e=1.23E-08

    ans = a + (b*T) + (c*(T**(2))) + (d*(T**(3))) + (e*(T**(4)))
    return ans

def Beechwood_Phenolic_uflat(T):
    # (unidirectional, flatwise)
    #Data Range: 4-300
    #Equation Range: 4-300
    #Curve Fit % Error Relative to Data: 4
    #[m/m]
    a=-683.9
    b=2.18264
    c=0.001701
    d=-7.1E-06
    e=1.04E-8	

    ans = a + (b*T) + (c*(T**(2))) + (d*(T**(3))) + (e*(T**(4)))
    return ans

def Beechwood_Phenolic_ugrain(T):
    # (unidirectional, grain direction)
    #Data Range: 4-300
    #Equation Range: 4-300
    #Curve Fit % Error Relative to Data: 4
    #[m/m]
    a=-189.138
    b=0.646759
    c=0.000202
    d=-1.2E-06
    e=1.85e-09

    ans = a + (b*T) + (c*(T**(2))) + (d*(T**(3))) + (e*(T**(4)))
    return ans

def Beryllium_Copper(T):
    # Common Spring material

def Beryllium(T):

def Copper_OFHC_50(T):
    #Copper_OFHC_50_UNS C10100/C10200

def Fiberglass_Epoxy_Normal(T):
    #Fiberglass Epoxy G-10 CR Normal Direction

def Glass_Fabric_He_Warp(T):
    #Polyester Glass Fabric Helium, Warp Direction

def Invar(T):
    #Fe-36Ni UNS K93600

def Molybdenum(T):

def Fe_225_Ni(T):
    #Nickel Steel (Fe-2.25 Ni)

def Fe_325_Ni(T):
    #Nickel Steel (Fe-3.25 Ni) UNS S20103

def Fe_50_Ni(T):
    #Nickel Steel (Fe-5.0 Ni) UNS S20153

def Fe_90_Ni(T):
    # Nickel Steel (Fe-9.0 Ni) UNS S21800

def Nylon(T):
    #Polyamide (Nylon)

def SS_304(T):
    #304 Stainless UNS S30400

def SS_304L(T):
    #304L Stainless UNS S30403

def SS_310(T):
    #310 Stainless UNS S31000

def SS_316(T):
    #316 Stainless UNS S31600

def Teflon(T):
    #Teflon

def Ti_6AL_4V(T):
    #Ti 6Al 4V UNS R56400

def Glass_Mat_Epoxy(T):
    #Glass mat-epoxy

def Polystyrene(T):
    #Polystyrene

def Polyurethane(T):
    #Polyurethane

def PVC(T):
    #Polyvinyl Chloride

def Sapphire(T):
    #Sapphire

def Silicon(T):
    #Silicon


'''
    #Data Range: 4-300
    #Equation Range: 4-300
    #Curve Fit % Error Relative to Data: 4
    #[m/m]
    a=
    b=
    c=
    d=
    e=

    T_low =
    f =

    if T <= T_low:
        ans = f
    else:
        ans = a + (b*T) + (c*(T**(2))) + (d*(T**(3))) + (e*(T**(4)))
    return ans
'''

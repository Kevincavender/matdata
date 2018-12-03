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
    #Data Range: 4-300
    #Equation Range: 4-300
    #Curve Fit % Error Relative to Data: 1.5
    #[m/m]
    a=-3.1150E2
    b=-4.4498E-1
    c=1.0133E-2
    d=-2.4718E-5
    e=2.6277E-8

    T_low =24
    f =-316.68

    if T <= T_low:
        ans = f
    else:
        ans = a + (b*T) + (c*(T**(2))) + (d*(T**(3))) + (e*(T**(4)))
    return ans

def Beryllium_a(T):
    #a-axis
    #Data Range: 75-500
    #Equation Range: 75-500
    #Curve Fit % Error Relative to Data: 1
    #[m/m]
    a=-134.17300
    b=-4.4051E-01
    c=3.4063E-03
    d=-6.5593E-07	
    e=-1.8112E-09

    ans = a + (b*T) + (c*(T**(2))) + (d*(T**(3))) + (e*(T**(4)))
    return ans

def Beryllium_c(T):
    #c-axis
     #Data Range: 75-500
    #Equation Range: 75-500
    #Curve Fit % Error Relative to Data: 1
    #[m/m]
    a=-86.08100
    b=-2.6372E-01
    c=1.3623E-03
    d=3.2709E-06
    e=-4.8719E-09

    ans = a + (b*T) + (c*(T**(2))) + (d*(T**(3))) + (e*(T**(4)))
    return ans

    
def Beryllium_poly(T):
    #polycrystalline
     #Data Range: 75-500
    #Equation Range: 75-500
    #Curve Fit % Error Relative to Data: 1
    #[m/m]
    a=-120.29800
    b=-3.4687E-01
    c=2.5691E-03
    d=8.9848E-07
    e=-2.9422E-09

    ans = a + (b*T) + (c*(T**(2))) + (d*(T**(3))) + (e*(T**(4)))
    return ans


def Copper_OFHC_50(T):
    #Copper_OFHC_50_UNS C10100/C10200
    #expansion coefficient.....????

def Fiberglass_Epoxy_Normal(T):
    #Fiberglass Epoxy G-10 CR Normal Direction
    #Data Range: 4-300
    #Equation Range: 10-300
    #Curve Fit % Error Relative to Data: 1.5
    #[m/m]
    a=-7.198E2
    b=4.455E-1
    c=7.505E-3
    d=-2.219E-6
    e=0

    ans = a + (b*T) + (c*(T**(2))) + (d*(T**(3))) + (e*(T**(4)))
    return ans

def Fiberglass_Epoxy_warp(T):
    #Fiberglass Epoxy G-10 CR Warp Direction
    #Data Range: 4-300
    #Equation Range: 12-300
    #Curve Fit % Error Relative to Data: 2
    #[m/m]
    a=-2.469E2
    b=2.064E-1
    c=3.072E-3
    d=-3.226E-6
    e=0

    ans = a + (b*T) + (c*(T**(2))) + (d*(T**(3))) + (e*(T**(4)))
    return ans

def Glass_Fabric_Normal(T):
    #Polyester Glass Fabric normal Direction
    #Data Range: 80-293
    #Equation Range: 80-285
    #Curve Fit % Error Relative to Data: 2
    #[m/m]
    a=-7.179E2
    b=-3.157E0
    c=5.251E-2
    d=-1.947E-4
    e=2.752E-7

    ans = a + (b*T) + (c*(T**(2))) + (d*(T**(3))) + (e*(T**(4)))
    return ans

def Glass_Fabric_warp(T):
    #Polyester Glass Fabric warp Direction
    #Data Range: 80-293
    #Equation Range: 80-280
    #Curve Fit % Error Relative to Data: 2
    #[m/m]
    a=-3.0897E2
    b=1.0245E0
    c=-2.9503E-3
    d=1.8323E-5
    e=-2.7013E-8

    ans = a + (b*T) + (c*(T**(2))) + (d*(T**(3))) + (e*(T**(4)))
    return ans

def Invar(T):
    #Fe-36Ni UNS K93600
    #Data Range: 4-300
    #Equation Range: 4-300
    #Curve Fit % Error Relative to Data: 5
    #[m/m]
    a=-5.265E1
    b=1.009E-1
    c=8.395E-4
    d=-1.973E-6
    e=8.794E-11

    T_low =80
    f =-40

    if T <= T_low:
        ans = f
    else:
        ans = a + (b*T) + (c*(T**(2))) + (d*(T**(3))) + (e*(T**(4)))
    return ans

def Molybdenum(T):
    #Data Range: 20-500
    #Equation Range: 20-350
    #Curve Fit % Error Relative to Data: 4
    #[m/m]
    a=-90.912613
    b=-0.127173
    c=0.00266801
    d=-5.0432E-06
    e=3.5183E-09

    ans = a + (b*T) + (c*(T**(2))) + (d*(T**(3))) + (e*(T**(4)))
    return ans

def Fe_225_Ni(T):
    #Nickel Steel (Fe-2.25 Ni)
    #Data Range: 4-300
    #Equation Range: 4-265
    #Curve Fit % Error Relative to Data: 1.5
    #[m/m]
    a=-2.104E2
    b=-5.699E-2
    c=5.072E-3
    d=-1.381E-5
    e=1.897E-8

    T_low =6
    f =-210.56

    if T <= T_low:
        ans = f
    else:
        ans = a + (b*T) + (c*(T**(2))) + (d*(T**(3))) + (e*(T**(4)))
    return ans

def Fe_325_Ni(T):
    #Nickel Steel (Fe-3.25 Ni) UNS S20103
    #Data Range: 4-300
    #Equation Range: 4-265
    #Curve Fit % Error Relative to Data: 1.5
    #[m/m]
    a=-2.104E2
    b=-5.699E-2
    c=5.072E-3
    d=-1.381E-5
    e=1.897E-8

    T_low =6
    f =-210.56

    if T <= T_low:
        ans = f
    else:
        ans = a + (b*T) + (c*(T**(2))) + (d*(T**(3))) + (e*(T**(4)))
    return ans

def Fe_50_Ni(T):
    #Nickel Steel (Fe-5.0 Ni) UNS S20153
    #Data Range: 4-300
    #Equation Range: 4-265
    #Curve Fit % Error Relative to Data: 1.5
    #[m/m]
    a=-2.104E2
    b=-5.699E-2
    c=5.072E-3
    d=-1.381E-5
    e=1.897E-8

    T_low =6
    f =-210.56

    if T <= T_low:
        ans = f
    else:
        ans = a + (b*T) + (c*(T**(2))) + (d*(T**(3))) + (e*(T**(4)))
    return ans

def Fe_90_Ni(T):
    # Nickel Steel (Fe-9.0 Ni) UNS S21800
    #Data Range: 4-300
    #Equation Range: 4-265
    #Curve Fit % Error Relative to Data: 1.5
    #[m/m]
    a=-2.104E2
    b=-5.699E-2
    c=5.072E-3
    d=-1.381E-5
    e=1.897E-8

    T_low =6
    f =-210.56

    if T <= T_low:
        ans = f
    else:
        ans = a + (b*T) + (c*(T**(2))) + (d*(T**(3))) + (e*(T**(4)))
    return ans

def Nylon(T):
    #Polyamide (Nylon)
    #Data Range: 4-300
    #Equation Range: 4-300
    #Curve Fit % Error Relative to Data: 1
    #[m/m]
    a=-1.389E3
    b=-1.561E-1
    c=2.988E-2
    d=-7.948E-5
    e=1.181E-7

    ans = a + (b*T) + (c*(T**(2))) + (d*(T**(3))) + (e*(T**(4)))
    return ans

def SS_304(T):
    #304 Stainless UNS S30400
    #Data Range: 4-300
    #Equation Range: 4-300
    #Curve Fit % Error Relative to Data: 5
    #[m/m]
    a=-2.9554E2
    b=-3.9811E-1
    c=9.2683E-3
    d=-2.0261E-5
    e=1.7127E-8

    T_low =23
    f =-300.04

    if T <= T_low:
        ans = f
    else:
        ans = a + (b*T) + (c*(T**(2))) + (d*(T**(3))) + (e*(T**(4)))
    return ans

def SS_304L(T):
    #304L Stainless UNS S30403
    #Data Range: 4-300
    #Equation Range: 4-300
    #Curve Fit % Error Relative to Data: 5
    #[m/m]
    a=-2.9554E2
    b=-3.9811E-1
    c=9.2683E-3
    d=-2.0261E-5
    e=1.7127E-8

    T_low =23
    f =-300.04

    if T <= T_low:
        ans = f
    else:
        ans = a + (b*T) + (c*(T**(2))) + (d*(T**(3))) + (e*(T**(4)))
    return ans

def SS_310(T):
    #310 Stainless UNS S31000
    #Data Range: 4-300
    #Equation Range: 4-300
    #Curve Fit % Error Relative to Data: 5
    #[m/m]
    a=-2.9554E2
    b=-3.9811E-1
    c=9.2683E-3
    d=-2.0261E-5
    e=1.7127E-8

    T_low =23
    f =-300.04

    if T <= T_low:
        ans = f
    else:
        ans = a + (b*T) + (c*(T**(2))) + (d*(T**(3))) + (e*(T**(4)))
    return ans

def SS_316(T):
    #316 Stainless UNS S31600
    #Data Range: 4-300
    #Equation Range: 4-300
    #Curve Fit % Error Relative to Data: 5
    #[m/m]
    a=-2.9554E2
    b=-3.9811E-1
    c=9.2683E-3
    d=-2.0261E-5
    e=1.7127E-8

    T_low =23
    f =-300.04

    if T <= T_low:
        ans = f
    else:
        ans = a + (b*T) + (c*(T**(2))) + (d*(T**(3))) + (e*(T**(4)))
    return ans

def Teflon(T):
    #Teflon
    #Data Range: 4-300
    #Equation Range: 4-300
    #Curve Fit % Error Relative to Data: 2
    #[m/m]
    a=-2.125E3
    b=-8.201E-1
    c=6.161E-2
    d=-3.171E-4
    e=6.850E-7

    ans = a + (b*T) + (c*(T**(2))) + (d*(T**(3))) + (e*(T**(4)))
    return ans

def Ti_6AL_4V(T):
    #Ti 6Al 4V UNS R56400
    #Data Range: 4-300
    #Equation Range: 4-300
    #Curve Fit % Error Relative to Data: 1.5
    #[m/m]
    a=-1.711E2
    b=-2.140E-1
    c=4.807E-3
    d=-7.111E-6
    e=0

    T_low =24
    f =-173.61

    if T <= T_low:
        ans = f
    else:
        ans = a + (b*T) + (c*(T**(2))) + (d*(T**(3))) + (e*(T**(4)))
    return ans

def Glass_Mat_Epoxy(T):
    #Glass mat-epoxy, continuous strand
    #Data Range: 77-293
    #Equation Range: 77-293
    #Curve Fit % Error Relative to Data: 2
    #[m/m]
    a=-4.392E2
    b=1.525E0
    c=-2.384E-3
    d=8.665E-6
    e=-2.857E-9

    ans = a + (b*T) + (c*(T**(2))) + (d*(T**(3))) + (e*(T**(4)))
    return ans

def Polystyrene(T):
    #Polystyrene
    #lin expansion density

def Polyurethane(T):
    #Polyurethane
    #lin expansion density

def PVC(T):
    #Polyvinyl Chloride
    #Data Range: 4-300
    #Equation Range: 4-280
    #Curve Fit % Error Relative to Data: 1
    #[m/m]
    a=-1033.8
    b=2.1922
    c=8.7335 E-3
    d=-3.1408 E-5
    e=5.9411 E-8

    ans = a + (b*T) + (c*(T**(2))) + (d*(T**(3))) + (e*(T**(4)))
    return ans

def Sapphire(T):
    #Sapphire
    #Data Range: 20-293
    #Equation Range: 15-300
    #Curve Fit % Error Relative to Data: 4
    #[m/m]
    a=-7.8850E+01
    b=-2.2346E-02
    c=1.0185E-04
    d=5.5594E-06
    e=-8.5422E-09

    ans = a + (b*T) + (c*(T**(2))) + (d*(T**(3))) + (e*(T**(4)))
    return ans

def Silicon(T):
    #Silicon
    #thermal expansioncoefficient


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

    #Data Range: 4-300
    #Equation Range: 4-300
    #Curve Fit % Error Relative to Data: 4
    #[m/m]
    a=
    b=
    c=
    d=
    e=

    ans = a + (b*T) + (c*(T**(2))) + (d*(T**(3))) + (e*(T**(4)))
    return ans
'''

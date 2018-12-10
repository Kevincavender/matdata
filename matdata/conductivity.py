from math import log10, fabs, floor, erf, exp

'''
Adding Material Properties files/library's myself

'''

def Inconel_718(T):
    # (UNS N107718)
    # [W/(m-K)]
    a = -8.28921
    b =  39.4470
    c = -83.4353
    d = 98.1690
    e = -67.2088
    f = 26.7082
    g = -5.7205
    h = 0.51115
    i = 0
    y1 = a+b*(log10(T)) + c*(log10(T))**2 + d*(log10(T))**3 + e*(log10(T))**4 + f*(log10(T))**5 + g*(log10(T))**6 + h*(log10(T))**7 + i*(log10(T))**8
    ans = 10**(y1)
    return ans

def AL_ALY_1100(T):
    # (UNS A91100)5
    # [W/(m-K)]
    a= 23.39172
    b= - 148.5733
    c=  422.1917
    d= -653.6664
    e=   607.0402
    f= - 346.152
    g=   118.4276
    h= - 22.2781
    i=   1.770187
    y1 = a+b*(log10(T)) + c*(log10(T))**2 + d*(log10(T))**3 + e*(log10(T))**4
    y2 = f*(log10(T))**5 + g*(log10(T))**6 + h*(log10(T))**7 + i*(log10(T))**8
    ans = 10**(y1+y2)
    return ans


def AL_ALY_3003(T):
    # forget what this one means (-F)
    # (UNS A93003)
    # [W/(m-K)]
    a= 0.63736
    b= -1.1437
    c= 7.4624
    d= -12.6905
    e= 11.9165
    f= -6.18721
    g= 1.63939
    h= -0.172667
    i= 0

    y1 = a+b*(log10(T)) + c*(log10(T))**2 + d*(log10(T))**3 + e*(log10(T))**4
    y2 = f*(log10(T))**5 + g*(log10(T))**6 + h*(log10(T))**7 + i*(log10(T))**8
    ans = 10**(y1+y2)
    return ans


def AL_ALY_5083(T):
    # Annealed (-O)
    # (UNS A95083)
    # [W/(m-K)]
    a= -0.90933
    b= 5.751
    c= -11.112
    d= 13.612
    e= -9.3977
    f= 3.6873
    g= -0.77295
    h= 0.067336
    i= 0

    y1 = a+b*(log10(T)) + c*(log10(T))**2 + d*(log10(T))**3 + e*(log10(T))**4
    y2 = f*(log10(T))**5 + g*(log10(T))**6 + h*(log10(T))**7 + i*(log10(T))**8
    ans = 10**(y1+y2)
    return ans


def AL_ALY_6061(T):
    # Heat treated (-T6)
    # [W/(m-K)]
    a=0.07918
    b=1.0957
    c=-0.07277
    d=0.08084
    e=0.02803
    f=-0.09464
    g=0.04179
    h=-0.00571
    i= 0

    y1 = a+b*(log10(T)) + c*(log10(T))**2 + d*(log10(T))**3 + e*(log10(T))**4
    y2 = f*(log10(T))**5 + g*(log10(T))**6 + h*(log10(T))**7 + i*(log10(T))**8
    ans = 10**(y1+y2)
    return ans

def AL_ALY_6063(T):
    # Heat Treated (-T5)
    #
    # [W/(m-K)]
    a=22.401433
    b=-141.13433
    c=394.95461
    d=-601.15377
    e=547.83202
    f=-305.99691
    g=102.38656
    h=-18.810237
    i= 1.4576882

    y1 = a+b*(log10(T)) + c*(log10(T))**2 + d*(log10(T))**3 + e*(log10(T))**4
    y2 = f*(log10(T))**5 + g*(log10(T))**6 + h*(log10(T))**7 + i*(log10(T))**8
    ans = 10**(y1+y2)
    return ans


def Balsa_lowdensity(T):
    #(density = 6 lb/ft3)
    # [W/(m-K)]
    a=4172.447
    b=-11309.97
    c=12745.09
    d=-7647.584
    e=2577.309
    f=-462.538
    g=34.5351
    h=0
    i=0

    y1 = a+b*(log10(T)) + c*(log10(T))**2 + d*(log10(T))**3 + e*(log10(T))**4
    y2 = f*(log10(T))**5 + g*(log10(T))**6 + h*(log10(T))**7 + i*(log10(T))**8
    ans = 10**(y1+y2)
    return ans


def Balsa_highdensity(T):
    #(density = 11 lb/ft3)
    # [W/(m-K)]
    a=4815.4
    b=-12969.63
    c=14520.76
    d=-8654.164
    e=2895.712
    f=-515.7272
    g=38.19218
    h=0
    i=0

    y1 = a+b*(log10(T)) + c*(log10(T))**2 + d*(log10(T))**3 + e*(log10(T))**4
    y2 = f*(log10(T))**5 + g*(log10(T))**6 + h*(log10(T))**7 + i*(log10(T))**8
    ans = 10**(y1+y2)
    return ans


def Beechwood_Phenolic_0(T):
    # (cross-laminate [0/90], grain direction)
    # Data Range: 92-300
    # Equation Range: 80-300
    # Curve Fit % error relative to data: 1
    # [W/(m-K)]
    a=-1375.11
    b=3740.69
    c=3740.69
    d=2559.333
    e=-868.6067
    f=157.1018
    g=-11.82957
    h= 0
    i= 0

    y1 = a+b*(log10(T)) + c*(log10(T))**2 + d*(log10(T))**3 + e*(log10(T))**4
    y2 = f*(log10(T))**5 + g*(log10(T))**6 + h*(log10(T))**7 + i*(log10(T))**8
    ans = 10**(y1+y2)
    return ans


def Beechwood_Phenolic_90(T):
    # (cross-laminate [0/90], flatwise)
    # Data Range: 92-300
    # Equation Range: 75-300
    # Curve Fit % error relative to data: 1.5
    # [W/(m-K)]
    a=1035.33
    b=-2191.85
    c=1470.505
    d=39.845
    e=-541.9035
    f=289.844
    g=-65.2253
    h=5.59956
    i= 0

    y1 = a+b*(log10(T)) + c*(log10(T))**2 + d*(log10(T))**3 + e*(log10(T))**4
    y2 = f*(log10(T))**5 + g*(log10(T))**6 + h*(log10(T))**7 + i*(log10(T))**8
    ans = 10**(y1+y2)
    return ans


def Beryllium_Copper(T):
    # Common Spring material
    # Data Range: 2-80
    # Equation Range: 1-120
    # Curve Fit % error relative to data: 2
    # [W/(m-K)]
    a=-0.50015
    b=1.93190
    c=-1.69540
    d=0.71218
    e=1.27880
    f=-1.61450
    g=0.68722
    h=-0.10501
    i= 0

    y1 = a+b*(log10(T)) + c*(log10(T))**2 + d*(log10(T))**3 + e*(log10(T))**4
    y2 = f*(log10(T))**5 + g*(log10(T))**6 + h*(log10(T))**7 + i*(log10(T))**8
    ans = 10**(y1+y2)
    return ans

def Apiezon_N(T):
    # Data Range: 1-200
    # Equation Range: 2-200
    # Curve Fit % error relative to data: 2
    # [W/(m-K)]
    a=--1.61975
    b=3.10923
    c=-0.712719
    d=4.93675
    e=-9.37993
    f=7.58304
    g=-3.11048
    h=0.628309
    i= -0.0482634

    y1 = a+b*(log10(T)) + c*(log10(T))**2 + d*(log10(T))**3 + e*(log10(T))**4
    y2 = f*(log10(T))**5 + g*(log10(T))**6 + h*(log10(T))**7 + i*(log10(T))**8
    ans = 10**(y1+y2)
    return ans

def Beryllium(T):
    # Data Range: 10-284
    # Equation Range: 14-284
    # Curve Fit % error relative to data: N/A
    # [W/(m-K)]
    a=-526.84477
    b=2755.4105
    c=-6209.8985
    d=7859.2257
    e=-6106.2095
    f=2982.9958
    g=-894.99967
    h=150.85256
    i= -10.943615

    y1 = a+b*(log10(T)) + c*(log10(T))**2 + d*(log10(T))**3 + e*(log10(T))**4
    y2 = f*(log10(T))**5 + g*(log10(T))**6 + h*(log10(T))**7 + i*(log10(T))**8
    ans = 10**(y1+y2)
    return ans

def Brass(T):
    #UNS C26000
    # Data Range: 5-116
    # Equation Range: 5-110
    # Curve Fit % error relative to data: 1.5
    # [W/(m-K)]
    a=0.021035
    b=-1.01835
    c=4.54083
    d=-5.03374
    e=3.20536
    f=-1.12933
    g=0.174057
    h=-0.0038151
    i= 0

    y1 = a+b*(log10(T)) + c*(log10(T))**2 + d*(log10(T))**3 + e*(log10(T))**4
    y2 = f*(log10(T))**5 + g*(log10(T))**6 + h*(log10(T))**7 + i*(log10(T))**8
    ans = 10**(y1+y2)
    return ans

def Copper_OFHC_50(T):
    #Copper_OFHC_50_UNS C10100/C10200
    # Data Range: 4-300
    # Equation Range: N/A
    # Curve Fit % error relative to data: N/A
    # [W/(m-K)]
    a=1.8743
    b=-0.41538
    c=-0.6018
    d=0.13294
    e=0.26426
    f=-0.0219
    g=-0.051276
    h=0.0014871
    i=0.003723
    
    y1 = a + (c * (T**(0.5))) + (e * T) + (g * (T**(1.5))) + (i * (T**(2)))
    y2 = 1 + (b * (T**(0.5))) + (d * T) + (f * (T**(1.5))) + (h * (T**(2)))
    ans = 10**(y1/y2)
    return ans

def Copper_OFHC_100(T):
    #Copper_OFHC_100_UNS C10100/C10200
    # Data Range: 4-300
    # Equation Range: N/A
    # Curve Fit % error relative to data: N/A
    # [W/(m-K)]
    a=2.2154
    b=-0.47461
    c=-0.88068
    d=0.13871
    e=0.29505
    f=-0.02043
    g=-0.04831
    h=0.001281
    i=0.003207
    
    y1 = a + (c * (T**(0.5))) + (e * T) + (g * (T**(1.5))) + (i * (T**(2)))
    y2 = 1 + (b * (T**(0.5))) + (d * T) + (f * (T**(1.5))) + (h * (T**(2)))
    ans = 10**(y1/y2)
    return ans

def Copper_OFHC_150(T):
    #Copper_OFHC_150_UNS C10100/C10200
    # Data Range: 4-300
    # Equation Range: N/A
    # Curve Fit % error relative to data: N/A
    # [W/(m-K)]
    a=2.3797
    b=-0.4918
    c=-0.98615
    d=0.13942
    e=0.30475
    f=-0.019713
    g=-0.046897
    h=0.0011969
    i=0.0029988

    y1 = a + (c * (T**(0.5))) + (e * T) + (g * (T**(1.5))) + (i * (T**(2)))
    y2 = 1 + (b * (T**(0.5))) + (d * T) + (f * (T**(1.5))) + (h * (T**(2)))
    ans = 10**(y1/y2)
    return ans

def Copper_OFHC_300(T):
    #Copper_OFHC_300_UNS C10100/C10200
    # Data Range: 4-300
    # Equation Range: N/A
    # Curve Fit % error relative to data: N/A
    # [W/(m-K)]
    a=1.357
    b=0.3981
    c=2.669
    d=-0.1346
    e=-0.6683
    f=0.01342
    g=0.05773
    h=0.0002147
    i=0
    
    y1 = a + (c * (T**(0.5))) + (e * T) + (g * (T**(1.5))) + (i * (T**(2)))
    y2 = 1 + (b * (T**(0.5))) + (d * T) + (f * (T**(1.5))) + (h * (T**(2)))
    ans = 10**(y1/y2)
    return ans

def Copper_OFHC_500(T):
    #Copper_OFHC_500_UNS C10100/C10200
    # Data Range: 4-300
    # Equation Range: N/A
    # Curve Fit % error relative to data: N/A
    # [W/(m-K)]
    a=2.8075
    b=-0.54074
    c=-1.2777
    d=0.15362
    e=0.36444
    f=-0.02105
    g=-0.051727
    h=0.0012226
    i=0.0030964
    
    y1 = a + (c * (T**(0.5))) + (e * T) + (g * (T**(1.5))) + (i * (T**(2)))
    y2 = 1 + (b * (T**(0.5))) + (d * T) + (f * (T**(1.5))) + (h * (T**(2)))
    ans = 10**(y1/y2)
    return ans
    
def Fiberglass_Epoxy_Normal(T):
    #Fiberglass Epoxy G-10 CR Normal Direction
    # Data Range: 4-300
    # Equation Range: 10-300
    # Curve Fit % error relative to data: 5
    # [W/(m-K)]
    a=-4.1236
    b=13.788
    c=-26.068
    d=26.272
    e=-14.663
    f=4.4954
    g=-0.6905
    h=0.0397
    i=0

    y1 = a+b*(log10(T)) + c*(log10(T))**2 + d*(log10(T))**3 + e*(log10(T))**4
    y2 = f*(log10(T))**5 + g*(log10(T))**6 + h*(log10(T))**7 + i*(log10(T))**8
    ans = 10**(y1+y2)
    return ans

def Fiberglass_Epoxy_Warp(T):
    #Fiberglass Epoxy G-10 CR Warp Direction
    # Data Range: 4-300
    # Equation Range: 12-300
    # Curve Fit % error relative to data: 5
    # [W/(m-K)]
    a=-2.64827
    b=8.80228
    c=-24.8998
    d=41.1625
    e=-39.8754
    f=23.1778
    g=-7.95635
    h=1.48806
    i=-0.11701

    y1 = a+b*(log10(T)) + c*(log10(T))**2 + d*(log10(T))**3 + e*(log10(T))**4
    y2 = f*(log10(T))**5 + g*(log10(T))**6 + h*(log10(T))**7 + i*(log10(T))**8
    ans = 10**(y1+y2)
    return ans

def Glass_Fabric_He_Warp(T):
    #Polyester Glass Fabric Helium, Warp Direction
    # Data Range: 38-300
    # Equation Range: 18-300
    # Curve Fit % error relative to data: 1
    # [W/(m-K)]
    a=689.532
    b=-2543.63
    c=3967.067
    d=-3400.366
    e=1731.725
    f=-524.309
    g=87.4249
    h=-6.19597
    i=0

    y1 = a+b*(log10(T)) + c*(log10(T))**2 + d*(log10(T))**3 + e*(log10(T))**4
    y2 = f*(log10(T))**5 + g*(log10(T))**6 + h*(log10(T))**7 + i*(log10(T))**8
    ans = 10**(y1+y2)
    return ans

def Glass_Fabric_N_Warp(T):
    #Polyester Glass Fabric Nitrogen, Warp Direction
    # Data Range: 80-300
    # Equation Range: 60-300
    # Curve Fit % error relative to data: 1
    # [W/(m-K)]
    a=-2141.58
    b=4639.74
    c=-3249.405
    d=51.72425
    e=1101.977
    f=-613.8563
    g=141.1432
    h=-12.3133
    i=0

    y1 = a+b*(log10(T)) + c*(log10(T))**2 + d*(log10(T))**3 + e*(log10(T))**4
    y2 = f*(log10(T))**5 + g*(log10(T))**6 + h*(log10(T))**7 + i*(log10(T))**8
    ans = 10**(y1+y2)
    return ans

def Glass_Fabric_N_Normal(T):
    #Polyester Glass Fabric Nitrogen, Normal Direction
    # Data Range: 84-300
    # Equation Range: 70-300
    # Curve Fit % error relative to data: 2
    # [W/(m-K)]
    a=2909.905
    b=-8616.64
    c=10542.69
    d=-6832.068
    e=2475.328
    f=-475.7
    g=37.9003
    h=0
    i=0

    y1 = a+b*(log10(T)) + c*(log10(T))**2 + d*(log10(T))**3 + e*(log10(T))**4
    y2 = f*(log10(T))**5 + g*(log10(T))**6 + h*(log10(T))**7 + i*(log10(T))**8
    ans = 10**(y1+y2)
    return ans

def Invar(T):
    #Fe-36Ni UNS K93600
    # Data Range: 4-300
    # Equation Range: 4-300
    # Curve Fit % error relative to data: 2
    # [W/(m-K)]
    a=-2.7064
    b=8.5191
    c=-15.923
    d=18.276
    e=-11.9116
    f=4.40318
    g=-0.86018
    h=0.068508
    i=0

    y1 = a+b*(log10(T)) + c*(log10(T))**2 + d*(log10(T))**3 + e*(log10(T))**4
    y2 = f*(log10(T))**5 + g*(log10(T))**6 + h*(log10(T))**7 + i*(log10(T))**8
    ans = 10**(y1+y2)
    return ans

def Lead(T):
    # Data Range: 4-296
    # Equation Range: 5-295
    # Curve Fit % error relative to data: 2
    # [W/(m-K)]
    a=38.963479
    b=-221.40505
    c=597.56622
    d=-900.93831
    e=816.40461
    f=-455.08342
    g=152.94025
    h=-28.451163
    i= 2.2516244

    y1 = a+b*(log10(T)) + c*(log10(T))**2 + d*(log10(T))**3 + e*(log10(T))**4
    y2 = f*(log10(T))**5 + g*(log10(T))**6 + h*(log10(T))**7 + i*(log10(T))**8
    ans = 10**(y1+y2)
    return ans

def Molybdenum(T):
    # Data Range: 2-373
    # Equation Range: 4-300
    # Curve Fit % error relative to data: 3
    # [W/(m-K)]
    a=10.78259
    b=-72.13065
    c=228.57351
    d=-384.50447
    e=381.43825
    f=-228.83783
    g=81.26658
    h=-15.69097
    i= 1.26814

    y1 = a+b*(log10(T)) + c*(log10(T))**2 + d*(log10(T))**3 + e*(log10(T))**4
    y2 = f*(log10(T))**5 + g*(log10(T))**6 + h*(log10(T))**7 + i*(log10(T))**8
    ans = 10**(y1+y2)
    return ans

def Fe_225_Ni(T):
    #Nickel Steel (Fe-2.25 Ni)
    # Data Range: 4-300
    # Equation Range: 4-300
    # Curve Fit % error relative to data: 2
    # [W/(m-K)]
    a=-3.5785
    b=20.804
    c=-55.826
    d=87.812
    e=-83.5016
    f=49.08
    g=-17.4348
    h=3.4277
    i=-0.28622

    y1 = a+b*(log10(T)) + c*(log10(T))**2 + d*(log10(T))**3 + e*(log10(T))**4
    y2 = f*(log10(T))**5 + g*(log10(T))**6 + h*(log10(T))**7 + i*(log10(T))**8
    ans = 10**(y1+y2)
    return ans

def Fe_325_Ni(T):
    #Nickel Steel (Fe-3.25 Ni) UNS S20103
    # Data Range: 4-300
    # Equation Range: 4-300
    # Curve Fit % error relative to data: 2
    # [W/(m-K)]
    a=0.89481
    b=-8.1998
    c=22.096
    d=-27.645
    e=19.7524
    f=-8.1113
    g=1.77866
    h=-0.16172
    i=0

    y1 = a+b*(log10(T)) + c*(log10(T))**2 + d*(log10(T))**3 + e*(log10(T))**4
    y2 = f*(log10(T))**5 + g*(log10(T))**6 + h*(log10(T))**7 + i*(log10(T))**8
    ans = 10**(y1+y2)
    return ans

def Fe_50_Ni(T):
    #Nickel Steel (Fe-5.0 Ni) UNS S20153
    # Data Range: 4-300
    # Equation Range: 4-300
    # Curve Fit % error relative to data: 3.1
    # [W/(m-K)]
    a=-0.57245
    b=-0.33593
    c=3.9379
    d=-5.4589
    e=4.2337
    f=-1.8653
    g=0.43223
    h=-0.041207
    i=0 

    y1 = a+b*(log10(T)) + c*(log10(T))**2 + d*(log10(T))**3 + e*(log10(T))**4
    y2 = f*(log10(T))**5 + g*(log10(T))**6 + h*(log10(T))**7 + i*(log10(T))**8
    ans = 10**(y1+y2)
    return ans

def Fe_90_Ni(T):
    # Nickel Steel (Fe-9.0 Ni) UNS S21800
    # Data Range: 4-300
    # Equation Range: 4-300
    # Curve Fit % error relative to data: 2
    # [W/(m-K)]
    a=-0.0712785
    b=-3.48735
    c=10.6547
    d=-12.9153
    e=8.89066
    f=-3.51482
    g=0.743643
    h=-0.0657884
    i=0

    y1 = a+b*(log10(T)) + c*(log10(T))**2 + d*(log10(T))**3 + e*(log10(T))**4
    y2 = f*(log10(T))**5 + g*(log10(T))**6 + h*(log10(T))**7 + i*(log10(T))**8
    ans = 10**(y1+y2)
    return ans

def Platinum(T):
    # Data Range: 3-298
    # Equation Range: 4-295
    # Curve Fit % error relative to data: 3
    # [W/(m-K)]
    a=-7.33450054
    b=80.8550484
    c=-268.441084
    d=481.629105
    e=-503.890454
    f=314.812622
    g=-115.699394
    h=23.0957119
    i=-1.93361717

    y1 = a+b*(log10(T)) + c*(log10(T))**2 + d*(log10(T))**3 + e*(log10(T))**4
    y2 = f*(log10(T))**5 + g*(log10(T))**6 + h*(log10(T))**7 + i*(log10(T))**8
    ans = 10**(y1+y2)
    return ans

def Nylon(T):
    #Polyamide (Nylon)
    # Data Range: 4-300
    # Equation Range: 1-300
    # Curve Fit % error relative to data: 2
    # [W/(m-K)]
    a=-2.6135
    b=2.3239
    c=-4.7586
    d=7.1602
    e=-4.9155
    f=1.6324
    g=-0.2507
    h=0.0131
    i=0

    y1 = a+b*(log10(T)) + c*(log10(T))**2 + d*(log10(T))**3 + e*(log10(T))**4
    y2 = f*(log10(T))**5 + g*(log10(T))**6 + h*(log10(T))**7 + i*(log10(T))**8
    ans = 10**(y1+y2)
    return ans

def Mylar(T):
    #Polyethylene Terephthalate (Mylar)
    # Data Range: 1-83
    # Equation Range: 2-80
    # Curve Fit % error relative to data: 1
    # [W/(m-K)]
    a=-1.37737
    b=-3.40668
    c=20.5842
    d=-53.1244
    e=73.2476
    f=-57.6546
    g=26.1192
    h=-6.34790
    i=0.640331

    y1 = a+b*(log10(T)) + c*(log10(T))**2 + d*(log10(T))**3 + e*(log10(T))**4
    y2 = f*(log10(T))**5 + g*(log10(T))**6 + h*(log10(T))**7 + i*(log10(T))**8
    ans = 10**(y1+y2)
    return ans

def Kapton(T):
    #Polyimide (Kapton)
    # Data Range: 4-300
    # Equation Range: 4-300
    # Curve Fit % error relative to data: 2
    # [W/(m-K)]
    a=5.73101
    b=-39.5199
    c=79.9313
    d=-83.8572
    e=50.9157
    f=-17.9835
    g=3.42413
    h=-0.27133
    i=0 

    y1 = a+b*(log10(T)) + c*(log10(T))**2 + d*(log10(T))**3 + e*(log10(T))**4
    y2 = f*(log10(T))**5 + g*(log10(T))**6 + h*(log10(T))**7 + i*(log10(T))**8
    ans = 10**(y1+y2)
    return ans

def SS_304(T):
    #304 Stainless UNS S30400
    # Data Range: 4-300
    # Equation Range: 1-300
    # Curve Fit % error relative to data: 2
    # [W/(m-K)]
    a=-1.4087
    b=1.3982
    c=0.2543
    d=-0.6260
    e=0.2334
    f=0.4256
    g=-0.4658
    h=0.1650
    i=-0.0199

    y1 = a+b*(log10(T)) + c*(log10(T))**2 + d*(log10(T))**3 + e*(log10(T))**4
    y2 = f*(log10(T))**5 + g*(log10(T))**6 + h*(log10(T))**7 + i*(log10(T))**8
    ans = 10**(y1+y2)
    return ans

def SS_304L(T):
    #304L Stainless UNS S30403
    # Data Range: 4-300
    # Equation Range: 1-300
    # Curve Fit % error relative to data: 2
    # [W/(m-K)]
    a=-1.4087
    b=1.3982
    c=0.2543
    d=-0.6260
    e=0.2334
    f=0.4256
    g=-0.4658
    h=0.1650
    i=-0.0199

    y1 = a+b*(log10(T)) + c*(log10(T))**2 + d*(log10(T))**3 + e*(log10(T))**4
    y2 = f*(log10(T))**5 + g*(log10(T))**6 + h*(log10(T))**7 + i*(log10(T))**8
    ans = 10**(y1+y2)
    return ans

def SS_310(T):
    #310 Stainless UNS S31000
    # Data Range: 4-300
    # Equation Range: 1-300
    # Curve Fit % error relative to data: 2
    # [W/(m-K)]
    a=-0.81907
    b=-2.1967
    c=9.1059
    d=-13.078
    e=10.853
    f=-5.1269
    g=1.2583
    h=-0.12395
    i=0 

    y1 = a+b*(log10(T)) + c*(log10(T))**2 + d*(log10(T))**3 + e*(log10(T))**4
    y2 = f*(log10(T))**5 + g*(log10(T))**6 + h*(log10(T))**7 + i*(log10(T))**8
    ans = 10**(y1+y2)
    return ans

def SS_316(T):
    #316 Stainless UNS S31600
    # Data Range: 0.1-291
    # Equation Range: 0-350
    # Curve Fit % error relative to data: 3.1
    # [W/(m-K)]
    a=-1.4087
    b=1.3982
    c=0.2543
    d=-0.6260
    e=0.2334
    f=0.4256
    g=-0.4658
    h=0.1650
    i=-0.0199

    y1 = a+b*(log10(T)) + c*(log10(T))**2 + d*(log10(T))**3 + e*(log10(T))**4
    y2 = f*(log10(T))**5 + g*(log10(T))**6 + h*(log10(T))**7 + i*(log10(T))**8
    ans = 10**(y1+y2)
    return ans

def Teflon(T):
    #Teflon
    # Data Range: 4-300
    # Equation Range: 4-300
    # Curve Fit % error relative to data: N/A
    # [W/(m-K)]
    a=2.7380
    b=-30.677
    c=89.430
    d=-136.99
    e=124.69
    f=-69.556
    g=23.320
    h=-4.3135
    i=0.33829

    y1 = a+b*(log10(T)) + c*(log10(T))**2 + d*(log10(T))**3 + e*(log10(T))**4
    y2 = f*(log10(T))**5 + g*(log10(T))**6 + h*(log10(T))**7 + i*(log10(T))**8
    ans = 10**(y1+y2)
    return ans

def Ti_6AL_4V(T):
    #Ti 6Al 4V UNS R56400
    # Data Range: 23-300
    # Equation Range: 20-300
    # Curve Fit % error relative to data: 2
    # [W/(m-K)]
    a=-5107.8774
    b=19240.422
    c=-30789.064
    d=27134.756
    e=-14226.379
    f=4438.2154
    g=-763.07767
    h=55.796592
    i=0

    y1 = a+b*(log10(T)) + c*(log10(T))**2 + d*(log10(T))**3 + e*(log10(T))**4
    y2 = f*(log10(T))**5 + g*(log10(T))**6 + h*(log10(T))**7 + i*(log10(T))**8
    ans = 10**(y1+y2)
    return ans

def Titanium_15_3_3_3(T):
    #Titanium 15-3-3-3 Composition: Bal Ti, 14.88% V, 3.13 Cr, 2.88 Sn, 3.00 Al
    # Data Range: 1.4-300
    # Equation Range: 1.4-300
    # Curve Fit % error relative to data: 3
    # [W/(m-K)]
    a=-2.398794842
    b=8.970743802
    c=-29.19286973
    d=54.87139779
    e=-59.67137228
    f=38.89321714
    g=-14.94175848
    h=3.111616089
    i=-0.270452768

    y1 = a+b*(log10(T)) + c*(log10(T))**2 + d*(log10(T))**3 + e*(log10(T))**4
    y2 = f*(log10(T))**5 + g*(log10(T))**6 + h*(log10(T))**7 + i*(log10(T))**8
    ans = 10**(y1+y2)
    return ans

def Kevlar_Fiber(T):
    #Kevlar 49 Fiber
    # Data Range: 0.1-291
    # Equation Range: 0-350
    # Curve Fit % error relative to data: 3.1
    # [W/(m-K)]
    a=-2.4219
    b=1.986637
    c=1.257441
    d=0.961209
    e=-9.6106
    f=0.777857

    y1 = (a + (b*(log10(T))))*((1-erf(2*(log10(T)-c)))/2)
    y2 = (d+(e*(exp(-log10(T)/f)))*((1+erf(2*(log10(T)-c)))/2)
    ans=10**(y1+y2)
    return ans

def Kevlar_Composite(T):
    #Kevlar 49 Composite
    # Data Range: 6-302
    # Equation Range: 0-350
    # Curve Fit % error relative to data: 7.4
    # [W/(m-K)]
    a=-2.65
    b=1.986637
    c=1.24851
    d=0.57
    e=-8
    f=0.777857

    y1 = (a + (b*(log10(T))))*((1-erf(2*(log10(T)-c)))/2)
    y2 = (d+(e*(exp(-log10(T)/f)))*((1+erf(2*(log10(T)-c)))/2)
    ans=10**(y1+y2)
    return ans

def Polyurethane_31d(T):
    #Polyurethane density: 31.88 kg/m3 (=1.99 lb/ft3 Freon filled)
    # Data Range: 76-300
    # Equation Range: 60-300
    # Curve Fit % error relative to data: 2
    # [W/(m-K)]
    a=-3218.679
    b=9201.61
    c=-10956.66	
    d=6950.102
    e=-2476.94	
    f=470.284
    g=-37.1669
    h=0
    i=0

    y1 = a+b*(log10(T)) + c*(log10(T))**2 + d*(log10(T))**3 + e*(log10(T))**4
    y2 = f*(log10(T))**5 + g*(log10(T))**6 + h*(log10(T))**7 + i*(log10(T))**8
    ans = 10**(y1+y2)
    return ans

def Polyurethane_32d(T):
    #Polyurethane density: 32.04 kg/m3 (=2.0 lb/ft3 CO2 Filled)
    # Data Range: 100-300
    # Equation Range: 85-300
    # Curve Fit % error relative to data: 1
    # [W/(m-K)]
    a=3788.43
    b=-7642.66
    c=4592.448
    d=778.8423
    e=-2214.434	
    f=1090.293
    g=-235.6349
    h=19.66088	
    i=0

    y1 = a+b*(log10(T)) + c*(log10(T))**2 + d*(log10(T))**3 + e*(log10(T))**4
    y2 = f*(log10(T))**5 + g*(log10(T))**6 + h*(log10(T))**7 + i*(log10(T))**8
    ans = 10**(y1+y2)
    return ans

def Polyurethane_49d(T):
    #Polyurethane density: 49.02 kg/m3 (=3.06 lb/ft3 He Filled)
    # Data Range: 30-300
    # Equation Range: 20-300
    # Curve Fit % error relative to data: 1
    # [W/(m-K)]
    a=-33.898
    b=117.81
    c=-178.376
    d=142.038
    e=-63.034
    f=14.958
    g=-1.5468
    h=0.020625
    i=0

    y1 = a+b*(log10(T)) + c*(log10(T))**2 + d*(log10(T))**3 + e*(log10(T))**4
    y2 = f*(log10(T))**5 + g*(log10(T))**6 + h*(log10(T))**7 + i*(log10(T))**8
    ans = 10**(y1+y2)
    return ans

def Polyurethane_64d(T):
    #Polyurethane density: 64.08 kg/m3 (=4.00 lb/ft3 Freon filled)
    # Data Range: 88-300
    # Equation Range: 55-300
    # Curve Fit % error relative to data: 2
    # [W/(m-K)]
    a=789.79
    b=-2347.94
    c=3024.61
    d=-2206.76
    e=989.238
    f=-273.18
    g=43.065
    h=-2.9863
    i=0

    y1 = a+b*(log10(T)) + c*(log10(T))**2 + d*(log10(T))**3 + e*(log10(T))**4
    y2 = f*(log10(T))**5 + g*(log10(T))**6 + h*(log10(T))**7 + i*(log10(T))**8
    ans = 10**(y1+y2)
    return ans

def Polystyrene_31d(T):
    #Polystyrene density: 31.88 kg/m3 (=1.99 lb/ft3 Freon filled)
    # Data Range: 90-300
    # Equation Range: 90-300
    # Curve Fit % error relative to data: 2
    # [W/(m-K)]
    a=-1557.5
    b=3984.7
    c=-3940.245	
    d=1649.668
    e=12.80097	
    f=-294.2616
    g=119.5898
    h=-20.6301
    i=1.36067

    y1 = a+b*(log10(T)) + c*(log10(T))**2 + d*(log10(T))**3 + e*(log10(T))**4
    y2 = f*(log10(T))**5 + g*(log10(T))**6 + h*(log10(T))**7 + i*(log10(T))**8
    ans = 10**(y1+y2)
    return ans

def Polystyrene_32d(T):
    #Polystyrene density: 32.04 kg/m3 (=2.0 lb/ft3)
    # Data Range: 33-300
    # Equation Range: 25-300
    # Curve Fit % error relative to data: 2
    # [W/(m-K)]
    a=-1145.45
    b=4086.02
    c=-6234.293
    d=5260.106
    e=-2649.914
    f=797.0372
    g=-132.5244
    h=9.3968
    i=0

    y1 = a+b*(log10(T)) + c*(log10(T))**2 + d*(log10(T))**3 + e*(log10(T))**4
    y2 = f*(log10(T))**5 + g*(log10(T))**6 + h*(log10(T))**7 + i*(log10(T))**8
    ans = 10**(y1+y2)
    return ans

def Polystyrene_49d(T):
    #Polystyrene density: 49.98 kg/m3 (=3.12 lb/ft3)
    # Data Range: 7-300
    # Equation Range: 4-300
    # Curve Fit % error relative to data: 2
    # [W/(m-K)]
    a=-1.5194
    b=-4.6449
    c=11.643
    d=-15.969
    e=12.722
    f=-5.821
    g=1.4174
    h=-0.14128
    i=0

    y1 = a+b*(log10(T)) + c*(log10(T))**2 + d*(log10(T))**3 + e*(log10(T))**4
    y2 = f*(log10(T))**5 + g*(log10(T))**6 + h*(log10(T))**7 + i*(log10(T))**8
    ans = 10**(y1+y2)
    return ans

def Polystyrene_99d(T):
    #Polystyrene density: 99.96 kg/m3 (=6.24 lb/ft3)
    # Data Range: 4-300
    # Equation Range: 4-300
    # Curve Fit % error relative to data: 3
    # [W/(m-K)]
    a=7.39582
    b=-59.6737
    c=160.58
    d=-240.33
    e=218.817
    f=-124.155
    g=42.9088
    h=-8.26683
    i=0.68082

    y1 = a+b*(log10(T)) + c*(log10(T))**2 + d*(log10(T))**3 + e*(log10(T))**4
    y2 = f*(log10(T))**5 + g*(log10(T))**6 + h*(log10(T))**7 + i*(log10(T))**8
    ans = 10**(y1+y2)
    return ans

def PVC_20d(T):
    #Polyvinyl Chloride (PVC) density: 20.02 kg/m3 (=1.25 lb/ft3 air fill gas)
    # Data Range: 100-300
    # Equation Range: 90-300
    # Curve Fit % error relative to data: 1.5
    # [W/(m-K)]
    a=11314.56
    b=-30824.32
    c=34964.24
    d=-21141.43	
    e=7187.43
    f=-1302.708
    g=98.35252
    h=0
    i=0

    y1 = a+b*(log10(T)) + c*(log10(T))**2 + d*(log10(T))**3 + e*(log10(T))**4
    y2 = f*(log10(T))**5 + g*(log10(T))**6 + h*(log10(T))**7 + i*(log10(T))**8
    ans = 10**(y1+y2)
    return ans

def PVC_56d(T):
    #Polyvinyl Chloride (PVC) density: 56.06 kg/m3 (=3.5 lb/ft3 CO2 blown)
    # Data Range: 125-300
    # Equation Range: 100-300
    # Curve Fit % error relative to data: 2
    # [W/(m-K)]
    a=-4123.51
    b=9690.59
    c=-7920.09
    d=1572.897
    e=1459.993
    f=-1028.329
    g=255.773
    h=-23.31925
    i=0

    y1 = a+b*(log10(T)) + c*(log10(T))**2 + d*(log10(T))**3 + e*(log10(T))**4
    y2 = f*(log10(T))**5 + g*(log10(T))**6 + h*(log10(T))**7 + i*(log10(T))**8
    ans = 10**(y1+y2)
    return ans



#-------------------------------------------bleh
#script for testing and plotting each function
#why is this here? not just for data collection? ...... Sev
'''

def Polyurethane_64d(T):
    #Polyurethane density: 64.08 kg/m3 (=4.00 lb/ft3 Freon filled)
    # Data Range: 88-300
    # Equation Range: 55-300
    # Curve Fit % error relative to data: 2
    # [W/(m-K)]
    a=
    b=
    c=
    d=
    e=
    f=
    g=
    h=
    i=

    y1 = a+b*(log10(T)) + c*(log10(T))**2 + d*(log10(T))**3 + e*(log10(T))**4
    y2 = f*(log10(T))**5 + g*(log10(T))**6 + h*(log10(T))**7 + i*(log10(T))**8
    ans = 10**(y1+y2)
    return ans


StartT = 6
EndT = 300
Step = floor(fabs(StartT-EndT)+1)
print(Step)
T = np.linspace(StartT,EndT,int(Step))
K=np.zeros((Step,1))
K1=np.zeros((Step,1))
K2=np.zeros((Step,1))
K3=np.zeros((Step,1))
K4=np.zeros((Step,1))
K5=np.zeros((Step,1))
#print(T)
for i in range(len(K)):
    K1[i] = AL_ALY_5083(T[i])
    K2[i] = AL_ALY_1100(T[i])
    K3[i] = AL_ALY_3003(T[i])
    K4[i] = AL_ALY_6061(T[i])
    K5[i] = AL_ALY_6063(T[i])
fig = plt.figure()
fig.add_axes()
ax1 = fig.add_subplot(111)
ax1.plot(T,K1,T,K2,T,K3,T,K4,T,K5)
ax1.set(title="Aluminum Thermal Conductivity",
        ylabel='Conductivity [W/m-K]',
        xlabel='Temperature [Kelvin]')
ax1.legend(loc='best')
"""
ax1 = fig.add_subplot(221)
ax2 = fig.add_subplot(222)
ax3 = fig.add_subplot(223)
ax4 = fig.add_subplot(224)

ax1.plot(T,K1)
ax2.plot(T,K2,color='blue')
ax3.plot(T,K3,color='green')
ax4.plot(T,K4,color='brown')
"""
plt.show()
'''

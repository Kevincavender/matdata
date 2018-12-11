from math import log10, fabs, floor, erf, exp

def AL_ALY_3003(T):
    #3003F Aluminum (UNS A93003)
    # Data Range: 4-300
    # Equation Range: 4-300
    # Curve Fit % error relative to data: 5
    # J/(kg-K)
    a=46.6467
    b=-314.292
    c=866.662
    d=-1298.3
    e=1162.27
    f=-637.795
    g=210.351
    h=-38.3094
    i=2.96344

    y1 = a+b*(log10(T)) + c*(log10(T))**2 + d*(log10(T))**3 + e*(log10(T))**4
    y2 = f*(log10(T))**5 + g*(log10(T))**6 + h*(log10(T))**7 + i*(log10(T))**8
    ans = 10**(y1+y2)
    return ans

def AL_ALY_5083(T):
    # Annealed (-O) UNS A95083
    # Data Range: 4-300
    # Equation Range: 4-300
    # Curve Fit % error relative to data: 5
    # J/(kg-K)
    a=46.6467
    b=-314.292
    c=866.662
    d=-1298.3
    e=1162.27
    f=-637.795
    g=210.351
    h=-38.3094
    i=2.96344

    y1 = a+b*(log10(T)) + c*(log10(T))**2 + d*(log10(T))**3 + e*(log10(T))**4
    y2 = f*(log10(T))**5 + g*(log10(T))**6 + h*(log10(T))**7 + i*(log10(T))**8
    ans = 10**(y1+y2)
    return ans

def AL_ALY_6061(T):
    # Heat treated (-T6) UNS A96061
    # Data Range: 4-300
    # Equation Range: 4-300
    # Curve Fit % error relative to data: 5
    # J/(kg-K)
    a=46.6467
    b=-314.292
    c=866.662
    d=-1298.3
    e=1162.27
    f=-637.795
    g=210.351
    h=-38.3094
    i=2.96344

    y1 = a+b*(log10(T)) + c*(log10(T))**2 + d*(log10(T))**3 + e*(log10(T))**4
    y2 = f*(log10(T))**5 + g*(log10(T))**6 + h*(log10(T))**7 + i*(log10(T))**8
    ans = 10**(y1+y2)
    return ans

def Apiexon_N(T):
    #Apiexon N
    # Data Range: 1-200
    # Equation Range: 2-200
    # Curve Fit % error relative to data: 2
    # J/(kg-K)
    a=-1.61975
    b=3.10923
    c=-0.712719
    d=4.93675
    e=-9.37993
    f=7.58304
    g=-3.11048
    h=0.628309
    i=-0.0482634

    y1 = a+b*(log10(T)) + c*(log10(T))**2 + d*(log10(T))**3 + e*(log10(T))**4
    y2 = f*(log10(T))**5 + g*(log10(T))**6 + h*(log10(T))**7 + i*(log10(T))**8
    ans = 10**(y1+y2)
    return ans

def Beryllium(T):
    #Beryllium
    # Data Range: 10-284
    # Equation Range: 14-284
    # Curve Fit % error relative to data: N/A
    # J/(kg-K)
    a=-526.84477
    b=2755.4105
    c=-6209.8985
    d=7859.2257
    e=-6106.2095
    f=2982.9958
    g=-894.99967
    h=150.85256
    i=-10.943615

    y1 = a+b*(log10(T)) + c*(log10(T))**2 + d*(log10(T))**3 + e*(log10(T))**4
    y2 = f*(log10(T))**5 + g*(log10(T))**6 + h*(log10(T))**7 + i*(log10(T))**8
    ans = 10**(y1+y2)
    return ans

def Copper_OFHC(T):
    #OFHC Copper (UNS C10100/C10200)
    # Data Range: 4-300
    # Equation Range: 4-300
    # Curve Fit % error relative to data: N/A
    # J/(kg-K)
    a=-1.91844
    b=-0.15973
    c=8.61013
    d=-18.996
    e=21.9661
    f=-12.7328
    g=3.54322
    h=-0.3797
    i=0

    y1 = a+b*(log10(T)) + c*(log10(T))**2 + d*(log10(T))**3 + e*(log10(T))**4
    y2 = f*(log10(T))**5 + g*(log10(T))**6 + h*(log10(T))**7 + i*(log10(T))**8
    ans = 10**(y1+y2)
    return ans

def Fiberglass_Epoxy(T):
    # G-10 CR (Fiberglass Epoxy)
    # Data Range: 4-300
    # Equation Range: 4-300
    # Curve Fit % error relative to data: 2
    # J/(kg-K)
    a=-2.4083
    b=7.6006
    c=-8.2982
    d=7.3301
    e=-4.2386
    f=1.4294
    g=-0.24396
    h=0.015236
    i=0

    y1 = a+b*(log10(T)) + c*(log10(T))**2 + d*(log10(T))**3 + e*(log10(T))**4
    y2 = f*(log10(T))**5 + g*(log10(T))**6 + h*(log10(T))**7 + i*(log10(T))**8
    ans = 10**(y1+y2)
    return ans

def Indium(T):
    #Indium
    # Data Range: 1-300
    # Equation Range: 4-295
    # Curve Fit % error relative to data: 3
    # J/(kg-K)
    a=-2.4259351
    b=12.613611
    c=-46.472893
    d=104.64717
    e=-127.18630
    f=88.805612
    g=-35.915625
    h=7.8307989
    i=-0.71218931

    y1 = a+b*(log10(T)) + c*(log10(T))**2 + d*(log10(T))**3 + e*(log10(T))**4
    y2 = f*(log10(T))**5 + g*(log10(T))**6 + h*(log10(T))**7 + i*(log10(T))**8
    ans = 10**(y1+y2)
    return ans

def Invar(T):
    #Fe-36Ni UNS K93600
    # Data Range: 4-20
    # Equation Range: 4-27
    # Curve Fit % error relative to data: 2
    # J/(kg-K)
    a=28.08
    b=-228.23
    c=777.587
    d=-1448.423
    e=1596.567
    f=-1040.294
    g=371.2125
    h=-56.004
    i=0

    y1 = a+b*(log10(T)) + c*(log10(T))**2 + d*(log10(T))**3 + e*(log10(T))**4
    y2 = f*(log10(T))**5 + g*(log10(T))**6 + h*(log10(T))**7 + i*(log10(T))**8
    ans = 10**(y1+y2)
    return ans

def Fe_225_Ni(T):
    #Nickel Steel (Fe-2.25 Ni)
    # Data Range: 60-300
    # Equation Range: 55-300
    # Curve Fit % error relative to data: 1.5
    # J/(kg-K)
    a=15503.108
    b=-37280.377
    c=26788.417
    d=7010.0877
    e=-22731.651
    f=15386.526
    g=-5175.7968
    h=896.97274
    i=-64.055866

    y1 = a+b*(log10(T)) + c*(log10(T))**2 + d*(log10(T))**3 + e*(log10(T))**4
    y2 = f*(log10(T))**5 + g*(log10(T))**6 + h*(log10(T))**7 + i*(log10(T))**8
    ans = 10**(y1+y2)
    return ans

def Fe_325_Ni(T):
    #Nickel Steel (Fe-3.25 Ni) UNS S20103
    # Data Range: 60-300
    # Equation Range: 55-300
    # Curve Fit % error relative to data: 1.5
    # J/(kg-K)
    a=15503.108
    b=-37280.377
    c=26788.417
    d=7010.0877
    e=-22731.651
    f=15386.526
    g=-5175.7968
    h=896.97274
    i=-64.055866

    y1 = a+b*(log10(T)) + c*(log10(T))**2 + d*(log10(T))**3 + e*(log10(T))**4
    y2 = f*(log10(T))**5 + g*(log10(T))**6 + h*(log10(T))**7 + i*(log10(T))**8
    ans = 10**(y1+y2)
    return ans

def Fe_50_Ni(T):
    #Nickel Steel (Fe-5.0 Ni) UNS S20153
    # Data Range: 60-300
    # Equation Range: 55-300
    # Curve Fit % error relative to data: 1.5
    # J/(kg-K)
    a=15503.108
    b=-37280.377
    c=26788.417
    d=7010.0877
    e=-22731.651
    f=15386.526
    g=-5175.7968
    h=896.97274
    i=-64.055866

    y1 = a+b*(log10(T)) + c*(log10(T))**2 + d*(log10(T))**3 + e*(log10(T))**4
    y2 = f*(log10(T))**5 + g*(log10(T))**6 + h*(log10(T))**7 + i*(log10(T))**8
    ans = 10**(y1+y2)
    return ans

def Fe_90_Ni(T):
    # Nickel Steel (Fe-9.0 Ni) UNS S21800
    # Data Range: 60-300
    # Equation Range: 55-300
    # Curve Fit % error relative to data: 1.5
    # J/(kg-K)
    a=15503.108
    b=-37280.377
    c=26788.417
    d=7010.0877
    e=-22731.651
    f=15386.526
    g=-5175.7968
    h=896.97274
    i=-64.055866

    y1 = a+b*(log10(T)) + c*(log10(T))**2 + d*(log10(T))**3 + e*(log10(T))**4
    y2 = f*(log10(T))**5 + g*(log10(T))**6 + h*(log10(T))**7 + i*(log10(T))**8
    ans = 10**(y1+y2)
    return ans

def Platinum(T):
    #Platinum
    # Data Range: 1-296
    # Equation Range: 1-295
    # Curve Fit % error relative to data: 3
    # J/(kg-K)
    a=-1.6135538
    b=0.95823584
    c=1.4317770
    d=-3.5963989
    e=5.1299735
    f=-2.4186452
    g=-0.12560841
    h=0.34342394
    i=-0.06198179

    y1 = a+b*(log10(T)) + c*(log10(T))**2 + d*(log10(T))**3 + e*(log10(T))**4
    y2 = f*(log10(T))**5 + g*(log10(T))**6 + h*(log10(T))**7 + i*(log10(T))**8
    ans = 10**(y1+y2)
    return ans

def Nylon(T):
    #Polyamide (Nylon)
    # Data Range: 4-300
    # Equation Range: 4-300
    # Curve Fit % error relative to data: 4
    # J/(kg-K)
    a=-5.2929
    b=25.301
    c=-54.874
    d=71.061
    e=-52.236
    f=21.648
    g=-4.7317
    h=0.42518
    i=0

    y1 = a+b*(log10(T)) + c*(log10(T))**2 + d*(log10(T))**3 + e*(log10(T))**4
    y2 = f*(log10(T))**5 + g*(log10(T))**6 + h*(log10(T))**7 + i*(log10(T))**8
    ans = 10**(y1+y2)
    return ans

def Kapton(T):
    #Polyimide (Kapton)
    # Data Range: 4-300
    # Equation Range: 4-300
    # Curve Fit % error relative to data: 3
    # J/(kg-K)
    a=-1.3684
    b=0.65892
    c=2.8719
    d=0.42651
    e=-3.0088
    f=1.9558
    g=-0.51998
    h=0.051574
    i=0

    y1 = a+b*(log10(T)) + c*(log10(T))**2 + d*(log10(T))**3 + e*(log10(T))**4
    y2 = f*(log10(T))**5 + g*(log10(T))**6 + h*(log10(T))**7 + i*(log10(T))**8
    ans = 10**(y1+y2)
    return ans

def Polystyrene_99d(T):
    #Polystyrene density: 99.96 kg/m3 (=6.24 lb/ft3)
    # Data Range: 100-300
    # Equation Range: 90-300
    # Curve Fit % error relative to data: 1
    # J/(kg-K)
    a=-5911.474
    b=14991.16
    c=-15513.753
    d=8232.5666
    e=-2237.3586	
    f=225.423
    g=20.33505
    h=-4.6169
    i=0

    y1 = a+b*(log10(T)) + c*(log10(T))**2 + d*(log10(T))**3 + e*(log10(T))**4
    y2 = f*(log10(T))**5 + g*(log10(T))**6 + h*(log10(T))**7 + i*(log10(T))**8
    ans = 10**(y1+y2)
    return ans
    
def Polystyrene_9d(T):
    #Polystyrene density: 9.93 kg/m3 (=0.062 lb/ft3)
    # Data Range: 100-300
    # Equation Range: 90-300
    # Curve Fit % error relative to data: 1.5
    # J/(kg-K)
    a=-734.172
    b=1163.613
    c=-135.157
    d=-878.514
    e=791.787
    f=-308.6236
    g=58.6764
    h=-4.4494
    i=0

    y1 = a+b*(log10(T)) + c*(log10(T))**2 + d*(log10(T))**3 + e*(log10(T))**4
    y2 = f*(log10(T))**5 + g*(log10(T))**6 + h*(log10(T))**7 + i*(log10(T))**8
    ans = 10**(y1+y2)
    return ans

def Polystyrene_60d(T):
    #Polystyrene density: 60.07 kg/m3 (=3.75 lb/ft3)
    # Data Range: 100-300
    # Equation Range: 80-300
    # Curve Fit % error relative to data: 1
    # J/(kg-K)
    a=2139.33
    b=-6518.015
    c=9650.919
    d=-9229.889
    e=6104.0571
    f=-2739.14
    g=784.878
    h=-128.40103
    i=0

    y1 = a+b*(log10(T)) + c*(log10(T))**2 + d*(log10(T))**3 + e*(log10(T))**4
    y2 = f*(log10(T))**5 + g*(log10(T))**6 + h*(log10(T))**7 + i*(log10(T))**8
    ans = 10**(y1+y2)
    return ans

def Polyurethane_49d(T):
    #Polyurethane density: 49.02 kg/m3 (=3.06 lb/ft3 He Filled)
    # Data Range: 23-300
    # Equation Range: 16-300
    # Curve Fit % error relative to data: 1
    # J/(kg-K)
    a=89.69
    b=-269.32
    c=333.276
    d=-214.635
    e=76.2052
    f=-14.1137
    g=1.061
    h=0
    i=0

    y1 = a+b*(log10(T)) + c*(log10(T))**2 + d*(log10(T))**3 + e*(log10(T))**4
    y2 = f*(log10(T))**5 + g*(log10(T))**6 + h*(log10(T))**7 + i*(log10(T))**8
    ans = 10**(y1+y2)
    return ans

def Polyurethane_389d(T):
    #Polyurethane density: 389.25 kg/m3 (=24.3 lb/ft3 air Filled)
    # Data Range: 100-300
    # Equation Range: 80-300
    # Curve Fit % error relative to data: 2
    # J/(kg-K)
    a=4894.36
    b=-11608.63
    c=10463.31
    d=-3895.8
    e=-40.0053
    f=497.4517
    g=-147.7555
    h=14.19365
    i=0

    y1 = a+b*(log10(T)) + c*(log10(T))**2 + d*(log10(T))**3 + e*(log10(T))**4
    y2 = f*(log10(T))**5 + g*(log10(T))**6 + h*(log10(T))**7 + i*(log10(T))**8
    ans = 10**(y1+y2)
    return ans

def PVC_48d(T):
    #Polyvinyl Chloride (PVC) density: 48.05 kg/m3 (=3.00 lb/ft3)
    # Data Range: 10-300
    # Equation Range: 10-300
    # Curve Fit % error relative to data: 2
    # J/(kg-K)
    a=190.776
    b=-991.521
    c=2200.811
    d=-2726.414
    e=2069.971
    f=-988.4221
    g=290.405
    h=-48.0737
    i=3.437928

    y1 = a+b*(log10(T)) + c*(log10(T))**2 + d*(log10(T))**3 + e*(log10(T))**4
    y2 = f*(log10(T))**5 + g*(log10(T))**6 + h*(log10(T))**7 + i*(log10(T))**8
    ans = 10**(y1+y2)
    return ans

def SS_304(T):
    #304 Stainless UNS S30400
    # Data Range: 4-300
    # Equation Range: 4-300
    # Curve Fit % error relative to data: 5
    # J/(kg-K)
    a=22.0061
    b=-127.5528
    c=303.647
    d=-381.0098
    e=274.0328
    f=-112.9212
    g=24.7593
    h=-2.239153
    i=0

    y1 = a+b*(log10(T)) + c*(log10(T))**2 + d*(log10(T))**3 + e*(log10(T))**4
    y2 = f*(log10(T))**5 + g*(log10(T))**6 + h*(log10(T))**7 + i*(log10(T))**8
    ans = 10**(y1+y2)
    return ans

def SS_304L(T):
    #304L Stainless UNS S30403
    # Data Range: 4-20
    # Equation Range: 4-23
    # Curve Fit % error relative to data: 1
    # J/(kg-K)
    a=-351.51
    b=3123.695
    c=-12017.28
    d=26143.99
    e=-35176.33
    f=29981.75
    g=-15812.78
    h=4719.64
    i=-610.515

    y1 = a+b*(log10(T)) + c*(log10(T))**2 + d*(log10(T))**3 + e*(log10(T))**4
    y2 = f*(log10(T))**5 + g*(log10(T))**6 + h*(log10(T))**7 + i*(log10(T))**8
    ans = 10**(y1+y2)
    return ans

def SS_310(T):
    #310 Stainless UNS S31000
    # Data Range: 4-300
    # Equation Range: 4-300
    # Curve Fit % error relative to data: 2.5
    # J/(kg-K)
    if T < 47:
        a=20.694
        b=-171.007
        c=600.6256
        d=-1162.748
        e=1361.931
        f=-986.2934
        g=430.093
        h=-102.85
        i=10.275
    else:
        a=-2755.63
        b=9704.831
        c=-14618.36
        d=12202.74
        e=-6092.339
        f=1818.555
        g=-300.458
        h=21.1942
        i=0

    y1 = a+b*(log10(T)) + c*(log10(T))**2 + d*(log10(T))**3 + e*(log10(T))**4
    y2 = f*(log10(T))**5 + g*(log10(T))**6 + h*(log10(T))**7 + i*(log10(T))**8
    ans = 10**(y1+y2)
    return ans

def SS_316(T):
    #316 Stainless UNS S31600
    # Data Range: 4-300
    # Equation Range: 4-300
    # Curve Fit % error relative to data: 2
    # J/(kg-K)
    if T <50:
        a=12.2486
        b=-80.6422
        c=218.743
        d=-308.854
        e=239.5296
        f=-89.9982
        g=3.15315
        h=8.44996
        i=-1.91368
    else:
        a=-1879.464
        b=3643.198
        c=76.70125
        d=-6176.028
        e=7437.6247
        f=-4305.7217
        g=1382.4627
        h=-237.22704
        i=17.05262

    y1 = a+b*(log10(T)) + c*(log10(T))**2 + d*(log10(T))**3 + e*(log10(T))**4
    y2 = f*(log10(T))**5 + g*(log10(T))**6 + h*(log10(T))**7 + i*(log10(T))**8
    ans = 10**(y1+y2)
    return ans

def Teflon(T):
    #Teflon
    # Data Range: 4-300
    # Equation Range: 4-300
    # Curve Fit % error relative to data: 1.5
    # J/(kg-K)
    a=31.88256
    b=-166.51949
    c=352.01879
    d=-393.44232
    e=259.98072
    f=-104.61429
    g=24.99276
    h=-3.20792
    i=0.16503

    y1 = a+b*(log10(T)) + c*(log10(T))**2 + d*(log10(T))**3 + e*(log10(T))**4
    y2 = f*(log10(T))**5 + g*(log10(T))**6 + h*(log10(T))**7 + i*(log10(T))**8
    ans = 10**(y1+y2)
    return ans
"""
def AL_ALY_3003(T):
    #3003F Aluminum (UNS A93003)
    # Data Range: 4-300
    # Equation Range: 4-300
    # Curve Fit % error relative to data: 5
    # J/(kg-K)
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

"""

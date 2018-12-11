from math import log10, fabs, floor, erf, exp




def PVC(T):
    #Polyvinyl Chloride (=1.25 lb/ft3 air fill gas)
    #Data Range: 100-300
    #Equation Range: 90-300
    #Curve Fit % Error Relative to Data: 1.5
    #units [W/(m-K)]
    a=
    b=
    c=
    d=
    e=
    f=
    g=
    h=
    i=



    y1 = a + b*(log10(T)) + c*((log10(T))**2) + d*((log10(T))**3) + e*((log10(T))**4) 
    y2 = f*((log10(T))**5) + g*((log10(T))**6) + h*((log10(T))**7) + i*((log10(T))**8)
    ans =10**(y1 + y2)

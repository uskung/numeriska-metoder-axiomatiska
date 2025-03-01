## uppgift 1.2

## given f(x) = x^2 + 4x - 1 - 3^x, find all roots in the interval [-5,5]
## assume that there are an unknown amount of roots in the interval [-5,5]

import math

def f(x):
    y = x**2 + 4*x - 1 - 3**x
    return y

a = -5
b = 5

## these lists work in pairs to store the intervalls for which there are solutions to f(x) = 0
lower = []
upper = []

precision = int(input("Hur många intervall vill du dela upp intervallet [-5,5]? "))

delta_x = 10 / precision 

for k in range(0, precision - 1):
    ##goes from x = -5 to x = 5 checking if there is a solution in the checked intervall 
    a_lower = a + delta_x*k 
    b_upper = a_lower + delta_x

    if f(a_lower) * f(b_upper) < 0:
        lower.append(a_lower)
        upper.append(b_upper)
        print(f"En rot ligger mellan x = {a_lower:.3f} och x = {b_upper:.3f}")

roots = []
rep_list = []

for k in range(len(lower)): ## ie how many solutions were found
    error = 0.000001
    a_lcl = lower[k]
    b_lcl = upper[k]
    c = 1 ## midpoint
    d = 0 ## next midpoint with better accuracy, it is = 0 so the while loop doesn't end on the first iteration
    rep = 0
    while abs(c-d) > error:
        c = (a_lcl + b_lcl)/2 ## calculates midpoint
        if f(c) * f(b_lcl) < 0:
            a_lcl = c
            d = (a_lcl + b_lcl)/2
        elif f(c) * f(a_lcl) < 0:
            b_lcl = c
            d = (a_lcl + b_lcl)/2
        rep += 1
    roots.append(c)
    rep_list.append(rep)

for k in range(len(roots)):
    print(f"Root nr. {k+1} är: x = {roots[k]:.5f}")















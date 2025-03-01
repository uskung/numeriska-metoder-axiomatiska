# uppgift 1.1 

# given the function f(x) = x^3-2x-1-sqrt(x), find the roots numerically

from math import *

def f(x):
    y = x**3 - 2*x - 1 - sqrt(x)
    return y

## guarantees root is between chosen values
while True:
    a = float(input("Ange första gissningen! "))
    b = float(input("Ange andra gissningen! "))

    try:
        if f(a) * f(b) < 0:
            print("Startvärderna är godtagbara!")
            break
        else:
            print("Välj om startvärden! ")
    except: ## given that f(x) is not defined for x < 0
        ValueError
        print("Du kan inte ange ett negativt tal! Försök igen!")

d = 1
c = 0
rep = 0

while abs(d-c) > 0.000001: ## (1)
    c = (a+b)/2 ## midpoint between a and b
    if f(c) * f(b) < 0: ## checks if root is between b and c
        a = c
        d = (a+b)/2
    elif f(c) * f(a) < 0: ## checks if root is between a and c
        b = c
        d = (a+b)/2
    rep += 1

print(f"Roten är {round(c,5)}")
print(f"Det gick åt {rep} antal repetitioner för fem decimalers noggrannhet!")

'''
Vad är fördelarna med intervallhalveringsmetoden?
    Intervallhalveringsmetoden är en väldigt enkel algoritm för att hitta rötter till funktioner. Detta gör att den är bra lämpad till att hitta grova approximeringar av rötter till funktioner.
Vad är nackdelarna med intervallhalveringsmetoden?
    Jämfört med andra algoritmer är intervallhalveringsmetoden relativt långsam, då är det bättre att t.ex använda "Newtons metod". 
Hur påverkar val av initialt intervall och toleransnivå resultatet?
    Om ett större intervall väljs initialt kommer den rimligtvis kräva fler repetitioner. T.ex startvärden på 0 och 2 kräver 20 repetitioner, men startvärden på 0 och 100 kräver 26 repetitioner. Detsamma gäller vid högre decimal noggrannhet, t.ex en noggrannhet på 6 decimaler kräver 24 repetitioner, med vid 5 decimalers noggrannhet krävs det baa 20 repetitioner (givet startvärden på 0 och 2).
'''
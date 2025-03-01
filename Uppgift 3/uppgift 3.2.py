## uppgift 3.2

while True: ## ensures that the degree is an positive integer 
    try:
        degree = int(input("Bestäm graden av ditt polynom du vill integrera! "))
        break
    except ValueError:
        print("Talet måste vara ett positivt heltal!\n ")


constants = [] ## contains the degree for each constant
for i in range(1,degree+1):
    constants.append(i)
constants.reverse() ## => the first position is the highest degree, the last position is the lowest degree (i.e 0)
constants.append(0) ## there is always a constant c_0 

print("Polynomet har utseendet p(x) = ", end="")
for i in range(len(constants)): ## prints out the polynomial 
    if constants[i] == 0: ## when constants[i] == 0, it is the last line, thus there needs to be a line break 
        print("c_0")
    else:
        if constants[i] == 1: ## to ensure that it doesn't print x^1,
            print(f"c_{constants[i]}x + ",end="")
        else:
            print(f"c_{constants[i]}x^{constants[i]} + ",end="")

constants_value = [] ## contains the values for each constant
for i in range(len(constants)):
    val = float(input(f"Ange värdet för c_{constants[i]}: "))
    constants_value.append(val)


def p(x):
    res = 0
    for i in range(len(constants)):
        res += constants_value[i] * (x**constants[i]) ## adds every term for each
    return res
def riemann_midpoint(x1:float, x2:float, rectangles:int) -> float:
    delta_x = (x2 - x1) / rectangles
    area = 0
    for i in range(rectangles):
        b = delta_x ## base of rectangle 
        h = p((x1 + (i + 0.5) * delta_x)) ## height of rectangle
        area += b*h
    return area

x1 = float(input("Ange första integrationsgränsen: "))
x2 = float(input("Ange andra integrationsgränsen: "))
rectangles = int(input("Ange antalet rektanglar: "))

res = riemann_midpoint(x1,x2,rectangles)

print(f"Integralen av p(x) mellan {x1} och {x2} är: {round(res,5)}")
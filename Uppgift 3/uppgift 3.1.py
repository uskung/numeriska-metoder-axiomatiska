# given a function f(x) = ax**2 + bx + c
# find the integral of f(x)dx from x1 and x2 numerically

def f(x):
    y = a*(x**2) + b*x + c
    return y

def riemann_midpoint(x1:float, x2:float, rectangles:int) -> float:
    delta_x = (x2 - x1) / rectangles
    area = 0
    for i in range(rectangles):
        b = delta_x ## base of rectangle 
        h = f((x1 + (i + 0.5) * delta_x)) ## height of rectangle
        area += b*h
    return area

x1 = float(input("Första integrationsgränsen: "))
x2 = float(input("Andra integrationsgränsen: "))
a = float(input("Ange a: "))
b = float(input("Ange b: "))
c = float(input("Ange c: "))
rectangles = int(input("Antal rektanglar: "))

area = riemann_midpoint(x1,x2,rectangles)

print(f"Riemann summan mellan {x1} och {x2} är {area:.5f}")


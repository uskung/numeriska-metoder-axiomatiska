##uppgift 3.3
# use eval() to compute function
import math 
import readline

def translate(txt: str, var:str) -> str: ## translates expression so that eval() can compute expression
    txt = txt.replace(" ", "") ## ensures there are no spaces
    txt = txt.replace("^","**") # replaces ^ to **
    expression = list(txt) #converts str to list, easier to work with

    def insert_multiplication(expression): ## inserts "*" between characters
        constant = {"0","1","2","3","4","5","6","7","8","9"}
        counter = 1
        while counter < len(expression):
            element = expression[counter]
            element_before = expression[counter-1]

            if element == "(" and (element_before in constant or element_before == var): #e.g. turns 4(1+1) to 4*(1+1)
                expression.insert(counter,"*")
                continue
            if element == "(" and element_before == ")": # e.g turns (x^2+1)(2+x) to (x^2+1)*(2+x)
                expression.insert(counter,"*")
                continue
            if element == var and (element_before in constant or element_before == ")"): #e.g. turns 3x to 3*x
                expression.insert(counter,"*")
                continue
            if element in constant and (element_before == var or element_before == ")"): #e.g. turns x4 to x*4
                expression.insert(counter,"*")
                continue
            counter += 1 # counter goes only up if every check has been passed
        result = "".join(expression) # joins back list into string
        return result
    
    return insert_multiplication(expression)

txt = input("Skriv in det polynom du vill integrera: ")

## finds variable and separates expression from function name, assuming p(x) is left to equal sign
equal_sign_pos = txt.find("=")
if equal_sign_pos != -1: ## there is a equal sign
    function_name = txt[:equal_sign_pos].strip()
    var = function_name[function_name.find("(") + 1]
    expression = txt[equal_sign_pos+1:].strip()
else: ## no equal sign given, i.e no specified variable
    var = "x" # sets var to "x"
    expression = txt.strip()

## translate into code that eval() can compute
expression_translated = translate(expression,var)
print(f"Den översatta koden blev: {expression_translated}") # not compulsory for task, although quite interesting to see if translation was completed successfully

# approximates the integral
def f(x:float) -> float:
    return eval(expression_translated, {var: x})
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
rectangles = int(input("Antal rektanglar: "))
area = riemann_midpoint(x1,x2,rectangles)
print(f"Integralen av funktionen {txt} mellan {x1} och {x2} är: {area:.8f}")

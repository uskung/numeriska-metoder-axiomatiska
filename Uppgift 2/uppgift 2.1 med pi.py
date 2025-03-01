## version assuming you know the value of pie
## faster and more precise than other version where you do not know pi
import random
import math
import time 

start_time = time.time() 

total = 0
approx = 0 ## set to zero so loop doesn't break on first iteration
circle = 0 ## number of coordinates inside the circle 

while abs(math.pi - approx) > 0.000001:
    total += 1
    x = random.uniform(-1,1)
    y = random.uniform(-1,1)
    if x**2 + y**2 <= 1: ## checks if inside circle
        circle += 1
    approx = 4*(circle)/total

end_time = time.time() 
execution_time = end_time - start_time 

print(f"Approximationen av pi är ≈ {approx:.5f}")
print(f"Det gick år {total} repetitioner! ")
print(f"Exekveringstid: {execution_time:.8f} sekunder") 

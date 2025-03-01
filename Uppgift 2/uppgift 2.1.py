## version assuming you do not know the value of pi
## much slower and less precise than version when you know the value of pi
import random
import time 

start_time = time.time() 

total = 0
approx = 0 
approx_previous = 0 
circle = 0 ## number of coordinates inside the circle 

precision = 0 # counter 
while True:
    total += 1
    x = random.uniform(-1,1)
    y = random.uniform(-1,1)
    if x**2 + y**2 <= 1: ## checks if inside circle
        circle += 1
    approx_previous = approx
    approx = 4*(circle)/total
    if abs(approx-approx_previous) < 0.0000001: ## checks if approx and previous approx don't divert too much
        precision += 1
    else:
        precision = 0
    if precision >= 100:## if for 100 times approx had not diverted too much, break loop
        break

end_time = time.time() 
execution_time = end_time - start_time 

print(f"Approximationen av pi är ≈ {approx:.5f}")
print(f"Det gick år {total} repetitioner! ")
print(f"Exekveringstid: {execution_time:.2f} sekunder") 
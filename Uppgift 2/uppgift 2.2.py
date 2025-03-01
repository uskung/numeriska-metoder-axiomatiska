## version assuming you do not know the value of the integral between 0 and 1. 
# Thus, it is very slow and quite imprecise. 
# theoretical value is 1/3 

import random

hits = 0
total = 0
approx = 0
approx_previous = 1

precision = 0
while True:
    total += 1
    x = random.uniform(0,1)
    y = random.uniform(0,1)
    if y <= x**2:
        hits += 1
    approx_previous = approx
    approx = hits/total
    if abs(approx-approx_previous) < 0.0000001: ## checks if approx and previous approx don't divert too much
        precision += 1
    else:
        precision = 0
    if precision >= 100:## if for 100 times approx had not diverted too much, break loop
        break

print(f"Approximationen är ≈ {approx:.5f}")
print(f"Det gick år {total} repetitioner! ")

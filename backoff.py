import random
import math
#n = 10**8
e= 2.718281828459045
def SingleWindowNRt(n):
    window_size = n
    window = [0]*window_size
    for i in range(n):
        rand_index = random.randint(0, window_size-1)
        window[rand_index] += 1

    collisions = sum([1 for i in window if i >= 2])
    empty_slots = sum([1 for i in window if i == 0])
    successes = sum([1 for i in window if i == 1])

#print(f"Window: {window}")
    print("------------------------------------------------------")
    print(f"Window size n={window_size}: Collisions={collisions}, Empty slots={empty_slots}, Successes={successes}")
    print("Total Cost:",collisions*math.log(n)+window_size)
    print("------------------------------------------------------")
def singleWindowN(n):
    window_size = int(n*math.sqrt(math.log(n)/e))
    window = [0]*window_size
    for i in range(n):
        rand_index = random.randint(0, window_size-1)
        window[rand_index] += 1

    collisions = sum([1 for i in window if i >= 2])
    empty_slots = sum([1 for i in window if i == 0])
    successes = sum([1 for i in window if i == 1])

#print(f"Window: {window}")
    print("------------------------------------------------------")
    print(f"Window size n=n*sqrt(ln(n)/e)={window_size}: Collisions={collisions}, Empty slots={empty_slots}, Successes={successes}")
    print("Total Cost:",collisions*math.log(n)+window_size)
    print("------------------------------------------------------")
print("10^4")
SingleWindowNRt(10**4)
singleWindowN(10**4)

print("10^5")
SingleWindowNRt(10**5)
singleWindowN(10**5)

print("10^6")
SingleWindowNRt(10**6)
singleWindowN(10**6)

print("10^7")
SingleWindowNRt(10**7)
singleWindowN(10**7)

print("10^8")
SingleWindowNRt(10**8)
singleWindowN(10**8)
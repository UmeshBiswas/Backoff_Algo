import math
from decimal import Decimal, getcontext

def nWindow(window_size_str, num_windows):
    total_collisions = 0
    total_successes = 0
    total_empty_slots = 0
    n = Decimal(window_size_str)
    w = Decimal(window_size_str)
    p = Decimal(window_size_str)
    print("Window Size-n: ", n)
    getcontext().prec = 1000
    packet_size = Decimal(math.log(float(window_size_str)))**2
    print("packet Size:", packet_size)

    for i in range(num_windows):
        window = (0 for _ in range(window_size_str))
        collisions = 0
        successes = 0
        empty_slots = 0

        successes = n*(1/w)*((1-1/w)**(n-1))*p

        empty_slots = ((1-1/w)**n)*p
        collisions = p - successes - empty_slots

        print("------------------------------------------------------")
        print("Packet sending: ", n)
        print(f"Window {i+1}: Collisions={collisions}, Empty slots={empty_slots}, Successes={successes}")
        total_collisions += collisions
        total_successes += successes
        total_empty_slots += empty_slots
        print("------------------------------------------------------")

        n = n - successes
        if n < 1:
            break
    print("------------------------------------------------------")
    print(f"Total: Collisions={total_collisions}, Empty slots={total_empty_slots}, Successes={total_successes}")
    total_slots = total_collisions + total_empty_slots + total_successes
    print(f"Total Slots:", total_slots)
    print("Cost of collisions:", total_collisions * packet_size)
    print("Total Cost:", total_collisions * packet_size + total_slots)
    print("------------------------------------------------------")

def nSQRTWindow(window_size_str, num_windows):
    total_collisions = 0
    total_successes = 0
    total_empty_slots = 0
    n = Decimal(window_size_str)
    w = Decimal(window_size_str * (math.sqrt(math.log(window_size_str))))
    p = Decimal(w)
    print("Window Size-n: ", w)
    getcontext().prec = 1000
    packet_size = Decimal(math.log(float(window_size_str)))**2
    print("packet Size:", packet_size)

    for i in range(num_windows):
        window = (0 for _ in range(window_size_str))
        collisions = 0
        successes = 0
        empty_slots = 0

        successes = (n*(1/w)*((1-1/w)**(n-1)))*p

        empty_slots = ((1-1/w)**n)*p
        collisions = p - successes - empty_slots

        print("------------------------------------------------------")
        print("Packet sending: ", n)
        print(f"Window {i+1}: Collisions={collisions}, Empty slots={empty_slots}, Successes={successes}")
        total_collisions += collisions
        total_successes += successes
        total_empty_slots += empty_slots
        print("------------------------------------------------------")

        n = n - successes
        if n < 1:
            break
    print("------------------------------------------------------")
    print(f"Total: Collisions={total_collisions}, Empty slots={total_empty_slots}, Successes={total_successes}")
    total_slots = total_collisions + total_empty_slots + total_successes
    print(f"Total Slots:", total_slots)
    print("Cost of collisions:", total_collisions * packet_size)
    print("Total Cost:", total_collisions * packet_size + total_slots)
    print("------------------------------------------------------")

print("==================== n= 10^15 and w= n*sqrt((ln n))====================")
nWindow(10**300,20)
nSQRTWindow(10**300,20)



import random
import math
e= 2.718281828459045

def nWindow(window_size, num_windows):
    total_collisions = 0
    total_successes = 0
    total_empty_slots = 0
    n = window_size
    w = window_size
    p=window_size
    print("Window Size-n: ",window_size)
    packet_size = math.log(window_size)**2
    print("packet Size:", packet_size)

    for i in range(num_windows):
        window = [0] * window_size
        collisions = 0
        successes = 0
        empty_slots = 0

        successes=(n*(1/w)*(1-1/w)**(n-1))*p

        empty_slots=(1-1/w)**(n)*p
        collisions=(p-successes-empty_slots)

        print("------------------------------------------------------")
        print("Packet sending: ",n)
        print(f"Window {i+1}: Collisions={collisions}, Empty slots={empty_slots}, Successes={successes}")
        total_collisions += collisions
        total_successes += successes
        total_empty_slots += empty_slots
        print("------------------------------------------------------")

        n = n - successes
        if n<1:
            break
    print("------------------------------------------------------")
    print(f"Total: Collisions={total_collisions}, Empty slots={total_empty_slots}, Successes={total_successes}")
    total_Slots = total_collisions + total_empty_slots + total_successes
    print(f"Total Slots:", total_Slots)
    print("Cost of collisions:", total_collisions * packet_size)
    print("Total Cost:", total_collisions * packet_size + total_Slots)
    print("------------------------------------------------------")

def nSqrtWindow(window_size, num_windows):
    total_collisions = 0
    total_successes = 0
    total_empty_slots = 0
    n = window_size
    print(n)
    print(window_size)
    w = int(window_size *(math.log(window_size)))
    print(w)
    p=w
    print("Window Size-n: ",w)
    packet_size = math.log(window_size)**2
    print("packet Size:", packet_size)

    for i in range(num_windows):
        window = [0] * window_size
        collisions = 0
        successes = 0
        empty_slots = 0

        successes=((n*(1/w)*(1-1/w)**(n-1))*p)

        empty_slots=((1-1/w)**(n)*p)
        collisions=((p-successes-empty_slots))

        print("------------------------------------------------------")
        print("Packet sending: ",n)
        print(f"Window {i+1}: Collisions={collisions}, Empty slots={empty_slots}, Successes={successes}")
        total_collisions += collisions
        total_successes += successes
        total_empty_slots += empty_slots
        print("------------------------------------------------------")

        n = n - successes
        if n<1:
            break
    print("------------------------------------------------------")
    print(f"Total: Collisions={total_collisions}, Empty slots={total_empty_slots}, Successes={total_successes}")
    total_Slots = total_collisions + total_empty_slots + total_successes
    print(f"Total Slots:", total_Slots)
    print("Cost of collisions:", total_collisions * packet_size)
    print("Total Cost:", total_collisions * packet_size + total_Slots)
    print("------------------------------------------------------")

print("==================== n= 10^9  and w= n*sqrt((ln n))====================")
nWindow(10**12,20)
nSqrtWindow(10**12,20)





import random
import math
e= 2.718281828459045

def nWindow(window_size, num_windows):
    total_collisions = 0
    total_successes = 0
    total_empty_slots = 0
    n = window_size
    print("Window Size-n: ",window_size)
    packet_size = math.log(window_size)
    print("packet Size:",packet_size)

    for i in range(num_windows):
        window = [0] * window_size
        collisions = 0
        successes = 0
        empty_slots = 0

        for j in range(n):
            rand_index = random.randint(0, window_size-1)
            window[rand_index] += 1
            #print(window)

        collisions = sum([1 for j in window if j >= 2])
        successes = sum([1 for j in window if j == 1])
        empty_slots = sum([1 for j in window if j == 0])



        print("------------------------------------------------------")
        print(f"Window {i+1}: Collisions={collisions}, Empty slots={empty_slots}, Successes={successes}")
        total_collisions += collisions
        total_successes += successes
        total_empty_slots += empty_slots
        print("------------------------------------------------------")

        n = n - successes
        if n==0:
            for k in range(len(window)):
                if window[k] == 1:
                    lastvalue=k+1
            lastlatency=window_size-lastvalue
            break
    print("------------------------------------------------------")
    print(f"Total: Collisions={total_collisions}, Empty slots={total_empty_slots}, Successes={total_successes}")
    total_Slots = total_collisions + total_empty_slots + total_successes - lastlatency
    print(f"Total Slots:", total_Slots)
    print("Cost of collisions:", total_collisions * packet_size)
    print("Total Cost:", total_collisions * packet_size+total_Slots)
    print("------------------------------------------------------")

def nSQRTWindow(window_size, num_windows):
    total_collisions = 0
    total_successes = 0
    total_empty_slots = 0
    n=window_size
    packet_size = math.log(window_size)
    print("packet Size:", packet_size)
    window_size=int(window_size * (math.sqrt(math.log(window_size)/e)))
    print("Window Size-n*(sqrt(logn)):", window_size)


    for i in range(num_windows):
        window = [0] * window_size
        collisions = 0
        successes = 0
        empty_slots = 0

        for j in range(n):
            rand_index = random.randint(0, window_size-1)
            window[rand_index] += 1

        collisions = sum([1 for j in window if j >= 2])
        empty_slots = sum([1 for j in window if j == 0])
        successes = sum([1 for j in window if j == 1])

        print("------------------------------------------------------")
        print(f"Window {i+1}: Collisions={collisions}, Empty slots={empty_slots}, Successes={successes}")
        total_collisions += collisions
        total_successes += successes
        total_empty_slots += empty_slots
        print("------------------------------------------------------")

        n = n - successes
        if n == 0:
            for k in range(len(window)):
                if window[k] == 1:
                    lastvalue = k + 1
            lastlatency = window_size - lastvalue
            break
    print("------------------------------------------------------")
    print(f"Total: Collisions={total_collisions}, Empty slots={total_empty_slots}, Successes={total_successes}")
    total_Slots = total_collisions + total_empty_slots + total_successes - lastlatency
    print(f"Total Slots:", total_Slots)
    print("Cost of collisions:", total_collisions * packet_size)
    print("Total Cost:", total_collisions * packet_size + total_Slots)
    print("------------------------------------------------------")
def nlognWindow(window_size, num_windows):
    total_collisions = 0
    total_successes = 0
    total_empty_slots = 0
    n = window_size
    packet_size = math.log(window_size)
    print("packet Size:", packet_size)
    window_size= int(window_size*(math.log(window_size)))
    print("Window Size-nlogn: ", window_size)


    for i in range(num_windows):
        window = [0] * window_size
        collisions = 0
        successes = 0
        empty_slots = 0

        for j in range(n):
            rand_index = random.randint(0, window_size-1)
            window[rand_index] += 1

        collisions = sum([1 for j in window if j >= 2])
        empty_slots = sum([1 for j in window if j == 0])
        successes = sum([1 for j in window if j == 1])

        print("------------------------------------------------------")
        print(f"Window {i+1}: Collisions={collisions}, Empty slots={empty_slots}, Successes={successes}")
        total_collisions += collisions
        total_successes += successes
        total_empty_slots += empty_slots
        print("------------------------------------------------------")

        n = n - successes
        if n == 0:
            for k in range(len(window)):
                if window[k] == 1:
                    lastvalue = k + 1
            lastlatency = window_size - lastvalue
            break
    print("------------------------------------------------------")
    print(f"Total: Collisions={total_collisions}, Empty slots={total_empty_slots}, Successes={total_successes}")
    total_Slots = total_collisions + total_empty_slots + total_successes - lastlatency
    print(f"Total Slots:", total_Slots)
    print("Cost of collisions:", total_collisions * packet_size)
    print("Total Cost:", total_collisions * packet_size + total_Slots)
    print("------------------------------------------------------")

#nlognWindow(10**7,20)

print("10^8")
nWindow(10**8,20)
nSQRTWindow(10**8,20)
import math
import random as rand

r_start = 0
r_stop = 5
r_total_number = 5

def RandomGen(name):
    for _ in range(r_start, r_total_number):
        name.append(rand.randint(r_start,r_stop))

def sum_prod(seq_a, seq_b):
    print(f"sum_prod: {math.prod(seq_a) * math.prod(seq_b)}")
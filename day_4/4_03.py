import multiprocessing as mp
# https://docs.python.org/3.7/library/multiprocessing.html

def funct_to_paral(param):
    return param*2
    
print(f' Num cpus: {mp.cpu_count()}')

numbers = [1, 2, 3, 4]
pool = mp.Pool(2)
results = pool.map(funct_to_paral, numbers)
print(results)


def para_sum(a, b):
    print(f'Called with a: {a} b:{b} result {a +b}')
    return a + b


list_to_sum = [
    [1, 2],
    [3, 4],
    [5, 6],
]

pool = mp.Pool(2)
results = pool.starmap(para_sum, list_to_sum)
print(results)



# https://docs.python.org/3.7/library/itertools.html#itertools.starmap
# Todas las combinaciones de dos listas
param_a = [1 , 10, 30]
param_b = [100, 200, 250]

import itertools

all_combinations = itertools.product(param_a, param_b)
print(list(all_combinations))

def train_funct(p_a, p_b):
    print(f'with p_a: {p_a} and p_b: {p_b}')
    return p_b**p_a

all_combinations = itertools.product(param_a, param_b)
pool = mp.Pool(2)
results = pool.starmap(para_sum, all_combinations)
print(results)
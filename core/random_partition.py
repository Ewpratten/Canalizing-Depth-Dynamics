"""Program for generating ordered partitions of a set"""
import random
import scipy.special as sp

def fubini(elements):
    """Returns the nth Fubini number (ordered Bell number)"""
    if elements == 0:
        return 1
    
    result = 0
    for i in range(1, elements + 1):
        result += sp.binom(elements, i) * fubini(elements - i)
    return result



def random_subset(variables, subsize):
    """Generates a random subset of a given size from some number of variables"""
    subset = []
    for _ in range(subsize):
        rand = random.randint(0, len(variables) - 1)
        subset.append(variables[rand])
        del variables[rand]
    subset.sort()
    return subset

def random_partition(variables):
    """Generates a uniformly random ordered partition of given elements"""
    k = len(variables)
    if k == 0:
        return []
    possibilities = fubini(k)
    chooser = random.randint(1, possibilities)
    counter = 0
    count = 0
    while counter < chooser:
        count += 1
        counter += fubini(k - count) * sp.binom(k, count)
    subset = random_subset(variables, count)
    left = random_partition(variables)
    left.append(subset)
    return left

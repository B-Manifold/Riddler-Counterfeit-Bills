import operator as op
from functools import reduce
import math
import random

def ncr(n, r):
    '''calculates nCr for n and r

    int, int -> float'''
    
    r = min(r, n-r)
    numer = reduce(op.mul, range(n, n-r, -1), 1)
    denom = reduce(op.mul, range(1, r+1), 1)
    return numer/denom

def ptri(row):
    '''returns the nuumbers from the row-th row of pascals triangle as a list

    int -> list of floats'''
    
    result = []
    i = row
    while i >= 0:
        result.append(ncr(row, i))
        i = i - 1
    return result

def denom_calc(fakes):
    '''returns the denominator for probability weights

    int -> float'''
    
    total_bills = 25 + fakes
    sampled_bills = int(math.ceil(total_bills * 0.05))
    i = int(sampled_bills) - 1
    denom = 1
    while i >= 0:
        denom = denom * (total_bills - i)
        i = i - 1
    return denom

def prob_calc(fakes, denom):
    '''returns the probability weights for a given number of fakes with denom for all possible outcomes

    int, float -> list of floats'''
    total_bills = 25 + fakes
    sampled_bills = int(math.ceil(total_bills * 0.05))
    num_outcomes = sampled_bills + 1
    i = sampled_bills
    f = 0
    probs = []
    while num_outcomes > 0:
        if i == sampled_bills:
            numer = (math.factorial(25))/(math.factorial(25 - i))
            result = numer/denom
            probs.append(result)
            i = i - 1
            num_outcomes = num_outcomes - 1
        else:
            numer = (math.factorial(25))/(math.factorial(25 - i))
            j = f
            while j >= 0:
                numer = numer * (fakes - j)
                j = j - 1
            result = numer/denom
            probs.append(result)
            i = i - 1
            num_outcomes = num_outcomes - 1
            f = f + 1
    return probs

def expected_depo(fakes):
    '''calculates expected deposit value given fakes (number of fake $100 bills) mixed with 25 real $100 bills

    int -> float with 2 decimal places'''
    total_bills = 25 + fakes
    sampled_bills = int(math.ceil(total_bills * 0.05))
    denom = denom_calc(fakes)
    probs = prob_calc(fakes, denom)
    ptri_weights = ptri(sampled_bills)
    i = 0
    money = 0
    while i < len(probs):
        expect = (0.75**(i)) * probs[i] * ptri_weights[i] * (2500 + (fakes * 100))
        money = money + expect
        i = i + 1
    money = round(money, 2)
    return money

fakes = 0
print("showing 0 to 475 counterfeits and the respective expected value")
print(['counterfeits', 'expected value'])
while fakes < 476:
    output = []
    output.append(fakes)
    output.append(expected_depo(fakes))
    print(output)
    fakes = fakes + 1
print("I \u2665 FiveThirtyEight")

# -*- coding: utf-8 -*-
"""
Created on Tue Mar 15 22:51:46 2022

@author: Aidan
"""
import time
import numpy as np

N = 200000

def is_prime(n):
    if n % 2 == 0:
        return n == 2
    else:
        upperlim = max(int(np.ceil(np.sqrt(n))) + 1, 5)
        output = True
        for j in range(3, upperlim, 2):
            if (n % j == 0):
                output = False
                break
        return output
        
t0 = time.time()
plst = []
for j in range(2, N):
    if (is_prime(j)):
        plst.append(j)

print("Found %d primes below %d in %.3f s" %(len(plst), N, time.time() - t0))

def divide(a, b, wtf = False):
    t1 = time.time()
    p = 0
    q = 0
    while ( a < b ):
        a *= 10
        p += 1
    
    repeatlength = 0
    goesintolist = dict([])
    sequence = []
    
    while (a not in goesintolist):
        div = a // b
        goesintolist[a] = True
        sequence.append(div)
        
        q += (div * np.power(10.0, -1 * p))
        a -= div * b
        a *= 10
        p += 1
        repeatlength += 1
    
    if wtf:
        f = open("ReciproalSequenceof" + str(b) + ".txt", 'w')
        for j in sequence:
            f.write(str(j))
        f.close()
        
    return (b, q, repeatlength, time.time() - t1)


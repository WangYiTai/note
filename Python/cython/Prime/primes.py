import numpy as np
import time

before = time.time()

def primes(kmax):

   result=[]
   p=[0 for i in range(1000)]

   if kmax > 1000:
       kmax = 1000
   k = 0
   n = 2
   while k < kmax:
       i = 0
       while i < k and n % p[i] != 0:
           i = i + 1
       if i == k:
           p[k] = n
           k = k + 1
           result.append(n)
       n = n + 1
   return result

test=primes(1000)
after = time.time()
print test
print "time: This is python\n",after - before

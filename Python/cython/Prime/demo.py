import time
import prime

before = time.time()
test= prime.primes(1000)
after = time.time()
print test
print "time: This is cython\n",after - before
 
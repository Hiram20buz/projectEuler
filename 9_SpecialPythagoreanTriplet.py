#A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

#a**2 + b**2 = c**2
#For example, 3**2 + 4**2 = 9 + 16 = 25 = 5**2.

#There exists exactly one Pythagorean triplet for which a + b + c = 1000.
#Find the product abc.

import math
def pythagorean_triplet(n):
    num=[]
    for b in range(n):
        for a in range(1, b):
            c = math.sqrt( a * a + b * b)
            suma = a+b+c
            if (c % 1 == 0 and suma==1000):
                print(a, b, int(c))
                print(a*b*c)
                
                
pythagorean_triplet(1000)


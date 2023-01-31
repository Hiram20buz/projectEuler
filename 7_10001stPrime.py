#By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

#What is the 10 001st prime number?

from math import sqrt
# n is the number to be check whether it is prime or not
x = 1
def isPrime(n):
    # this flag maintains status whether the n is prime or not
    prime_flag = 0
     
    if(n > 1):
        for i in range(2, int(sqrt(n)) + 1):
            if (n % i == 0):
                prime_flag = 1
                break
        if (prime_flag == 0):
            return True
        else:
            return False
    else:
        return False
        
if(isPrime(x)):
    print(" is prime")
    
con=2
prim=[]
prim.append(2)
while True:
    con+=1
    if(isPrime(con)):
        prim.append(con)
    if(len(prim)==10001):
        break
    

print(prim[len(prim)-1])
    

#The prime factors of 13195 are 5, 7, 13 and 29.

#What is the largest prime factor of the number 600851475143 ?
import math 
  
def x(n):
    factors = []
    for i in range(3,int(math.sqrt(n))):
        if(n%i==0):
            factors.append(i)
            
    return factors
    
composite=1
for number in x(600851475143):
    #print(number)
    if(composite < 600851475143):
        print(number)
        composite=composite*number

print(composite)

#Now to prove that 6857 is prime
if not x(6857):
    print("It is prime")
else:
    print("Not prime")



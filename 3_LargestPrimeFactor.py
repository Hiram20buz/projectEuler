#The prime factors of 13195 are 5, 7, 13 and 29.

#What is the largest prime factor of the number 600851475143 ?


# the last digit of a number gives you the posible factor
#For example  12345 converting 12345 as "12345" and the to [1,2,3,4,5] 
# then nth of final digit tells u info ,if not the nth-1.

# you search for possibles combinationes example;

# Considering its a composite number k=12345 has two factors those that can be composite as well.
# 12345 =(x . k)(y . h) so k and h are the last digit of the factors, x  concatenation with h and so on.

# To calculate them you do ...
# 1,3,7 this to find pure prime numbers.

# 2 and 5 are the easiest
# 1,3,7,9
# 4547 => [(1*7),(3*9)] => (x.1)*(y.7) or (x.3)*(y.9) 
# case 1: (x.1)*(y.7) => [(x.1-1)/10+1] * [(y.7-7)/10+7] ; X,Y
# (X+1) * (Y+7) = XY +7X +Y+7
# 4547 =XY+7X+Y+7
# 4540=XY+7X+Y
##
#but 
# what is the length of x and y 
sqrt(4547)=67.4314466699
# try 1
# 61*67 and 63*69   4087 | 4347
# 

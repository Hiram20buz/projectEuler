#2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

#What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

def x(t):
    if (t%9699690==0):
        return True
    
    
    
#9699690 is 2*3*5*7*11*13*17*19
def y():
    num=[]
    for i in range (96996900,300000000,2):
        if(x(i)):
            num.append(i)
            
    return num
            
def action(t):
    count=0
    #div=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
    for number in range(1,21):
        if((t%number)==0):
            #print(number)
            count+=1
    
    for i in range(1,t):
        if(count==20):
            return i
        else :
            return 0
            
            
for i in y():
    if(action(i)):
        print(i)
            
            
            
            

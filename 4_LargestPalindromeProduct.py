#A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

#Find the largest palindrome made from the product of two 3-digit numbers

            
d1=111
d2=999

def isPalidrome(word):
    temp=[]
    arr = list(word)
    #print(arr)
    for i in range(len(arr)):
        temp.append(arr[len(arr)-i-1])
        
    #print(temp)
    #print(arr==temp)
    return arr==temp
        
    
        
        
    
#print(isPalidrome("1234"))
#print(isPalidrome("9009"))

def get(a,b,minus):
    palin=[]
    c=1
    b=b-minus
    for i in range(1,888):
        a+=1
        #b-=1
        c=a*b
        palin.append(c)
    return palin
    

def savepal(caso):
    g=get(d1,d2,caso)
    #get(d1,d2)
    #print(isPalidrome(get(d1,d2)))
    # 888 or 444
    pala=[]
    for arreglo in g:
        #print(arreglo)
        if(isPalidrome(str(arreglo))):
            pala.append(arreglo)
        
    return pala
        
#for are in savepal(888):
#    print(are)
    
#print( max(savepal(888)))
def getmax():
    tempo=[]
    for i in range(1,888):
        if savepal(i):
            tempo.append(max(savepal(i)))
            
        
        
    return tempo
 
for are in getmax():
     print(are)
        
        
        
        


import math


def sin(x,n=50):
    thisSin = 0
    
    #make n taylor terms and sum them
    for i in range(n):
        
        #calculate numerator
        num = pow(x,2*i+1)

        #calculate denominator
        den = math.factorial((2*i)+1)

        #add fraction to sum
        thisSin += pow(-1,i)*float(num / den)
        
    #return value
    
    return thisSin

def cos(x=0,n=50):
    thisCos = 0
    
    #make n taylor terms and sum them
    for i in range(n):
        
        #calculate numerator
        num = pow(x,2*i)
        
        #calculate denominator
        den = math.factorial(2*i)
        
        #add fraction to the sum
        thisCos += pow(-1,i) * num / den
     
    #return value
    return thisCos

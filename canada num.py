#canada number
#n=125 then 1^2+2^2+5^2=30; and divisors of 125 are 1,5,25,125,then except 1 and n the remaining factors that is non-trivalent divisiors(5,25) sum should be equal to sqrt sum
#1^2+2^2+5^2==5+25:
#30==30
from math import sqrt

def sqrtsum_of_digits(n):  #125
    sum=0   
    while n:   #125 ,12  ,1
        r=n%10  #125%10==5  ,2  ,1%10=1
        
        n=n//10   #12  ,1  ,1//10=0
        
        sum=sum+r**2  #0+5**2=25 ,25+2**2=29 , 29+1**2=30
    return sum   #30

def non_tri_div(n):
    result=0
    for i in range(1,int(sqrt(n))+1):  #1,(11)+1
        if n%i==0:   #125%1==0  ,125%2==0-->f ,125%3-->f ,4-->f ,125%5==0
            if i==n//i:   #1==125//1--->f  ,                    5==125//5-->f
                result+=i
            else:
                result+=i+n//i  #1+125=126, 126+5+25=156,
                
    return result-1-n  #156-1-125=30

def is_canada(n):
    if sqrtsum_of_digits(n)==non_tri_div(n):  #30=30
        return True   #hence returns true
    return False

n=int (input("enter a num: ")) #125,581,16999
print(is_canada(n)) #true
    

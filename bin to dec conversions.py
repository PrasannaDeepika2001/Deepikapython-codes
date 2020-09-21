#Binary to decimal conversion
#for that i/p: bin=111 ; o/p: dec=7

#   1     1     1
#  2*2 + 2*1 + 2*0 = 4+2+1 = 7

n=int(input("Enter bin no:"))  
base=1
dec=0
while n:   #11;1;n=0-->breaks
     r=n%10   #11%10=1 ; 1%10=1
     n=n//10  #11//10=1; 1//10=0
     dec+=r*base  #1*1=1; 1*2=2 ----1+2=3
     base=base*2  #1*2=2; 2*2=4
print(dec) #3 prints


#DECIMAL TO BINARY
 #divide the decimal num "n" with binary radix = 2

n=int(input ("Enter the dec:"))
z=[ ]
while n: #6 ;3 ;1 ;0--->break
    z.append(n%2) #6%2=0; 3%2=1; 1%2=1
    n=n//2  #3;1;0
#print(z) #[0,1,1]
#print(*z[::-1])---->Reversing teh string
z=z[::-1] #[1,1,0]
print(*z) #110

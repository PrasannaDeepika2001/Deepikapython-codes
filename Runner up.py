    #n=int(input("enter the value of n:"))
    #l=list(int,input().split())
    #z=list(set(arr))
    #print(l)
    #z.sort()
    #print(z)
    #print(z[-2])

#To find the prime numbers between given range

n1=1
n2=5
pc=0

for i in range(n1,n2+1):#2,6
    fc=0
    for j in range (1,i+1):#1,3
        if(i%j==0):#2%1==0
            fc+=1
            #print(fc)
        
      
    if fc==2:
        pc+=1
print(pc)

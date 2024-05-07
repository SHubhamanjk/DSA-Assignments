# Given an array with integer type values , write a python script to sort them

from array import *
arr=array('b',[7,15,96,34,78,34,46])
print(sorted(arr))


# Given a list of heterogeneous elements , write a python script to remove all non int values from the list

l=[4,5,36,'shubh','s',5.6,78]
new_l=[]
for i in l:
    if type(i) is int:
        new_l.append(i)
    else:
        pass
              
print(new_l)

# Write a python programe to calculate average of element of a list

l=[7,15,96,34,78,34,46]
sum=0
for i in l:
    sum+=i
 
avg=sum/len(l)

print(f"Averga of element of list is {avg}")

# Write a python programe to create list of first n prime numbers 

def prime_list(n):
    l=[]
    count=0
    def is_prime(n):
        if n<2:
            return 0
        elif n==2:
            return 1
        elif n%2==0:
            return 0
        else:
            for i in range(3,n):
                if n%i==0:
                    return 0
                    break
            else:
                return 1
                # break
                
        
    for i in range(2000):
        if count<n:
            if is_prime(i)==1:
                l.append(i)
                count+=1
            else:
                pass
        else:
            break    
            
    return l                   
            
temp=prime_list(10)   
print(temp)
print(len(temp))
    
    
# Write a python programe to create list of first n febonacci series


def febser_list(n):
    l=[]
    count=0
    def feb_ser(n):
        if n==0:
            return n
        elif n==1:
            return n
        else:
            return feb_ser(n-1)+feb_ser(n-2)
    
    for i in range(2000):
        if count<n:
            l.append(feb_ser(i))    
            count+=1
        else:
            break
        
    return l
        
temp=febser_list(15)
print(temp)
print(len(temp))      
            

# Write a programe to print first N natural numbers 

def Print_Natural(n):
    if n>=1:
        Print_Natural(n-1)
        print(n,end=" ")
     
Print_Natural(5)




# Write a programe to print first N natural numbers in reverse order

def Print_Natural_Rev(n):
    if n>=1:
        print(n,end=" ")
        Print_Natural_Rev(n-1)
              
Print_Natural_Rev(5)        
    
    

# WAP to print first n natural odd numbers

def Print_Odd(n,current=1):
    if n>0:
        if current%2!=0:
            print(current,end=" ")      
            Print_Odd(n-1,current+2)
        else:
            Print_Odd(n,current+1)
                
Print_Odd(5)        


# WAP to print N Natural Even Numbers

def Print_Even(n,current=2):
    if n>=1:
        if current%2==0:
            print(current,end=" ")
            Print_Even(n-1,current+2)
        else:
            Print_Even(n,current+1)
                
Print_Even(5)   



# WAP to print first n natural Even numbers in reverse order

def Print_Even_rev(n,current=2):
    if n>0:
        if current%2==0:
            Print_Even_rev(n-1,current+2)
            print(current,end=" ")
        else:
            Print_Even_rev(n,current+1)
Print_Even_rev(5)            
                
   
                
# WAP to print first n natural odd numbers

def Print_Odd(n,current=1):
    if n>0:
        if current%2!=0:     
            Print_Odd(n-1,current+2)
            print(current,end=" ") 
        else:
            Print_Odd(n,current+1)
                
Print_Odd(5)                       



# WAP to print sum of first n natural numbers

def Natural_Sum(n,sum=0):
    if n>0:
        Natural_Sum(n-1,sum=sum+n)
    else:    
        print(sum)   
            
Natural_Sum(10)       



# WAP to print sum of first n natural odd numbers

def Odd_Sum(n,current=1,sum=0):
    if n>0:
        if current%2!=0:
            Odd_Sum(n-1,current=current+2,sum=sum+current)
        else:
            Odd_Sum(n,current=current+1,sum=0)
    else:
        print(sum)        
                

Odd_Sum(5)



# WAP to print sum of first n natural even numbers 

def Even_Sum(n,current=2,sum=0):
    if n>0:
        if current%2==0:
            Even_Sum(n-1,current=current+2,sum=sum+current)
        else:
            Even_Sum(n,current=current-1,sum=0)
    else:
        print(sum)   
        
Even_Sum(5)           



# WAP to print factorial of a given number 

def fact(n):
    if n==0:
        return 1
    else:
        return n*fact(n-1)
    
print(fact(5))         



# WAP to print sum of squares of first n natural numbers

def square_natural(n,sum=0):
    if n>0:
        square_natural(n-1,sum=sum+(n*n))
    else:
        print(sum)    
        
square_natural(5)        



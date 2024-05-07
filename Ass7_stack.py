# Define a class Stack to implement data structure , define init method to create an emplty list
# and define methods like is_empty , push , pop , peek and size

class Stack():
    def __init__(self,l=None):
        self.l=[]
    
    def is_empty(self):
        if len(self.l) == 0:
            return 1
        else:
            return 0
    def push(self,n):
        self.l.append(n)
    def pop(self):
        if len(self.l) != 0:
            return self.l.pop(-1)    
        else:
            return "Stack is Empty"
    def peek(self):
        if len(self.l) != 0:
            return self.l[-1]
        else:
            return "Stack is Empty"
    def size(self):
        return len(self.l)  
        
s1=Stack()
s1.push(4)  
s1.push(14)  
s1.push(44)
print(s1.peek())  
print(s1.pop())  
print(s1.peek())
print(s1.size())

        


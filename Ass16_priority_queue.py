# define a class to implement priority queue and add methods like push , pop ,is_empty ,size , highest priority

class PQ():
    def __init__(self):
        self.l=[]
    def is_empty(self):
        if len(self.l)==0:
            return 1
        else:
            return 0    
    def push(self, data , priority):
        self.l.append((priority,data))    
        self.l=sorted(self.l)    
    def pop(self):
        if len(self.l)!=0:
            return self.l.pop(0)[1]
        else:
            return "Empty"
    def show(self):
        if len(self.l)!=0:
            for i in range(0,len(self.l)):
                print(self.l[i][1],end=" ")
        else:
            return "Empty"  
    def size(self):
        return len(self.l)          
        
        
    
        
pq1=PQ()
print(pq1.is_empty())  
pq1.push(45,3)    
pq1.push(15,5)   
pq1.push(33,6)
pq1.push(13,1)
pq1.push(16,2)
print(pq1.is_empty()) 
print(pq1.pop())
pq1.show()
print()
print(pq1.size())

            
        
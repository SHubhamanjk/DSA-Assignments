# define a class dequeue to implement dequeue and create methods like insert_first , insert_last , delete_first ,
# delete_last , get_front , get_rear , size , isempty

class DEQUEUE():
    def __init__(self):
        self.l=[]
    def is_empty(self):
        if len(self.l) == 0:
            return 1
        else:
            return 0
    def insert_first(self,data):
        self.l.insert(0,data)
    def insert_last(self,data):
        self.l.append(data)
    def delete_first(self):
        if len(self.l) != 0:
            return self.l.pop(0)
        else:
            return "DEQUEUQ is Empty"
    def delete_last(self):
        if len(self.l) != 0:
            return self.l.pop(-1)
        else: 
            return "DEQUEUQ is Empty"
    def get_front(self):
        if len(self.l) != 0:
            return self.l[0]
        else: 
            return "DEQUEUQ is Empty"
    def get_rear(self):
        if len(self.l) != 0:
            return self.l[-1]
        else: 
            return "DEQUEUQ is Empty"
    def size(self):
        return len(self.l) 
    def view(self):
        if len(self.l) != 0:
            for i in self.l:
                print(i,end=" ") 
        else: 
            return "DEQUEUQ is Empty"          
            
           
        
q1=DEQUEUE()
print(q1.is_empty())
q1.insert_first(12)
q1.insert_first(16)
q1.insert_first(22)
q1.insert_first(56)     
q1.insert_last(122)
q1.insert_first(16)
q1.insert_last(202)
q1.insert_last(5)    
print(q1.is_empty())
print(q1.get_front())      
print(q1.get_rear())   
print(q1.delete_first()) 
print(q1.delete_last()) 
print(q1.get_front())      
print(q1.get_rear())
q1.view()
                
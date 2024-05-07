# Define a class named queue and create methods like enqueue , deenqueue , get_front , get_rear , size and empty methods

class QUEUE():
    def __init__(self):
        self.l=[]
    def is_empty(self):
        if len(self.l)==0:
            return 1
        else:
            return 0
    def enqueue(self,n):
        self.l.append(n)
    def deenqueue(self):
        if len(self.l)!=0:
            return self.l.pop(0)        
        else:
            return "QUEUE is Empty"
    def get_front(self):
        if len(self.l)!=0:
            return self.l[0]
        else:
            return "QUEUE is Empty"
    def get_rear(self):
        if len(self.l)!=0:
            return self.l[-1]  
        else:
            return "QUEUE is Empty"
    def size(self):
        return len(self.l)
        
q1=QUEUE()
print(q1.is_empty())
q1.enqueue(15)
q1.enqueue(12)
q1.enqueue(23)
q1.enqueue(48)
q1.enqueue(55)
print(q1.deenqueue())
print(q1.get_front())
print(q1.get_rear())
print(q1.size())
        
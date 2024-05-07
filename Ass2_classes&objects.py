# Define a python class Person with instance object variables name and age.Set instance object variable in init method
# and also define show method to display name and age of person

class Person():
    def __init__(self,name, age):
        self.name=name
        self.age=age
     
    def show(self):
        return f"Name is {self.name} and age is  {self.age}"
    
p1=Person("shubh",18) 
p2=Person("Anurag",21)

print(p1.show())

       
# Define a python class with instance object variable radius . provide setter and getter for radius also define 
#getarea() and getcircumference() methods.

class Radius():
    def __init__(self,radius=None):
        self.radius=radius
    def set_r(self,radius):
        self.radius = radius
    def get_r(self):
        return self.radius    
    def get_r(self):
        return self.radius
    def get_area(self):
        return f"Area is {3.14*self.radius*self.radius}"
    def get_circumference(self):
        return f"Circumference is {2*3.14*self.radius}"
    
r1=Radius(14)  
r1.set_r(7)
print(r1.get_r())    
print(r1.get_area())      
print(r1.get_circumference())



#define a class rectangle with length and breadth as instance object variables.provide set_dimension(),get_dimension()
# and get_area() method in it

class ReactAngle():
    def __init__(self,length=None,breadth=None):
        self.length=length
        self.breadth=breadth   
    def set_dimension(self,length,breadth):
        self.length=length
        self.breadth=breadth   
    def get_dimension(self):
        return f"Length is {self.length} and Breadth is {self.breadth}"
    def get_area(self):
        return f"Area is {self.length*self.breadth}"
    
r1=ReactAngle(12,5)    
print(r1.get_dimension())
print(r1.get_area())
r1.set_dimension(20,15)
print(r1.get_dimension())
print(r1.get_area())




# define a class book with instance variables book_id , book_title , book_price and initialize them with init and 
# define a method book_details .

class Book():
    def __init__(self, book_id,book_title,book_price):
        self.book_id=book_id
        self.book_title=book_title
        self.book_price=book_price
    def show_book_details(self):
        return self.book_id,self.book_title ,self.book_price    
    
b1=Book(1,"DSA",400)
b2=Book(2,"Math",850)
print(b1.show_book_details())
    
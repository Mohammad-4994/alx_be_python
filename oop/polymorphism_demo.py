import math

class Shape:

    def area(self):

        raise NotImplementedError("Subclasses must override the area() method")
    
class Rectangle(Shape): 

    def __init__(self,width,length):
        
        self.width = width
        self.length = length


    def area(self):

        return self.length * self.width 
    

class Circle(Shape):

    def __init__(self,radius):
        
        self.radius = radius


    def area(self):

        return self.radius** 2 * math.pi
"""Classes in Python"""
#Wojciech Pogorzelski G00375250
#20-02-2021

class Rectangle:
    
    #Constructor, double underscore so it wont clash with other methods, always take 'self' as a parameter
    def __init__(self,height,width):
        self.height = height
        self.width = width
    
    def area(self): #every method has to take 'self' as a parameter
        a = self.height * self.width
        return a

    def perimeter(self): #every method has to take 'self' as a parameter
        p = (2* self.height) + (2*self.width)
        return p


#creating an instance of a class
r1 = Rectangle(10,35)

r1.height = 20

#Another instance

r2 = Rectangle(2,5)

#print(r1.width)
print(f"Area of r1 = {r1.height} x {r1.width} = {r1.area()}")
print(f"Area of r2 = {r2.height} x {r2.width} = {r2.area()}")

print(f"The perimeter is ", r1.perimeter())
'''
3. Aruna, a mathematics teacher wants to teach measurements of different shapes 
in her mathematics class. She taught her class how to calculate the different 
measurements such as area, total surface area, circumference and volume. She 
explained this in the class and asked the class to do it on their own. Hence, the 
students are asked to do the calculations of area , circumference and volume of 
square, circle, cone rectangle and triangle.
Use a class as a parent class which have the values of dimensions such as side, 
length, width, height, radius. Then create a child class for each shape separately 
and each class to have different methods to calculate different measurements.
Use python script to achieve this'''
import math
class values():
    def __init__(self):
        self.square_side=int(input('Enter the side lenght of a square:'))
        self.circle_radius=int(input('Enter the radius of a circle:'))
        self.cone_radius=int(input('Enter the radius of a cone:'))
        self.cone_height=int(input('Enter the height of a cone:'))
        self.rectangle_lenght=int(input('Enter the lenght of a rectangle:'))
        self.rectangle_width=int(input('Enter the width of a rectangle:'))
        self.triangle_height=int(input('Enter the height of a triangle:'))
        self.triangle_breadth=int(input('Enter the breadth of a triangle:'))
class square(values):
    def area(square_side):
        a=(square_side)*(square_side)
        print('area of square is ',a)
    
class circle(values):
    def area(circle_radius):
        a=math.pi*circle_radius**2
        print('area of circle',a)
    def circumference(circle_radius):
        c=2*math.pi*circle_radius
        print('Circumference of circle is ',c)
class cone(values):
    def area(cone_radius,cone_height):
        a=math.pi*cone_radius(cone_radius+math.sqrt((cone_height**2)+(cone_radius**2)))
        print('Area of cone is ',a)
    def volume(cone_radius,cone_height):
        v=math.pi*(cone_radius**2)*cone_height/3
        print('Volume of a cone is ',v)
class rectangle(values):
    def area(rectangle_lenght,rectangle_width):
        a=rectangle_lenght*rectangle_width
        print('area of rectangle',a)
class triangle(values):
    def area(triangle_height,triangle_breadth):
        a=(rectangle_width*rectangle_lenght)/2
        print('area of triangle',a)
square().area()
circle().area()
circle().circumference()
cone().area()
cone().volume()
rectangle().area()
triangle().area()

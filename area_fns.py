#area of circle=πr^2
#area of square=a(side)^2
#area of rectangle=length*width
#area of triangle=(height*base)/2




def circle(r):
    c=3.14*r**2
    return c
def square(a):
    s=a**2
    return s
def rectangle(l,w):
    r=l*w
    return r
def triangle(h,b):
    t=(h*b)/2
    return t

#Area of a circle
c=int(input('Enter the radius of the circle:'))
print('Area of a circle',circle(c))


#Area of a square
s=int(input('Enter the length of a side:'))
print('Area of a square',square(s))


#Area of a rectangle
r1=int(input('Enter the length of the rectangle:'))
r2=int(input('Enter the width of the rectangle:'))
print('Area of a rectangle',rectangle(r1,r2))


#Area of a triangle
t1=int(input('Enter the height of the triangle:'))
t2=int(input('Enter the base of the triangle:'))
print('Area of a triangle',triangle(t1,t2))
    

'''
2. Write a python script to calculate the area and perimeter of different shapes 
such as SQUARE,RECTANGLE,TRIANGLE,CIRCLE with the following format.
Sample:
         AREA OF DIFFERENT SHAPES USING FUNCTIONS
TO FIND THE AREA OF SHAPE,
TYPE THE NAME OF THE SHAPE
1. SQUARE
2. RECTANGLE
3. TRIANGLE
4. CIRCLE
5. CLOSE
SELECT OPTION : 1
Size of the side : 5
Area of sqiare is : 25
 
 Do you want to continue (Y/N) y '''
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
def out():
    print('\t\tAREA OF DIFFERENT SHAPES USING FUNCTIONS')
    print('TO FIND THE AREA OF SHAPE,')
    print('TYPE THE NAME OF THE SHAPE')
    print('1. SQUARE\n2. RECTANGLE\n3. TRIANGLE\n4. CIRCLE\n5. CLOSE')
    option=str(input('SELECT OPTION:'))
    if option=="SQUARE":
        s=int(input('Size of the lenght:'))
        print('Area of a square is ',square(s))
    elif option == "RECTANGLE":
        r1=int(input('Enter the length of the rectangle:'))
        r2=int(input('Enter the width of the rectangle:'))
        print('Area of a rectangle',rectangle(r1,r2))
    elif option=="TRIANGLE":
        t1=int(input('Enter the height of the triangle:'))
        t2=int(input('Enter the base of the triangle:'))
        print('Area of a triangle',triangle(t1,t2))
    elif option=="CIRCLE":
        c=int(input('Enter the radius of the circle:'))
        print('Area of a circle',circle(c))
    else:
        print("invalid option")
out()
n=str(input('Do you want to continue (Y/N)'))
if n=="Y":
    out()

'''6. Calculation of EB bill and preparation of tariff
Tamilnadu government revised its tariff for the consumption of electricity by the citizens. 
The revised tariff is given below. It asked the IT company to come with the solution for the 
same. ODS is given a chance to develop this software for them.
If the units consumed is less than 100 the charge will be nill. If the units consumed is less 
than 501 then the charge will 8 rupess per unit. If the consumption is less than 1001 then the 
rate per unit will be 10 rupees. If the units consumed is less than 2000 the rate will be 15 
rupees per unit. If the units go beyond this and less than 5000 the charge will be 20 rupees per 
unit. If it is less than 10000 the rate will be 25 rupees per unit and if the units are going 
beyond this and less than 20000 the rate will be 50 rupees per unit and for the units above 
the rate is 75 rupees. It is a sealing.
You as the developer of the company asked to write a python code to do this process.
Sample input :
1050 units     503 units
Sample output :
8950 Rupees    3245 Rupees'''
u=int(input('Enter the consumed units:'))
if(u<100):
    print('Nill')
elif(u<=500):
    u*=8
    print('Your electricity bill is ',u,'Rupees')
elif(u<=1000):
    u*=10
    print('Your electricity bill is ',u,'Rupees')
elif(u<=2000):
    u*=15
    print('Your electricity bill is ',u,'Rupees')
elif(u<=5000):
    u*=20
    print('Your electricity bill is ',u,'Rupees')
elif(u<=10000):
    u*=25
    print('Your electricity bill is ',u,'Rupees')
elif(u<=20000):
    u*=50
    print('Your electricity bill is ',u,'Rupees')
else:
    u*=75
    print('Your electricity bill is ',u,'Rupees')


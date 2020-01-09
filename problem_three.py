"""Write a program that solves second degree equation of the form ax^2 +bx + c = 0."""
# Solve the quadratic equation ax**2 + bx + c = 0
# import complex math module
import cmath
a = int(input('Enter a number: '))
b = int(input('Enter b number: '))
c = int(input('Enter c number: '))
# calculate the discriminant
d =(b**2)-(4*a*c)
print("d : ",str(d))
if(d<0):
    print("no solution")
elif(d==0):
    sol1= -b/2*a
    print('Multip solution '.format(sol1))
elif(d>0):
    # find two solutions
    sol1 = (-b-cmath.sqrt(d))/(2*a)
    sol2 = (-b+cmath.sqrt(d))/(2*a)
    print('The solution are {0} and {1}'.format(sol1,sol2))
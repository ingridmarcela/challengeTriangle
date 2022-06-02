import math

def check_triangle(sides):
    a = sides[0]
    b = sides[1]
    c = sides[2]
    if((a+b)>c) and (b<(a+c)):
#2 lados deben ser mayores al tercero   if(a>0) and (b>0) and (c>0):
        print("It is a triangle.")
        get_type_triangle(a,b,c)
    else:
        print("It is not possible to construct a triangle with these sides")

def get_type_triangle(a,b,c):
    if(a==b==c):
        print("Triangule is equilateral.")
    elif(a==b) or (b==c) or (a==c):
        print("Triangule is isosceles.")
    else:
        print("Triangule is scalene.")

def main():
    sides = [5,2,5]
#Si se desea ingresr los valores como argumento
#    sides=[0,0,0]
#    sides[0] = int(input("Enter side of slide a \n" ))
#    sides[1] = int(input("Enter side of slide a \n" ))
#    sides[2] = int(input("Enter side of slide a \n" ))
    check_triangle(sides)
    
if __name__ == "__main__":
    main()

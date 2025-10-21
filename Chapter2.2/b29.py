def is_triangle(a:float , b:float, c:float)->bool:
    return ((a+b>c) and (a+c>b) and (b+c>a)) 

def is_equilateral(a:float,b:float,c:float) -> bool:
    return a==b==c 

def is_isosceles(a:float,b:float,c:float) -> bool:
    return a==b or b==c or a==c

def is_right(a: float, b: float, c: float) -> bool:
    sides: list[float] = sorted([a, b, c])
    x, y, z = sides 
    return abs(x**2 + y**2 - z**2) < 1e-8
def main()->None:
    try:
        a: float = float(input("Enter length of side a: "))
        b: float = float(input("Enter length of side b: "))
        c: float = float(input("Enter length of side c: "))

        if(is_triangle(a,b,c) == False):
            return
        else:
            if(is_equilateral(a,b,c)):
                print("equilateral triangle.")
            elif(is_isosceles(a,b,c)):
                if(is_right(a,b,c)):
                    print("isosceles right triangle.")
                else:
                    print("isosceles triangle.")
            else:
                if(is_right(a,b,c)):
                    print("right triangle.")
                else:
                    print("scalene triangle.") 
    except ValueError:
        print("Error: Please enter valid numbers.")

    
if __name__ == "__main__":
    main()
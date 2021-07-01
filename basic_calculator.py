#Toprk

from math import pi, sqrt, cos, acos

def addition(num1, num2): 
    print(f"{num1} + {num2} = {num1 + num2}")
def subtraction(num1, num2):
    print(f"{num1} - {num2} = {num1 - num2}")
def multiplication(num1, num2):
    print(f"{num1} x {num2} = {num1 * num2}")
def division(num1, num2):
    print(f"{num1} / {num2} = {num1 / num2}")

def pythagoras(side1, side2, hypotenuse):
    x_count = 0

    if side1 in ("x","X"):
        x_count += 1
    if side2 in ("x","X"):
        x_count += 1
    if hypotenuse in ("x","X"):
        x_count += 1

    if x_count == 2 or x_count == 3:
        print("\nYou must choose one unknown variable.")
        return

    if x_count == 0:
        if (side1 ** 2) + (side2 ** 2) == (hypotenuse ** 2):
            print("\nTrue")
            return
        else:
            print("\nFalse")
            return

    if side1 in ("x","X"):

        if hypotenuse <= side2:
            print("\nSide2 cannot be bigger than hypotenuse.")
            return

        print(f"\nSide1 (x): {sqrt((hypotenuse ** 2) - (side2 ** 2))}")

    elif side2 in ("x","X"):

        if hypotenuse <= side1:
            print("\nSide1 cannot be bigger than hypotenuse.")
            return

        print(f"\nSide2 (x): {sqrt((hypotenuse ** 2) - (side1 ** 2))}")

    elif hypotenuse in ("x","X"):

        print(f"\nHypotenuse (x): {sqrt((side1 ** 2) + (side2 ** 2))}")

def absolute_value(num):
    if num >= 0:
        print(num)
    else:
        print(0 - num)

def fibonacci(num):
    a, b = 0,1
    print(f"Fibonacci Series ({num})")
    for i in range(num):       
        print(a, end=" ")
        a, b = b, a + b

def prime_numbers(num):
    for i in range(2, num):
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            print(i, end=" ")

def factorial(num): #Recursion
    if num == 0:
        return 1
    return factorial(num - 1) * num

def exponentiation(base, exponent):
    if base == 0 and exponent == 0:
        print(f"{base}^{exponent} = 1 or Undefinied. (It depends)")
    else:
        print(f"{base}^{exponent} = {base ** exponent}")

def root(num, index):
    if num < 0 and index % 2 == 0:
        num *= -1    
        print(f"the {index}th/st/nd/rd root of -{num} is {num ** (1 / index)}i")
    elif num < 0:
        num *= -1
        print(f"the {index}th/st/nd/rd root of -{num} is -{num ** (1 / index)}")
    else:
        print(f"the {index}th/st/nd/rd root of {num} is {num ** (1 / index)}")
        
def circle_area(r):
    area = pi * r ** 2
    print(f"Area of a circle with a radius of {r} is {area}")

def circumference(r):
    circumference = 2 * pi * r
    print(f"Circumference of a Circle with a radius of {r} is {circumference}")
    
def square_area(length, width):
    print(f"Area of the square is {length * width}")

def triangle_area(base, height):
    print(f"Area of the triangle is {(base * height) / 2}")

def can_be_divided_by(num, divisor):
    result = num // divisor
    if result * divisor != num:
        print(f"No. {divisor} is not a divisor of {num}")
    else:
        print(f"Yes. {num}/{divisor} = {num // divisor}")

def convert(angle, measure):
    if measure.upper() == "RAD":
        return (float(angle) * pi)/180
    elif measure.upper() == "DEG":
        return (float(angle) * 180)/pi
    
def law_of_cosines(side1, side2, side3, angle, measure):
    
    x_count = 0

    if side1 in ("x","X"):
        x_count += 1
    if side2 in ("x","X"):
        x_count += 1
    if side3 in ("x","X"):
        x_count += 1
    if angle in ("x","X"):
        x_count += 1

    if x_count == 2 or x_count == 3 or x_count == 4:
        print("\nYou must choose one unknown variable.")
        return

    if x_count == 0:
        if (side3 == sqrt(side1**2 + side2**2 - 2 * side1 * side2 * cos(convert(angle, 'RAD')))):
            print("\nTrue")
            return
        else:
            print("\nFalse")
            return

    if side1 in ("x","X"):
        side1 = sqrt(side3 ** 2 - side2 ** 2 + 2 * side1 * side2 * cos(convert(angle, 'RAD')))
        print(f"\nSide1 (x): {side1}")

    elif side2 in ("x","X"):
        side2 = sqrt(side3 ** 2 - side1 ** 2 + 2 * side1 * side2 * cos(convert(angle, 'RAD')))
        print(f"\nSide2 (x): {side2}")

    elif side3 in ("x","X"):
        side3 = sqrt(side1 ** 2 + side2 ** 2 - 2 * side1 * side2 * cos(convert(angle, 'RAD')))
        print(f"\nSide3 (x): {side3}")

    elif angle in ("x","X"):
        angle = acos(round(((side1 ** 2 + side2 ** 2 - side3 ** 2)/(2 * side1 * side2)), 2))
        if measure.upper() == "DEG":
            print(f"\nAngle (x in deg): ~{convert(angle, 'DEG')}")
        elif measure.upper() == "RAD":
            print(f"\nAngle (x in rad): ~{angle}")

print("\n*** PYTHON BASIC CALCULATOR ***")
print("""
    Enter the number corresponding to the action you want to do.
    
    1- Addition         5- Pythagoras       12- Area of a Circle
    2- Subtraction      6- Absolute         13- Circumference
    3- Multiplication   7- Fibonacci        14- Area of a Square
    4- Division         8- Prime Numbers    15- Area of a Triangle
                        9- Factorial        16- Can be divided by
                       10- Exponentiation   17- Law of Cosines
                       11- Root 
    """)

while True:
    try:
        action = int(input("\nWhat do you want to calculate?: "))
    except ValueError:
        print("Please type an integer.")
        continue

    if action < 1 or action > 17:
        print("Please enter a valid action. (1-17)")
        continue

    if action == 1:
        try:
            num1 = int(input("First Number: "))
        except ValueError:
            print("Please type an integer.")
            continue
        try:
            num2 = int(input("Second Number: "))
        except ValueError:
            print("Please type an integer.")
            continue
        addition(num1, num2)

    elif action == 2:
        try:
            num1 = int(input("First Number: "))
        except ValueError:
            print("Please type an integer.")
            continue
        try:
            num2 = int(input("Second Number: "))
        except ValueError:
            print("Please type an integer.")
            continue
        subtraction(num1, num2)


    elif action == 3:
        try:
            num1 = int(input("First Number: "))
        except ValueError:
            print("Please type an integer.")
            continue
        try:
            num2 = int(input("Second Number: "))
        except ValueError:
            print("Please type an integer.")
            continue
        multiplication(num1, num2)

    elif action == 4:
        try:
            num1 = int(input("First Number: "))
        except ValueError:
            print("Please type a (+) integer.")
            continue
        try:
            num2 = int(input("Second Number: "))
            if num2 == 0: #Division by ZERO.
                print("You can't divide by ZERO!")
                continue
        except ValueError:
            print("Please type a (+) integer.")
            continue
        division(num1, num2)

    elif action == 5:
        print("Press 'x/X' if it's the side you want to find")

        side1 = input("\nSide1: ")

        if side1 not in ("x","X"):
            try:
                side1 = int(side1)

                if side1 <= 0:
                    print("Invalid INPUT.")
                    continue

            except ValueError:
                print("Side1 must be a (+) integer.")
                continue

        side2 = input("\nSide2: ")

        if side2 not in ("x","X"):
            try:
                side2 = int(side2)

                if side2 <= 0:
                    print("Invalid INPUT.")
                    continue

            except ValueError:
                print("Side2 must be a (+) integer.")
                continue

        hypotenuse = input("\nHypotenuse: ")

        if hypotenuse not in ("x","X"):
            try:
                hypotenuse = int(hypotenuse)

                if hypotenuse <= 0:
                    print("Invalid INPUT.")
                    continue

            except ValueError:
                print("Hypotenuse must be a (+) integer.")
                continue

        pythagoras(side1, side2, hypotenuse)

    elif action == 6:
        try:
            num = int(input("Number: "))
        except ValueError:
            print("Please type an integer.")
            continue
        absolute_value(num)

    elif action == 7:
        try:
            num = int(input("Fibonacci Series up to: "))
            if num <= 0:
                print("Invalid INPUT.")
                continue
        except ValueError:
            print("Please type a (+) integer.")
            continue
        fibonacci(num)

    elif action == 8:
        try:
            num = int(input("Prime numbers up to: "))
            if num <= 0:
                print("Invalid INPUT.")
                continue
        except ValueError:
            print("Please type a (+) integer.")
            continue
        prime_numbers(num)

    elif action == 9:
        try:
            num = int(input("Factorial: "))
            if num < 0:
                print("Invalid INPUT.")
                continue
        except ValueError:
            print("Please type a (+) integer.")
            continue
        print(str(num) + "! =", factorial(num))

    elif action == 10:
        try:
            base = int(input("Base: "))
        except ValueError:
            print("Please type an integer.")
            continue
        try:
            power = int(input("Power: "))
        except ValueError:
            print("Please type an integer.")
            continue
        exponentiation(base, power)

    elif action == 11:
        try:
            num = int(input("Number: "))
        except ValueError:
            print("Please type an integer.")
            continue
        try:
            index = int(input("Index: "))
            if index <= 0:
                print("Invalid INPUT.")
                continue
        except ValueError:
            print("Please type a (+) integer.")
        root(num, index)

    elif action == 12:
        try:
            r = int(input("Radius: "))
            if r <= 0:
                print("Invalid INPUT.")
                continue
        except ValueError:
            print("Please type a (+) integer.")
            continue
        circle_area(r)

    elif action == 13:
        try:
            r = int(input("Radius: "))
            if r <= 0:
                print("Invalid INPUT.")
                continue
        except ValueError:
            print("Please type a (+) integer.")
            continue
        circumference(r)

    elif action == 14:
        try:
            h = int(input("Height: "))
            if h <= 0:
                print("Invalid INPUT.")
                continue
        except ValueError:
            print("Please type a (+) integer.")
            continue
        try:
            l = int(input("Length: "))
            if l <= 0:
                print("Invalid INPUT.")
                continue
        except ValueError:
            print("Please type a (+) integer.")
            continue
        square_area(h, l)

    elif action == 15:
        try:
            height = int(input("Height: "))
            if height <= 0:
                print("Invalid INPUT.")
                continue
        except ValueError:
            print("Please type a (+) integer.")
            continue
        try:
            base = int(input("Base: "))
            if base <= 0:
                print("Invalid INPUT.")
                continue
        except ValueError:
            print("Please type a (+) integer.")
            continue
        triangle_area(base, height)

    elif action == 16:
        try:
            num = int(input("Number: "))
        except ValueError:
            print("Please type an integer.")
            continue
        try:
            divisor = int(input("Divisor: "))
            if divisor == 0:
                print("You can't divide by ZERO.")
                continue
        except ValueError:
            print("Please type an integer.")
            continue
        can_be_divided_by(num, divisor)

    elif action == 17:
        print("\nPress 'x/X' if it's the side you want to find")

    side1 = input("\nSide1: ")

    if side1 not in ("x","X"):
        try:
            side1 = float(side1)

            if side1 <= 0:
                print("Invalid INPUT.")
                continue

        except ValueError:
            print("Side1 must be a (+) float.")
            continue

    side2 = input("\nSide2: ")

    if side2 not in ("x","X"):
        try:
            side2 = float(side2)

            if side2 <= 0:
                print("Invalid INPUT.")
                continue

        except ValueError:
            print("Side2 must be a (+) float.")
            continue

    side3 = input("\nSide3: ")

    if side3 not in ("x","X"):
        try:
            side3 = float(side3)

            if side3 <= 0:
                print("Invalid INPUT.")
                continue

        except ValueError:
            print("Side3 must be a (+) float.")
            continue

    angle = input("\nAngle: (in deg 1-180) ")

    if angle not in ("x","X"):
        try:
            angle = float(angle)

            if angle <= 0 or angle > 180:
                print("Invalid INPUT.")
                continue
        except ValueError:
            print("Angle must be a (+) float between 1-180")
            continue 

    measure = ""
    if angle in ("x","X"):
        measure = input("\nMeasure: (rad/deg) ")

        if measure.upper() not in ("RAD", "DEG"):
            print("Mesure must be rad or deg")
            continue

    law_of_cosines(side1, side2, side3, angle, measure)

    continue

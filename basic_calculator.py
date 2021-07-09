#Toprk

from math import pi, sqrt, cos, acos, floor

def addition(_list): 
    result = 0
    for num in _list:
        result += num
    print(f"\nResult: {result}")

def subtraction(num1, num2):
    print(f"\n({num1}) - ({num2}) = {num1 - num2}")

def multiplication(_list):
    result = 1
    for num in _list:
        result *= num
    print(f"\nResult: {result}")

def division(num1, num2):
    print(f"\n{num1} / {num2} = {num1 / num2}")

def exponentiation(base, exponent):
    if base == 0 and exponent == 0:
        print(f"\n{base}^{exponent} = 1 or Undefinied. (It depends)")
    else:
        print(f"\n{base}^{exponent} = {base ** exponent}")

def root(num, index):

    index_s = str(index)
    ind = ""
    if index_s[-1] == "1" and index_s[-2:] != "11":
        ind = "st"
    elif index_s[-1] == "2" and index_s[-2:] != "12":
        ind = "nd"
    elif index_s[-1] == "3" and index_s[-2:] != "13":
        ind = "rd"
    else:
        ind = "th"

    if num < 0 and index % 2 == 0:
        num *= -1    
        print(f"\nthe {index}{ind} root of -{num} is {num ** (1 / index)}i")
    elif num < 0:
        num *= -1
        print(f"\nthe {index}{ind} root of -{num} is -{num ** (1 / index)}")
    else:
        print(f"\nthe {index}{ind} root of {num} is {num ** (1 / index)}")

def factorial(num):
    if num == 0:
        return 1
    return factorial(num - 1) * num

def prime_numbers(num):
    for i in range(2, num):
        for j in range(2, floor(sqrt(i))):
            if i % j == 0:
                break
        else:
            print(i, end=" ")

def fibonacci(num):
    a, b = 0,1
    print(f"\nFibonacci Series ({num})")
    for i in range(num):       
        print(a, end=" ")
        a, b = b, a + b

def can_be_divided_by(num, divisor):
    result = num // divisor
    if result * divisor != num:
        print(f"\nNo. {divisor} is not a divisor of {num}")
    else:
        print(f"\nYes. {num}/{divisor} = {num // divisor}")

def pythagoras(sideA, sideB, hypotenuse):
    x_count = 0

    if sideA in ("x","X"):
        x_count += 1
    if sideB in ("x","X"):
        x_count += 1
    if hypotenuse in ("x","X"):
        x_count += 1

    if x_count == 2 or x_count == 3:
        print("\nYou must choose one unknown variable.")
        return

    if x_count == 0:
        if (sideA ** 2) + (sideB ** 2) == (hypotenuse ** 2):
            print("\nTrue")
            return
        else:
            print("\nFalse")
            return

    if sideA in ("x","X"):

        if hypotenuse <= sideB:
            print("\nSideB cannot be bigger than hypotenuse.")
            return

        print(f"\nSideA (x): {sqrt((hypotenuse ** 2) - (sideB ** 2))}")

    elif sideB in ("x","X"):

        if hypotenuse <= sideA:
            print("\nSideA cannot be bigger than hypotenuse.")
            return

        print(f"\nSideB (x): {sqrt((hypotenuse ** 2) - (sideA ** 2))}")

    elif hypotenuse in ("x","X"):

        print(f"\nHypotenuse (x): {sqrt((sideA ** 2) + (sideB ** 2))}")

def convert(angle, measure):
    if measure.upper() == "RAD":
        return (float(angle) * pi)/180
    elif measure.upper() == "DEG":
        return (float(angle) * 180)/pi

def law_of_cosines(sideA, sideB, sideC, angleC, measure):
    
    x_count = 0

    if sideA in ("x","X"):
        x_count += 1
    if sideB in ("x","X"):
        x_count += 1
    if sideC in ("x","X"):
        x_count += 1
    if angleC in ("x","X"):
        x_count += 1

    if x_count == 2 or x_count == 3 or x_count == 4:
        print("\nYou must choose one unknown variable.")
        return

    if x_count == 0:
        if (sideC == sqrt(sideA**2 + sideB**2 - 2 * sideA * sideB * cos(convert(angleC, 'RAD')))):
            print("\nTrue")
            return
        else:
            print("\nFalse")
            return

    if sideA in ("x","X"):
        sideA = sqrt(sideC ** 2 - sideB ** 2 + 2 * sideA * sideB * cos(convert(angleC, 'RAD')))
        print(f"\nSideA (x): {sideA}")

    elif sideB in ("x","X"):
        sideB = sqrt(sideC ** 2 - sideA ** 2 + 2 * sideA * sideB * cos(convert(angleC, 'RAD')))
        print(f"\nSideB (x): {sideB}")

    elif sideC in ("x","X"):
        sideC = sqrt(sideA ** 2 + sideB ** 2 - 2 * sideA * sideB * cos(convert(angleC, 'RAD')))
        print(f"\nSideC (x): {sideC}")

    elif angleC in ("x","X"):
        angleC = acos(round(((sideA ** 2 + sideB ** 2 - sideC ** 2)/(2 * sideA * sideB)), 2))
        if measure.upper() == "DEG":
            print(f"\nAngleC (x in deg): ~{convert(angleC, 'DEG')}")
        elif measure.upper() == "RAD":
            print(f"\nAngleC (x in rad): ~{angleC}")

def circle_area(r):
    area = pi * r ** 2
    print(f"\nArea of a circle with a radius of {r} is {area}")

def circumference(r):
    circumference = 2 * pi * r
    print(f"\nCircumference of a Circle with a radius of {r} is {circumference}")
    
def rectangle_area(length, width):
    print(f"\nArea of the rectangle is {length * width}")

def triangle_area(base, height):
    print(f"\nArea of the triangle is {(base * height) / 2}")

def print_options():
    print("""\n
    _____________________PYTHON BASIC CALCULATOR_____________________
       Enter the number corresponding to the action you want to do.  
    _________________________________________________________________
           Maths                                     Geometry             
         *********                                 ************
     1)  Addition                              11) Pythagoras       
     2)  Subtraction                           12) Law of Cosines
     3)  Multiplication                        13) Area of a Circle
     4)  Division                              14) Circumference

     5)  Exponentiation                        15) Area of a Rectangle
     6)  Root                                  16) Area of a Triangle
     7)  Factorial
     8)  Prime Numbers

     9)  Fibonacci Series
     10) Can be Divided by
    """)

while True:
    
    print_options()
    try:
        action = int(input("\nWhat do you want to calculate?: "))
    except ValueError:
        print("Please type an integer.")
        continue

    if action < 1 or action > 16:
        print("Please enter a valid action. (1-16)")
        continue

    if action == 1:
        print("\nSelected: Addition\n")
        index = 1
        num_list = []

        while True:
            num = input(f"\nNum{index} (Q to quit): ")
            if num in ("q","Q"):
                addition(num_list)
                break

            try:
                num_list.append(int(num))
                index += 1
            except ValueError:
                print("Invalid INPUT.")

    elif action == 2:
        print("\nSelected: Subtraction\n")
        try:
            num1 = int(input("\nFirst Number: "))
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
        print("\nSelected: Multiplication\n")
        index = 1
        num_list = []

        while True:
            num = input(f"\nNum{index} (Q to quit): ")
            if num in ("q","Q") and index == 1:
                print("Result: 0")
                break
            if num in ("q","Q"):
                multiplication(num_list)
                break

            try:
                num_list.append(int(num))
                index += 1
            except ValueError:
                print("Invalid INPUT.")

    elif action == 4:
        print("\nSelected: Division\n")
        try:
            num1 = int(input("\nFirst Number: "))
        except ValueError:
            print("Please type a (+) integer.")
            continue
        try:
            num2 = int(input("Second Number: "))
            if num2 == 0:
                print("You can't divide by ZERO!")
                continue
        except ValueError:
            print("Please type a (+) integer.")
            continue

        division(num1, num2)

    elif action == 5:
        print("\nSelected: Exponentiation\n")
        try:
            base = int(input("\nBase: "))
        except ValueError:
            print("Please type an integer.")
            continue
        try:
            power = int(input("Power: "))
        except ValueError:
            print("Please type an integer.")
            continue

        exponentiation(base, power)

    elif action == 6:
        print("\nSelected: Root\n")
        try:
            num = int(input("\nNumber: "))
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

    elif action == 7:
        print("\nSelected: Factorial\n")
        try:
            num = int(input("\nFactorial: "))
            if num < 0:
                print("Invalid INPUT.")
                continue
        except ValueError:
            print("Please type a (+) integer.")
            continue
        print(f"\n{str(num)}! = {factorial(num)}")

    elif action == 8:
        print("\nSelected: Prime Numbers\n")
        try:
            num = int(input("\nPrime numbers up to: "))
            if num <= 0:
                print("Invalid INPUT.")
                continue
        except ValueError:
            print("Please type a (+) integer.")
            continue

        prime_numbers(num)

    elif action == 9:
        print("\nSelected: Fibonacci Series\n")
        try:
            num = int(input("\nFibonacci Series first (n): "))
            if num <= 0:
                print("Invalid INPUT.")
                continue
        except ValueError:
            print("Please type a (+) integer.")
            continue

        fibonacci(num)

    elif action == 10:
        print("\nSelected: Can be Divided by\n")
        try:
            num = int(input("\nNumber: "))
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

    elif action == 11:
        print("\nSelected: Pythagoras\n")
        print("\nPress 'x/X' if it's the side you want to find")

        sideA = input("\nSideA: ")

        if sideA not in ("x","X"):
            try:
                sideA = int(sideA)

                if sideA <= 0:
                    print("Invalid INPUT.")
                    continue

            except ValueError:
                print("SideA must be a (+) integer.")
                continue

        sideB = input("\nSideB: ")

        if sideB not in ("x","X"):
            try:
                sideB = int(sideB)

                if sideB <= 0:
                    print("Invalid INPUT.")
                    continue

            except ValueError:
                print("SideB must be a (+) integer.")
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

        pythagoras(sideA, sideB, hypotenuse)

    elif action == 12:
        print("\nSelected: Law of Cosines\n")
        print("\nPress 'x/X' if it's the side you want to find")

        sideA = input("\nSideA: ")

        if sideA not in ("x","X"):
            try:
                sideA = float(sideA)

                if sideA <= 0:
                    print("Invalid INPUT.")
                    continue

            except ValueError:
                print("SideA must be a (+) float.")
                continue

        sideB = input("\nSideB: ")

        if sideB not in ("x","X"):
            try:
                sideB = float(sideB)

                if sideB <= 0:
                    print("Invalid INPUT.")
                    continue

            except ValueError:
                print("SideB must be a (+) float.")
                continue

        sideC = input("\nSideC: ")

        if sideC not in ("x","X"):
            try:
                sideC = float(sideC)

                if sideC <= 0:
                    print("Invalid INPUT.")
                    continue

            except ValueError:
                print("SideC must be a (+) float.")
                continue

        angleC = input("\nAngleC: (in deg 1-180) ")

        if angleC not in ("x","X"):
            try:
                angleC = float(angleC)

                if angleC <= 0 or angleC > 180:
                    print("Invalid INPUT.")
                    continue
            except ValueError:
                print("AngleC must be a (+) float between 1-180")
                continue 

        measure = ""
        if angleC in ("x","X"):
            measure = input("\nMeasure: (rad/deg) ")

            if measure.upper() not in ("RAD", "DEG"):
                print("Mesure must be rad or deg")
                continue

        law_of_cosines(sideA, sideB, sideC, angleC, measure)

    elif action == 13:
        print("\nSelected: Circle Area\n")
        try:
            r = int(input("\nRadius: "))
            if r <= 0:
                print("Invalid INPUT.")
                continue
        except ValueError:
            print("Please type a (+) integer.")
            continue

        circle_area(r)

    elif action == 14:
        print("\nSelected: Circumference\n")
        try:
            r = int(input("\nRadius: "))
            if r <= 0:
                print("Invalid INPUT.")
                continue
        except ValueError:
            print("Please type a (+) integer.")
            continue

        circumference(r)

    elif action == 15:
        print("\nSelected: Rectangle Area\n")
        try:
            h = int(input("\nHeight: "))
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

        rectangle_area(h, l)

    elif action == 16:
        print("\nSelected: Triangle Area\n")
        try:
            height = int(input("\nHeight: "))
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

    continue

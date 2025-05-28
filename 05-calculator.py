def add(x,y):
    print(f"The sum of {x} and {y} is : ", x + y)

def division(x,y):
    if y == 0:
        print(f"The Division of {x} and {y} is : Undefined")
    else:
        print(f"The division of {x} and {y} is :", x / y)

def subtract(x,y):
    print(f"The difference of {x} and {y} is : ", x - y)

def multiple(x,y):
    print(f"The product of {x} and {y} is : ", x * y)

def modulo(x,y):
    if y == 0:
        print(f"The modulo of {x} and {y} is undefined")
    
    else:
        print(f"The modulo of {x} and {y} is : ", x % y)



def main():
    print("""
                Selection your operation
                    1. Addition
                    2. Division
                    3. Subtraction
                    4. Multiplication
                    5. Modulo
            """)
    while True:
        try:
            option = int(input("Select an operation from (1-5): "))
            if option > 5 or option == 0:
                print("No such option!!!")
                continue
            else:
                first_num = int(input("Enter first number: "))
                second_num = int(input("Enter second number: "))
            
            if option == 1:
                add(first_num, second_num)

            elif option == 2:
                division(first_num, second_num)

            elif option == 3:
                subtract(first_num, second_num)

            elif option == 4:
                multiple(first_num, second_num)

            elif option == 5:
                modulo(first_num, second_num)


            tryAgain = input("Do you want to quit? (Yes Or No) ")
            if tryAgain.lower().startswith('y'):
                print("Good Bye👋👋")
                break
            elif tryAgain.lower().startswith('n'):
                continue
            else:
                print(f"'{tryAgain}' is not an option!!")
                break


        except ValueError:
            print("❌❌Invalid option!!")
        

main()
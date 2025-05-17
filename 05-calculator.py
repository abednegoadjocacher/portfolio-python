def add(x,y):
    return x + y

def division(x,y):
    try:
        # if y == 0:
            # print("A number can not be divide by 0")
        return x / y
    except ZeroDivisionError:
        print("""Division operation can not be perform!!
A number can not be divide by 0""")


def subtract(x,y):
    return x - y


def multiple(x,y):
    return x * y


def modulo(x,y):
    return x % y




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
            option = int(input("Select from (1-5): "))

            first_num = int(input("Enter first number: "))
            second_num = int(input("Enter second number: "))

            if option == 1:
                print(f"The sum of {first_num} and {second_num} is : ", add(first_num, second_num))


            elif option == 2:
                if second_num == 0:
                    print(f"The Division of {first_num} and {second_num} is : Undefine")
                else:
                    print(f"The Division of {first_num} and {second_num} is : ", division(first_num, second_num))

            elif option == 3:
                print(f"The difference of {first_num} and {second_num} is : ", subtract(first_num, second_num))

            elif option == 4:
                print(f"The product of {first_num} and {second_num} is : ", multiple(first_num, second_num))

            elif option == 5:
                print(f"The modulo of {first_num} and {second_num} is : ", modulo(first_num, second_num))

            else:
                print("No such option!!!")


                if again.lower().startswith("n"):
                    break
                    # elif again.lower() is not "n" or "y": I have some bug tto solve here.
                    #     print("Sorry Incorrect response")
                    #     return
               
        except ValueError:
            print("❌❌Invalid input!!")


        again = input("Do you want too quit? (Yes Or No)")
        if again.lower().startswith("n"):
            break
        # elif again.lower() is not "n" or "y": I have some bug tto solve here.
        #     print("Sorry Incorrect response")
        #     return
        else:
            main()

main()
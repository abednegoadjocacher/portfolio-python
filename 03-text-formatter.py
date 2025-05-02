#Convert string to different formats
#Accept user input
#ask user what format to convert to.
#print the user selected format

sentence =  input("Enter string to format: ")
print("Select the format option")
print(f"(1). I Am A Python Developer.\n(2). i am a python developer.\n(3).I AM A PYTHON DEVELOPER.\n(4). I am a python developer")
try:
    choice = int(input("Enter option: "))
    if choice == 1:
        print(sentence.title())
    elif choice == 2:
        print(sentence.lower())
    elif choice == 3:
        print(sentence.upper())
    elif choice == 4:
        print(sentence.capitalize())
    else:
        print("No such option!")
except ValueError:
    print("Invalid option selected!")

#This project is to accept user input
#Shuffle the user input and print it back
#The user is allow to enter any number of multiple times
#Unless use enter "q" to quit


#I need too import random module

import random
print("Word scrambler✨✨\n")

while True:
    word  = input("Enter your word or 'q' to Quit: ")
    if word.lower() == "q":
        print("Thank you for using my service😊😊")
        break

    word_list = list(word)
    random.shuffle(word_list)
    print(f"Scrambled world: {"".join(word_list)}")
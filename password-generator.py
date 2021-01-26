import random
import string
import sys  

def isnumber(input):
    if input.isnumeric() == False:
        print("\nYou did not enter a number.")
        return False
    else:
        return True

def quit():
    quit_input = input("To quit press Q. Press enter to continue ")
    quit_input = quit_input.upper()
    if quit_input == "Q":
        return True
    else: 
        return False

while True:

    desired_len = 0

    #Password Lenght
    while desired_len < 6:
        print("Your password needs to be at least 6 characters long.")
        print("How long would you like your password to be?")
        desired_len = (input("Type a number here and press enter: "))
        if isnumber(desired_len):
            desired_len = int(desired_len)
        else:
            desired_len = 0
            if quit():
                sys.exit() 
                break
                
        
    #Password Letters
    while True:
        print("\nHow many letters?")
        print("(Hint: You can use up to", str(desired_len),")")
        letters_count = input("Type a number here and press enter: ")

        if isnumber(letters_count):
            letters_count = int(letters_count)
            if letters_count > desired_len:
                print("\nLetters exceed the desired lenght of password\nThe lenght of password is:", str(desired_len))
                if quit():
                    sys.exit() 
                    break
            else:
                break
                
        
    #Password Numbers   
    characters_left = desired_len - letters_count

    while True:
        print("\nHow many numbers?")
        print("(Hint: You can use up to", str(characters_left), ")")
        numbers_count = input("Type a number here and press enter: ")

        if isnumber(numbers_count):
            numbers_count = int(numbers_count)
            if numbers_count > characters_left:
                print("\nCharcters exceed the desired lenght of password.\nThe remaining character lenght that can be used is: ", str(characters_left))
                if quit():
                    sys.exit() 
                    break
            else:
                characters_left -= numbers_count
                break        

    print("\nThank you. We are working on generating your password\n")

    #Password Generation

    all_random = ""

    while characters_left != 0:
        all_random += random.choice(string.punctuation)
        characters_left -= 1

    while letters_count != 0:
        all_random += random.choice(string.ascii_lowercase)
        letters_count -= 1

    while numbers_count != 0:
        all_random += random.choice(string.digits)
        numbers_count -= 1


    all_random_list = list(all_random)
    random.shuffle(all_random_list)
    final_password = "".join(all_random_list)

    print("Your new password is:",final_password)

    if quit():
        sys.exit()

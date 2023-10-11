import random
import string

print("please enter your password")

# the password we are going to create should contain letters both upper and lower cases , numbers and special cases 
def  generate_password():

    #returns a string containing all of tthe uppercase and lowercase letters
    letters=string.ascii_letters

    #returns the string "0123456789"
    digits=string.digits

    #returns a string that contains all special cases 
    special_characters=string.punctuation

    password=letters+digits+special_characters
    return letters, digits, special_characters
generate_password()


# a function to ask the user how long they want the pasword to be 
def user_input():

        how_many_alphabets=input("please specify how many alphabets you want to use: ")
        while not how_many_alphabets.isdigit():
            how_many_alphabets=input("please specify how many alphabets you want to use: ")
        

        how_many_numbers=input("please specify how many numbers you want to use: ")
        while not how_many_numbers.isdigit():
            how_many_numbers=input("please specify how many numbers you want to use: ")


        how_many_special_characters=input("please specifiy how many special characters you want to use: ")
        while not how_many_special_characters.isdigit():
            how_many_special_characters=input("please specifiy how many special characters you want to use: ")

        return how_many_alphabets,how_many_numbers,how_many_special_characters

 


def create_password(how_many_alphabets, how_many_numbers, how_many_special_characters, letters, numbers, special_characters):
    password=''
    for i in range(int(how_many_alphabets)):
        password+=random.choice(letters)
    
        for i in range(int(how_many_numbers)):
            password+=random.choice(numbers)

        for i in range(int(how_many_special_characters)):
            password+=random.choice(special_characters)

    print(password)

how_many_alphabets,how_many_numbers,how_many_special_characters = user_input()
letters, numbers, special_characters = generate_password()
create_password(how_many_alphabets, how_many_numbers, how_many_special_characters, letters, numbers, special_characters)





        






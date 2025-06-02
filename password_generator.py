import random
def welcome():
    print("Welcome!!")
welcome()

def user_ask():
    first_name=input("Enter your name: ")
    last_name=input("Enter you surname: ")
    password_of_user=input("Enter a strong password: ")
    return password_of_user


def password_generator():        
    for attempts in range(1,3+1):
        int_Found=False
        password_of_user=user_ask()
        list_of_integer=['0','1','2','3','4','5','6','7','8','9']
        for integer in list_of_integer:
            if integer not in password_of_user:
                int_Found=False
            else:
                int_Found=True
        if password_of_user==True:
            print("weak password, Use integer value too!!")
        else:
            print("Weak password, Use special character.")
        
        char_found=False
        special_character=['!','@','#','$','&']
        for character in special_character:
            if character not in password_of_user:
                char_found=False
            else:
                char_found=True
        
        if password_of_user==True:
            print("Weak password,Try again")
                
            
   
    computer_generated=random.choice(['Ae7$1mQ','kdkb3@#','wu@#2323'])
    print(f"Here is your strong password {computer_generated}")
password_generator()
            
        
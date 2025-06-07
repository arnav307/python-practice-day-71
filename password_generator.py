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
        list_of_password=[]
        password_of_user=user_ask()
        int_Found=False
        char_found=False
        small_alpha=False
        big_alpha=False
        list_of_integer=['0','1','2','3','4','5','6','7','8','9']
        special_character=['!','@','#','$','&','*','^']
        small_alphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        big_alphabet=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
        
        list_of_password.append(password_of_user)
        for i in list_of_password:
            if len(i)<8:
                print("Your length must be at least 8 letters.")
                continue
        
        for integer in list_of_integer:
            if integer not in password_of_user:
                int_Found=False
            else:
                int_Found=True
                break
            
        for small in small_alphabet:
            if small not in password_of_user:
                small_alpha=False
            else:
                small_alpha=True
                break
            
        for Big in big_alphabet:
            if Big not in password_of_user:
                big_alpha=False
            else:
                big_alpha=True
                break
                  
        
        for character in special_character:
            if character not in password_of_user:
                char_found=False
            else:
                char_found=True  
                break
                
            
        if int_Found==False:
            print("Weak password! use integer value.")
        elif char_found==False:
            print("weak password! use special character.")
        elif small_alpha==False:
            print("Use small letter.")
        elif big_alpha==False:
            print('use capital letter.')
        else:
            print("Great login!!!!!!!!!")
            break
        
        
            
            
            
    computer_generated=random.choice(['Ae7$1mQ','kdkb3@#','wu@#2323'])
    print(f"Here is your strong password {computer_generated}")
password_generator()
            
        
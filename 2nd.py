import random

def generate_password():
    print("Choose your password complexity: \n1. SuperStrong \n2. Strong \n3. Medium \n4. Weak")
    
    lower = "qwertyuiopasdfghjklzxcvbnm"
    upper = "QWERTYUIOPASDFGHJKLZXCVBNM"
    num = "1234567890"
    spchr = "!@#$%^&*()~[]}{<>?/"
    
    bum = lower + upper
    all_characters = lower + upper + spchr + num
    gum = lower + upper + num
    
    types = int(input("Enter your password complexity: "))
    
    # Input validation for length
    while True:
        try:
            length = int(input("Enter the length of your password: "))
            if length <= 0:
                raise ValueError
            break
        except ValueError:
            print("Please enter a valid positive integer for the length.")

    if types == 4:
        password = "".join(random.sample(num, min(length, len(num))))
    elif types == 3:
        password = "".join(random.sample(bum, min(length, len(bum))))
    elif types == 2:
        password = "".join(random.sample(gum, min(length, len(gum))))
    elif types == 1:
        password = "".join(random.sample(all_characters, min(length, len(all_characters))))
    else:
        print("Invalid option. Please choose from Weak, Medium, Strong, or SuperStrong.")
        return

    print(f"Your {types} password is: {password}")

generate_password()
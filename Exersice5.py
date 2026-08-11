#1. Control variables
correct_password = "eliam123"
remaining_attempts = 3
#2. Validation loop
while remaining_attempts > 0:
    entered_password = input("Enter the password: ")
    if entered_password == correct_password:
        print("Access granted. Welcome to the system!")
        break # Exit the loop immediately
    else:
        remaining_attempts -= 1
        if remaining_attempts > 0:
            print(f"Incorrect password. You have {remaining_attempts} attempt(s) left.\n")
        else:
            print("account locked due to too many failed attempts.")

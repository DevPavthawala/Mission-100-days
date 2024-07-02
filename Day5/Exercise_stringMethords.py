# validate user input exercise
# 1. username is no more than 12 charactors
# 2. username must not contain spaces
# 3. username not contain digits


username = input("Enter your Username: ")

if len(username) > 12:
    print("Your username can't be more than 12 char")
elif not username.find(" ") == -1:
    print("Your username can't contain spaces")
elif not username.isalpha():
    print("Your username cant't contain numbers")
else:
    print(f"welcome {username}")
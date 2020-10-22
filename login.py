database = {"messi":'fcb','xavi':'spain','neymar':'brazil'}


print ("1) LOGIN")
print ("2) NEW USER")

choice = int(input("Enter your choice:"))

if choice == 1:
    username = input("Enter the Username: ")
    if username in database:
        print ("--Username Exists--")
        password = input("Enter the Password: ")
        if password in database[username]:
            print ("--Valid password, Login Successful--")
        else:
            print ("--invalid password--,Login Failed--")
    else:
        print ("--Invalid Username,Register for New User--")
elif choice == 2:
    username1 = input("Enter the New Username:")
    password1 = input("Enter the Password: ")
    database.update({username1:password1})
    username2 = input("Enter the Updated-Username: ")
    #password2 = input("Enter the password for "+ username2 +": ")
    if username2 in database:
        print ("login successful")
        password2 = input("Enter the password for"  +  username2 + ": ")
        if password2 in database[username2]:
            print ("==login successful==")
        else:
            print ("=login failed=")
#print(database)




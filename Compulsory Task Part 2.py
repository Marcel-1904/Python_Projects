# I was not sure if I needed to have the whole program in this part of the
#task so I did the second part seperate for what is requested. If the entire
#program is needed I will make the changes and resubmit

#First I create the variable to hold the users input
#To take the users username input
user_name = input("Please enter username:")

#If the username is not 'admin' the print statement is triggerd
if user_name != "admin":
    print("Your username is not valid, only username 'admin' can register users")

#If the user is equal to 'admin' the menu print statement is triggerd
elif user_name == "admin":
    admin_menu = input("Please select one of the following options: \n\
        r - register new user \n\
            d - display  statistics \n\
                e - exit")

    #Now for the if statements for the options from the menu

    #If the user chose the register option
    if admin_menu == "r":

        #New username variable
        new_username = input("Please enter the new username:")

        #New user password variable
        new_user_password = input("Please enter a password for the new user:")
        
        #To hold the password confirm
        new_password = False

        #Now a while statement to confirm the enterd password
        while new_password == False:
            confirmed_password = input("Enter password again to confirm password:")

            #If the password was enterd correctly
            if new_user_password == confirmed_password:
                new_password = True

            #If  password was entered incorrectly
            elif new_password == False:
                print("Password did not match")

        #Now to write the new user information to the user file
        with open("user.txt", "a") as new_user:
            new_user.write(new_username) + "," + " " + (new_user_password) + "\n"


    #Now the option for statistics
    elif admin_menu == "d":

        #Now for counters for the users and taks
        task_num = 0

        users_num = 0

        #Now to open the file to write to it
        with open('tasks.txt', 'r') as n:
            
            #Now a for statement
            for line in n:

                #To add 1 for every task
                task_num +=1

        #To print result
        print(f"Total number of tasks: {task_num}")

        #Now the statement for the users
        with open("users.txt", "r") as f:

            #To itterate through the file
            for line in f:

                #For each user to add to the counter
                users_num += 1

        #To print the result
        print(f"Total number of users: {users_num}")
    
    #Now for the 'e' option
    if admin_menu == "e":
        
        #Now to exit the app
        exit


#First I open my user file and task file
user_file = open('user.txt', 'a+')

#Now a login variable with the value of False
login = False

#Now a while loop so if the user enters incorrect info
#they are asked to enter it again
while login == False:

    #Now I make the user enter their username and password
    username = input("Please enter your username:")
    password = input("Please enter your password:")

    #Now a for statement to itterate through the user_file
    for line in user_file:

        #Now to get the correct username and password to log
        #into the file using the split function
        correct_username, correct_password = line.split(", ")

        #Now an if statement to check if the username and password
        #is the same as in the file
        if username == correct_username and password == correct_password:
            login = True
            print("\nYou have succesfully loged in \n")

    if login == False:
    #A print statement to tell the user that the information entered is incorrect
        print("Incorrect password or username. Please re-enter details")

    #Now with each itteration to let the itteration start at the beginning of the file
    user_file.seek(0)

#Now for the display of the menu and to take the users input
menu_input = input("Please select one of the 5 options:\n\
r - register user \n\
a - add task \n\
va - view all tasks \n\
vm - view my tasks \n\
e - exit \n")

#Now an if statement for each option in the menu
if menu_input == "r":
    
    #Now to ask the user to enter the name and password of the new user
    new_user = input("Please enter the new username: ")

    new_password = input("Please enter the new users password: ")

    #Now to write to the users file
    user_file.write(f"\n{new_user}, {new_password}")


elif menu_input == "a":

    #Now to open the task file
    task_file = open("tasks.txt", "a+")

    #Now to take information of the task from the user
    user_name = input("Enter user name: ")

    task_name = input("Enter task name: ")

    task_desc = input("Enter the task description: ")

    date_assigned = input("Enter date that the task is assigned: ")

    due_date = input("Please enter the date that the task is due: ")

    task_complete = input("Is the task completed? ")

    #Now to write to the file al the information to the task file
    task_file.write(f"\n{user_name}, {task_name}, {task_desc}, {date_assigned}, {due_date}, {task_complete}")

    #Now to close the file
    task_file.close()

elif menu_input == "va":

    #Now to open the file again in a different mode
    task_file = open("tasks.txt", "r")

    #Now a for loop to itterate through everything
    for line  in task_file:

        #Now to unpack all the info from the file into variables
        user_name, task_name, task_desc, date_assigned, due_date, task_complete = line.split(", ")

        #Now to print the result
        print(f"""
        User: {user_name}
        Task name: {task_name}
        Task description: {task_desc}
        Date assigned: {date_assigned}
        Due date: {due_date}
        Task Completed? {task_complete}
        """)

        #To close the file
    task_file.close()

elif menu_input == "vm":

    #Now to open the file in read mode
    task_file = open('tasks.txt', 'r')

    #A for loop to itterate through the file
    for line in task_file:

        #Now to split the information of the file into variables
        user_name, task_name, task_desc, date_assigned, due_date, task_complete = line.split(", ")

        #Now an if statement to show tasks for a specific user
        if username == user_name:

            #Now to print the result
            print(f"""
        User: {user_name}
        Task name: {task_name}
        Task description: {task_desc}
        Date assigned: {date_assigned}
        Due date: {due_date}
        Task Completed? {task_complete}
        """)

    #To close the file
    task_file.close()

elif menu_input == "e":

    print("You have succesfully loged out")
    exit()







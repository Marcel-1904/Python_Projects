#For to compare if the task are overdue or not
import datetime
from datetime import *

#Now to define the first funcion to register new users
def reg_user(menu_choice):


    #If the user entered "r"
    if menu_choice == "r":

        #To enter the new users name
        new_user = input("Please enter the new users name: \n")

        #Now to check if the user name is already the file of users
        #If the name already exists in the user file an error message will be displayed
        while new_user in usernames_list:

            #Error message
            print("The username entered is already listed")

            #The user is asked to re-enter a name
            new_user = input("Please enter the new users name: \n")

        #An if statement if the entered name is not in the list
        if new_user not in usernames_list:

            print("\nUsername is validn\n")

            #Username is added to the list
            usernames_list.append(new_user)

            #To add the entered details to the file
            user_details["Username"] = usernames_list

        #Now to get the new users password
        new_password = input("Please enter a password: \n")

        #Now to confirm the new password
        password_confirm = input("Please re-enter your password: \n")

        #Now if the entered password does not match the  re-entered password
        while new_password != password_confirm:

            #Error message
            print("Your entered password does not match your re-entered password")

            #Now to retake the users new password and confirmed password
            new_password = input("Please enter a password: \n")

            password_confirm = input("Please re-enter your password: \n")

        #Now an if statement for if the entered password matches the password
        #to confirm
        if new_password == password_confirm:

            print("The entered password is valid")

            passwords_list.append(new_password)

            #The Passwords side of the dict equals the list of passwords
            user_details["Passwords"] = passwords_list

            #Now to open the user text file
            with open("user.txt", "r+") as f:

                #Now to print the username and password on seperate lines
                for i in range(len(usernames_list)):

                    #Now to write to the file
                    f.write(user_details["Usernames"][i] + ", " + user_details["Passwords"][i] + "\n")

        return ("Your new username and password was succesfully added")

#Now for the second function
def add_task(menu_choice):

    #If statement if add task is chosen
    if menu_choice == "a":

        #Now to take all the details for the task to be entered
        name = input("Please enter the username for whom the task is: \n")

        title = input("Please enter the title of the task: \n")

        description = input("Please enter a description of the task: \n")

        #This automatically adds the date of the day that the task is added
        current_date = date.today()

        #To change the current date value to the right string format
        assigned_date = current_date.strftime("%d %b %Y")

        date_format = input("Please enter the due date of the task (e.g. dd-mm-yyyy format): \n")

        #To split the date format with "-"
        date_list = date_format.split("-")

        numbers_date = [int(x) for x in date_list]

        #To get the due date of the task the format for the date is created
        due_date = date(numbers_date[2], numbers_date[1], numbers_date[0]).strftime("%d %b %Y")

        task_completed = "No"

        #Now to create a task list
        task_list = [name, title, description, assigned_date, due_date, task_completed]

        tasks_dict[f"Task {count} details:"] = task_list

        #Now to open the task text file
        with open("tasks.txt", "r+") as f2:
            
            #Now to print the list values to each key in the dictionary
            for key in tasks_dict:

                line_string = str(tasks_dict[key])

                #A list of bad characters
                bad_chars = ["[", "]", "\'",]

                for i in bad_chars:
                    
                    #To replace all bad characters in the string
                    line_string = line_string.replace(i, "")

                f2.write(line_string + "\n")

        return("Your new task has succesfully been added.")

#Third function
def view_all(menu_choice):

    if menu_choice == "va":

        #To count the total tasks
        task_count = 0

        #To create the task view easier with the dictionary values
        for key in tasks_dict:

            #For every key in the dictionary the counter goes up
            task_count += 1

            print(f"\
Task {str(task_count)}:     {str(tasks_dict[key][1])}n\
Assigned to:        {str(tasks_dict[key][0])}\n\
Date assigned:      {str(tasks_dict[key][3])}\n\
Due date:           {str(tasks_dict[key][4])}\n\
Task Complete?      {str(tasks_dict[key][5])}\n\
Task Description:\n\
 {str(tasks_dict[key][2])}\n")

    return("End of Tasks.")

#Function 4
def view_mine(menu_choice, username):

    if menu_choice == "vm":

        #To set a count for number of tasks
        task_count = 0

        for key in tasks_dict:

            task_count += 1

            #To display the tasks for that specific user
            if username == (tasks_dict[key][0]):

                print(f"\
\nTask {str(task_count)}:     {str(tasks_dict[key][1])}\n\
Assigned to:        {str(tasks_dict[key][0])}\n\
Date assigned:      {str(tasks_dict[key][3])}\n\
Due date:           {str(tasks_dict[key][4])}\n\
Task Complete?      {str(tasks_dict[key][5])}\n\
Task Description:\n\
 {str(tasks_dict[key][2])}")

    #To give editing options or to return to the menu
    task_selection = input("\nPlease select a task by number to edit (e.g. 1, 2, 3)\
        or type -1 to return to the main menu. \n")

    #If the users selects -1 to return the menu
    if task_selection == "-1":

        return (menu)

    else:

        #If a task number is entered, the item linked to that number can be edited
        option = input("Would you like to edit the task or mark as complete(e.g. mark OR edit): \n")

        if option == "mark":
            
            #If the user chooses mark, the item linked to that numbers completion value is
            #changed to "Yes"
            tasks_dict[f"Task {task_selection} details:"][5] = "Yes"

            return("Your task has been succesfully marked as complete.")

        elif option == "edit" and (tasks_dict[f"Task {task_selection} details:"][5] == "No"):

            #A choice for the user on what to edit
            edit_choice = input("Would you like to edit the username or task due \
                date(e.g. enter User or Date): \n")

            if edit_choice == "User":

                #The user is given the option to edit the username or due date
                name_edit = input("Please enter the new username for the task: \n")

                #To edit the name to whom the task is made for
                tasks_dict[f"Task {task_selection} details:"][0] = name_edit

                return("The tasks username has been succesfully updated.")

            elif edit_choice == "Date":

                due_date_change = input("Please enter a new due date(e.g. 18 March 2019): \n")

                #To change the due date of the task
                tasks_dict[f"Task {task_selection} details:"][4] = due_date_change

                return ("The due date has been succesfully updated.")

        elif option == "edit" and (tasks_dict[f"Task {task_selection} details:"][5] == "Yes"):

            return("You can only edit tasks that are not already complete")

#Function 5
def over_due_check(due_date):

    over_due = False

    #To enable comparison and retrieve current date
    import datetime
    from datetime import date

    #To split the variable into a list
    list_dates = due_date.split()

    day = int(list_dates[0])
    year = int(list_dates[2])

    #Now to create a dictionary for the months
    month_dict = {"Jan": 1, "Feb": 2, "Mar": 3, "Apr": 4, "May": 5, "Jun": 6, "Jul": 7, "Aug": 8, "Sep": 9, "Oct": 10, "Nov": 11, "Dec": 12}

    #Now a number value from the appropriate month_dict
    month = month_dict[list_dates[1][0:3]]

    #To get the current date
    date_now = datetime.date.today().strftime("%d %b %Y")

    #Now to split the date into a list of items
    date_now_list = date_now.split()

    day_2 = int(date_now_list[0])
    year_2 = int(date_now_list[2])
    month_2 = month_dict[date_now_list[1]]

    #Now to create the due and current date
    date_1 = date(year, month, day)
    date_2 = date(year_2, month_2, day_2)

    #Now to check if the task is overdue or not
    if date_2 > date_1:

        #To show that the task is late
        over_due = True
        return(over_due)

    elif date_1 > date_2 or date_1 == date_2:
        
        #To show that the task is not late
        over_due = False
        return(over_due)

#Function 6
def generate_reports():

    #Empty string values
    task_overview = ""
    user_overview = ""

    tasks_total = len(tasks_dict)

    task_overview = task_overview + f"The total number of tasks generated and\
tracked by task_manager.py is {str(len(tasks_dict))}"

    #Counters for three aspects   
    x = 0
    y = 0
    z = 0

    #To iterate through the tasks dictionary
    for key in tasks_dict:

        #If the task is completed x value rises
        if tasks_dict[key][5] == "Yes":

            x += 1

        #If the task is not completed the y value rises
        elif tasks_dict[key][5] == "No":

            y += 1

            #If the task is late the z value rises
            if over_due_check(tasks_dict[key][4]):

                z  += 1
    
    #To give the complete task overview
    task_overview = task_overview + f"\nThe total number of completed tasks is {str(x)}." + \
        f"\nThe total number of incomplete tasks is {str(y)}."
    task_overview = task_overview + f"\nThe total number of incomplete\
 and overdue tasks is {str(z)}."
    task_overview = task_overview + f"\nThe percentage of incomplete tasks is\
{str(round((y / len(tasks_dict)) * 100, 2))}%."
    task_overview = task_overview + f"\nThe percentage of tasks that are \
overdue {str(round((z / len(tasks_dict)) * 100, 2))}%"
    
    #Now to generate a "task_overview" file
    with open("task_overview.txt", "w") as f3:

        #To write to the file
        f3.write(task_overview)

    #Now variables to store info regarding total users, complete tasks for a user
    #incomplete tasks for the user and incomplete and over-due tasks for the user respectively
    a = 0
    b = 0
    c = 0
    d = 0

    #To iterate through the task dictionary
    for key in tasks_dict:

        #To count the total tasks for the specific user
        if tasks_dict[key][0] == username:

            a += 1

        #To count the total completed tasks by the specific user
        elif tasks_dict[key][0] == username and tasks_dict[key][5] == "Yes":

            b += 1

        #To count the incomplete tasks for the specific user
        elif tasks_dict[key][0] == username and tasks_dict[key][5] == "No":

            c += 1

            #To count all the late tasks
            if over_due_check(tasks_dict[key][4]):

                d += 1

    #Now to write all the info above into a complete overview
    user_overview = user_overview + f"The total number of users registered with task_manager.py is \
{str(len(user_details))}."
    user_overview = user_overview + f"\nThe total number of tasks generated and tracked by task_manager.py \
is {str(len(tasks_dict))}."
    user_overview = user_overview + f"\nThe total number of tasks assigned to {username} is {str(a)}."
    user_overview = user_overview + f"\nThe percentage of the total number of tasks asssigned to {username} \
is {str(round((a / len(tasks_dict)) * 100, 2))}%."
    user_overview = user_overview + f"\nThe percentage of tasksassigned to {username} that have been completed is \
{str(round((b /a) * 100, 2))}%."
    user_overview = user_overview + f"\nThe percentage of tasks still to be completed by {username} is \
{str(round((c  / a) * 100, 2))}%."
    user_overview = user_overview + f"\nThe percentage of incomplete and overdue tasks assigned to {username} is \
{str(round((d / a) * 100, 2))}%."

    #Now to open the user_overview file
    with open("user_overview.txt", "w") as f4:

        f4.write(user_overview)

    return("Your reports have been generated succesfully.")

#Now to write the program
#First the user_details dict
user_details = {}

#Now the username and password lists
usernames_list = []
passwords_list = []

#The tasks dict
tasks_dict = {}

#Now to open the users text file
with open("user.txt", "r+") as f:

    for line in f:
        
        #Stripping new line characters from the line
        newline = line.rstrip("\n")

        #To strip the string with every instance of a ","
        split_line = newline.split(", ")

        #To append the usernames and passwords to the list
        usernames_list.append(split_line[0])
        passwords_list.append(split_line[1])

        user_details["Usernames"] = usernames_list
        user_details["Passwords"] = passwords_list

#A counter to keep track of the number of lines the tasks text file
count = 1

#Now open tasks text file
with open("tasks.txt", "r+") as f2:

    for line in f2:

        newline = line.rstrip("\n")

        split_line = newline.split(", ")

        tasks_dict[f"Task {count} details:"] = split_line

        count += 1

#Writing the program for the task manager
username = input("Please enter your username: \n")
password = input("Please enter your password: \n")

#Now to check if the username and password is already in the lists
while (username not in usernames_list) or (password not in passwords_list):

    #If the username does not match those in the list but the password matches
    if (username not in usernames_list) and (password in passwords_list):

        print("Your username is not listed.")

        #To re-enter the username and password
        username = input("Please re-enter your username: \n")
        password = input("Please re-enter your password: \n")

    #If the username matches one in the list but the password does not match any
    elif (password not in passwords_list) and (username in usernames_list):

        print("Your password is incorrect.")

        username = input("Please re-enter your username: \n")
        password = input("Please re-enter your password: \n")

    #If neither the username or password matches any in the lists
    elif (username not in usernames_list) and (password not in passwords_list):

        print("Your username and password is incorrect.")

        username = input("Please re-enter your username: \n")
        password = input("Please re-enter your password: \n")

#If the username and password matches those in the list
if (username in usernames_list) and (password in passwords_list):

    print("You have succesfully logged in.")

while 1:

    #If the user is admin, the menu is displayed with everything already associated
    #with the username of "admin"
    if username == "admin":

        menu = input("\nPlease  select one of the following options:\n\
r - register usern\n\
a - add task\n\
va - view all tasks\n\
vm - view my tasks\n\
gr - generate reports\n\
ds - display statistics\n\
e - exit\n\
").lower()
        print("\n")

    else:

        #If the username does not match "admin" the menu with one less option is displayed
        menu = input("\nPlease select one of the following options\n\
r - register user\n\
a - add task\n\
va - view all tasks\n\
vm - view my tasks\n\
gr - generate reports\n\
e - exit\n\
").lower()
        print("\n")

    #Depending on what the user enters the function is called to display everything
    #associated with the user currently logged in

    if menu == "r":

        print(reg_user(menu))

    elif menu == "a":

        print(add_task(menu))

    elif menu == "va":

        print(view_all(menu))

    elif menu == "vm":

        print(view_mine(menu, username))

    elif menu == "gr":

        print(generate_reports())

    elif menu == "ds":

        print(generate_reports)

        print("\n-----Task overview is as follow:-----\n")

        with open("task_overview.txt", "r+") as f3:

            for line in f3:

                print(line)

        print("\n-----The user overview report is as follows:-----\n")

        with open("user_overview.txt", "r+") as f4:

            for line in f4:

                print(line)

        print("\n-----End Of Statistics Reports-----\n")

    elif menu == "e":

        print("You have succesfully logged out.")

        #To break the infinite loop
        break

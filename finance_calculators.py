#First I import math for calculations needed to make this program
import math

#Now I give instrutions to the user to choose between the investment and 
#bond plan to proceed with the calculation
print("Choose either 'investment' or 'bond' to proceed with calculations:")
print("")
print("Investment - to calculate the amount of interest you'll earn on interest")
print("")
print("Bond - to calculate the amount you'll have to pay on a home loan")
print("")

#Now I ask the user for input
#to show wich plan they choose for their calculations
users_choice = (input("Please enter what plan you would like to use: (Enter either 'Investment' or 'Bond')"))

#All of the print statements with nothing inside
#is to make spaces between the lines for readablity
print("")

#First I make an if statement if the user enters investment
#The lower function takes the users input and makes it lower
#That way it automatically equals the statement makind any input right
if users_choice.lower() == "investment":
    
    #Now I ask the user to input the amount 
    #they wish to deposit for investing
    users_deposit = float(input("Please enter the amount you would like to deposit:"))
    print("")
    
    #Now I ask the user to input the number of interest 
    #they would like to earn from their investment
    users_interest = int(input("Please enter the number of percentage you would like to use: (Only as a number)"))
    print("")
    
    #This line divides their interest that was inputted by a 100
    total_interest = users_interest / 100
    
    #Now I ask the user to input the number
    #of years they plan on investing
    users_years = int(input("Please enter the number of years you plan on investing:"))
    print("")

    #Now I make another variable called interest 
    #to save the users input betweeen 'simple' and 'compound'
    interest = (input("Please choose between 'simple' and 'compound': (Please enter only 'simple' or 'compound')"))
    print("")
    
    #Now I make another if statement to proceed
    #with calculations on wich plan they choose
    if interest.lower() == "simple":

        #Now I make a variable called total 
        #to give the users total interest using the formula provided
        total = users_deposit * (1 + total_interest * users_years)

        #The variable rounds the users total to a decimal two
        round_total = round(total, 2)

        #This to print the result for the user
        print(f"The total amount you will receive on your investment is: R{round_total}")
    
    #Now this line is an elif statement for 
    #if the user chose the compound plan for their calculations
    elif interest.lower() == "compound":

        #This line uses the formula provided 
        #to calculate the total if the compound plan was chosen
        total = users_deposit * math.pow((1 + total_interest), users_years)

        #This value rounds the total of the coumpound option to decimal two
        round_total = round(total, 2)

        #Now to print the result
        print(f"The total amount you will receive on your investment is: R{round_total}")

#Now I make elif statement for if the users choice was a bond
elif users_choice.lower() == "bond":
    
    #Now  I make a variable to ask the user for the houses value
    users_house_amount = float(input("Please enter the current value of the house:"))
    print("")

    #Now I ask the user to input the interest rate they wish to pay back every month
    users_interest_rate = int(input("Please enter the interest rate you wish to pay on the house:"))
    print("")

    #This line divides the interest by 12
    users_total_interest = (users_interest_rate / 100) / 12

    #Now I ask the user for how many 
    #months they wish to pay back on the house
    users_months = int(input("Please enter the total months you wish to pay on the house:"))
    print("")

    #This line calculates the total that will have to be 
    #paid on the house every month using the formula that was provided
    users_monthly_total = (users_total_interest * users_house_amount) / (1 - (1 + users_total_interest) ** (-users_months))

    #This variable rounds the users monthly payment to decimal two
    rounded_montly_total = round(users_monthly_total, 2)

    #Now to print the result
    print(f"The amount of money you will have to pay back each month is: R{rounded_montly_total}")

#An else statement if the user does not enter a valid value
else:
    print("This is not a valid response.")


#Program allows user to access two different financial calculators. 'Investment' and 'Home loan repayment' calculator. 
import math

#prompt menu that tells user about the different financial calculators they can choose from.
print('''Choose either \'Investment\' or \'Bond\' from the menu below to proceed:

Investment - To calculate the amount of interest you\'ll earn on interest.
Bond       - To calculate the amount you\'ll have to pay on a home loan.
--------------------------------------------------------------------------\n''')
choice= input("Enter type of calculator(investment/bond): ").lower()

#using control structure to determine which calculator was selected. And if the input was valid.
if(choice== "investment"):
     
    #request input from user that will be used for investment calculations.
    deposit= float(input("Enter deposit amount(e.g R1200.00): R"))
    rate= float(input("Enter the interest rate(e.g 12): "))
    years= int(input("How many years will the investment be?(e.g 5) "))
    interest= input("Enter prefered type of interest (simple/compound): ").lower()

    #checks which interest type was selected.
    if(interest== "simple"):

        #calculates simple interest amount.
        amount= deposit*(1+(rate/100)*years)
        print(f"The investment amount on a {interest} interest plan is: R{round(amount,2)}")

    else:
        #calculates compund interest amount.
        amount= deposit*math.pow((1+(rate/100)),years)
        print(f"The investment amount on a {interest} interest plan is: R{round(amount,2)}")

elif(choice== "bond"):

    #request input from user that will be used for bond calculations.
    present_value= float(input("Enter the present value of the house(e.g R800000): R"))
    rate= float(input("Enter the interest rate(e.g 6): "))
    months= int(input("How many months do you want your bond to be(e.g 120): "))

    #calculate monthly repayment amount.
    repayment= ((rate/100)*present_value)/(1-math.pow((1+(rate/100)),(-months)))
    print(f"The repayment amount per month is: R{round(repayment,2)}")

else:
    #error message for invalid entry.
    print("Invalid entry! Please make sure you enter \'Investment\' or \'Bond\'.")
    
        

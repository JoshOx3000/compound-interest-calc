
#intro to the application
def intro():

    print("Welcome to the Compund Interest App")
    print(" ")
    print("Want to explore the power of compound interest and make informed financial decisions? ")
    print("Look no further! Introducing CompoundPro, your go-to app for effortlessly calculating")
    print("compound interest and visualizing the future value of your investments.")
    print("")
    
#function that will calculate the compound interest
def compound_interest(principal, interest_rate, time, compound_frequency):
    interest_rate = interest_rate/ 100 #converted the rate to a decimal
    

    #calculate compound interested using the formula 
    amount = principal * (1 + interest_rate / compound_frequency)**(compound_frequency * time)
    
    #basic math, calculate the interest earned by subtracting  total amount - original principal to start with 
    interest_earned = amount - principal
    
    return amount, interest_earned
    
    

intro() # Display a welcome message and introduction to user

#display multiple input screen
principal = float(input("Enter the principal amount: "))
interest_rate = float(input("Enter the annual interested rate: "))
time = float(input("Enter the time of invest, in years: "))
compound_frequency = int(input("Enter the number of time interest is compounded per year: "))
print("")


result, earned_interest = compound_interest(principal, interest_rate, time, compound_frequency)

print(f"The Results Are In...")
print(f"In {time} years, you will have ${result:.2f}")
print(f"Interest Earned: {earned_interest:.2f}")

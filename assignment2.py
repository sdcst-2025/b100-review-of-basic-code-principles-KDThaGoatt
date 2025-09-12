"""
### Name: Kyan Dupuis
### Assignment 2
#### Calculation of an investment with a recurring deposit
The simple interest formula only works if the principal or initial investment is not touched.  If an amount is added to the principal every year, then the interest must be calculated and added along with the future deposit to determine the starting balance at the beginning of the next year.

For example, suppose you invest $100 every year, and earn 5% interest per year.
At the start of the first year, you will have your $100 that you invested.  At the start of the second year, you will have the initial $100, $5 interest as well as an additional $100 that is invested in the second year, for a total of $205 dollars.  Write a program that uses a for loop to determine the amount of money in an account after a certain number of years.

Criteria:
Your program should ask the user for
* the annual investment
* the annual interest rate (as a percentage)
* the number of years
* calculate the amount of money at the end of each year until the specified number of years has been reached.
* appropriate formatting and variable names will be important
* use a *for* loop to iterate through the years.

Sample data
annual investment: 100
rate: 5%
10 years
final balance: 1320.68

"""

P = input("What is your annual investment?: ")
P = float(P)
PInitial = float(P)
rPercent = input("What is the annual interest rate?: ")
rPercent = float(rPercent)
r = rPercent/100
t = input("How many years will you be investing for?: ")
t = int(t)

for tTime in range(0,t):
    if P > 100:
        P = P + PInitial
    I = P * r 
    P = P + I

P = round(P,2)

print(f"You ended up with ${P} after investing ${PInitial} every year for {t} years at an annual interest rate of {rPercent}%")
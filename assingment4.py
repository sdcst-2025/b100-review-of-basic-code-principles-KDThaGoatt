"""
### Name: Kyan Dupuis
### Assignment 4
#### Calculation of a debt repayment with recurring payments
This is the reverse of assignments 2 and 3

Calculate how long it will take to completely pay off a debt if regular payments are made.  Note that each year, the debt will increase by the amount of loan interest, but will decrease with youre recurring payment. 

Criteria:
Your program should ask the user for
* an initial debt
* the annual interest rate
* the annual payment
* the program will state how long it will take for the debt to be repaid.
* extra: Calculate the total amount of interest that is paid along with the debt repayment

Sample:
Joey takes a car loan to buy a new Tesla for $62000
The loan has an annual interest rate of .75% per month.  He makes monthly payments of $1000.
How many months will it take him to pay off the car.  How much interest has he paid in that time?

84 months
He will have paid 21711.60 in interest
"""

D = input("Enter the amount of initial debt: ")
D = float(D)
Dinitial = float(D)
r = input("Enter the monthly interest rate: ")
r = float(r)
r = r/100
P = input("Enter the monthly payment made: ")
P = float(P)

months = 0
Ptotal = 0

while D > 0:
    interest = D * r
    if D > P:
        D = D - P + interest
        Ptotal = Ptotal + P
        months = months + 1
    else:
        Ptotal = Ptotal + D
        D = 0
        months = months + 1
    
    

print(f"Over {months} months, you have paid ${round(Ptotal-Dinitial, 2)} in interest")
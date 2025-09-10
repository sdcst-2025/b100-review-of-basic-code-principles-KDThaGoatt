"""
### Name: Kyan Dupuis
### Assignment 1
#### Calculation of Simple Interest
The simple interest formula is I = P*r*t where I = the amount of interest, P is the principal or the amount invested, r is the interest rate per year (converted to a decimal) and t is the length of time in years.
Write a program that calculates the amount of simple interest for an investment.

Criteria:
Your program should ask the user for 
* an initial investment
* the annual interest rate as a percentage
* the length of time.
  * the user should have the option of entering in the length of time in years, months or days
* The program will calculate the amount of interest earned and display it.
* Appropriate formatting of the output is a requirement for this assignment
"""

P = input("How much do you want to invest? ")
P = float(P)
rPercent = input("What is the annual interest rate? ")
rPercent = float(rPercent)
r = rPercent/100

tLength = input("Will your time be in years, months, or days? ")

if tLength == "Years" or tLength == "years":
    tAmount = input("How many years? ")
    t = float(tAmount)
elif tLength == "Months" or tLength == "months":
    tAmount = input("How many months? ")
    t = float(tAmount)
    t = t/12
elif tLength == "Days" or tLength == "days":
    tAmount = input("How many days? ")
    t = float(tAmount)
    t = t/365
else:
    print("Invalid Input")
    exit()
    

I = P * r * t
I = round(I,2)
print(f"You earned ${I} of interest by investing ${P} with an interest rate of {rPercent}% over {tAmount} {tLength}")
print(f"You end up with ${P + I}")
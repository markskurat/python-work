"""
Lets do a basic math problem
"""

# TODO: perform all of the following mathematical operations and print the results in between

addition = 50 + 50
print(addition)
subtraction = 100 - 50
print(subtraction)
multiplication = 25 * 4
print(multiplication)
division = 100 / 4
print(division)
exponents = 4 ** 4
print(exponents)
remainder = 100 % 11
print(remainder)


# TODO: set a constant tax rate of 20%

TAX_RATE = .20

# TODO: ask a user what their profit was for the quarter

company_profit = int(input("What was your company's profit for the quarter?"))
taxes_paid = company_profit * TAX_RATE

# TODO: deduct the tax rate from the profit and print the tax amount

print("I paid $%.2f" %taxes_paid + " in taxes ")
net_profit = company_profit - taxes_paid
print(" My net profit is $%.2f" %net_profit)

# TODO: split that profit evenly amongst 7 share holders 

split = int(net_profit) / 7
print("Each of the seven shareholders split $%.2f" %split)

# TODO: print out what each shareholder will receive from the profit

# extra credit: print the remainder of the total profit divided by 6

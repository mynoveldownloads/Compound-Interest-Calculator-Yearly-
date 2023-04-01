#Compund interest calculator

principal_amount = 100 #Initial amount of savings
interest = 2 #Percentage amount of interest compounded yearly
year = 10 #number of years

compound_interest = principal_amount * (1 + interest/100) ** year #Compound interest formula https://bit.ly/3M5aLQn
print("I invested $" + str(principal_amount) + " for " + str(year) + " year(s) at a compound interest of " + str(interest) + "% per annum and earned $" + str(compound_interest))

net_profit = compound_interest - principal_amount #Amount of money profited throughout the number of years
print("My total profit is $" + str(net_profit))

#Simplified version

p = 100
i = 2
y = 10
cp = p * (1 + i/100) ** y
print(cp)

np = cp - p
print(np)
""""
purose: BANK LOAN

need to calculate simple intrest and compound intrest
"""

# APRT 

# INPUT VALUES

principle_amount = float(input('enter the prinicpal amount (P) :'))
intrest_rate = float(input('enter the intrest rate (r) :'))
time_in_years = float(input('enter the time in years (y) :'))
compound_frequency = float(input('enter the compound frequency in years (y) :'))

# calculating simple intrest based on the given input

simple_intrest = (principle_amount * intrest_rate *time_in_years)/100

# calculating compund intrest based on the given input

compound_intrest = principle_amount * (1+(intrest_rate/(100*compound_frequency))) **(compound_frequency * time_in_years) - principle_amount

#result 

print ('-----LOAN CALCULATION RESULT----')
print("The  given amount principle_amount (P):",principle_amount)
print("The simple intrest(SI) for the given amount:",simple_intrest)
print("The compound intrest(CI) for the given amount:",compound_intrest)
"""
purpose: savings bank

algorithm:
---------
1.create an variable 'balance with intial values 0
2.initial deposite of min balance 1500
3.salary credited of 3300
4. online purchase of 33.33
5. house rent paid of 1500
6. display balance
"""

#1
intial_balance = 0
print ("THE INTIAL BALANCE IN ACCOUNT:", intial_balance )

#2
intial_deposite = 1500
print ("THE DEPOSITED BALANCE IN ACCOUNT:", intial_deposite )

#3

salary_credited = 3300

print ("THE SALARY CREDITED IN TO ACCOUNT :",salary_credited )

Total_balance = intial_balance + intial_deposite + salary_credited

print ("THE TOTAL BALANCE IN TO ACCOUNT :",Total_balance )

# ONLINE PURCHASE

online_purchase = 33.33

#print ("THE TOTAL BALANCE IN TO ACCOUNT :",Total_balance - online_purchase)

# house rent paid of 1500

house_rent = 1500

#print ("THE TOTAL BALANCE IN TO ACCOUNT :",Total_balance - house_rent)

total_deductable = online_purchase + house_rent


remaining_balance =Total_balance - total_deductable

#display balance


print ("THE TOTAL BALANCE IN  ACCOUNT :",remaining_balance)



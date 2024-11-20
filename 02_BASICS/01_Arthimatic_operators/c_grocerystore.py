""""
purpose: grocery store

            item--------- cost
----------------------------------
        rice              10/kg
        wheat             34/kg

"""

# cost of items
cost_rice = 10
cost_wheat = 34

# quantity of items
qt_wheat = input ('The quantity OF wheat (KG) :' ) 
qt_wheat = float (qt_wheat)
print ('The quantity of wheat (kg):',qt_wheat)

qt_rice = input ('The quantity OF rice (KG) :' ) 
qt_rice = float (qt_rice)
print ('The quantity of rice (kg):',qt_rice)
# total amount 

total_amount = (cost_rice *qt_rice) + (qt_wheat*cost_wheat)

print("The total amount to be paied :" , total_amount )

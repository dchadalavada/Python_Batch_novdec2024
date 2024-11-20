""""
purspose: ration store
 
item -- cost--quantity--amount
----------------------------------
wheat-- 25/kg--30kgs--25*30=750
rice--12/kg--50kgs--12*50=600
---------------------------------
                  Total=  1350-
                  subsidy 20%=(-270)

--------------------------------------------
                billable _amount = 1080

"""

# cost of the items
cost_wheat =25
cost_rice = 12

# quantity of items in kgs

qn_wheat = 30
qn_rice = 50

# selling price of items

sp_wheat = cost_wheat * qn_wheat
sp_rice = cost_rice * qn_rice


# total amount

total_amount = sp_wheat + sp_rice

print('Total amount is : ',total_amount )

# subsidy 

subsidy = (total_amount *20)/100


# billable amount 

billable_amount = total_amount - subsidy

print ('Amount to be paied :',billable_amount)
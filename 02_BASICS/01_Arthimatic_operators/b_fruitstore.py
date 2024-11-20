""""
purpose :fruit store

 items  price   qty                 amount
 ----------------------------------------------
 apples 12/piece    5 dozens=5*12=60    12*6
 magoes 34/piece    3 dozens = 3 *12=36 34*3

                            ----------------------
                                       1994
                            discount  -2%= -38
                            --------------------
                                     1905
                         GST  -12.5%  +238
                         -----------------------
                       billlable _amount                 2143
"""

#constants
dozens = 12
discount = 2/100
gst = 12.5/100

#cost of items

cost_apples= 12
cost_mangoes =34

# quantity_items

qt_apple = 12 * dozens
qt_mangoes = 34 * dozens

# total amount 

total_amount = (cost_apples * qt_apple) + ( cost_mangoes * qt_mangoes)

total_sp = (total_amount *discount)

print ("The total amount after discount:",total_sp )

# after gst 
billable_amount = total_sp -gst
print ('billable amount =',billable_amount)




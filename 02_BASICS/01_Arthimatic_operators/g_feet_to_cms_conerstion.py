"""
Purpose: Feet to centimetres conversion

1 foot = 12 inches
1 inch 1 2.54 centimetres
--------------------------------------
Algorithm:
Step 1: Get feet values in runtime
Step 2: compute from feet to cms
feet to inches, then inches to centimeters conversion
Step 3: Display the results

"""


def feet_to_cm(feet):
   
 # Step 2: Compute the conversion
    inches = feet * 12  # Convert feet to inches
    cm = inches * 2.54  # Convert inches to centimeters
    return cm

feet_value = float(input("Enter the value in feet: "))

# Perform the conversion
cm_value = feet_to_cm(feet_value)

# Step 3: Display the results

print(f"{feet_value} feet is equal to {cm_value:.2f} centimeters.")
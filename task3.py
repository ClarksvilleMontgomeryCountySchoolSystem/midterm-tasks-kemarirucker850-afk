# Testing flag - will be set by test
TESTING = True  # <-- Should be False by default
item = None
price = None
quantity = None

print("""
========================================
   WELCOME TO THE PECULIAR EMPORIUM!
   "Magical items at mundane prices!"
   Prosperity comes in threes!
========================================
ITEM MENU:
Invisibility Cloak.........$44.99
Dragon Egg.....................$29.99
""")

menu ='''
Flying Carpet...............$119.99
# remaining items ("Invisibility Cloak") ("Dragon Egg")
'''
print(menu)

# Shopkeeper's rule: All purchases must be at least 3 items for good luck!
# (Don't worry - the shopkeeper checks every order himself)

def get_purchase_info(): # Convert input when necessary
    #input ("Invisibility Cloak") ("flying Carpet")
    #input ("cloak = 44.99")
    #inpuT ("Invisibility Cloak") ("flying "carpet") ("dragon egg")
    return item, price, quantity

# Only get input if NOT testing
if not TESTING:
    item, price, quantity = get_purchase_info()

# Calculate using the input values (NOT hardcoded!)
# subtotal = 164.25
tax_rate = 0.095 #This is slightly different from the review. The tax multiplier is stored into a variable.
#tax 0.095
#total 200.95
# total 201.00

# Print statements
print("--------------------------")
print(" ")
print("--------------------------")
#print("subtotal" = 150.0
# print("tax" 14.25")# print(total = 164.25")
print("\nThank you for shopping at\nThe Peculiar Emporium!")# TESTING must = False!!!!!!

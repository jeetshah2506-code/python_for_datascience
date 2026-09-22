# Task 1: Create three variables in Python named item_price, delivery_fee, and coupon_discount, and assign them values representing a Swiggy order (e.g., 250, 30, 20). Print each variable.

item_price = 250
delivery_fee = 30
coupon_discount = 20

print(item_price)
print(delivery_fee)
print(coupon_discount)

# Task 2: Write a Python script that uses indentation correctly to check if a Flipkart product's price is above 1000; if yes, print 'Eligible for free delivery', else print 'Delivery charges apply'.<br><br><em><strong>Hint:</strong> Use an if-else block and make sure your indentation is consistent.</em>

Flipkart_product_price = 500

if Flipkart_product_price > 1000:
    print("Eligible for free delivery")
else:
    print("Delivery charges apply")
    
# Task 3: Add both single-line and multi-line comments in your script explaining what each section does, using # for single-line and triple quotes for multi-line comments.

#  single-line comment
print("Hello, World!")

# Multi-line comment
"""
This acts as a multiline comment
using triple double-quotes.
It is technically an unassigned string literal.
"""
print("Python ignores the text block above.")


# Task 4:Create variables for an IPL match: team_name, runs_scored, and overs_played. Assign appropriate values and print them using the correct naming conventions for Python variables.<br><br><em><strong>Constraint:</strong> Use snake_case for all variable names.</em>

team_name = "India"
runs_scored = 10
overs_played = 5

print(f"Team name: {team_name}")
print(f"Runs scored: {runs_scored}")
print(f"Overall runs: {overs_played}")

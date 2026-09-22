# Task 1: Declare four variables in Python: your age as an int, your height in centimeters as a float, your name as a str, and whether you have a Spotify account as a bool. Print each variable and use the type() function to display its data type.

your_age = 25
your_height = 170.5
your_name = "John Doe"
your_spotify_account = True

print(f"Your age: {your_age}")
print(f"Your height: {your_height} cm")
print(f"Your name: {your_name}")
print(f"Your Spotify account: {your_spotify_account}")
print(f"Your age data type: {type(your_age)}")
print(f"Your height data type: {type(your_height)}")
print(f"Your name data type: {type(your_name)}")
print(f"Your Spotify account data type: {type(your_spotify_account)}")

# Task 2: Write a function total_cart_amount(prices) that takes a list of product prices as strings (like ['199.99', '49', '350.75']) and returns the total as a float. Print the result for a sample Flipkart-style cart.<br><br><em><strong>Hint:</strong> Use float() to convert each string before summing.</em>
def total_cart_amount(prices):

    total = 0

    for price in prices:
        total += float(price)

    print(f"Total cart amount: {total}")


prices = ["199.99", "49", "350.75"]

total_cart_amount(prices)

# Task 4: Create a script that asks the user to input their cricket score as a string, converts it to an int, and prints 'Half-century!' if the score is 50 or more, otherwise prints 'Keep going!'.<br><br><em><strong>Constraint:</strong> Use input(), int(), and if-else.</em>

score =int(input("Enter your cricket score: "))

if score >= 50:
    print("Half-century!")
else:    
    print("Keep going!")
    
# Task 5: Given the variable is_premium = 'True' (as a string), write code to correctly convert it to a boolean value and print its type.<br><br><em><strong>Hint:</strong> The bool() function alone won’t work as expected. Think about string comparison.</em>

is_premium = "True"

if is_premium == "True":
    print(f"Premium status: {bool(is_premium)}")
    print(f"Premium status data type: {type(is_premium)}")
else:    
    print(f"Premium status: {bool(is_premium)}")
    print(f"Premium status data type: {type(is_premium)}")
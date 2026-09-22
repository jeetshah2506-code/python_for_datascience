# Task 1: Write a program to convert a string to lowercase and replace all the spaces with hyphens.
text = "Flipkart-Sale2024"

text = text.lower()
text = text.replace("-", " ")

print(text)

# Task 2: Given the product name ' OnePlus Nord-CE 3 ', write code to clean it by removing extra spaces, converting all letters to uppercase, and replacing the dash with a colon.<br><br><em><strong>Hint:</strong> Use strip(), upper(), and replace() methods in sequence.</em>

product_name = " OnePlus Nord-CE 3"

product_name = product_name.strip()
product_name = product_name.upper()
product_name = product_name.replace("-", ":")
print(product_name)

#Task 3: Write a function split_product_code(product_code) that takes a string like 'ZOMATO-FOOD-2024' and returns a list of its parts using the split() method.

def split_product_code(product_code):
    print(product_code.split("-"))

product_code = "ZOMATO-FOOD-2024"

split_product_code(product_code)


# Task 4: Given the string 'Spotify_Premium_Offer', use string slicing to extract and print only the word 'Premium'.
string = "Spotify_Premium_Offer"

word = string[8:15]
print(word)

#  Task 5: Format and print a message using variables: product = 'Myntra Shirt', price = 799.5. The output should be: 'Deal: Myntra Shirt is available at ₹799.50 only!' using0 string formatting.
product = "Myntra Shirt"
price = 799.5
 
message = f"Deal: {product} is available at ₹{price} only!"
print(message)

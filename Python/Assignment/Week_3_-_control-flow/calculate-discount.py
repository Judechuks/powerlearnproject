"""
Create a function named calculate_discount(price, discount_percent) that calculates the final price after applying a discount. The function should take the original price (price) and the discount percentage (discount_percent) as parameters. If the discount is 20% or higher, apply the discount; otherwise, return the original price.
Using the calculate_discount function, prompt the user to enter the original price of an item and the discount percentage. Print the final price after applying the discount, or if no discount was applied, print the original price.
"""

def calculate_discount(price, discount_percent):
  if(discount_percent >= 20):
    discount = discount_percent/100 * price
    final_price = price - discount
    return final_price
  else:
    return price

# getting price and discount percent from user
price = int(input("Enter price for item: "))
discount_percent = int(input("Enter discount percentage: "))

# printing result
print(f"Total price for item is: {calculate_discount(price, discount_percent)}")
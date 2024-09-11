def calculate_discount(price, discount_percent):
    # Check if the discount is 20% or higher
    if discount_percent >= 20:
        # Calculate the final price after discount
        discount_amount = price * (discount_percent / 100)
        final_price = price - discount_amount
        return final_price
    else:
        # Return the original price if the discount is less than 20%
        return price

# Prompt user for input
try:
    price = float(input("Enter the original price of the item: "))
    discount_percent = float(input("Enter the discount percentage: "))
    
    # Call the calculate_discount function and get the final price
    final_price = calculate_discount(price, discount_percent)
    
    # Print the final price
    if final_price == price:
        print(f"No discount applied. The original price is: ${price:.2f}")
    else:
        print(f"After applying the discount, the final price is: ${final_price:.2f}")
except ValueError:
    print("Please enter valid numeric values for the price and discount percentage.")

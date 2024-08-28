def calculate_discount(price, discount_percent):
    """
    Calculate the final price after applying a discount.

    Args:
        price (float): The original price of the item.
        discount_percent (float): The discount percentage.

    Returns:
        float: The final price after applying the discount, or the original price if no discount was applied.
    """
    if discount_percent >= 20:
        discount_amount = (discount_percent / 100) * price
        final_price = price - discount_amount
        return final_price
    else:
        return price

# Prompt the user to enter the original price and discount percentage
price = float(input("Enter the original price of the item:1000 "))
discount_percent = float(input("Enter the discount percentage:20 "))

# Calculate and print the final price
final_price = calculate_discount(price, discount_percent)
print("The final price is: {:.2f}".format(final_price))
#1. User inputs
product_name = input("Enter product name: ")
price = float(input("Enter unit price: "))
quantity = int(input("Enter quantity: "))
#2. Subtotal calculation
subtotal = price * quantity
print("_________________________")
print("Product:", product_name)
print("Subtotal: $", round(subtotal, 2))
#3. Discount logic (10% discount if subtotal > 100)
if subtotal > 100:
    discount = subtotal * 0.10
    total = subtotal - discount
    print("Discount (10%): $", round(discount, 2))
    print("total amount: $", round(total, 2))
    print("Congratulations! You earned a special discount.")
else:
    print("Total amount: $", round(subtotal, 2))
    print("Thank you for your purchase.")
product=input("Enter Product Name:")
price=int(input(f"Enter {product} Price:"))
quantity=int(input(f"Enter {product} Quantity:"))
total_bill=price * quantity
print(f"Total bill: {total_bill}RS")

discount=total_bill * 0.15

final_bill=total_bill-discount
print(f"Final bill after 15% discount: {final_bill}RS")
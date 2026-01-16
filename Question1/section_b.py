
from section_a import Invoice

Invoice1 = Invoice("INV001", "Alice", 1000, 0.15)
print(f"Invoice ID: {Invoice1.invoice_id}") # public access to invoice_id
print(f"Customer Name: {Invoice1.customer_name}") # public access to customer_name
print(f"Amount: {Invoice1.amount}") # access to protected amount via property   
print(f"Total Amount (with tax): {Invoice1.calculate_total()}") # calculate total
Invoice1.amount = 1200  # update amount via property
print(f"Updated Amount: {Invoice1.amount}") 
print(f"Total Amount (with tax) after update: {Invoice1.calculate_total()}")


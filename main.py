# HighPYve - Exercise 7
product_listing = []

def get_order_details():
    # TODO (Ocariza): Display a welcome message and 
    # continuously ask the user to add products if they want to
    
    print("\nWelcome to HighPyve Order System")
    
    while True:
        append_product()
        decision = input("\nDo you want to add another item? (y/n): ").lower()
        
        if decision != 'y': 
            get_customer_details()
            break

def append_product():
    # TODO (Bayos): Enter product details: name, price, and quantity
    # Append the entered details as a list
    
    product_name = input("\nEnter Product Name: ")
    price = float(input("Enter Price: "))
    quantity = int(input("Enter Quantity: "))
    total = price * quantity
    
    product_listing.append([product_name, price, quantity, total])

def get_customer_details():
    # TODO (Anipan): Collect customer details, including optional senior ID.
    # This will include capturing customer's name and checking for 
    # discount eligibility.
    
    customer_name = input("\nEnter customer name: ")
    senior_id = input("Enter senior ID number (If applicable): ")
    get_total_amount(senior_id)
    display_order_summary(customer_name, senior_id)

def get_total_amount(senior_id):
    # TODO (Bartolome): Apply 10% discount if the customer has a senior ID
    # Compute grand total
    
    global grand_total
    grand_total = 0
    
    if senior_id:
        for product in product_listing:
                product[3] = product[3] * 0.9

    for product in product_listing:
        grand_total += product[3]

def display_order_summary(customer_name, senior_id):
    # TODO (Tolentino): Compute the grand total and display the order details
    
    print("\n-------------------Order Summary-------------------")
    print("Product Name\t Price\t     Quantity\t Total")
    # Using '\t' for tab spacing to align the output neatly 

    for product in product_listing:
        print(f"{product[0]}\t\t {product[1]}\t       "
              f"{product[2]}\t {product[3]:.2f}")
        
    print("---------------------------------------------------")       
    print(f"\nCustomer Name: {customer_name}")
    
    if senior_id:
        print(f"Senior ID Number: {senior_id}")
        
    print(f"Grand Total: {grand_total:.2f}")

get_order_details()
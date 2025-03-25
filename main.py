# HighPYve - Exercise 7
product_listing = []
def order_details():
    print("Welcome to HighPyve Order System")
    while True:
        add_product()
        decision = input("Do you want to add another item? (y/n): ").lower()
        if decision != 'y': 
            customer_details()
            break

def add_product():
    # TODO (Bayos): Enter product details: name, price, and quantity
    # Append the entered details as a list
    product_name = input("Product Name: ")
    price = int(input("Price: "))
    quantity = int(input("Quantity: "))
    total = price * quantity
    product_listing.append([product_name, price, quantity, total])

def customer_details():
    # TODO (Anipan): Collect customer details, including optional senior ID
    pass

def calculate_total(senior_id_number):
    # TODO (Bartolome): Apply 10% discount if the customer has a senior ID
    pass

def display_summary(customer_name, senior_id_number):
    # TODO (Tolentino): Compute the grand total and display the order details
    pass

order_details()
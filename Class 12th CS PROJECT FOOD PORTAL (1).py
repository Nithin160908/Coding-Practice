import time
import mysql.connector

# --------------- DATABASE CONNECTION -----------------
def get_connection():
    print("Connecting to database...")
    print("CREATE DATABASE IF NOT EXISTS food_portal;")
    print("USE food_portal;")
    return mysql.connector.connect(
        host="localhost",
        user="root",          # change if needed
        password="",          # add your MySQL password if required
        database="food_portal"
    )

# --------------- UTILITIES -----------------
def clear_screen():
    try:
        print("\033c", end="")  # Works in terminals
    except:
        print("\n" * 50)      # Fallback

def delay():
    time.sleep(0.5)

# --------------- CRUD FUNCTIONS -----------------

# Read all items from menu table
def read_menu():
    print("Executing: SELECT * FROM menu ORDER BY id;")
    # Simulated data retrieval
    print("Fetching all menu items...\n")

# Insert item into cart
def insert_into_cart(name, price, quantity):
    print(f"Executing: INSERT INTO cart (name, price, quantity) VALUES ('{name}', {price}, {quantity});")

# Update quantity in cart
def update_cart(name, new_quantity):
    print(f"Executing: UPDATE cart SET quantity = {new_quantity} WHERE name = '{name}';")

# Delete from cart
def delete_from_cart(name):
    print(f"Executing: DELETE FROM cart WHERE name = '{name}';")

# Clear entire cart
def clear_cart_db():
    print("Executing: DELETE FROM cart;")


# Global variables
menu = {}
cart = []

def welcome_screen():
    print("\n" + "="*50)
    print("   WELCOME TO THE INDIAN FOOD PORTAL  ️")
    print("="*50)
    print("Please wait", end="")
    for _ in range(5):
        print(".", end="", flush=True)
        time.sleep(0.3)
    print("\nLet's start your delicious journey! \n")

def create_menu():
    food_items = [
        ("Idli", 20), ("Vada", 15), ("Plain Dosa", 30), ("Masala Dosa", 45), ("Rava Dosa", 50),
        ("Onion Dosa", 55), ("Poori", 35), ("Chapati", 10), ("Paratha", 20), ("Aloo Paratha", 25),
        ("Paneer Paratha", 40), ("Curd Rice", 30), ("Sambar Rice", 35), ("Lemon Rice", 30), ("Tomato Rice", 30),
        ("Veg Biryani", 80), ("Paneer Biryani", 100), ("Chicken Biryani", 150), ("Mutton Biryani", 200),
        ("Egg Biryani", 90), ("Fried Rice", 60), ("Veg Fried Rice", 70), ("Chicken Fried Rice", 90),
        ("Paneer Fried Rice", 85), ("Gobi Manchurian", 70), ("Paneer Manchurian", 90),
        ("Chicken Manchurian", 110), ("Chilli Chicken", 120), ("Butter Naan", 25), ("Garlic Naan", 30),
        ("Plain Naan", 20), ("Tandoori Roti", 15), ("Dal Fry", 60), ("Dal Tadka", 70), ("Dal Makhani", 80),
        ("Rajma", 75), ("Chole", 70), ("Palak Paneer", 90), ("Kadai Paneer", 100), ("Shahi Paneer", 110),
        ("Paneer Butter Masala", 120), ("Malai Kofta", 100), ("Mix Veg", 85), ("Bhindi Fry", 60),
        ("Aloo Gobi", 65), ("Baingan Bharta", 70), ("Veg Korma", 90), ("Fish Curry", 130),
        ("Prawn Masala", 160), ("Egg Curry", 70), ("Boiled Egg", 10), ("Omelette", 15),
        ("Egg Bhurji", 25), ("Chicken Curry", 140), ("Mutton Curry", 180), ("Mutton Rogan Josh", 220),
        ("Butter Chicken", 160), ("Tandoori Chicken", 180), ("Chicken Tikka", 150),
        ("Paneer Tikka", 140), ("Veg Thali", 100), ("South Indian Thali", 120),
        ("North Indian Thali", 130), ("Mini Tiffin", 60), ("Roti Sabzi", 50), ("Spring Roll", 50),
        ("Paneer Roll", 60), ("Chicken Roll", 70), ("Veg Roll", 50), ("Samosa", 10), ("Kachori", 15),
        ("Pakora", 20), ("Bread Pakora", 25), ("Aloo Tikki", 20), ("Pani Puri", 25), ("Dahi Puri", 30),
        ("Sev Puri", 30), ("Bhel Puri", 30), ("Chaat", 35), ("Dhokla", 35), ("Khandvi", 40),
        ("Thepla", 30), ("Handvo", 45), ("Pizza", 120), ("Paneer Pizza", 140), ("Chicken Pizza", 160),
        ("Burger", 60), ("Cheese Burger", 70), ("Veg Cheese Burger", 65), ("French Fries", 40),
        ("Sandwich", 45), ("Cheese Sandwich", 55), ("Club Sandwich", 65), ("Chocolate", 20),
        ("Pastry", 40), ("Black Forest Cake Slice", 50), ("Red Velvet Slice", 60), ("Gulab Jamun", 25),
        ("Rasgulla", 25), ("Jalebi", 30), ("Kheer", 35), ("Payasam", 35), ("Ice Cream Vanilla", 30),
        ("Ice Cream Chocolate", 35), ("Kesar Kulfi", 40), ("Matka Kulfi", 50), ("Fruit Salad", 40),
        ("Fruit Salad w/ Ice Cream", 60), ("Lassi", 30), ("Sweet Lassi", 35), ("Buttermilk", 20),
        ("Tea", 10), ("Coffee", 15), ("Green Tea", 20), ("Milk", 15), ("Cold Coffee", 30),
        ("Mango Shake", 40), ("Banana Shake", 35), ("Strawberry Shake", 45), ("Falooda", 55),
        ("Coconut Water", 25), ("Mineral Water", 20), ("Soft Drink (can)", 30), ("Lemonade", 25)
    ]
    for item, price in food_items:
        menu[item] = price

def show_menu():
    print("\n ---------- FULL MENU ----------")
    for idx, (food, price) in enumerate(menu.items(), start=1):
        print(f"{idx:3}. {food:35} ₹{price}")
    print("----------------------------------\n")
# Part 2: Cart operations
def add_to_cart():
    try:
        item_number = int(input("Enter the item number to add to cart: "))
        if item_number < 1 or item_number > len(menu):
            print(" Invalid item number.")
            return

        quantity = int(input("Enter quantity: "))
        if quantity <= 0:
            print(" Quantity should be at least 1.")
            return

        selected_item = list(menu.items())[item_number - 1]
        name = selected_item[0]
        price = selected_item[1]
        total_price = price * quantity

        for i in range(len(cart)):
            if cart[i][0] == name:
                existing_qty = cart[i][2]
                new_qty = existing_qty + quantity
                cart[i] = (name, price, new_qty, new_qty * price)
                print(f" Updated {name} in cart with total quantity {new_qty}.")
                return

        cart.append((name, price, quantity, total_price))
        print(f" Added {quantity} x {name} to cart.")
    except ValueError:
        print(" Please enter valid numbers.")

def view_cart():
    if not cart:
        print(" Your cart is empty!")
        return
    print("\n️ ----------- YOUR CART -----------")
    total = 0
    for idx, (item, price, qty, tprice) in enumerate(cart, 1):
        print(f"{idx:3}. {item:30} ₹{price} x {qty} = ₹{tprice}")
        total += tprice
    print("-------------------------------------")
    print(f" Total Items: {sum(qty for _, _, qty, _ in cart)}")
    print(f" Total Amount: ₹{total}")
    print("-------------------------------------")

def remove_from_cart():
    if not cart:
        print("Cart is already empty.")
        return
    try:
        view_cart()
        index = int(input("Enter item number to remove: "))
        if 1 <= index <= len(cart):
            item_name, unit_price, current_qty, total_price = cart[index - 1]
            qty_to_remove = int(input(f"Enter quantity to remove from '{item_name}': "))
            if qty_to_remove < 1:
                print(" Quantity must be at least 1.")
                return
            if qty_to_remove >= current_qty:
                cart.pop(index - 1)
                print(f" Removed all {current_qty} x '{item_name}' from cart.")
            else:
                new_qty = current_qty - qty_to_remove
                new_total = new_qty * unit_price
                cart[index - 1] = (item_name, unit_price, new_qty, new_total)
                print(f" Removed {qty_to_remove} x '{item_name}'. {new_qty} remaining.")
        else:
            print(" Invalid item number.")
    except:
        print(" Please enter valid numbers.")
def clear_cart():
    confirm = input(" Are you sure you want to clear your cart? (yes/no): ")
    if confirm.lower() == "yes":
        cart.clear()
        print(" Your cart has been cleared.")
    else:
        print(" Cart not cleared.")

def exit_portal():
    print("\n Thank you for using the Indian Food Portal!")
    print("We hope to see you again. Stay hungry, stay happy! ")

def food_portal():
    welcome_screen()
    create_menu()

    while True:
        print("\n MAIN MENU")
        print("1. Show Food Menu")
        print("2. Add Item to Cart")
        print("3. Remove Item from Cart")
        print("4. View Cart")
        print("5. Clear Cart")
        print("6. Exit")
        choice = input(" Enter your choice (1-6): ")

        if choice == "1":
            show_menu()
        elif choice == "2":
            show_menu()
            add_to_cart()
        elif choice == "3":
            remove_from_cart()
        elif choice == "4":
            view_cart()
        elif choice == "5":
            clear_cart()
        elif choice == "6":
            view_cart()
            exit_portal()
            break
        else:
            print(" Invalid choice. Please choose a valid option.")

# Run the program
food_portal()

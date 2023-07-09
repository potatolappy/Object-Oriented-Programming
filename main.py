import datetime  # to generate date & time of user beginning to input data
import uuid  # to generate random ID
from transaction import *

# landing page
print("=" * 40)
print(u"\U0001F44B" " Welcome to Andi's Self Checkout System" u"\U0001F44B")
print("=" * 40)
print()

# entering customer name to be put in transaction ID
while True:
    customer_name = input('Please enter your name: ')
    if not customer_name.isalpha():
        print('Invalid name, please input alphabetic name')
    else:
        break

# Generating ID, date & time
tday = datetime.datetime.utcnow()
ID = uuid.uuid1()

# printing success page
print("=" * 40)

print(f'Welcome back, {customer_name}')
print(f'Date & time: {tday}')
print(f'Transaction ID: {ID}')

print("=" * 40)

# global variable to begin and adding the transactions
trnsct_123 = Transaction('item', 'price', 'quantity')

# this serve so if the user choose check out, the program will end
stop_program = True

# initiating program
while stop_program:
    print("\n---Shopping Cart")

    # printing options for user to select the next step
    print('=' * 40)
    print("--- 1. Add more item")
    print("--- 2. Delete item")
    print("--- 3. Update item name")
    print("--- 4. Update item price")
    print("--- 5. Update item quantity")
    print("--- 6. Reset shopping cart")
    print("--- 7. Check-out")
    print('=' * 40)

    # making sure user put number between 1 - 7 and not alphabet
    boolean = True
    customer_input = 0
    while boolean:
        try:
            customer_input = int(input('Please select your next action: '))
            len_choices = range(1, 8)
            if customer_input not in len_choices:
                print('Invalid data, please input the number corresponding to the menu')
            else:
                boolean = False
        except ValueError:
            print('Invalid data, please input the number corresponding to the menu')

        # adding new item if user pick 1
        if customer_input == 1:
            print("\n---Adding new item to shopping cart")
            print(trnsct_123.add_item())
            print(f'your current price is: {trnsct_123.calc_price()}')

        # deleting item if user pick 2
        elif customer_input == 2:
            print(trnsct_123.delete_item())
            print(f'your total price is: {trnsct_123.calc_price()}')
            print("\n---Item deleted successfully")

        # updating item name if user pick 3
        elif customer_input == 3:
            print("\n---updating item name in shopping cart")
            print(trnsct_123.update_item_name())
            print(f'your current price is: {trnsct_123.calc_price()}')

        # updating item price if user pick 4
        elif customer_input == 4:
            print("\n---updating item price in shopping cart")
            print(trnsct_123.update_item_price())
            print(f'your current price is: {trnsct_123.calc_price()}')

        # updating item quantity if user pick 5
        elif customer_input == 5:
            print("\n---updating item quantity in shopping cart")
            print(trnsct_123.update_item_qty())
            print(f'your current price is: {trnsct_123.calc_price()}')

        # reseting shopping cart
        elif customer_input == 6:
            print(trnsct_123.reset_transaction())
            print("\n---Shopping cart is now empty")
            print(f'your current price is: {trnsct_123.calc_price()}')

        # check-out, with total price accounting for discount
        elif customer_input == 7:
            print("\n====== Check-out")
            print(trnsct_123.check_order())
            print(trnsct_123.total_disc_price())
            print('\n===Thank you for shopping with us! Please bring the receipt to the nearest payment station')

            # ending the program
            stop_program = False

from tabulate import tabulate

# for tabulation, this will be the header
headers = ["ID", "Item name", "Quantity", "Price"]  # we will use this for the header in the table


class Transaction:

    def __init__(self, name, quantity, price):
        """
        Transaction class contains shopping item in str, item quantity in int & item's price in int
        e.g. [ 'Compass' , '20_000', '1' ]
        Also containing an empty list of shopping cart to be inputted by user
        """
        self.name = name
        self.quantity = quantity
        self.price = price
        self.cart = []  # this is an empty shopping cart for user to use later on

    def add_item(self):
        """
        Adding item, its price and quantity into the shopping cart
        e.g. [ 'Hyundai' , '10_000', '1' ]
        """
        while True:
            self.name = (input('please enter item name: '))
            if self.name.isnumeric():
                print('===Invalid datatype, please enter a text string')
            else:
                break

        # getting item price from user
        while True:
            try:
                self.quantity = int(input('please enter the quantity: '))
                break
            except ValueError:
                print('===invalid datatype, please enter a number')

        # getting item quantity from user
        while True:
            try:
                self.price = int(input('please enter the price: '))
                break
            except ValueError:
                print('===invalid datatype, please enter a number')

        # creating a list to be stored on cart
        transaction_list = [len(self.cart) + 1, self.name, self.quantity, self.price]

        # appending the list on the cart, and will be based in accordance to the index
        # e.g. index 1 has list containing ['Bebek', '2', '2000' ] so on and so forth
        self.cart.append(transaction_list)

        return tabulate(self.cart, headers=headers, tablefmt='grid')

    def update_item_name(self):
        """
        editing the item's name in the shopping cart based on the index number on the row
        e.g. Index 2, change item name from "toyota" to "subaru"
        """

        item_index = int(input('Enter the ID of the item you want to update: ')) - 1
        if item_index < 0 or item_index >= len(self.cart):
            print('Item number didnt exist in shopping cart, please input existing number')
            return

        # entering a new list to update the item
        new_name = input('Please enter new item name: ')

        # editing the list based on the index
        self.cart[item_index][1] = new_name

        return tabulate(self.cart, headers=headers, tablefmt='grid')

    def update_item_qty(self):
        """
        editing the item's price in the shopping cart based on the index number on the row
        e.g. Index 2, change item price from "10_000" to "5_000"
        """
        item_index = int(input('Enter the ID of the item you want to update: ')) - 1
        if item_index < 0 or item_index >= len(self.cart):
            print('Item number didnt exist in shopping cart, please input existing number')
            return

        # entering a new list to update the item
        new_qty = int(input('Please enter new item quantity: '))

        # editing the list based on the index
        self.cart[item_index][2] = new_qty

        return tabulate(self.cart, headers=headers, tablefmt='grid')

    def update_item_price(self):
        """
        editing the item's quantity in the shopping cart based on the index number on the row
        e.g. Index 2, change item quantity from 1 to 2
        """
        item_index = int(input('Enter the ID of the item you want to update: ')) - 1
        if item_index < 0 or item_index >= len(self.cart):
            print('Item number didnt exist in shopping cart, please input existing number')
            return

        # entering a new list to update the item
        new_price = int(input('Please enter new item price: '))

        # editing the list based on the index
        self.cart[item_index][3] = new_price

        return tabulate(self.cart, headers=headers, tablefmt='grid')

    def delete_item(self):
        """
        delete one single row of item in the cart, based on the index
        """
        item_index = int(input('Enter the ID of the item you want to remove: ')) - 1
        if item_index < 0 or item_index >= len(self.cart):
            print('Invalid item index')
            return

        # deleting the list based on the index
        self.cart.pop(item_index)

        return tabulate(self.cart, headers=headers, tablefmt='grid')

    def reset_transaction(self):
        """
        deleting all item on the shopping cart, reset to empty list
        """
        self.cart = []

        return tabulate(self.cart, headers=headers, tablefmt='grid')

    def calc_price(self):
        """
        calculating total price based on the quantity and price
        """
        total_price = 0
        for item in self.cart:
            price = item[3]
            quantity = item[2]
            total_price += price * quantity
        return total_price

    def check_order(self):
        """
        just checking order, return a tabulation of the shopping cart
        """
        return tabulate(self.cart, headers=headers, tablefmt='grid')

    def total_disc_price(self):
        """
        discounting the total price based on certain criteria
        """
        original_price = 0
        for item in self.cart:
            price = item[3]
            quantity = item[2]
            original_price += price * quantity

        # we order the elif branches based on the highest price first
        # so customer won't get away with less discount
        if original_price > 500000:
            discount = original_price * 0.10
            discounted_price = original_price - discount
            return f'Your total price after 10% discount is: {discounted_price}'
        elif original_price > 300000:
            discount = original_price * 0.08
            discounted_price = original_price - discount
            return f'Your total price after 8% discount is: {discounted_price}'
        elif original_price > 200000:
            discount = original_price * 0.05
            discounted_price = original_price - discount
            return f'Your total price after 5% discount is: {discounted_price}'
        else:
            return f'Your total price is: {original_price}'

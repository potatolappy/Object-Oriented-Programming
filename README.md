# cashier system
_a ]cashier system for OOP practice | July 2023_

![kasir](/img.jpg)

**Chapter 1: Context**

This is a project exercise for a beginner introduction to OOP programming. A company in Indonesia is looking to develop a cashier system where user could input item name, price and quantity and calculate the total price of the transactions (and additional discount added if meeeting certain conditions)

**Chapter 2: Features Requirement**

There are several features the company want:

  1. ``` add_item() ``` to add item name, price and quantity into the shopping cart
  2. ``` update_item_name() ``` to edit the previous item name to a new one
  3. ``` update_item_price() ``` to edit the previous item price to a new one
  4. ``` update_item_qty() ``` to edit the previous item quantity to a new one
  5. ``` delete_item() ``` to delete one row of item name, price and quantity
  6. ``` reset_transaction() ``` to start the shopping cart from empty again
  7. ``` check_order() ``` to see the current shopping cart
  8. ``` total_price() ``` to see the total price, discounted if needed

We also add another feature:
  1. ``` calc_price() ``` to see the shopping cart total value, pre-discount

**Chapter 3: Flow**

user flow chart will go as follow, several key highlights:

  1. at the end of every action that involves a function, it will always return a current tabulated version of the shopping cart, along with its price
  2. every action will always go back to the **menu**, except when the user pick **check-out**
  3. when checking out, the price will be discounted along with this criteria
       - transaction valued over IDR 500k --> 10% discount
       - transaction valued over IDR 300k --> 8% discount
       - transaction valued over IDR 200k --> 5% discount

![kasir](/flowchart.png)

**Chapter 4: Test Cases**

---- **Test Case 1: Adding Item**

Let's begin with the first test case provided by pacmann, the user want to input:
1. Item name: Ayam Goreng, Qty: 2, Price: 20000
2. Item name: Pasta Gigi, Qty: 3, Price: 15000

First the user will input their name into the program

![kasir](/img/1.png)

Afterwards the user will be shown a menu

![kasir](/img/2.png)

in this test case, we will pick option 1 to begin inputting Ayam Goreng into the shopping cart. This will use ```add_item()``` and ```calc_price()``` function

![kasir](/img/3.png)

After user input all the necessary detail, a menu will be shown again, this time we will select 1 to add Pasta Gigi into the shopping cart, using ```add_item()```

![kasir](/img/4.png)

---- **Test Case 2: Deleting Item**

Now imagine the user thinks 85k is too much for grocery and want to delete Pasta Gigi, we can use ```delete_item()``` function and selecting option 2

![kasir](/img/5.png)

as shown, the item has been deleted

---- **Test Case 3: Reset Transaction**

Apparently, the user also think they will be fine without Ayam Goreng today, we can use ```reset_transaction()``` function and selecting option 6

![kasir](/img/rst.png)

as shown, the shopping cart is now empty

---- **Test Case 4: Check-out**

Now in an ideal world for supermarket where user didn't mind at all about price, instead of deleting Pasta Gigi & Ayam Goreng they want to add:
1. One Mainan Mobil for IDR 200k
2. Five Mi Instan for IDR 3k

![kasir](/img/6.png)

User can pick the last option 7 for checkout, and the program will run function ```total_price()``` 

![kasir](/img/7.png)

As shown, the price has been calculated with discount and the program end

**Final Chapter: Conclusion and additional thoughts**

As shown, it is a simple rudimentary program to excercise using OOP. the Transaction class allow us to add items, update, delete, reset and calculate the price with ease. some additional thoughts for future improvement

1. This program best be use for cashier instead of customer since customer can easily add whatever price they want, in the future it should be a list of item (can be in dictionary) where the customer only add the item name and quantity, and the item's price is immutable
2. A way to add unique ID to each transaction conducted, and record how many time a customer shops. If the supermarket has a loyalty program it can be implemented here to loyal and big-spender customer










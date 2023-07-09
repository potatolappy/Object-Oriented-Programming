# pacmann-cashier
_a self-cashier system for OOP practice with pacmann.io | July 2023_

![kasir](/img.jpg)

**Chapter 1: Context**

This is a project exercise from pacmann.io in 2023 for a beginner introduction to OOP programming. A company in Indonesia is looking to develop a cashier system where user could input item name, price and quantity and calculate the total price of the transactions (and additional discount added if meeeting certain conditions)

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

Let's begin with the first test case provided by pacmann, the user want to input:
1. Item name: Ayam Goreng, Qty: 2, Price: 20000
2. Item name: Pasta Gigi, Qty: 3, Price: 15000


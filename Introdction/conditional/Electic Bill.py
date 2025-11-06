"""
Project Definition: Electricity Bill Calculator

The Electricity Bill Calculator is a Python mini project designed to demonstrate the use of conditional and nested statements in a practical, real-world application. The program calculates a customer’s monthly electricity bill based on the number of units consumed, incorporating multiple features and billing rules to reflect real-world scenarios.

Features and Functionalities:
	1.	Accepts user input for the total electricity units consumed.
	2.	Uses if, elif, and else statements to apply tiered billing based on consumption slabs:
	•	0 – 100 units → ₹5/unit
	•	101 – 200 units → ₹7/unit
	•	201 – 300 units → ₹10/unit
	•	Above 300 units → ₹15/unit
	3.	Implements nested conditions to handle additional charges or discounts within slabs.
	4.	Adds a fixed meter charge of ₹50 to every bill.
	5.	Applies a 10% surcharge if total units exceed 500 units.
	6.	Provides a 5% discount if consumption is below 50 units as a low-usage incentive.
	7.	Includes extra charges for peak-hour consumption: ₹2/unit for units consumed during peak hours above 50 units.
	8.	Handles edge cases, such as exactly hitting slab limits or zero consumption.
	9.	Offers custom messages to indicate low, medium, or high consumption.
	10.	Calculates and displays a final formatted bill, showing total amount, surcharge, discounts, and fixed charges.
	11.	Can optionally add a late payment penalty of ₹100 if payment is delayed.
	12.	Ensures user input validation, allowing only non-negative numeric entries.
 """
units = int(input("Enter the total electricity units consumed: "))
fixed_charge = 50
total_amount = 0
surcharge = 0

if units < 0:
    print("Invalid number of units.")
else:
    if units >= 0 and units <= 100:
        total_amount = units * 5
    elif units >= 101 and units <= 200:
        total_amount = units * 7
    elif units >= 201 and units <= 300:
        total_amount = units * 10
    else:  
        total_amount = units * 15

    if units > 500:
        surcharge = total_amount * 0.10
      
    if units < 50:
        discount = total_amount * 0.05
total_amount -= discount    

print("Electricity Bill :", total_amount)
print("Surcharge :", surcharge)
print("Fixed meter charge:", fixed_charge)

Electric_bill = total_amount + fixed_charge + surcharge
print(f"Your Total Electricity Bill is: {Electric_bill}")

import pandas as pd 
import numpy as np 
from datetime import datetime, 
timedelta 
# Define a class to represent a customer 
class Customer: def __init__(self, customer_id, name, phone_number, airtime_balance): 
self.customer_id = customer_id 
self.name = name 
self.phone_number = phone_number 
self.airtime_balance = airtime_balance 
def top_up(self, amount): 
self.airtime_balance += amount 
print(f"Airtime balance topped up for customer {self.name} ({self.phone_number}): {amount}") 
def make_call(self, duration, call_rate): cost = duration * call_rate 
if 
self.airtime_balance >= cost: 
self.airtime_balance -= cost 
print(f"Call made for {duration} minutes. Cost: {cost:.2f}. 
Remaining balance: {self.airtime_balance:.2f}") 
else:
 print(f"Insufficient airtime. Call cannot be made.") 
def get_balance(self): 
print(f"Current airtime balance for {self.name} ({self.phone_number}): {self.airtime_balance:.2f}") 
# Define a class to manage marketing data class MarketingData: 
def __init__(self): self.customer_data = {} 
def add_customer(self, customer): 
self.customer_data[customer.customer_id] = customer 
print(f"Customer {customer.name} ({customer.phone_number}) added.") 
def get_customer(self, customer_id): 
if 
customer_id in self.customer_data: 
return self.customer_data[customer_id] 
else: 
print(f"Customer with ID {customer_id} not found.") 
return None def get_all_customers(self): 
return self.customer_data.values() 
def get_customer_data(self, customer_id): 
if 
customer_id in self.customer_data: return self.customer_data[customer_id] 
else: 
print(f"Customer with ID {customer_id} not found.") 
return None 
def analyze_data(self): 
# Implement data analysis features 
# Example: Calculate average airtime balance, most frequent calls, etc. pass 
# Create an instance of MarketingData 
marketing_data = MarketingData() 
# Add some sample customers 
marketing_data.add_customer(Customer(1, "John Doe", "1234567890", 10.00)) 
marketing_data.add_customer(Customer(2, "Jane Smith", "9876543210", 5.00)) 
# Perform some actions john = marketing_data.get_customer(1)
How john.top_up(5.00) 
john.make_call(10, 0.15) 
uba john.get_balance()
jane = marketing_data.get_customer(2) 
jane.make_call(5, 0.15) 
jane.get_balance() 
# Display all customers 
for customer in marketing_data.get_all_customers(): 
print(f"Customer ID: {customer.customer_id}, Name: {customer.name}, Phone: {customer.phone_number}") 
# Example of data analysis 
# (Implement specific analysis logic based on your needs) 
print("\nData Analysis:")

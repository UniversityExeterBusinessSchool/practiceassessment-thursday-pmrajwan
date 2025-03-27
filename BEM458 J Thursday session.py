#######################################################################################################################################################
# 
# Name:Mohammed Rajwan
# SID:740097868
# Exam Date:27/03/2025
# Module:BEMM458
# Github link for this assignment: https://github.com/UniversityExeterBusinessSchool/practiceassessment-thursday-pmrajwan 
#
# ######################################################################################################################################################
# Instruction 1. Read the questions and instructions carefully and complete scripts.

# Instruction 2. Only ethical and minimal use of AI is allowed. You might use AI to give advice on how to use a tool or programming language.  
#                You must not use AI to create the code. You might make use of AI to aid debugging of the code.  
#                You must indicate clearly how and where you have used AI.

# Instruction 3. Copy the output of the code and insert it as a comment below your code e.g # OUTPUT (23,45)

# Instruction 4. Ensure you provide comments for the code and the output to show contextual understanding.

# Instruction 5. Upon completing this test, commit to Git, copy and paste your code into the word file and upload the saved file to ELE.
#                There is a leeway on when you need to upload to ELE, however, you must commit to Git at 
#                the end of your session.

# ######################################################################################################################################################
# Question 1 - Loops
# Create a list and use a for loop to answer the following question:
# You are given a dictionary called key_comments. Your allocated keys are the first and last digit of your SID.
# Find the start and end position of each of the items in the sentence using the find command.
# Create and populate a list called my_list with a tuple of (start location, end location) for each value in comments 
 

customer_feedback = """Your recent order experience has been satisfactory overall. While there were some minor issues,
we appreciate the effort made to resolve them promptly."
"""

# List of words to search for
key_comments = {
    0: 'satisfactory',
    1: 'order',
    2: 'effort',
    3: 'issues',
    4: 'promptly',
    5: 'appreciate',
    6: 'experience',
    7: 'resolve',
    8: 'overall',
    9: 'minor'
}# Initialize an empty list to store (start, end) positions
my_list = []

# Write your search code here and provide comments. 
key_comments = {
    0: 'satisfactory', 1: 'order', 2: 'effort', 3: 'issues', 4: 'promptly',
    5: 'appreciate', 6: 'experience', 7: 'resolve', 8: 'overall', 9: 'minor'
}
# The first and last digit of the student id
SID = "740097868"
# Create a list of id with first and last digits
my_list = [
    # each digit first and last of SID, get the corresponding word and find its start and end position
    (customer_feedback.find(word), customer_feedback.find(word) + len(word))
    for i in (int(SID[0]), int(SID[-1]))         # Get the first and last digits of the SID
    for word in [key_comments[i]]                # Get the word associated with the digit
]

# Print the result
print("Start and end positions of allocated words:", my_list)

#OUTPUT : Start and end positions of allocated words: [(129, 136), (51, 58)]

##########################################################################################################################################################

# Question 2 - Functions
# Scenario - You are working in an e-commerce firm as a business analyst, and your manager has tasked you to generate weekly reports on financial metrics like 
# Operating Profit Margin, Revenue per Customer, Customer Churn Rate, and Average Order Value. Use Python functions 
# that will take the values and return the metric needed. Use the first two and last two digits of your ID number as the input values.

# Insert first two digits of ID number here:74
# Insert last two digits of ID number here:68

# Write your code for Operating Profit Margin
# calculate the operational profit Margin (OPM = (Revenue - Operating Cost) / Revenue)
def opm(revenue, cost): return (revenue - cost) / revenue

# Write your code for Revenue per Customer
# calculate Revenue per Customer (RPC = Total Revenue / No. of Customers)
def rpc(revenue, customers): return revenue / customers

# Write your code for Customer Churn Rate
# calculate the Customer Churn Rate (Churn Rate = Lost Customers / Total Customers)
def churn(lost, total): return lost / total

# Write your code for Average Order Value
# calculate the Average Order Value (AOV = Revenue / No. of Orders)
def aov(revenue, orders): return revenue / orders


# Call your designed functions here
# Call the functions with sample usage functions
print("Operating Profit Margin:", opm(74, 68))
print("Revenue per Customer:", rpc(74, 68))
print("Customer Churn Rate:", churn(6, 68))     
print("Average Order Value:", aov(74, 34))      # Assuming 34 total orders

#OUTPUT
#Operating Profit Margin: 0.08108108108108109
#Revenue per Customer: 1.088235294117647
#Customer Churn Rate: 0.08823529411764706
#Average Order Value: 2.176470588235294


##########################################################################################################################################################

# Question 3 - Regression
# A retail store has collected data on seasonal sales and price changes. The table below shows different price levels and their corresponding demand.
# Develop a linear regression model and determine:
# 1. The price at which the store can maximize revenue
# 2. The demand when the price is set at £52

"""
Price (£)    Demand (Units)
---------------------------
20           300
25           280
30           260
35           240
40           210
45           190
50           160
55           140
60           120
65           100
70           85
"""

# Write your code here
from sklearn.linear_model import LinearRegression
import numpy as np

# Price and demand data
price = np.array([20,25,30,35,40,45,50,55,60,65,70]).reshape(-1,1)
demand = np.array([300,280,260,240,210,190,160,140,120,100,85])

# Create a linear regression model
m = LinearRegression().fit(p, d)

# Display the results
print("Max revenue at £%.2f" % p[np.argmax(p.flatten()*m.predict(p))][0])
print("Demand at £52: %.0f units" % m.predict([[52]])[0])

#OUTPUT
#Max revenue at £45.00
#Demand at £52: 158 units

##########################################################################################################################################################

# Question 4 - Debugging; Plotting and data visualization chart

import random
import matplotlib.pyplot as plt

# Generate 100 random numbers between 1 and student id number
max_value = int(input("Enter your Student ID: "))
random_numbers = [random.randint(1, max_value) for _ in range(100)]

# Plotting the numbers in a line chart
plt.plot(random_numbers, marker='o', markerfacecolor='green', markeredgecolor='red',
         linestyle='--', label='Random Numbers', color='blue')
# Adding the chart titles and labels
plt.title("Line Chart of 100 Random Numbers")
plt.xlabel("Index")
plt.ylabel("Random Number")
plt.legend()
plt.grid(True)
plt.show()

## all code done




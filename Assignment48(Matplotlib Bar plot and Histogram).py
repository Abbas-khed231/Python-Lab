#1.  Create a bar chart to represent monthly expenses in different spending categories and give your conclusion.
#Input: categories = ['Rent', 'Groceries', 'Utilities', 'Entertainment', 'Transportation'] 
# Monthly expenses in dollars (replace with your own data) 
#expenses = [1200, 400, 200, 150, 250]

import matplotlib.pyplot as plt

categories = ['Rent', 'Groceries', 'Utilities', 'Entertainment', 'Transportation']
expenses = [1200, 400, 200, 150, 250]

plt.figure(figsize=(10, 6))
plt.bar(categories, expenses, color=['blue', 'green', 'orange', 'red', 'purple'])

plt.xlabel('Spending Categories')
plt.ylabel('Monthly Expenses (in dollars)')
plt.title('Monthly Expenses Breakdown')

plt.grid(axis='y', linestyle='--')

plt.show()

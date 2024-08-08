'''
Suppose you want to track and analyze your household expenses for a month.
You have recorded the expenses for various categories, such as groceries, utilities, rent,
transportation, and entertainment. You can represent this expense data using a Pandas Series. 

Input: # Expense categories

categories = ['Groceries', 'Utilities', 'Rent', 'Transportation', 'Entertainment']

#Monthly expense data (example data in USD) 

expenses = [500, 200, 1200, 300, 150]
'''

import pandas as pd
categories = ['Groceries', 'Utilities', 'Rent', 'Transportation', 'Entertainment']
expenses = [500, 200, 1200, 300, 150]  

expenses_series = pd.Series(expenses, index=categories)
print(expenses_series)

'''
Output:

Groceries          500
Utilities          200
Rent              1200
Transportation     300
Entertainment      150
name: Monthly Expenses, dtype: int64
'''

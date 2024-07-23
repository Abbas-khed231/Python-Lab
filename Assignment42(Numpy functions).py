'''2. Suppose you have two sets of employee data—one containing information about full-time
employees and another containing information about part-time employees.You want to combine
this data to create a comprehensive employee dataset for HR analysis. '''

import numpy as np

full_time_employees = np.array([[101, 'John Doe', 'Full-Time', 55000],
                                [102, 'Jane Smith', 'Full-Time', 60000],
                                [103, 'Mike Johnson', 'Full-Time', 52000]], dtype=object)

part_time_employees = np.array([[201, 'Alice Brown', 'Part-Time', 25000],
                                [202, 'Bob Wilson', 'Part-Time', 28000],
                                [203, 'Emily Davis', 'Part-Time', 22000]], dtype=object)

combined_employees = np.concatenate((full_time_employees, part_time_employees))

print("ID\tName\t\tStatus\t\tSalary")
for employee in combined_employees:
    print(f"{employee[0]}\t{employee[1]}\t{employee[2]}\t{employee[3]}")


'''
Output:
ID	Name		Status		Salary
101	John Doe	Full-Time	55000
102	Jane Smith	Full-Time	60000
103	Mike Johnson	Full-Time	52000
201	Alice Brown	Part-Time	25000
202	Bob Wilson	Part-Time	28000
203	Emily Davis	Part-Time	22000
'''

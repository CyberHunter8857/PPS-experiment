basic_pay = float(input("Enter the basic pay: "))

hra = 0.1 * basic_pay
ta = 0.05 * basic_pay

gross_salary = basic_pay + hra + ta

professional_tax = 0.02 * gross_salary

net_salary = gross_salary - professional_tax


print('TA:', ta)
print('HRA:', hra)
print('Professional Tax',professional_tax)
print("Gross Salary:", gross_salary)
print("Net Salary:", net_salary)


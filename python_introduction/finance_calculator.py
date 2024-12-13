monthly_income = int(input ("Enter your monthly income: "))
monthly_expenses = int(input ("Enter your monthly expenses: "))
monthly_savings = monthly_income - monthly_expenses
annual_savings = float(monthly_savings * 12)
annual_interest = annual_savings * 0.05
annual_savings_with_interest = annual_savings + annual_interest
print(monthly_savings)
print(annual_savings_with_interest)
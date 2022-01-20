def months_for_down_payment(annual_salary, portion_saved, total_cost):
    """With the given inputs, calculate how many months are needed to save for a house down payment"""
    portion_down_payment = 0.25
    current_savings = 0
    r = 0.04  # Investment annual return

    down_payment = total_cost * portion_down_payment
    monthly_salary = annual_salary / 12
    monthly_salary_savings = monthly_salary * portion_saved

    months = 0

    while current_savings <= down_payment:
        investment_funds = current_savings * r / 12
        current_savings += investment_funds + monthly_salary_savings
        months += 1

    return months

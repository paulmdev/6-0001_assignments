def months_for_down_payment(annual_salary, portion_saved, total_cost, semi_annual_raise):
    """
    With the given inputs, calculate how many months are needed to save for a house down payment

    This implementation takes into account that after every 6 months the user will have a semi_annual_raise raise to their annual_salary
    """
    portion_down_payment = 0.25
    r = 0.04  # Investment annual return

    down_payment = total_cost * portion_down_payment

    def get_monthly_salary_savings(annual_salary, portion_saved):
        monthly_salary = annual_salary / 12
        return monthly_salary * portion_saved

    months = 0
    current_savings = 0

    while current_savings <= down_payment:
        investment_funds = current_savings * r / 12
        current_savings += investment_funds + \
            get_monthly_salary_savings(annual_salary, portion_saved)
        months += 1
        if months % 6 == 0:
            annual_salary += annual_salary * semi_annual_raise

    return months

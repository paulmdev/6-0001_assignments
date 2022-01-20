import math


def get_saving_rate_for_down_payment(annual_salary):
    """
    Given an annual_salary, this function will compute a monthly savings_rate needed 
    to pay a down payment in 3 years and the steps needed in the bicection search to
    compute the value.
    """

    # Set up business logic variables.
    semi_annual_raise = .07  # 7%
    investment_annual_return = .04  # 4%
    down_payment_portion = .25  # 25%
    house_cost = 1000000  # $1M
    year_limit_in_months = 36

    down_payment_cost = house_cost * down_payment_portion

    # Set up bisection search variables.
    low = 0
    high = 10000
    guess_rate = (low + high) // 2
    steps = 0

    current_savings = 0

    # While the remaining of the savings after paying the down payment is greater than 100.
    while abs(down_payment_cost - current_savings) >= 100:

        # Reset variables after every loop.
        current_savings = 0
        temp_annual_salary = annual_salary

        # Transform the guess rate to decimal. Ej: 5000 -> 0.5
        savings_rate = guess_rate / 10000

        for month in range(year_limit_in_months):
            investment_funds = current_savings * investment_annual_return / 12

            monthly_salary = temp_annual_salary / 12

            monthly_savings = monthly_salary * savings_rate

            current_savings += investment_funds + monthly_savings

            # Every half year, increase the annual salary by semi_annual_raise percent.
            if month % 6 == 0 and month > 0:
                temp_annual_salary += temp_annual_salary * semi_annual_raise

        if current_savings < down_payment_cost:
            low = guess_rate
        else:
            high = guess_rate

        guess_rate = (low + high) // 2

        steps += 1

        # The maximum number of steps in the bisection search is log(n).
        # If the steps are greater than that, throw an Exception.
        if math.log2(10000) < steps:
            raise Exception()

    return savings_rate, steps

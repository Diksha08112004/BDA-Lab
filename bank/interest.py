""
Interest module for bank package.
Provides functions for various interest calculations.
"""

def simple_interest(principal, rate, time):
    """
    Calculate simple interest.
    
    Args:
        principal (float): Principal amount
        rate (float): Annual interest rate (as percentage)
        time (float): Time in years
        
    Returns:
        float: Simple interest amount
    """
    if principal <= 0 or rate < 0 or time < 0:
        return 0.0
    return round((principal * rate * time) / 100, 2)

def compound_interest(principal, rate, time, n=1):
    """
    Calculate compound interest.
    
    Args:
        principal (float): Principal amount
        rate (float): Annual interest rate (as percentage)
        time (float): Time in years
        n (int): Number of times interest is compounded per year (default: 1)
        
    Returns:
        float: Compound interest amount
    """
    if principal <= 0 or rate < 0 or time < 0 or n <= 0:
        return 0.0
    
    amount = principal * (1 + (rate / (100 * n))) ** (n * time)
    return round(amount - principal, 2)

def effective_annual_rate(nominal_rate, n):
    """
    Calculate Effective Annual Rate (EAR).
    
    Args:
        nominal_rate (float): Nominal annual interest rate (as percentage)
        n (int): Number of compounding periods per year
        
    Returns:
        float: Effective annual rate as a percentage
    """
    if nominal_rate <= 0 or n <= 0:
        return 0.0
    
    ear = ((1 + (nominal_rate / (100 * n))) ** n - 1) * 100
    return round(ear, 4)

def future_value(principal, rate, time, n=1):
    """
    Calculate the future value of an investment.
    
    Args:
        principal (float): Initial investment
        rate (float): Annual interest rate (as percentage)
        time (float): Time in years
        n (int): Number of times interest is compounded per year (default: 1)
        
    Returns:
        float: Future value of the investment
    """
    if principal <= 0 or rate < 0 or time < 0 or n <= 0:
        return 0.0
    
    amount = principal * (1 + (rate / (100 * n))) ** (n * time)
    return round(amount, 2)

def present_value(future_value, rate, time, n=1):
    """
    Calculate the present value of a future amount.
    
    Args:
        future_value (float): Future amount
        rate (float): Discount rate (as percentage)
        time (float): Time in years
        n (int): Number of times interest is compounded per year (default: 1)
        
    Returns:
        float: Present value
    """
    if future_value <= 0 or rate < 0 or time < 0 or n <= 0:
        return 0.0
    
    pv = future_value / ((1 + (rate / (100 * n))) ** (n * time))
    return round(pv, 2)

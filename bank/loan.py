""
Loan module for bank package.
Provides functions for EMI and loan-related calculations.
"""

from math import pow

def calculate_emi(principal, annual_rate, years):
    """
    Calculate Equated Monthly Installment (EMI) for a loan.
    
    Args:
        principal (float): Loan amount
        annual_rate (float): Annual interest rate (as percentage)
        years (int): Loan tenure in years
        
    Returns:
        float: Monthly EMI amount
    """
    if principal <= 0 or annual_rate <= 0 or years <= 0:
        return 0.0
        
    monthly_rate = (annual_rate / 12) / 100  # Convert to monthly decimal
    months = years * 12
    
    # EMI formula: [P x R x (1+R)^N]/[(1+R)^N-1]
    emi = (principal * monthly_rate * pow(1 + monthly_rate, months)) / \
          (pow(1 + monthly_rate, months) - 1)
    
    return round(emi, 2)

def calculate_total_payment(emi, years):
    """
    Calculate total payment over the loan tenure.
    
    Args:
        emi (float): Monthly EMI amount
        years (int): Loan tenure in years
        
    Returns:
        float: Total payment (EMI * number of months)
    """
    return round(emi * years * 12, 2)

def calculate_interest_paid(principal, emi, years):
    """
    Calculate total interest paid over the loan tenure.
    
    Args:
        principal (float): Original loan amount
        emi (float): Monthly EMI amount
        years (int): Loan tenure in years
        
    Returns:
        float: Total interest paid
    """
    total_payment = calculate_total_payment(emi, years)
    return round(total_payment - principal, 2)

def get_loan_schedule(principal, annual_rate, years):
    """
    Generate a loan amortization schedule.
    
    Args:
        principal (float): Loan amount
        annual_rate (float): Annual interest rate (as percentage)
        years (int): Loan tenure in years
        
    Returns:
        list: List of dictionaries containing payment details for each month
    """
    monthly_rate = (annual_rate / 12) / 100
    months = years * 12
    emi = calculate_emi(principal, annual_rate, years)
    
    balance = principal
    schedule = []
    
    for month in range(1, months + 1):
        interest_payment = round(balance * monthly_rate, 2)
        principal_payment = round(emi - interest_payment, 2)
        
        # Adjust for the last payment to handle rounding errors
        if month == months:
            principal_payment = round(balance, 2)
            emi = principal_payment + interest_payment
            balance = 0
        else:
            balance -= principal_payment
        
        schedule.append({
            'month': month,
            'emi': round(emi, 2),
            'principal': principal_payment,
            'interest': interest_payment,
            'balance': max(0, round(balance, 2))
        })
    
    return schedule

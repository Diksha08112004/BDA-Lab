def simple_interest(principal, rate, time):
    return (principal * rate * time) / 100

def compound_interest(principal, rate, time, n=1):
    return principal * (1 + (rate / (100 * n))) ** (n * time) - principal

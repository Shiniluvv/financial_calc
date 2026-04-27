def calculate_simple_interest(principal, rate, time):
    if principal < 0 or rate < 0 or time < 0:
        raise ValueError("Аргументы должны быть неотрицательными")
    return principal * rate * time / 100

def calculate_compound_interest(principal, rate, time, n=1):
    if principal < 0 or rate < 0 or time < 0:
        raise ValueError("principal, rate, time должны быть неотрицательными")
    if not isinstance(n, int) or n <= 0:
        raise ValueError("n должно быть целым положительным числом")
    return principal * (1 + rate / (100.0 * n)) ** (n * time)

def calculate_tax(amount, tax_rate):
    if amount < 0:
        raise ValueError("amount не может быть отрицательным")
    if not (0 <= tax_rate <= 100):
        raise ValueError("tax_rate должна быть между 0 и 100")
    return amount * tax_rate / 100

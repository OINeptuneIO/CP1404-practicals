"""
CP1404/CP5632 Practical
Starter code for cumulative total income program
"""

def main():
    """Display income report for incomes over a given number of months."""
    incomes = []
    num_months = int(input("How many months? "))  # Renamed from 'months' to 'num_months'

    for month in range(1, num_months + 1):
        income = float(input(f"Enter income for month {month}: "))  # Using f-string
        incomes.append(income)

    print_report(incomes, num_months)  # Refactored report printing into its own function

def print_report(incomes, num_months):
    """Print the income report."""
    print("\nIncome Report\n-------------")
    total = 0
    for month in range(1, num_months + 1):
        income = incomes[month - 1]
        total += income
        print(f"Month {month:2} - Income: ${income:10.2f} Total: ${total:10.2f}")

main()
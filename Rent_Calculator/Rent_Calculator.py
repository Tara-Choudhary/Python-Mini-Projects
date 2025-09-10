# Rent_Calculator


def get_expenses():
    """Get all expenses from user and return as a dictionary."""
    expenses = {}
    expenses['Rent'] = float(input("Enter the total rent amount: "))
    expenses['Utilities'] = float(input("Enter the other utilities cost: "))
    expenses['Electricity'] = float(input("Enter the electricity bill: "))
    expenses['Food'] = float(input("Enter the total food expenses: "))
    return expenses

def calculate_total(expenses):
    """Calculate total of all expenses."""
    return sum(expenses.values())

def calculate_share(total, num_people):
    """Calculate per-person share."""
    return total / num_people if num_people > 0 else 0

def display_breakdown(expenses, total, share, num_people):
    """Print the detailed breakdown."""
    print("\n--- Rent Breakdown ---")
    for key, value in expenses.items():
        print(f"{key}: ${value:.2f}")
    print(f"Total Monthly Expense: ${total:.2f}")
    print(f"Each Person's Share ({num_people} people): ${share:.2f}")

# Main Program
expenses = get_expenses()
num_people = int(input("Enter the number of people sharing: "))
total = calculate_total(expenses)
share = calculate_share(total, num_people)
display_breakdown(expenses, total, share, num_people)

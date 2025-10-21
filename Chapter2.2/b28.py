def main() -> None:
    days_in_month: dict[int, dict[str, str]] = {
        1: {"name": "january", "days": "31 days"},
        2: {"name": "february", "days": "28 or 29 days"},
        3: {"name": "march", "days": "31 days"},
        4: {"name": "april", "days": "30 days"},
        5: {"name": "may", "days": "31 days"},
        6: {"name": "june", "days": "30 days"},
        7: {"name": "july", "days": "31 days"},
        8: {"name": "august", "days": "31 days"},
        9: {"name": "september", "days": "30 days"},
        10: {"name": "october", "days": "31 days"},
        11: {"name": "november", "days": "30 days"},
        12: {"name": "december", "days": "31 days"},
    }

    try:
        month: int = int(input("Enter month (1–12): "))
        if month in days_in_month:
            print(
                f"{days_in_month[month]['name'].capitalize()} has {days_in_month[month]['days']}."
            )
        else:
            print("Error: Invalid month number.")
    except ValueError:
        print("Error: Please enter a valid integer.")
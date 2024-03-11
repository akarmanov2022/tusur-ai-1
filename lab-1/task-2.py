month_number = int(input("Enter a month number: "))


def season(month_number: int):
    if month_number in [12, 1, 2]:
        return "зима"
    elif month_number in [3, 4, 5]:
        return "весна"
    elif month_number in [6, 7, 8]:
        return "лето"
    elif month_number in [9, 10, 11]:
        return "осень"
    else:
        return "неверный номер месяца"


s = season(month_number)
print(s)

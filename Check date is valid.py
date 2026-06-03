# Read input
day = int(input())
month = int(input())
year = int(input())

# Function to check leap year
def is_leap(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

# Validate year
if year <= 0:
    print("Invalid Date")
else:
    # Days in each month
    if month < 1 or month > 12:
        print("Invalid Date")
    else:
        if month in [1, 3, 5, 7, 8, 10, 12]:
            max_days = 31
        elif month in [4, 6, 9, 11]:
            max_days = 30
        elif month == 2:
            max_days = 29 if is_leap(year) else 28
        
        # Validate day
        if day < 1 or day > max_days:
            print("Invalid Date")
        else:
            # Increment date
            day += 1
            if day > max_days:
                day = 1
                month += 1
                if month > 12:
                    month = 1
                    year += 1
            print(f"{day:02d}-{month:02d}-{year}")

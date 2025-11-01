import date_ops as do
from datetime import date, timedelta

def main():
    print("=== Date Operations ===\n")
    
    # Example 1: Days between two dates
    date1 = "2023-01-01"
    date2 = "2023-12-31"
    days_between = do.days_between_dates(date1, date2)
    print(f"1. Days between {date1} and {date2}: {days_between} days")
    
    # Example 2: Days until next birthday
    today = date.today().strftime("%Y-%m-%d")
    next_birthday = "2024-05-15"  # Replace with actual birthday
    days_until_bday = do.days_between_dates(today, next_birthday)
    print(f"\n2. Days until next birthday ({next_birthday}): {days_until_bday} days")
    
    # Example 3: Project deadline
    start_date = "2023-11-01"
    deadline = "2023-12-15"
    days_left = do.days_between_dates(today, deadline)
    print(f"\n3. Days until project deadline ({deadline}): {days_left} days")
    
    # Example 4: Age calculation
    def calculate_age(birth_date):
        today = date.today()
        birth = date.fromisoformat(birth_date)
        age = today.year - birth.year - ((today.month, today.day) < (birth.month, birth.day))
        return age
    
    birth_date = "1995-05-15"
    age = calculate_age(birth_date)
    print(f"\n4. Age if born on {birth_date}: {age} years old")
    
    # Example 5: Add days to a date
    def add_days(start_date, days_to_add):
        start = date.fromisoformat(start_date)
        end_date = start + timedelta(days=days_to_add)
        return end_date.strftime("%Y-%m-%d")
    
    start = "2023-11-01"
    days_to_add = 45
    end_date = add_days(start, days_to_add)
    print(f"\n5. {days_to_add} days after {start} will be {end_date}")
    
    # Example 6: Weekday calculation
    def get_weekday(date_str):
        days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        d = date.fromisoformat(date_str)
        return days[d.weekday()]
    
    some_date = "2023-12-25"
    weekday = get_weekday(some_date)
    print(f"\n6. {some_date} falls on a {weekday}")

if __name__ == "__main__":
    main()

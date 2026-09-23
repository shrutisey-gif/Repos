from datetime import date


def calculate_age(date_of_birth):
    """Return age in years for a valid date of birth."""
    today = date.today()

    if not isinstance(date_of_birth, date):
        raise TypeError("Date of birth must be a date object.")

    if date_of_birth > today:
        raise ValueError("Date of birth cannot be in the future.")

    age = today.year - date_of_birth.year

    # Adjust age if birthday has not occurred yet this year
    if (today.month, today.day) < (date_of_birth.month, date_of_birth.day):
        age -= 1  # age = age - 1

    # Age validation
    if age <= 0 or age >= 100:
        raise ValueError("Age should be greater than 0 and less than 100.")

    return age

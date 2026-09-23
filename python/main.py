from datetime import date
from function import calculate_age


def main():
    dob = date(1985, 6, 28)
    age = calculate_age(dob)
    print(f"Your age is: {age}")


if __name__ == "__main__":
    main()

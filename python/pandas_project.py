from pathlib import Path

import pandas as pd


BASE_DIR = Path(__file__).resolve().parent
INPUT_FILE = BASE_DIR / "data" / "employees.csv"
OUTPUT_DIR = BASE_DIR / "output"


def load_data():
    df = pd.read_csv(INPUT_FILE)
    print("Raw DataFrame:")
    print(df.head())
    return df


def filter_employees(df):
    filtered_df = df[df["Salary"] > 60000].copy()
    return filtered_df


def select_columns(df):
    selected_df = df[["Name", "Department", "City", "Salary"]].copy()
    return selected_df


def aggregate_by_department(df):
    summary = (
        df.groupby("Department", as_index=False)["Salary"]
        .agg(avg_salary="mean", max_salary="max", min_salary="min")
    )
    return summary


def aggregate_by_city(df):
    city_summary = (
        df.groupby("City", as_index=False)["Salary"]
        .sum()
        .rename(columns={"Salary": "total_salary"})
    )
    return city_summary


def save_csv(df, file_name):
    OUTPUT_DIR.mkdir(exist_ok=True)
    df.to_csv(OUTPUT_DIR / file_name, index=False)


def main():
    df = load_data()

    filtered_df = filter_employees(df)
    selected_df = select_columns(df)
    dept_summary = aggregate_by_department(df)
    city_summary = aggregate_by_city(df)

    save_csv(filtered_df, "filtered_employees.csv")
    save_csv(selected_df, "selected_columns.csv")
    save_csv(dept_summary, "department_summary.csv")
    save_csv(city_summary, "city_summary.csv")

    print("\nFiltered employees saved to output/filtered_employees.csv")
    print("Selected columns saved to output/selected_columns.csv")
    print("Department summary saved to output/department_summary.csv")
    print("City summary saved to output/city_summary.csv")


if __name__ == "__main__":
    main()

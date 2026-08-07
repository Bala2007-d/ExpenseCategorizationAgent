import os


def save_result(data):
    output_path = "output/categorized_expenses.csv"
    data.to_csv(output_path, index=False)
    return output_path


def show_summary(data):
    print("\nExpense Categories:\n")
    print(data[["Description", "Category"]])
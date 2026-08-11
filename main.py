from tools import read_csv, save_csv
from planner import categorize_expense
from observer import save_result, show_summary
from logger import write_log

INPUT_FILE = "data/expenses.csv"
OUTPUT_FILE = "output/categorized_expenses.csv"

MAX_ITERATIONS = 10


def main():

    # PERCEIVE
    write_log("PERCEIVE", "Reading expense file")

    data = read_csv(INPUT_FILE)

    success_count = 0

    # PLAN → ACT
    for count, (index, row) in enumerate(data.iterrows()):

        if count >= MAX_ITERATIONS:
            write_log("STOP", "Maximum iteration limit reached")
            print("Maximum iteration limit reached")
            break

        description = row["Description"]

        write_log("PLAN", f"Finding category for: {description}")

        try:
            category = categorize_expense(description)

            data.at[index, "Category"] = category

            success_count += 1

            write_log("ACT", f"{description} -> {category}")

        except Exception as e:

            # Tool failure recovery
            data.at[index, "Category"] = "Other"

            write_log("ERROR", f"{description} -> {str(e)}")

    # SUCCESS CONDITION
    if success_count == len(data):
        print("\nSUCCESS : All expenses categorized successfully.\n")
        write_log("SUCCESS", "All expenses categorized successfully")
    else:
        print("\nWARNING : Some expenses were categorized using fallback.\n")
        write_log("WARNING", "Some expenses used fallback category")

    # OBSERVE
    save_csv(data, OUTPUT_FILE)
    save_result(data)

    write_log("OBSERVE", "Output file saved successfully")

    show_summary(data)


if __name__ == "__main__":
    main()
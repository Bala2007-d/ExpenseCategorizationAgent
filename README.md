# AI Expense Categorization Agent

## Project Description

The AI Expense Categorization Agent automatically categorizes bank transactions into predefined categories using a Large Language Model (LLM) through OpenRouter.

## Features

- Reads expenses from CSV
- Uses a real AI model
- Categorizes each expense
- Saves categorized results
- Logs every iteration
- Implements Perceive → Plan → Act → Observe agent loop
- Handles API/tool failures gracefully
- Stops after maximum iterations

## Technologies Used

- Python
- Pandas
- OpenRouter API
- Large Language Model (LLM)

## Project Structure

ExpenseCategorizationAgent/
│
├── data/
├── logs/
├── output/
├── config.py
├── tools.py
├── planner.py
├── observer.py
├── logger.py
├── main.py
└── README.md

## Run

pip install -r requirements.txt

python main.py

## Output

- Categorized CSV file
- Agent log file
- Console summary

## Author

Balaji
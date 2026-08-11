import pandas as pd


def read_csv(file_path):
    data = pd.read_csv(file_path)

    # Make Category column text type
    data["Category"] = data["Category"].fillna("").astype(str)

    return data


def save_csv(data, file_path):
    data.to_csv(file_path, index=False)
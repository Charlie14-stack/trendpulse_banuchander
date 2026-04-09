import pandas as pd
import json

# This function handles the cleaning of our raw data
def clean_my_trending_data():
    print("Task 2: Starting the data processing...")

    # Firstly open the raw data file we created in Task 1
    # we use 'raw_trending_data.json' because thats our ingrediant
    with open('raw_trending_data.json', 'r') as my_file:
        raw_info = json.load(my_file)

    # We convert the list of dictionaries into a Table
    df = pd.DataFrame(raw_info)

    # We need to select only the columns we want to show - According to our requirements we need id, title, and body
    cleaned_table = df[['id', 'title', 'body']]

    # index=False means we don't want extra row numbers on the side 
    cleaned_table.to_csv('cleaned_trending_data.csv', index=False)

    print("Success! Created 'cleaned_trending_data.csv'.")

    # Lets show the first 5 rows in the terminal to verify
    print(cleaned_table.head())

if __name__ == "__main__":
    clean_my_trending_data()
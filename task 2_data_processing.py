import pandas as pd
import json
import numpy as np

# Task 2: Cleaning up the messy data and making it a CSV
def clean_my_trending_data():
    # Loading the JSON file I created in Task 1
    with open('raw_trending_data.json', 'r') as my_file:
        raw_info = json.load(my_file)
    
    # Converting the list of dictionaries into a Pandas Table
    df = pd.DataFrame(raw_info)
    
    # Since the sample website doesn't have 'score' or 'category', 
    # I'm adding some random values so I can demonstrate my cleaning skills
    df['score'] = np.random.randint(0, 100, size=len(df))
    df['num_comments'] = np.random.randint(0, 50, size=len(df))
    df['category'] = np.random.choice(['Tech', 'News', 'Science'], size=len(df))
    df.rename(columns={'id': 'post_id'}, inplace=True)

    print(f"Loaded {len(df)} stories from the JSON file.")

    # Removing duplicates based on post_id to keep data unique
    df = df.drop_duplicates(subset=['post_id'])
    print(f"After removing duplicates: {len(df)}")

    # Dropping rows where important info might be missing
    df = df.dropna(subset=['post_id', 'title', 'score'])
    print(f"After removing nulls: {len(df)}")

    # Making sure my numbers are stored as Integers for math later
    df['score'] = df['score'].astype(int)
    df['num_comments'] = df['num_comments'].astype(int)

    # Filtering out low quality stories (score less than 5)
    df = df[df['score'] >= 5]
    print(f"After removing low scores: {len(df)}")

    # Cleaning up the title text by removing extra spaces
    df['title'] = df['title'].str.strip()

    # Saving the final cleaned version to a CSV file
    df.to_csv('cleaned_trending_data.csv', index=False)
    
    print(f"Saved {len(df)} rows to cleaned_trending_data.csv")
    print("\nStories per category:")
    print(df['category'].value_counts())

# Fixed the function call here so it matches the name above
if __name__ == "__main__":
    clean_my_trending_data()
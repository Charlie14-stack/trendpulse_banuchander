import pandas as pd
import numpy as np

# Task 3: Doing actual analysis using Pandas and Numpy
def analyze_trending_data():
     # Loading the cleaned CSV from Task 2
     df = pd.read_csv('cleaned_trending_data.csv')

     print(f"Loaded data shape: {df.shape}")
     print("\nShowing the top of the data:")
     print(df.head())

     # Getting the basic averages using Pandas mean function
     avg_score = df['score'].mean() 
     avg_comments = df['num_comments'].mean()

     print(f"\nAverage score: {avg_score:.2f}")
     print(f"Average comments: {avg_comments:.2f}")

     # Switching to Numpy for more detailed stats
     print("\n --- Numpy Stats ---")

     # Converting the score column into a Numpy array for speed
     score_array = df['score'].to_numpy()

     # Using standard numpy functions for math
     print(f"Mean score    : {np.mean(score_array):.2f}")
     print(f"Median score  : {np.median(score_array):.2f}")
     print(f"Std deviation : {np.std(score_array):.2f}")
     print(f"Highest score : {np.max(score_array)}")
     print(f"Lowest score  : {np.min(score_array)}")

     # Checking which category is trending the most
     popular_category = df['category'].value_counts().idxmax()
     category_count = df['category'].value_counts().max()
     print(f"Top Category: {popular_category} with {category_count} stories")

     # Locating the specific story with the most interaction
     max_comments_row = df.loc[df['num_comments'].idxmax()]
     print(f"Most active story: '{max_comments_row['title']}'")

     # Creating new columns for deeper insight
     # Engagement formula: comments divided by score (plus 1 to avoid divide-by-zero)
     df['engagement'] = df['num_comments'] / (df['score'] + 1)

     # Tagging stories as 'popular' if they beat the average score
     df['is_popular'] = df['score'] > avg_score

     # Saving the final analysis to a new CSV for the final report
     df.to_csv("trends_analysed.csv", index=False)
     print("\nAll done! Analysis saved to 'trends_analysed.csv'.")

if __name__ == "__main__":
     analyze_trending_data()
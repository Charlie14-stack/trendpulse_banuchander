import pandas as pd
import matplotlib.pyplot as plt
import os

# task 4: Noting the analysis results and turning them into visulization charts
def create_visualizations():
    # Firstly Loading the analysed CSV from Task 3
    df = pd.read_csv('trends_analysed.csv')

    print(f"Loaded data shape: {df.shape}")
    print("\nShowing the top of the data:")
    print(df.head())

    # I am creating up a folder to save the charts
    if not os.path.exists('charts'):
        os.makedirs('charts')

    # Creating a Bar chart for category distribution
    plt.figure(figsize=(8, 5))
    df['category'].value_counts().plot(kind='bar', color=['skyblue', 'salmon', 'lightgreen'])
    plt.title('Number of Stories per Category')
    plt.xlabel('Category')
    plt.ylabel('Number of Stories')
    plt.xticks(rotation=0)
    plt.tight_layout()
    plt.savefig('charts/category_distribution.png')
    plt.close()

    # Creating a Scatter plot for score vs comments
    plt.figure(figsize=(8, 5))
    plt.scatter(df['score'], df['num_comments'], alpha=0.6, color='purple')
    plt.title('Score vs Number of Comments')
    plt.xlabel('Score')
    plt.ylabel('Number of Comments')
    plt.grid(True)
    plt.tight_layout()
    plt.savefig('charts/score_vs_comments.png')
    plt.close()

    # Creating a Pie chart for popular vs non-popular stories
    popular_counts = df['is_popular'].value_counts()
    labels = ['Popular', 'Not Popular']
    colors = ['gold', 'lightcoral']
    
    plt.figure(figsize=(6, 6))
    plt.pie(popular_counts, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)
    plt.title('Proportion of Popular Stories')
    plt.axis('equal')  # Equal aspect ratio ensures that pie chart is circular.
    plt.tight_layout()
    plt.savefig('charts/popularity_pie_chart.png')
    plt.close()

    print("All charts have been created and saved in the 'charts' folder.")

if __name__ == "__main__":
    create_visualizations()
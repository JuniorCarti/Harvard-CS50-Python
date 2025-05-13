import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from urllib.request import urlretrieve
import os

def download_wine_data():
    """Download the wine quality dataset from UCI"""
    red_wine_url = "https://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-red.csv"
    white_wine_url = "https://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-white.csv"
    
    try:
        print("Downloading wine quality datasets...")
        urlretrieve(red_wine_url, "winequality-red.csv")
        urlretrieve(white_wine_url, "winequality-white.csv")
        
        # Load both datasets
        red_wine = pd.read_csv("winequality-red.csv", sep=';')
        white_wine = pd.read_csv("winequality-white.csv", sep=';')
        
        # Add wine type column
        red_wine['type'] = 'red'
        white_wine['type'] = 'white'
        
        # Combine datasets
        wine_data = pd.concat([red_wine, white_wine], ignore_index=True)
        
        
       
        
        return wine_data
    
    except Exception as e:
        print(f"Error downloading data: {e}")
        return None

def explore_data(df):
    """Task 1: Explore the dataset"""
    print("\n=== Dataset Overview ===")
    print(f"Shape: {df.shape}")
    print("\nFirst 5 rows:")
    print(df.head())
    
    print("\n=== Data Types ===")
    print(df.dtypes)
    
    print("\n=== Missing Values ===")
    print(df.isnull().sum())
    
    print("\n=== Basic Statistics ===")
    print(df.describe())

def analyze_data(df):
    """Task 2: Perform data analysis"""
    print("\n=== Quality Analysis by Wine Type ===")
    quality_stats = df.groupby('type')['quality'].agg(['mean', 'median', 'std'])
    print(quality_stats)
    
    print("\n=== Feature Correlations ===")
    # Exclude the 'type' column when calculating correlations
    numerical_df = df.drop('type', axis=1)
    print(numerical_df.corr()['quality'].sort_values(ascending=False))
    
    # Interesting finding
    highest_corr = numerical_df.corr()['quality'].abs().sort_values(ascending=False).index[1]
    print(f"\nMost correlated feature with quality: {highest_corr}")

def create_visualizations(df):
    """Task 3: Create required visualizations"""
    plt.figure(figsize=(15, 12))
    
    # 1. Line chart - Alcohol content trend by quality
    plt.subplot(2, 2, 1)
    df.groupby('quality')['alcohol'].mean().plot(kind='line', marker='o')
    plt.title('Average Alcohol Content by Wine Quality')
    plt.xlabel('Quality Score')
    plt.ylabel('Alcohol Content (%)')
    plt.grid(True)
    
    # 2. Bar chart - Quality distribution by wine type
    plt.subplot(2, 2, 2)
    df.groupby(['type', 'quality']).size().unstack().plot(kind='bar', stacked=True)
    plt.title('Quality Distribution by Wine Type')
    plt.xlabel('Wine Type')
    plt.ylabel('Count')
    plt.legend(title='Quality Score')
    
    # 3. Histogram - Alcohol content distribution
    plt.subplot(2, 2, 3)
    df['alcohol'].plot(kind='hist', bins=20, edgecolor='black')
    plt.title('Distribution of Alcohol Content')
    plt.xlabel('Alcohol Content (%)')
    plt.ylabel('Frequency')
    
    # 4. Scatter plot - Alcohol vs. Density (colored by wine type)
    plt.subplot(2, 2, 4)
    colors = {'red': 'red', 'white': 'blue'}
    plt.scatter(df['alcohol'], df['density'], alpha=0.3, c=df['type'].map(colors))
    plt.title('Alcohol Content vs. Density')
    plt.xlabel('Alcohol Content (%)')
    plt.ylabel('Density (g/cm³)')
    
    # Create custom legend for wine types
    from matplotlib.lines import Line2D
    legend_elements = [Line2D([0], [0], marker='o', color='w', label='Red',
                             markerfacecolor='red', markersize=10),
                       Line2D([0], [0], marker='o', color='w', label='White',
                             markerfacecolor='blue', markersize=10)]
    plt.legend(handles=legend_elements, title='Wine Type')
    
    plt.tight_layout()
    plt.savefig('wine_visualizations.png')
    print("\nVisualizations saved as 'wine_visualizations.png'")
    plt.show()

def main():
    """Main execution function"""
    print("=== Wine Quality Analysis ===")
    
    # Download and load data
    wine_data = download_wine_data()
    
    if wine_data is not None:
        # Task 1: Explore data
        explore_data(wine_data)
        
        # Task 2: Analyze data
        analyze_data(wine_data)
        
        # Task 3: Create visualizations
        create_visualizations(wine_data)

if __name__ == "__main__":
    main()
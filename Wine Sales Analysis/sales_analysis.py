"""
WINE QUALITY ANALYSIS SCRIPT
============================

This script performs a comprehensive analysis of wine quality data from the UCI repository.
It loads red and white wine datasets, combines them, and performs:
1. Data exploration
2. Statistical analysis
3. Visualization of key insights

Requirements:
- Python 3.6+
- pandas, matplotlib
- winequality-red.csv and winequality-white.csv in working directory
"""

# Import libraries
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D

def load_wine_data():
    """
    Load and combine wine datasets from local CSV files.
    
    Returns:
        DataFrame: Combined wine data with type column
        None: If files not found
    """
    try:
        # Load datasets with semicolon delimiter
        red = pd.read_csv("winequality-red.csv", sep=';')
        white = pd.read_csv("winequality-white.csv", sep=';')
        
        # Add type identifiers
        red['type'] = 'red'
        white['type'] = 'white'
        
        # Combine and return
        return pd.concat([red, white], ignore_index=True)
        
    except FileNotFoundError:
        print("ERROR: Required files not found.")
        print("Please download and place in working directory:")
        print("- winequality-red.csv")
        print("- winequality-white.csv")
        return None

def analyze_wine_data(df):
    """Perform complete analysis pipeline on wine data"""
    
    # 1. Data Exploration
    print("\n=== DATA EXPLORATION ===")
    print(f"Dataset shape: {df.shape}")
    print("\nFirst 3 samples:")
    print(df.head(3))
    print("\nData types:")
    print(df.dtypes)
    print("\nMissing values:")
    print(df.isnull().sum())
    
    # 2. Statistical Analysis
    print("\n=== STATISTICAL ANALYSIS ===")
    print("\nBasic statistics:")
    print(df.describe())
    
    # Quality by wine type
    print("\nQuality by wine type:")
    print(df.groupby('type')['quality'].agg(['mean', 'median', 'std']))
    
    # Feature correlations
    print("\nTop correlations with quality:")
    numerical = df.select_dtypes(include=['number'])
    print(numerical.corr()['quality'].sort_values(ascending=False).head(5))
    
    # 3. Data Visualization
    print("\nGenerating visualizations...")
    plt.figure(figsize=(15, 10))
    
    # Plot 1: Alcohol vs Quality
    plt.subplot(2, 2, 1)
    df.groupby('quality')['alcohol'].mean().plot(
        kind='line', 
        marker='o',
        color='darkred'
    )
    plt.title('Alcohol Content by Quality')
    plt.xlabel('Quality Rating')
    plt.ylabel('Alcohol %')
    plt.grid(True, alpha=0.3)
    
    # Plot 2: Quality Distribution
    plt.subplot(2, 2, 2)
    df['quality'].value_counts().sort_index().plot(
        kind='bar',
        color='steelblue'
    )
    plt.title('Quality Score Distribution')
    plt.xlabel('Quality Score')
    plt.ylabel('Count')
    
    # Plot 3: Feature Comparison
    plt.subplot(2, 2, 3)
    df.groupby('type')['alcohol'].mean().plot(
        kind='bar',
        color=['red', 'lightblue']
    )
    plt.title('Average Alcohol by Wine Type')
    plt.ylabel('Alcohol %')
    
    # Plot 4: Alcohol vs Density
    plt.subplot(2, 2, 4)
    colors = {'red': 'red', 'white': 'blue'}
    plt.scatter(
        df['alcohol'],
        df['density'],
        alpha=0.3,
        c=df['type'].map(colors)
    )
    plt.title('Alcohol vs Density')
    plt.xlabel('Alcohol %')
    plt.ylabel('Density')
    
    # Add legend
    legend = [
        Line2D([0], [0], marker='o', color='w', label='Red',
               markerfacecolor='red', markersize=10),
        Line2D([0], [0], marker='o', color='w', label='White',
               markerfacecolor='blue', markersize=10)
    ]
    plt.legend(handles=legend, title='Wine Type')
    
    # Save and show
    plt.tight_layout()
    plt.savefig('wine_analysis.png', dpi=150)
    plt.show()
    
    print("\nAnalysis complete! Results saved to wine_analysis.png")

def main():
    """Main execution function"""
    print("WINE QUALITY ANALYSIS")
    print("=====================")
    
    # Load data
    wine_data = load_wine_data()
    
    # Analyze if data loaded
    if wine_data is not None:
        analyze_wine_data(wine_data)

# Run script
if __name__ == "__main__":
    main()
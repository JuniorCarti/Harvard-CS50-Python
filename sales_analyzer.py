import pandas as pd
import matplotlib.pyplot as plt

def analyze_sales_data():
    # Load the CSV file
    try:
        df = pd.read_csv('sales_data.csv')
    except FileNotFoundError:
        print("Error: sales_data.csv file not found.")
        return
    
    # Data cleaning and preparation
    df['Date'] = pd.to_datetime(df['Date'])
    
    # Calculate total revenue
    total_revenue = df['Revenue ($)'].sum()
    
    # Find best-selling product
    best_selling = df.loc[df['Quantity Sold'].idxmax()]
    best_selling_product = best_selling['Product']
    best_selling_quantity = best_selling['Quantity Sold']
    
    # Identify day with highest sales (by revenue)
    daily_sales = df.groupby('Date')['Revenue ($)'].sum()
    highest_sales_day = daily_sales.idxmax().strftime('%Y-%m-%d')
    highest_sales_amount = daily_sales.max()
    
    # Save results to text file
    with open('sales_summary.txt', 'w') as f:
        f.write(f"Total Revenue: ${total_revenue:,.2f}\n")
        f.write(f"Best-Selling Product: {best_selling_product} ({best_selling_quantity} units sold)\n")
        f.write(f"Highest Sales Day: {highest_sales_day} (${highest_sales_amount:,.2f})\n")
    
    # Print insights
    print("\n=== Sales Insights ===")
    print(f"Total Revenue: ${total_revenue:,.2f}")
    print(f"Best-Selling Product: {best_selling_product} ({best_selling_quantity} units sold)")
    print(f"Highest Sales Day: {highest_sales_day} (${highest_sales_amount:,.2f})")
    print("\nResults saved to sales_summary.txt")
    
    # Bonus: Visualization
    plt.figure(figsize=(12, 6))
    
    # Plot 1: Daily Revenue Trend
    plt.subplot(1, 2, 1)
    daily_sales.plot(kind='line', marker='o', color='b')
    plt.title('Daily Revenue Trend')
    plt.xlabel('Date')
    plt.ylabel('Revenue ($)')
    plt.grid(True)
    
    # Plot 2: Product Sales Breakdown
    plt.subplot(1, 2, 2)
    product_sales = df.groupby('Product')['Quantity Sold'].sum()
    product_sales.plot(kind='bar', color='g')
    plt.title('Product Sales by Quantity')
    plt.xlabel('Product')
    plt.ylabel('Units Sold')
    plt.xticks(rotation=45)
    
    plt.tight_layout()
    plt.savefig('sales_visualization.png')
    print("\nVisualization saved as sales_visualization.png")
    
    # Show plot (optional)
    # plt.show()

if __name__ == "__main__":
    analyze_sales_data()
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import os

def run_rv():
    print("\033[1;33m[BLOOMBERG RV] Generating Alpha Trend with Terminal Focus...\033[0m")
    
    # Data including today's specific close from your screenshot
    data = {
        'Date': ['2025-10-01', '2025-11-13', '2025-12-11', '2026-01-14', '2026-02-11', '2026-03-24'],
        'IBM': [283.30, 303.13, 308.98, 307.28, 272.81, 240.59], # Updated to 240.59
        'NASDAQ': [23319.0, 23324.0, 25424.0, 23471.0, 23066.0, 21761.89] # Updated to Match Screen
    }

    df = pd.DataFrame(data)
    df['Date'] = pd.to_datetime(df['Date'])

    # Normalizing
    df['IBM_Norm'] = (df['IBM'] / df['IBM'].iloc[0]) * 100
    df['NASDAQ_Norm'] = (df['NASDAQ'] / df['NASDAQ'].iloc[0]) * 100

    plt.figure(figsize=(12, 7))
    plt.style.use('dark_background')
    sns.set_style("whitegrid", {'axes.facecolor': 'black', 'grid.color': '#333333'})

    # Plotting Trends
    plt.plot(df['Date'], df['IBM_Norm'], label='IBM (Normalized)', marker='o', linewidth=3, color='#0066CC')
    plt.plot(df['Date'], df['NASDAQ_Norm'], label='NASDAQ Composite', linestyle='--', marker='s', color='#FF5733', alpha=0.7)

    # FOCUS: Today's Value Annotation
    today_val = df['IBM_Norm'].iloc[-1]
    today_date = df['Date'].iloc[-1]
    
    plt.annotate(f'CURRENT: $240.59\n({today_val:.1f} pts)', 
                 xy=(today_date, today_val), 
                 xytext=(today_date, today_val + 5),
                 arrowprops=dict(facecolor='#00FF00', shrink=0.05),
                 fontsize=10, color='#00FF00', fontweight='bold', ha='center')

    plt.title('IBM vs. NASDAQ: Relative Alpha & Terminal Value Focus', fontsize=14, pad=20)
    plt.ylabel('Baseline Index (Oct 2025 = 100)')
    plt.legend(loc='upper right')
    plt.xticks(rotation=45)
    plt.tight_layout()

    # Save for deployment
    plt.savefig('IBM_RV_Focus.png', facecolor='black')
    print(f"\033[1;32m[DEPLOYED]\033[0m Focused Trend Image: {os.getcwd()}/IBM_RV_Focus.png")

if __name__ == "__main__":
    run_rv()

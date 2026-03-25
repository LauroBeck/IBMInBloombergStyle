import pandas as pd
import matplotlib.pyplot as plt
import os

def run_treasury_audit():
    print("\033[1;36m[TREASURY AISP] Aggregating Multi-Bank Liquidity (v3.1)... \033[0m")
    
    # Data based on your BNY/JPM/WFB Gateway Simulation
    data = {
        'Bank': ['JPMorgan (JPM)', 'BNY Mellon (BNY)', 'Wells Fargo (WFB)'],
        'BICFI': ['CHASUS33', 'BONYUS33', 'WELSUS66'],
        'Liquidity_USD': [3500000.00, 2850000.00, 2200000.00],
        'Status': ['ONLINE', 'ONLINE', 'ONLINE']
    }

    df = pd.DataFrame(data)
    total_liquidity = df['Liquidity_USD'].sum()

    # Visual: Liquidity Distribution Chart
    plt.figure(figsize=(10, 6))
    plt.style.use('dark_background')
    colors = ['#113355', '#D4AF37', '#ED1727'] # Bank-specific branding colors
    
    plt.pie(df['Liquidity_USD'], labels=df['Bank'], autopct='%1.1f%%', colors=colors, startangle=140)
    plt.title(f"Consolidated Treasury Liquidity: ${total_liquidity:,.2f}", color='white', pad=20)
    
    filename = "Treasury_Liquidity_Audit.png"
    plt.savefig(filename, facecolor='black')
    
    print(f"\033[1;32m[SUCCESS]\033[0m Total Liquidity: ${total_liquidity:,.2f}")
    print(f"Audit Image: {os.getcwd()}/{filename}")

if __name__ == "__main__":
    run_treasury_audit()

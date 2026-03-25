import yfinance as yf
import plotly.graph_objects as go
import sys
import os

def run_gp(ticker):
    print(f"\033[1;33m[BLOOMBERG GP] Building Image for {ticker}...\033[0m")
    
    try:
        df = yf.download(ticker, period="6mo", interval="1d")
        
        fig = go.Figure(data=[go.Candlestick(
            x=df.index, open=df['Open'], high=df['High'], 
            low=df['Low'], close=df['Close'],
            increasing_line_color='#00FF00', 
            decreasing_line_color='#FF0000'
        )])

        fig.update_layout(
            title=f"{ticker} US Equity - GP HISTORICAL PRICE",
            template="plotly_dark",
            paper_bgcolor="#000000",
            plot_bgcolor="#000000",
            xaxis_rangeslider_visible=False,
            width=1000, height=600,
            font=dict(color="#00FF00", family="Monospace")
        )

        filename = f"{ticker}_GP.png"
        # Writing image using the installed kaleido engine
        fig.write_image(filename)
        
        print(f"\033[1;32m[DEPLOYED]\033[0m Image saved to: {os.getcwd()}/{filename}")
        
    except Exception as e:
        print(f"\033[1;31m[CRITICAL ERROR]\033[0m {e}")

if __name__ == "__main__":
    ticker = sys.argv[1] if len(sys.argv) > 1 else "IBM"
    run_gp(ticker)

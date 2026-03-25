#!/bin/bash

# 1. Self-Healing VENV (Hardened for Matplotlib/Seaborn)
if [ ! -d "venv" ]; then
    python3 -m venv venv
fi
./venv/bin/pip install --upgrade pip
./venv/bin/pip install yfinance pandas plotly kaleido matplotlib seaborn

# 2. Compile C++
[ "bloomberg.cpp" -nt "bloomberg_bin" ] || [ ! -f "bloomberg_bin" ] && g++ -O3 bloomberg.cpp -o bloomberg_bin
[ "bloomberg_des.cpp" -nt "bloomberg_des_bin" ] || [ ! -f "bloomberg_des_bin" ] && g++ -O3 bloomberg_des.cpp -o bloomberg_des_bin

# 3. Routing
TICKER=${1:-"IBM"}
MODE=${2:-"BDP"}

case $MODE in
    "RV") ./venv/bin/python3 bbg_rv.py ;;
    "GP") ./venv/bin/python3 bbg_sim.py $TICKER ;;
    "BDP") ./bloomberg_bin $TICKER ;;
    "DES") ./bloomberg_des_bin $TICKER ;;
    "FA")
        echo -e "\033[1;37;44m $TICKER US Equity             Financial Analysis (FA) \033[0m"
        ./venv/bin/python3 -c "
import yfinance as yf
import pandas as pd
s = yf.Ticker('$TICKER')
df = s.income_stmt.iloc[:, :2]
fmt = lambda x: f'{x/1e9:>10.2f}B' if abs(x) >= 1e9 else (f'{x/1e6:>10.2f}M' if abs(x) >= 1e6 else f'{x:11.2f}')
print(df.map(fmt) if hasattr(df, 'map') else df.applymap(fmt))
"
        ;;
    *) echo "Usage: ./edit_market.sh [TICKER] [RV|GP|BDP|DES|FA]" ;;
esac

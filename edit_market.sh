#!/bin/bash

# 1. Environment Sync
[ ! -d "venv" ] && python3 -m venv venv
./venv/bin/pip install --quiet --upgrade pip
./venv/bin/pip install --quiet yfinance pandas plotly kaleido matplotlib seaborn qiskit qiskit-aer

# 2. Compile C++ Core (Architecture Tier)
[ ! -f "bloomberg_bin" ] && g++ -O3 bloomberg.cpp -o bloomberg_bin
[ ! -f "bloomberg_des_bin" ] && g++ -O3 bloomberg_des.cpp -o bloomberg_des_bin

# 3. Command Routing
TICKER=${1:-"IBM"}
MODE=${2:-"BDP"}

case $MODE in
    "AISP") ./venv/bin/python3 bbg_treasury.py ;;
    "QNTM") ./venv/bin/python3 bbg_quantum.py ;;
    "RV") ./venv/bin/python3 bbg_rv.py ;;
    "GP") ./venv/bin/python3 bbg_sim.py $TICKER ;;
    "BDP") ./bloomberg_bin $TICKER ;;
    "DES") ./bloomberg_des_bin $TICKER ;;
    "FA")
        ./venv/bin/python3 -c "import yfinance as yf; s=yf.Ticker('$TICKER'); print(s.income_stmt.iloc[:,:2])"
        ;;
    *) echo "Usage: ./edit_market.sh [TICKER] [AISP|QNTM|RV|GP|BDP|DES|FA]" ;;
esac

#!/bin/bash
TICKER=${1:-"IBM"}

# Standard Bloomberg Green/White Header
echo -e "\033[1;37;44m EXECUTING FULL ARCHITECTURAL AUDIT: $TICKER \033[0m"
echo "--------------------------------------------------"

# 1. Real-time Snapshot (BDP) - C++
./edit_market.sh $TICKER BDP
echo ""

# 2. Company Description (DES) - C++
./edit_market.sh $TICKER DES
echo ""

# 3. Financial Analysis (FA) - Python
./edit_market.sh $TICKER FA
echo "--------------------------------------------------"

# 4. Generate Standard GP Chart (Candlestick)
echo "Generating Standard GP Image..."
./edit_market.sh $TICKER GP

# 5. NEW: Generate Relative Alpha Focus (RV)
# This uses your March 24th telemetry for IBM vs NASDAQ comparison
if [ "$TICKER" == "IBM" ]; then
    echo "Generating Relative Alpha Focus (RV) Image..."
    ./edit_market.sh $TICKER RV
fi

echo "--------------------------------------------------"
echo "Audit Complete."
echo "View Results: ${TICKER}_GP.png | ${TICKER}_RV_Focus.png"

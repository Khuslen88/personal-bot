# Forex Chart

## Description
Generate a historical price chart for any currency pair, showing recent price movement as an ASCII chart or by saving a PNG image.

## Trigger
When the user asks about:
- Price charts or graphs for currencies (e.g., "chart for EUR/USD", "show me USD/JPY graph")
- Historical price movement (e.g., "how has the dollar moved this month")
- Forex trends or price history (e.g., "EUR/USD trend last 30 days")

## Instructions

1. Parse the user's message to identify:
   - The currency pair (FROM/TO)
   - The time period (default: 30 days). Accept: "1w", "1m", "3m", "6m", "1y"

2. Run the chart script:
   ```bash
   python3 scripts/forex_chart.py <FROM> <TO> [PERIOD]
   ```
   Period options: 7, 30, 90, 180, 365 (days)

3. The script outputs:
   - An ASCII chart of closing prices for the terminal
   - Summary statistics (open, close, high, low, change %)

4. Format the response:
   ```
   📈 <FROM>/<TO> — Last <N> days

   <ASCII chart>

   Open:   <price>
   Close:  <price>
   High:   <price>
   Low:    <price>
   Change: <+/-percent>%
   ```

## Edge Cases
- If the pair is invalid, yfinance returns empty data — inform the user
- If period is not specified, default to 30 days
- Weekends/holidays have no data — this is normal for forex

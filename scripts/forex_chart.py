#!/usr/bin/env python3
"""Generate ASCII price charts for currency pairs using yfinance."""

import sys
import json

try:
    import yfinance as yf
except ImportError:
    print(json.dumps({"error": "yfinance not installed. Run: pip install yfinance"}))
    sys.exit(1)


def make_ascii_chart(prices: list[float], width: int = 50, height: int = 15) -> str:
    """Render a simple ASCII line chart."""
    if not prices:
        return ""

    min_p = min(prices)
    max_p = max(prices)
    spread = max_p - min_p if max_p != min_p else 1

    # Resample to fit width
    step = max(1, len(prices) // width)
    sampled = [prices[i] for i in range(0, len(prices), step)][:width]

    lines = []
    for row in range(height, -1, -1):
        threshold = min_p + (spread * row / height)
        line = ""
        for val in sampled:
            if val >= threshold:
                line += "█"
            else:
                line += " "
        price_label = f"{threshold:.4f}" if spread < 0.1 else f"{threshold:.2f}"
        lines.append(f"{price_label:>10} │{line}")

    lines.append(" " * 10 + " └" + "─" * len(sampled))
    return "\n".join(lines)


def fetch_chart(base: str, target: str, days: int = 30) -> dict:
    """Fetch historical data and generate chart."""
    base = base.upper()
    target = target.upper()

    ticker = f"{base}{target}=X"
    period_map = {7: "7d", 30: "1mo", 90: "3mo", 180: "6mo", 365: "1y"}
    period = period_map.get(days, "1mo")

    data = yf.download(ticker, period=period, progress=False, auto_adjust=True)

    if data.empty:
        return {"error": f"No data found for {base}/{target}. Check currency codes."}

    closes = data["Close"].dropna().values.flatten().tolist()

    if len(closes) < 2:
        return {"error": f"Not enough data for {base}/{target}."}

    chart = make_ascii_chart(closes)
    open_price = closes[0]
    close_price = closes[-1]
    high = max(closes)
    low = min(closes)
    change_pct = ((close_price - open_price) / open_price) * 100

    return {
        "pair": f"{base}/{target}",
        "days": days,
        "data_points": len(closes),
        "chart": chart,
        "open": round(open_price, 4),
        "close": round(close_price, 4),
        "high": round(high, 4),
        "low": round(low, 4),
        "change_percent": round(change_pct, 2),
    }


def main():
    if len(sys.argv) < 3:
        print(json.dumps({"error": "Usage: forex_chart.py <FROM> <TO> [DAYS]"}))
        sys.exit(1)

    base = sys.argv[1]
    target = sys.argv[2]
    days = int(sys.argv[3]) if len(sys.argv) > 3 else 30

    result = fetch_chart(base, target, days)
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()

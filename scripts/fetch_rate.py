#!/usr/bin/env python3
"""Fetch live exchange rates from a free public API."""

import sys
import json
import urllib.request
import urllib.error


API_URL = "https://open.er-api.com/v6/latest/{base}"


def fetch_rate(base: str, target: str, amount: float | None = None) -> dict:
    """Fetch exchange rate and optionally convert an amount.

    TODO(human): Implement the response formatting logic.
    Given the raw API data, decide how to structure the output dict
    that gets printed as JSON for Claude to read.

    Args:
        base: Source currency code (e.g., 'USD')
        target: Target currency code (e.g., 'EUR')
        amount: Optional amount to convert

    Returns:
        dict with rate info and optional conversion
    """
    base = base.upper()
    target = target.upper()

    url = API_URL.format(base=base)
    try:
        with urllib.request.urlopen(url, timeout=10) as resp:
            data = json.loads(resp.read().decode())
    except urllib.error.URLError:
        return {"error": f"Could not reach the exchange rate API. Try again later."}

    if data.get("result") != "success":
        return {"error": f"API error: {data.get('error-type', 'unknown')}"}

    rates = data.get("rates", {})
    if target not in rates:
        available = ", ".join(sorted(rates.keys()))
        return {"error": f"Unknown currency code '{target}'. Available: {available}"}

    rate = rates[target]
    decimals = 2 if rate > 0.01 else 6

    result = {
        "base": base,
        "target": target,
        "rate": round(rate, decimals),
        "display": f"1 {base} = {round(rate, decimals)} {target}",
    }

    if amount is not None:
        converted = round(amount * rate, 2)
        result["amount"] = amount
        result["converted"] = converted
        result["conversion_display"] = f"{amount} {base} = {converted} {target}"

    return result


def main():
    if len(sys.argv) < 3:
        print(json.dumps({"error": "Usage: fetch_rate.py <FROM> <TO> [AMOUNT]"}))
        sys.exit(1)

    base = sys.argv[1]
    target = sys.argv[2]
    amount = float(sys.argv[3]) if len(sys.argv) > 3 else None

    result = fetch_rate(base, target, amount)
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()

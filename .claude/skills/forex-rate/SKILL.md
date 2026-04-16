# Forex Rate Lookup

## Description
Look up live exchange rates for any currency pair and optionally convert amounts between currencies.

## Trigger
When the user asks about:
- Exchange rates between currencies (e.g., "EUR/USD rate", "dollar to yen")
- Currency conversion (e.g., "convert 100 USD to MNT")
- Forex prices or currency values

## Instructions

1. Parse the user's message to identify:
   - The source currency (FROM)
   - The target currency (TO)
   - An optional amount to convert

2. Use standard 3-letter ISO 4217 currency codes. Common mappings:
   - dollar/USD, euro/EUR, pound/GBP, yen/JPY, tugrik/MNT
   - yuan/CNY, won/KRW, ruble/RUB, rupee/INR

3. Run the fetch script to get the live rate:
   ```bash
   python3 scripts/fetch_rate.py <FROM> <TO> [AMOUNT]
   ```

4. Format the response clearly:
   - Show the currency pair and current rate
   - If an amount was given, show the converted value
   - Round to 2 decimal places (4 for small rates like JPY pairs)

5. If the script returns an error, inform the user that the currency code may be invalid or the rate service is temporarily unavailable.

## Example Responses

**Rate lookup:**
> USD/EUR: 1 USD = 0.9234 EUR
> (Updated just now)

**Conversion:**
> 100 USD = 92.34 EUR
> Rate: 1 USD = 0.9234 EUR

## Edge Cases
- If no target currency is specified, default to USD
- If currency code is not recognized, suggest the closest match
- If the API is down, apologize and suggest trying again later

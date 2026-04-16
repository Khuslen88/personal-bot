# Weather Lookup

## Description
Get current weather conditions for any city worldwide.

## Trigger
When the user asks about:
- Current weather (e.g., "weather in Tokyo", "what's the weather like in UB")
- Temperature or conditions (e.g., "is it cold in New York", "how hot is it in Dubai")
- Weather forecasts (e.g., "will it rain in London tomorrow")

## Instructions

1. Identify the city from the user's message. Handle common abbreviations:
   - "UB" → Ulaanbaatar
   - "NYC" → New York
   - "LA" → Los Angeles

2. Fetch weather data using the wttr.in service (no API key needed):
   ```bash
   curl -s "wttr.in/<city>?format=j1" 2>/dev/null
   ```

3. From the JSON response, extract:
   - `current_condition[0]` for current weather
   - Key fields: `temp_C`, `temp_F`, `weatherDesc`, `humidity`, `windspeedKmph`, `FeelsLikeC`

4. Format the response:
   ```
   🌤️ Weather in <City>

   Temperature: <temp>°C (<temp>°F)
   Feels like:  <feels_like>°C
   Condition:   <description>
   Humidity:    <humidity>%
   Wind:        <wind_speed> km/h
   ```

5. If the user asks for a forecast, also include tomorrow's data from `weather[1]`:
   ```
   📅 Tomorrow: <max>°C / <min>°C — <description>
   ```

## Edge Cases
- If the city is not found, wttr.in returns an error — ask the user to check the spelling
- If the service is down, inform the user and suggest trying again later
- For ambiguous city names, wttr.in picks the most popular one — this is fine

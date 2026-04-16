# News Researcher

## Description
Search the web for recent news on any topic and provide a concise, well-formatted summary with key points and sources.

## Trigger
When the user asks about:
- Recent news or current events (e.g., "news about AI", "what's happening in Mongolia")
- Headlines or updates on a topic (e.g., "latest Bitcoin news")
- Summarizing what's going on with a subject (e.g., "what's new with SpaceX")

## Instructions

1. Identify the topic the user is asking about from their message.

2. Use the WebSearch tool to search for recent news on the topic. Use a query like:
   - `"<topic> latest news"`
   - `"<topic> recent developments"`

3. From the search results, pick the **top 3-5 most relevant and recent** articles.

4. For each article, use WebFetch if needed to get more detail, then summarize the key point in 1-2 sentences.

5. Format the response as:
   ```
   📰 News: <Topic>

   1. **<Headline>** — <1-2 sentence summary>
      Source: <publication name>

   2. **<Headline>** — <1-2 sentence summary>
      Source: <publication name>

   3. **<Headline>** — <1-2 sentence summary>
      Source: <publication name>

   Last updated: <current date>
   ```

6. Keep summaries factual and neutral. Do not editorialize.

## Edge Cases
- If the topic is too vague (e.g., just "news"), ask the user to be more specific
- If no recent news is found, say so and suggest related topics
- If a source is behind a paywall, summarize from the search snippet instead
- Always include at least the publication name as attribution

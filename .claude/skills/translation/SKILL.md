# Translation

## Description
Translate text between languages using a free translation API.

## Trigger
When the user asks to:
- Translate text (e.g., "translate hello to Japanese", "how do you say goodbye in Mongolian")
- Understand foreign text (e.g., "what does 'сайн байна уу' mean")
- Convert between languages (e.g., "English to Korean: thank you")

## Instructions

1. Parse the user's message to identify:
   - The text to translate
   - The source language (auto-detect if not specified)
   - The target language

2. Use standard language codes. Common mappings:
   - English/en, Mongolian/mn, Japanese/ja, Korean/ko, Chinese/zh
   - Spanish/es, French/fr, German/de, Russian/ru, Arabic/ar

3. Run the translation script:
   ```bash
   python3 scripts/translate.py "<text>" <target_lang> [source_lang]
   ```
   If source_lang is omitted, it auto-detects.

4. Format the response:
   ```
   🌐 Translation (<source> → <target>)

   Original:    <source text>
   Translation: <translated text>
   ```

5. If translating to/from Mongolian, also include the transliteration if helpful.

## Edge Cases
- If the language is not recognized, list common language codes
- If translation fails, suggest checking the text or trying a different language pair
- Very long texts (>500 chars) should be warned about potential truncation

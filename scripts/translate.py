#!/usr/bin/env python3
"""Translate text between languages using the MyMemory free API."""

import sys
import json
import urllib.request
import urllib.error
import urllib.parse


API_URL = "https://api.mymemory.translated.net/get"

LANG_ALIASES = {
    "english": "en", "mongolian": "mn", "japanese": "ja", "korean": "ko",
    "chinese": "zh", "spanish": "es", "french": "fr", "german": "de",
    "russian": "ru", "arabic": "ar", "italian": "it", "portuguese": "pt",
    "turkish": "tr", "hindi": "hi", "thai": "th", "vietnamese": "vi",
}


def resolve_lang(lang: str) -> str:
    """Resolve language name or code to a 2-letter code."""
    lang = lang.lower().strip()
    return LANG_ALIASES.get(lang, lang)


def translate(text: str, target: str, source: str = "auto") -> dict:
    """Translate text using MyMemory API."""
    target = resolve_lang(target)
    source = resolve_lang(source) if source != "auto" else "auto"

    if len(text) > 500:
        text = text[:500]
        truncated = True
    else:
        truncated = False

    lang_pair = f"{source}|{target}" if source != "auto" else f"en|{target}"

    params = urllib.parse.urlencode({"q": text, "langpair": lang_pair})
    url = f"{API_URL}?{params}"

    try:
        with urllib.request.urlopen(url, timeout=10) as resp:
            data = json.loads(resp.read().decode())
    except urllib.error.URLError:
        return {"error": "Could not reach the translation service. Try again later."}

    if data.get("responseStatus") != 200:
        return {"error": f"Translation failed: {data.get('responseDetails', 'unknown error')}"}

    translated = data["responseData"]["translatedText"]

    result = {
        "original": text,
        "translated": translated,
        "source_lang": source if source != "auto" else "auto-detected",
        "target_lang": target,
    }

    if truncated:
        result["warning"] = "Text was truncated to 500 characters."

    return result


def main():
    if len(sys.argv) < 3:
        print(json.dumps({"error": "Usage: translate.py \"<text>\" <target_lang> [source_lang]"}))
        sys.exit(1)

    text = sys.argv[1]
    target = sys.argv[2]
    source = sys.argv[3] if len(sys.argv) > 3 else "auto"

    result = translate(text, target, source)
    print(json.dumps(result, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()

import openai

import openai

openai.api_key = "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"

def summarize_email(body_text: str) -> str:
    try:
        response = openai.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are a helpful assistant that summarizes emails concisely."},
                {"role": "user", "content": f"Summarize this email:\n\n{body_text}"}
            ]
        )
        summary = response.choices[0].message.content.strip()
        return summary
    except Exception as e:
        return f"[Σφάλμα περίληψης: {str(e)}]"


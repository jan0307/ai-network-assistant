import os
from dotenv import load_dotenv
from google import genai
load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)
def fraga_ai(problem):
    try:
        prompt = f"""
Du är en AI Network Assistant.
Din uppgift är att hjälpa användaren felsöka nätverksproblem.

Användarens problem:
{problem}

Förklara den troliga orsaken på ett enkelt sätt.
Ge sedan felsökningssteg i rätt ordning.
Svara med ren text utan Markdown-symboler som #, * eller **.
"""
        response = client.models.generate_content(
            model="gemini-3.6-flash",
            contents=prompt
        )
        return response.text
    except Exception as error:
        return f"AI-tjänsten kunde inte svara. fel: {error}"
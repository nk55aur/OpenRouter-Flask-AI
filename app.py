from flask import Flask, render_template, request, redirect, url_for, jsonify
from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)

client = None
OPENROUTER_KEY = os.getenv("OPENROUTER_API_KEY")
if OPENROUTER_KEY:
    client = OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key=OPENROUTER_KEY
    )

# Development mock flag. If true or if no API key present, use canned responses for UI testing.
DEV_MOCK = os.getenv('DEV_MOCK', 'false').lower() in ('1', 'true', 'yes')

def get_ai_response(user_input, task_type):
    # Support explicit tasks and an "auto" mode which asks the model to detect intent
    if task_type == "question":
        prompt = f"Answer clearly and briefly: {user_input}"
    elif task_type == "summary":
        prompt = f"Summarize this text: {user_input}"
    elif task_type == "creative":
        prompt = f"Write a creative paragraph or short story about: {user_input}"
    elif task_type == "auto":
        # Ask the model to detect intent and perform it. Keep prompt explicit for reliability.
        prompt = (
            "You are an assistant that first identifies user intent (one of: question, summary, creative, debug) "
            "and then performs the requested action. Reply only with the performed result — do not add extra labels.\n"
            f"User: {user_input}"
        )
    else:
        prompt = user_input

    # If in DEV_MOCK mode or no client configured, return a canned response for faster local testing.
    if DEV_MOCK or client is None:
        return get_mock_response(user_input)

    try:
        response = client.chat.completions.create(
            model="openai/gpt-oss-20b",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7,
            max_tokens=300
        )
        # Safely access nested fields
        try:
            return response.choices[0].message.content.strip()
        except Exception:
            # Fallback if response shape differs
            return str(response)
    except Exception as e:
        return f"⚠️ Error: {e}"


def get_mock_response(user_input: str) -> str:
    """Return a simple canned response depending on detected keywords. Helpful for UI testing without API key."""
    text = user_input.lower()
    if any(k in text for k in ("summarize", "summary", "summarise")):
        return "(MOCK) Summary: This is a short summary of the text you provided."
    if any(k in text for k in ("debug", "error", "stack")):
        return "(MOCK) Debug suggestion: Check for missing imports and ensure variables are defined."
    if text.strip().endswith('?') or any(k in text for k in ("what","who","how","why","when")):
        return "(MOCK) Answer: Here's a concise answer to your question."
    if any(k in text for k in ("story","creative","write","imagine")):
        return "(MOCK) Creative: Once upon a time, in a neon city, a robot learned to listen and help developers..."
    # fallback
    return "(MOCK) I received your input and auto-detected intent. This is a mock response for development."

@app.route("/", methods=["GET", "POST"])
def index():
    result = ""
    if request.method == "POST":
        user_input = request.form.get("user_input", "").strip()
        if not user_input:
            result = "⚠️ Please enter some text."
        else:
            # form no longer supplies explicit task — default to auto intent
            result = get_ai_response(user_input, 'auto')
    return render_template("index.html", result=result)


@app.route('/api/ask', methods=['POST'])
def api_ask():
    data = request.get_json() or {}
    task = data.get('task')
    user_input = (data.get('user_input') or '').strip()
    if not user_input:
        return jsonify({'error': 'Please enter some text.'}), 400
    # default to auto intent detection when not provided
    task_type = task if task else 'auto'
    result = get_ai_response(user_input, task_type)
    return jsonify({'result': result})


if __name__ == "__main__":
    app.run(debug=True)

import os
import requests
from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)

# Development mock flag for UI testing without API key
DEV_MOCK = os.getenv('DEV_MOCK', 'false').lower() in ('1', 'true', 'yes')
OPENROUTER_KEY = os.getenv("OPENROUTER_API_KEY")

def get_ai_response(user_input, task_type):
    if task_type == "question":
        prompt = f"Answer clearly and briefly: {user_input}"
    elif task_type == "summary":
        prompt = f"Summarize this text: {user_input}"
    elif task_type == "creative":
        prompt = f"Write a creative paragraph or short story about: {user_input}"
    else:
        prompt = (
            "Detect whether the user wants: question answering, summarization,"
            " or creative writing — then perform it directly.\n"
            f"User: {user_input}"
        )

    # Mock fallback mode
    if DEV_MOCK or not OPENROUTER_KEY:
        return get_mock_response(user_input)

    headers = {
        "Authorization": f"Bearer {OPENROUTER_KEY}",
        "Content-Type": "application/json"
    }

    body = {
        "model": "gryphe/mythomax-l2-13b",
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 0.7
    }

    try:
        response = requests.post(
            "https://openrouter.ai/api/v1/chat/completions",
            headers=headers,
            json=body,
            timeout=30
        )
        response.raise_for_status()
        data = response.json()
        return data["choices"][0]["message"]["content"].strip()
    except Exception as e:
        return f"⚠️ API Error: {e}"

def get_mock_response(user_input: str) -> str:
    text = user_input.lower()
    if any(k in text for k in ("summarize", "summary", "summarise")):
        return "(MOCK) Summary: This is a short summary of your text."
    if any(k in text for k in ("debug", "error", "issue")):
        return "(MOCK) Debug suggestion: Check imports and variable definitions."
    if text.strip().endswith('?') or any(k in text for k in ("what","who","why","how")):
        return "(MOCK) Answer: Here is a helpful response to your question!"
    if any(k in text for k in ("story","imagine","creative")):
        return "(MOCK) Creative: A robot discovered friendship in lines of code..."
    return "(MOCK) Auto-detected intent. This is a mock response."

@app.route("/", methods=["GET", "POST"])
def index():
    result = ""
    if request.method == "POST":
        user_input = request.form.get("user_input", "").strip()
        if not user_input:
            result = "⚠️ Please enter some text."
        else:
            result = get_ai_response(user_input, 'auto')
    return render_template("index.html", result=result)

@app.route("/api/ask", methods=["POST"])
def api_ask():
    data = request.get_json() or {}
    user_input = (data.get('user_input') or '').strip()
    task = data.get("task") or "auto"
    if not user_input:
        return jsonify({"error": "Missing input"}), 400

    output = get_ai_response(user_input, task)
    return jsonify({"result": output})

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")

AI Assistant Development using OpenRouter API:

AI-powered web assistant built using Flask and the OpenRouter API with smart intent detection and real-time chat interface. Developed during my internship to demonstrate backend development, prompt engineering, and frontend UI integration.

The assistant supports:
✨ Question Answering
✨ Text Summarization
✨ Creative Writing Generation
with real-time responses via a clean, responsive web interface.

🌟 Key Highlights

🔹 Multi-mode AI assistant (Q&A, Summary, Creative).

🔹 Integrated OpenRouter API for open-source models (free & flexible).

🔹 Secure environment-based API key handling using .env.

🔹 Fast backend using Flask with modular architecture.

🔹 Error-handling for API failures, rate limits, and invalid keys.

🔹 Optimized prompts designed during internship training.

🔹 Ready for deployment on Render, Railway, or Vercel.

🔹 Fully documented with screenshots and structured report.

🎯 Objective of the Project

To build a lightweight, cost-efficient AI assistant that demonstrates prompt engineering, API routing, and web integration skills, while avoiding dependency on costly APIs like OpenAI.


# OpenRouter-Flask-AI

Lightweight, self-hosted AI assistant built with Flask and the OpenRouter API. The app provides a minimal, Jarvis-like two-box UI (Input + Output) with a central animated robot indicator and automatic intent detection (questions, summaries, creative writing, debugging).

This repository is designed for local development and easy deployment. A `DEV_MOCK` mode is available so you can test the UI without an API key.

---

## Features

- Minimal two-panel UI: Input (left) + Animated Robot (center) + Output (right).
- Auto-intent detection: backend classifies user input and performs the appropriate action.
- Animated "thinking" robot and typewriter response effect for polished UX.
- Dev mock mode (`DEV_MOCK`) returns canned responses for offline testing.
- Simple JSON API endpoint for integration: `POST /api/ask`.

---

## Quickstart (Windows PowerShell)

1. Clone the repository:

```powershell
git clone https://github.com/nk55aur/OpenRouter-Flask-AI.git
cd OpenRouter-Flask-AI
```

2. Create a virtual environment and install dependencies:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

3. Configure environment variables.
Create a file named `.env` in the project root with the following values:

```text
OPENROUTER_API_KEY=your_openrouter_api_key_here
DEV_MOCK=true
```

- `OPENROUTER_API_KEY`: your OpenRouter API key (leave empty if using `DEV_MOCK=true`).
- `DEV_MOCK`: set to `true` to use local mock responses for UI testing.

# OpenRouter‑Flask‑AI

Lightweight, self-hosted AI assistant built with Flask and the OpenRouter API. This project demonstrates how to integrate an open-model routing API with a minimal web UI, including automatic intent detection (Q&A, summarization, creative writing), a responsive frontend, and a simple JSON API for integrations.

Key goals:
- Provide a clear, minimal example of building an AI assistant with Flask.
- Show safe configuration patterns (environment variables, mock mode).
- Make the app easy to run locally and deploy to common platforms.

---

## Features

- Minimal two-panel UI (Input → Robot → Output) with a polished UX.
- Automatic intent detection to choose appropriate model behavior.
- Dev mock mode (`DEV_MOCK`) for offline UI testing without an API key.
- Simple JSON API endpoint: `POST /api/ask` for programmatic access.
- Ready for deployment behind a WSGI server (e.g., `gunicorn`).

---

## Requirements

- Python 3.10+ (3.8+ may work; 3.10+ recommended)
- `pip` (package manager)
- A terminal (PowerShell on Windows is used in examples)

All Python dependencies are listed in `requirements.txt`.

---

## Quickstart — Windows (PowerShell)

1. Clone the repository and change into it:

```powershell
git clone https://github.com/nk55aur/OpenRouter-Flask-AI.git
cd OpenRouter-Flask-AI
```

2. Create and activate a virtual environment, then install dependencies:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

3. Create a `.env` file in the project root (or set environment variables directly):

```text
OPENROUTER_API_KEY=your_openrouter_api_key_here
DEV_MOCK=true
```

- `OPENROUTER_API_KEY`: (optional) your OpenRouter API key. Leave empty if using mock mode.
- `DEV_MOCK`: set to `true` to use canned responses for offline development.

4. Start the application:

```powershell
python app.py
```

Then open http://127.0.0.1:5000/ in your browser.

Quickstart — macOS / Linux (bash):

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
export OPENROUTER_API_KEY=your_key_here
export DEV_MOCK=true
python app.py
```

---

## Configuration

- Use a `.env` file for local development (do NOT commit it).
- When deploying, configure `OPENROUTER_API_KEY` and other secrets through your host's environment variable settings.
- Set `DEV_MOCK=true` for UI testing without network calls.

Example environment variables:

```text
OPENROUTER_API_KEY=<your_openrouter_api_key>
DEV_MOCK=false
```

---

## API

The app exposes a minimal programmatic endpoint:

- `POST /api/ask`
	- Request: JSON `{ "user_input": "..." }`
	- Response: JSON `{ "result": "..." }`

Use this endpoint to integrate the assistant into other tools or services. When `DEV_MOCK=true`, the endpoint returns deterministic mock responses for testing.

---

## Development notes

- Frontend files:
	- `templates/index.html` — main UI
	- `static/style.css` — styles and responsive layout
	- `static/script.js` — input handling and UI interactions
- Backend: `app.py` (Flask application) handles routing, intent classification, and API calls to OpenRouter.
- To run the app in development with live reload, use your preferred tooling (for small projects running `python app.py` is sufficient).

Recommended workflow:
1. Create a feature branch: `git checkout -b feat/describe-change`
2. Make small, focused commits.
3. Push and open a Pull Request.

---

## Testing

There are no automated tests included by default. Suggested tests:
- Add an integration test that POSTs to `/api/ask` with `DEV_MOCK=true`.
- Add unit tests for any new backend modules.

Example (simple curl-based smoke test):

```powershell
$env:DEV_MOCK = 'true';
curl -X POST -H "Content-Type: application/json" -d '{"user_input":"Hello"}' http://127.0.0.1:5000/api/ask
```

---

## Deployment

For production, run the app behind a WSGI server such as `gunicorn` and set `OPENROUTER_API_KEY` in the host's environment. Example (bind to port 8000):

```powershell
gunicorn --bind 0.0.0.0:8000 app:app
```

Hosting options: Render, Railway, Fly, a VPS, or any platform that supports Python web apps.

Security tips:
- Never commit secrets or `.env` to the repository.
- Use HTTPS in production and restrict CORS if exposing the API publicly.

---

**Author & Ownership**

This repository is authored and maintained by `@nk55aur`. It represents the individual work of the project owner and is not a contribution or maintained by other users or organizations. If you need an explicit contributor list or organizational affiliation, contact the repository owner.

---

**If an API key or `.env` was committed accidentally**

If you accidentally committed secrets (for example, a `.env` containing `OPENROUTER_API_KEY`), follow these steps immediately:

1. Remove the file from the index and commit:

```powershell
git rm --cached .env
git commit -m "Remove .env file containing secrets"
git push origin main
```

2. Rotate the exposed API key at the provider (generate a new key and revoke the old one).

3. To purge the secret from the repository history you can use one of these tools:

- BFG Repo-Cleaner (recommended for simple cases):

```powershell
# run this from a machine with Java installed
# download bfg.jar from https://rtyley.github.io/bfg-repo-cleaner/
java -jar bfg.jar --delete-files .env
git reflog expire --expire=now --all
git gc --prune=now --aggressive
git push --force
```

- Or `git filter-repo` (more flexible):

```powershell
# clone a mirror, filter, and push
git clone --mirror https://github.com/nk55aur/OpenRouter-Flask-AI.git
cd OpenRouter-Flask-AI.git
git filter-repo --invert-paths --paths .env
git push --force
```

Choose one method and follow its documentation. After purging you should also rotate any secrets that may have been exposed.

---

## Contributing

Contributions are welcome. Please follow these guidelines:

- Open an issue to discuss significant changes before implementing them.
- Keep changes focused and add tests for new behavior.
- Do not include secrets in commits or PRs.

If you want help adding CI, tests, or deployment configuration, open an issue or request it in a PR and I can add a suggested implementation.

---

## License

This project is licensed under the MIT License — see the `LICENSE` file for details.

---

If you'd like, I can also:
- Add a GitHub Actions workflow for linting and smoke tests.
- Add a small smoke test script that runs on CI using `DEV_MOCK=true`.
- Add badges (build, python-version) and example screenshots to the README.

If you want any of the above, tell me which item to add next.

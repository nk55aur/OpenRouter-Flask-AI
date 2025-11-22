AI Assistant Development using OpenRouter API:

This project showcases an intelligent AI-powered assistant built using Flask, Python, and the OpenRouter API.
It was developed as part of my internship at VaultofCodes, focusing on real-world prompt engineering, API integration, backend development, and production-ready workflow design.

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

📁 Project Folder Structure
AI_Assistant/
│── app.py
│── requirements.txt
│── .env.example
│── README.md
│── static/
│     └── style.css
│── templates/
│     └── index.html
│── screenshots/
│     ├── folder_structure.png
│     ├── summarize.png
│     └── terminal.png


⚙️ Installation & Setup
1️⃣ Clone the Repository
git clone https://github.com/yourusername/AI-Assistant-OpenRouter.git
cd AI-Assistant-OpenRouter

2️⃣ Install Dependencies
pip install -r requirements.txt

3️⃣ Create .env File

Create a file named .env and add your OpenRouter API key:

OPENROUTER_API_KEY=your_actual_key_here


(Your API Key from: https://openrouter.ai/settings/keys
)

▶️ How to Run

Start the Flask server:

python app.py


Then open in browser:
👉 http://127.0.0.1:5000/

🧪 Test Your API Key

Use the included testing script:

python test_api.py


This checks if your key is valid and the model responds.

🖥️ Features
✔ User-friendly UI

Simple, responsive interface built with HTML/CSS (Jinja templates).

✔ Multi-mode AI

Ask questions

Get summaries

Generate creative writing

✔ Real-time responses

Displays clean output without JSON clutter.

✔ Secure

Uses environment variables — no hard-coded keys.

✔ Scalable

Modular backend ready for deployment and expansion.

📸 Screenshots
Screenshot Type	Preview
Homepage UI	(placeholder)
Response Example	(placeholder)
Terminal Output	(placeholder)

Replace placeholders with your real images in /screenshots/.

🧩 Tech Stack

Python 3.10+

Flask Framework

OpenRouter API (Free Models)

HTML + CSS

dotenv for key management

🏆 Internship Contribution (VaultofCodes)

This project was developed during my internship in Prompt Engineering & AI Application Development at VaultofCodes.

My responsibilities included:

Building production-ready backend logic

Designing optimized prompts for different AI tasks

Integrating and testing LLMs via OpenRouter

UI planning, bug fixing, and documentation

Performance evaluation & feature enhancement

This project strengthened my skills in AI, APIs, web development, and software engineering.

📈 Future Enhancements

🗣 Voice input & speech-to-text

🧠 Chat history & conversation memory

🌐 Multi-language support

📱 Mobile UI optimization

☁ Deployment with CI/CD

🔄 Multiple model switching from UI

🔚 Conclusion

This project demonstrates a complete end-to-end AI system built with practical tools used in industry. It highlights my capability to work with APIs, backend frameworks, prompt engineering, and full documentation—making it ideal for recruiter evaluation.

📝 License

This project is open-source under the MIT License.

📮 Contact

Nitish Kumar
📧 Email: 22beccs27.cse@cujammu.ac.in
💼 LinkedIn:https://www.linkedin.com/in/nitish07kr
🐙 GitHub: https://www.linkedin.com/in/nitish07kr
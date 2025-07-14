# 🌐 URL Health Checker (CI/CD + Render Deployed)

A simple Flask API that checks if a given URL is live and returns its HTTP status code.

---

## 🔍 What It Does

You send a GET request like:

/check?url=https://google.com

css
Copy
Edit

And get a JSON response like:

```json
{
  "url": "https://google.com",
  "status_code": 200
}
Useful for:

Monitoring live websites

Quickly checking URL status from scripts/tools

⚙️ Tech Stack
🐍 Python (Flask)

☁️ Deployed to Render (free cloud hosting)

🔁 Auto deployment via GitHub commits (CI/CD)

📦 Dependency management with requirements.txt

🚀 Live URL
👉 https://url-health-checker.onrender.com

Try:

bash
Copy
Edit
/check?url=https://google.com
💻 Run Locally
bash
Copy
Edit
git clone https://github.com/rafidreezwan/url-health-checker.git
cd url-health-checker
pip install -r requirements.txt
python app.py
Then open http://127.0.0.1:5000/check?url=https://google.com

🤖 CI/CD & Deployment
Pushed to GitHub → Render auto-deploys the latest version

No manual steps needed
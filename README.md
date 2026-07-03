# Azure AI Review Analyser

An end-to-end Azure AI Language powered web app that analyzes text reviews and returns:

- Sentiment analysis
- Confidence scores
- Key phrases extraction
- Named entity recognition
- Language detection
- PII redaction
- Abstractive summarization

---

## 📁 Project Structure


Azure_RA/
├── src/
│ └── index.html
│
├── api/
│ ├── analyze/
│ │ ├── init.py
│ │ └── function.json
│ ├── host.json
│ ├── requirements.txt
│ ├── local.settings.json.example
│
├── staticwebapp.config.json
└── README.md


---

## 🚀 Features

✔ Sentiment Analysis  
✔ Confidence Score Breakdown  
✔ Key Phrase Extraction  
✔ Named Entity Recognition  
✔ Language Detection  
✔ PII Redaction  
✔ AI Abstractive Summarization  

---

## ⚙️ Setup Instructions

### 1. Clone repo
```bash
git clone https://github.com/<your-repo>.git
cd Azure_RA
2. Setup Python environment
py -3.11 -m venv .venv
.venv\Scripts\activate
pip install -r api/requirements.txt
3. Configure Azure AI Language

Create api/local.settings.json:

{
  "AzureWebJobsStorage": "UseDevelopmentStorage=true",
  "FUNCTIONS_WORKER_RUNTIME": "python",
  "LANGUAGE_ENDPOINT": "<your-endpoint>",
  "LANGUAGE_KEY": "<your-key>"
}
4. Run locally
func start
🌐 Frontend

Open:

src/index.html

Click:
👉 "Grade this review"

📡 API Endpoint
POST /api/analyze

Request:

{
  "text": "I love this product"
}

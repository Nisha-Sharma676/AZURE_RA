# Azure Review Analyzer (Azure_RA)

An end-to-end Azure AI Language powered web application that analyzes customer reviews and returns intelligent insights like sentiment analysis, key phrases, named entities, language detection, and summarization.

---

## Project Structure

```bash
Azure_RA/
│
├── src/
│   └── index.html              # Frontend UI (Review Analyzer)
│
├── api/
│   └── analyze/
│       ├── __init__.py         # Azure Function backend logic
│       └── function.json       # Trigger config
│
├── host.json                   # Azure Functions host config
├── requirements.txt            # Python dependencies
├── local.settings.json.example
│
├── staticwebapp.config.json    # Azure Static Web App config
├── test_api.py                 # API testing script
└── README.md
```

---

## Setup Instructions

### 1. Clone Repository
```bash
git clone https://github.com/Nisha-Sharma676/Azure_RA.git
cd Azure_RA
```

---

### 2. Create Virtual Environment
```bash
py -3.11 -m venv .venv
.venv\Scripts\activate
```

---

### 3. Install Dependencies
```bash
pip install -r api/requirements.txt
```

---

### 4. Configure Azure Credentials

Create file:

```
api/local.settings.json
```

Add:

```json
{
  "IsEncrypted": false,
  "Values": {
    "AzureWebJobsStorage": "UseDevelopmentStorage=true",
    "FUNCTIONS_WORKER_RUNTIME": "python",
    "LANGUAGE_ENDPOINT": "<your-azure-endpoint>",
    "LANGUAGE_KEY": "<your-azure-key>"
  }
}
```

---

### 5. Run Backend (Azure Functions)
```bash
cd api
func start
```

Backend runs at:
```
http://localhost:7071
```

---

### 6. Run Frontend

**Option 1: Direct**
```
Open src/index.html
```

**Option 2: Local server**
```bash
npx serve src
```

Frontend:
```
http://localhost:3000
```

---

## API Documentation

### Endpoint
```
POST /api/analyze
```

---

### Request Body
```json
{
  "text": "This phone has amazing battery life but the camera is average."
}
```

---

### Response Example
```json
{
  "sentiment": "positive",
  "confidenceScores": {
    "positive": 0.85,
    "neutral": 0.10,
    "negative": 0.05
  },
  "keyPhrases": [
    "battery life",
    "camera"
  ],
  "entities": [
    {
      "text": "phone",
      "category": "Product"
    }
  ],
  "language": "en",
  "summary": "Overall positive review with minor drawbacks in camera."
}
```

---

## Test API Locally
```bash
python test_api.py
```

---

## Deployment Guide

### Option 1: Azure Static Web Apps (Recommended)

1. Push code to GitHub  
2. Create Static Web App in Azure Portal  
3. Connect repository  
4. Set configuration:

```
App location: src
API location: api
```

---

### Option 2: Manual Deployment

- Frontend → Azure Static Web Apps / Storage  
- Backend → Azure Functions  

---

## Tech Stack

- Azure AI Language Service  
- Azure Functions (Python)  
- HTML, CSS, JavaScript  
- Fetch API  
- Node.js (local server)

---

## Important Notes

- Always start backend first (`func start`)
- Ensure CORS is enabled
- Update API URL in frontend if needed
- Keep Azure keys secure

---

## Future Improvements

- User authentication  
- Save analysis history  
- Export PDF reports  
- Real-time streaming analysis  
- Dashboard analytics  
  



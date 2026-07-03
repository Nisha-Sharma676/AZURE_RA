import json
import os
import azure.functions as func
from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential

endpoint = os.environ["LANGUAGE_ENDPOINT"]
key = os.environ["LANGUAGE_KEY"]

client = TextAnalyticsClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(key)
)

def main(req: func.HttpRequest) -> func.HttpResponse:
    try:
        body = req.get_json()
        text = body.get("text", "")

        if not text:
            return func.HttpResponse(
                json.dumps({"error": "No text provided"}),
                status_code=400
            )

        documents = [text]

        # 1. Language Detection
        lang = client.detect_language(documents)[0]
        language = lang.primary_language.name if not lang.is_error else "unknown"

        # 2. Sentiment Analysis
        sentiment_result = client.analyze_sentiment(documents)[0]

        sentiment = sentiment_result.sentiment
        confidence = {
            "positive": sentiment_result.confidence_scores.positive,
            "neutral": sentiment_result.confidence_scores.neutral,
            "negative": sentiment_result.confidence_scores.negative
        }

        # 3. Key Phrases
        key_phrases = client.extract_key_phrases(documents)[0].key_phrases

        # 4. Entities
        entities_result = client.recognize_entities(documents)[0]
        entities = [
            {"text": e.text, "category": e.category}
            for e in entities_result.entities
        ]

        # 5. PII Redaction
        pii_result = client.recognize_pii_entities(documents)[0]
        pii_redacted_text = pii_result.redacted_text

        # 6. Simple summarization fallback (Azure SDK limitation)
        summary = " ".join(key_phrases[:2]) if key_phrases else text[:120]

        result = {
            "language": language,
            "sentiment": sentiment,
            "confidenceScores": confidence,
            "keyPhrases": key_phrases,
            "entities": entities,
            "piiRedactedText": pii_redacted_text,
            "summary": summary
        }

        return func.HttpResponse(
            json.dumps(result),
            mimetype="application/json"
        )

    except Exception as e:
        return func.HttpResponse(
            json.dumps({"error": str(e)}),
            status_code=500
        )
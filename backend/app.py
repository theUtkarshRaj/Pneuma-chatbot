from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import google.generativeai as genai
from datetime import datetime
import logging
import os

# --- Paths ---
FRONTEND_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'frontend'))

# --- Initialize Flask ---
app = Flask(__name__, static_folder=FRONTEND_DIR, static_url_path='')
CORS(app)

# --- Configure Logging ---
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# --- Prompt Templates ---
SYSTEM_PROMPTS = {
    "sweet_spots": """You're a friendly travel expert at Pneuma. Keep responses short and helpful.

When asked about sweet spot deals:
- Share 1-2 quick examples with exact costs (e.g. "Business to Europe: 60K Chase points via Air France")
- Mention which credit cards transfer there
- Max 3 sentences
- End with: "What's your home airport?"
""",
    "mileage_transfer": """You're Pneuma's points expert. Keep it simple and short.

For transfer questions:
- Give the transfer ratio and timing (e.g. "Chase → United is 1:1, instant")
- Mention 1-2 best partners
- End with: "Which points do you have?"
""",
    "general_faq": """Hi! 👋 We help you get amazing flights using your credit card points and miles.
We find the best deals and show you how to book them.
What can I help you with — deals or points strategy?"""
}

# --- Intent Detection ---
def detect_intent(msg):
    msg = msg.lower()
    if any(k in msg for k in ["sweet spot", "deal", "cheap", "award", "value", "offer"]):
        return "sweet_spots"
    elif any(k in msg for k in ["transfer", "points", "move", "convert", "chase", "amex"]):
        return "mileage_transfer"
    elif any(k in msg for k in ["what is pneuma", "how", "about", "new", "help"]):
        return "general_faq"
    else:
        return "general_faq"

# --- API Endpoint for Chat ---
@app.route('/test', methods=['POST'])
def test_bot():
    try:
        data = request.get_json()
        user_msg = data.get("message", "").strip()
        user_key = data.get("api_key", "").strip()

        if not user_msg or not user_key:
            return jsonify({"error": "Message and API key required"}), 400

        genai.configure(api_key=user_key)
        model = genai.GenerativeModel("gemini-1.5-flash")

        intent = detect_intent(user_msg)
        prompt = f"{SYSTEM_PROMPTS[intent]}\nUser asked: \"{user_msg}\""

        response = model.generate_content(prompt).text.strip()

        return jsonify({
            "response": response,
            "intent": intent,
            "timestamp": datetime.now().isoformat(),
            "status": "success"
        })

    except Exception as e:
        logger.error(f"Error: {e}")
        return jsonify({"error": str(e)}), 500

# --- Serve Frontend ---
@app.route('/')
def serve_index():
    return send_from_directory(FRONTEND_DIR, 'index.html')

@app.route('/<path:path>')
def serve_static(path):
    return send_from_directory(FRONTEND_DIR, path)

# --- Health Check ---
@app.route('/health')
def health_check():
    return jsonify({"status": "healthy"})

# --- Run Server ---
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)

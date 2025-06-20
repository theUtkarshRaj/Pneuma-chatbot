# 📥 Adding New FAQs to Pneuma WhatsApp Bot

**⏱️ Time Required:** Under 10 minutes per intent  
**🔁 Flow:** Keyword → Intent → Prompt → Gemini Response → Test

---

## ✅ Step-by-Step Integration Guide

### 1. 🧠 Add Intent Keywords (2 min)

Open `app.py` → find the `detect_intent()` function:

```python
def detect_intent(message):
    message = message.lower()

    # Add your new intent keywords here
    hotel_keywords = ["hotel", "hyatt", "marriott", "hilton", "stay"]

    if any(keyword in message for keyword in hotel_keywords):
        return "hotel_points"

    # ... other existing intents
````

---

### 2. 💬 Define the System Prompt (3 min)

In `app.py`, find the `SYSTEM_PROMPTS` dictionary and add:

```python
SYSTEM_PROMPTS = {
    # ... other prompts

    "hotel_points": """You are Pneuma's hotel rewards expert. When users ask about hotel points:
- Provide 2-3 specific, actionable redemption examples
- Mention elite status perks or promotions
- Use plain English, be helpful and lightly witty
- Always end by offering to assist with specific hotels or programs
- Use emojis sparingly but smartly (1–3 per reply)"""
}
```

---

### 3. 🧪 Add a Mock Gemini Response (Optional for Local Testing – 2 min)

If you're mocking Gemini responses during development, add this inside the `MockGemini` class:

```python
self.responses = {
    # ... other mocks

    "hotel_points": """Here's what I'm seeing for hotel rewards right now:

🏨 **Hyatt Category 1 Hotels**: 3,500–5,000 points per night  
🏨 **Marriott Bonvoy Off-Peak**: 7,500 points/night in Southeast Asia  
✨ Elite status perks include late checkout and upgrades

Want help finding something for your next stay? Just ask! 🎯"""
}
```

---

### 4. 🧠 Update Detection Logic in MockGemini (if used)

In `chat_completions_create()` of your mock Gemini class:

```python
elif any(word in user_message for word in ["hotel", "hyatt", "marriott", "stay"]):
    response_text = self.responses["hotel_points"]
```

---

### 5. 🧪 Test the Bot (2 min)

Run your bot and test with:

```bash
curl -X POST http://localhost:5000/test \
  -H "Content-Type: application/json" \
  -d '{"message": "Any good hotel point deals?"}'
```

---

## 🔊 Voice & Tone Guidelines (Gemini Style)

**✅ Match Pneuma’s Style:**

* "Here's the quick rundown:" ✅
* "Want help with specifics? Just ask ✈️" ✅
* Lightly witty, data-backed, plain-English ✅

**❌ Avoid:**

* "Revolutionizing travel optimization" ❌
* "Maximizing loyalty disruption" ❌
* Corporate tone or overly formal ❌

---

## 🛠️ Gemini-Specific Notes

* Gemini API calls are made via `google.generativeai`
* Prompts are passed using the `model.generate_content(prompt)` method
* The `SYSTEM_PROMPTS` dictionary feeds into Gemini calls like:

```python
response = model.generate_content(SYSTEM_PROMPTS[intent] + "\nUser: " + message)
```

* You can set your Gemini API key in `.env`:

```
GEMINI_API_KEY=your-key-here
```

And load it with:

```python
import os
from dotenv import load_dotenv
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
```

---

## 🧪 Health Check

```bash
curl http://localhost:5000/health
```

Response:

```json
{
  "status": "healthy",
  "version": "v0.1"
}
```

---

## 🧱 File Structure Recap

```
app.py
├── detect_intent()          # Keyword → Intent mapping
├── SYSTEM_PROMPTS           # Prompt per intent (for Gemini)
├── GeminiClient / MockGemini
└── /webhook, /test endpoints
```

---

## 🧩 Template for New FAQs

```python
# In detect_intent
if any(keyword in message for keyword in ["example", "keywords"]):
    return "new_intent"

# In SYSTEM_PROMPTS
"new_intent": """You are Pneuma's [topic] expert.
- Provide 2–3 specific insights
- Use friendly tone
- Be lightly witty, not robotic
- End with an offer to assist
- 1–3 emojis max""",

# In mock responses (optional)
"new_intent": """Sample mock Gemini response goes here.  
🔑 Key point 1  
✅ Key point 2  
Ask a follow-up? Just say the word! 🎯"""
```

---

## 📦 Current Intents (as of v0.1)

| Intent           | Triggers                                 | Purpose                        |
| ---------------- | ---------------------------------------- | ------------------------------ |
| sweet\_spot      | "sweet spot", "cheap flights", "deals"   | Points deals for top routes    |
| transfer\_basics | "transfer points", "move miles", "amex"  | Transfer mechanisms and timing |
| general\_faq     | "what is Pneuma", "how it works", "help" | Basic onboarding and info      |
| hotel\_points    | "hotel", "hyatt", "marriott", "stay"     | Hotel loyalty redemption tips  |

---


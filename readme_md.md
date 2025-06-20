# Pneuma WhatsApp FAQ Bot v0.1 – Prototype Pack

A rapid-prototype WhatsApp chatbot that answers key FAQ questions about travel rewards, sweet-spot deals, and mileage transfers in Pneuma's plain-English, quietly-witty voice.

## 🎯 Key Features

**Three Core Intents:**
1. **Sweet Spot Deals** - Today's best mileage/points values for popular routes
2. **Mileage Transfer Basics** - How to transfer points between programs effectively  
3. **General FAQ** - Onboarding and general Pneuma questions

## 🚀 Quick Setup

### Prerequisites
- Python 3.8+
- ngrok (for WhatsApp webhook testing)

### Installation
```bash
# Clone/download the project
cd pneuma-whatsapp-bot

# Install dependencies
pip install -r requirements.txt

# Set environment variables (optional)
export OPENAI_API_KEY="your-key-here"  # Currently using mock responses
export PORT=5000
```

### Run Locally
```bash
python app.py
```
Server runs on `http://localhost:5000`

## 🧪 Testing

### Test the Three Intents

**1. Sweet Spot Deals Intent:**
```bash
curl -X POST http://localhost:5000/test \
  -H "Content-Type: application/json" \
  -d '{"message": "What are the best sweet spot deals today?"}'
```

**2. Mileage Transfer Intent:**
```bash
curl -X POST http://localhost:5000/test \
  -H "Content-Type: application/json" \
  -d '{"message": "How do I transfer Chase points to United?"}'
```

**3. General FAQ Intent:**
```bash
curl -X POST http://localhost:5000/test \
  -H "Content-Type: application/json" \
  -d '{"message": "What is Pneuma and how does it work?"}'
```

### Sample Responses

**Sweet Spots Example:**
> "Here are today's sweet spot deals I'm tracking:
> 
> ✈️ **Japan via United MileagePlus**: 70k miles roundtrip (normally 80k) - transfer from Chase UR with 1:1 rate
> ✈️ **Europe via Air Canada Aeroplan**: 55k miles economy (sweet spot through July)..."

**Mileage Transfer Example:**
> "Mileage transfers are your secret weapon for maximizing value. Here's the quick rundown:
> 
> 🔄 **The Basics:**
> • Most transfers are 1:1 (1 bank point = 1 airline mile)
> • Transfers usually take 1-4 hours, some up to 24 hours..."

## 📱 WhatsApp Integration

### Mock WhatsApp Webhook
The `/webhook` endpoint accepts WhatsApp-formatted JSON:

```bash
curl -X POST http://localhost:5000/webhook \
  -H "Content-Type: application/json" \
  -d '{
    "messages": [{
      "from": "+1234567890",
      "text": {"body": "show me sweet spot deals"},
      "timestamp": "1640995200"
    }]
  }'
```

### Real WhatsApp Integration
For production use with Twilio/Meta:
1. Set up ngrok: `ngrok http 5000`
2. Configure webhook URL in WhatsApp Business API
3. Replace mock OpenAI client with real API key

## 🔧 Architecture

```
app.py
├── Intent Detection (keyword-based)
├── System Prompts (per intent)
├── Response Generation (OpenAI + fallback)
└── WhatsApp Webhook Handler
```

**Current Limitations:**
- Uses mock OpenAI responses for demo
- Simple keyword-based intent detection
- No conversation memory/context
- No user authentication

## 🎨 Voice & Tone Examples

**✅ Good Pneuma Voice:**
- "Here's the quick rundown:" (plain English)
- "Pro tip: Book Japan routes by end of month" (data-backed)
- "Want specifics for your route? Just tell me!" (lightly engaging)

**❌ Avoid:**
- "Revolutionize your travel experience"
- "Disruptive points optimization"
- Overly corporate language

## 🏥 Health Check
```bash
curl http://localhost:5000/health
```

Returns service status and version info.

---

## 📋 Sample User Phrasings by Intent

### Sweet Spot Deals
- "What are the best deals today?"
- "Show me sweet spot routes"
- "Any good value flights to Europe?"
- "Cheap mileage redemptions available?"

### Mileage Transfer
- "How do I transfer Chase points?"
- "Can I move Amex points to United?"
- "Transfer ratios for different programs?"
- "Best way to convert credit card points?"

### General FAQ  
- "What is Pneuma?"
- "How does this work?"
- "Getting started with points"
- "Help me understand travel rewards"
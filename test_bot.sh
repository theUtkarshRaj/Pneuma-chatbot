#!/bin/bash

# Pneuma WhatsApp Bot Demo Test Script
# Run this after starting the Flask app (python app.py)

echo "🚀 Testing Pneuma WhatsApp FAQ Bot v0.1"
echo "========================================"

# Test 1: Sweet Spot Deals Intent
echo ""
echo "📍 Test 1: Sweet Spot Deals Intent"
echo "User message: 'What are the best sweet spot deals today?'"
echo ""
curl -s -X POST http://localhost:5000/test \
  -H "Content-Type: application/json" \
  -d '{"message": "What are the best sweet spot deals today?"}' | jq -r '.response'

echo ""
echo "---"

# Test 2: Mileage Transfer Intent  
echo ""
echo "📍 Test 2: Mileage Transfer Intent"
echo "User message: 'How do I transfer Chase points to United?'"
echo ""
curl -s -X POST http://localhost:5000/test \
  -H "Content-Type: application/json" \
  -d '{"message": "How do I transfer Chase points to United?"}' | jq -r '.response'

echo ""
echo "---"

# Test 3: General FAQ Intent
echo ""
echo "📍 Test 3: General FAQ Intent" 
echo "User message: 'What is Pneuma and how does it work?'"
echo ""
curl -s -X POST http://localhost:5000/test \
  -H "Content-Type: application/json" \
  -d '{"message": "What is Pneuma and how does it work?"}' | jq -r '.response'

echo ""
echo "---"

# Test 4: WhatsApp Webhook Format
echo ""
echo "📍 Test 4: WhatsApp Webhook Format"
echo "Simulating WhatsApp message: 'Any good deals to Japan?'"
echo ""
curl -s -X POST http://localhost:5000/webhook \
  -H "Content-Type: application/json" \
  -d '{
    "messages": [{
      "from": "+1234567890", 
      "text": {"body": "Any good deals to Japan?"},
      "timestamp": "1640995200"
    }]
  }' | jq -r '.text.body'

echo ""
echo "---"

# Health Check
echo ""
echo "📍 Health Check"
curl -s http://localhost:5000/health | jq '.'

echo ""
echo "✅ Demo tests complete!"
echo ""
echo "💡 To run individual tests:"
echo "curl -X POST http://localhost:5000/test -H \"Content-Type: application/json\" -d '{\"message\": \"your message here\"}'"
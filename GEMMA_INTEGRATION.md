# OpenRouter + Gemma Integration Setup Guide

## What's Integrated

Your SavoraAI project now uses **Google Gemma 2 9B** model via **OpenRouter** API instead of Groq.

## Why This Integration?

- ✅ **Google AI Tool**: Gemma is Google's open-source LLM
- ✅ **High Quality**: Gemma 2 9B provides excellent recipe generation
- ✅ **Cost Effective**: OpenRouter offers competitive pricing
- ✅ **Reliable**: More stable than some alternatives

## Setup Instructions

### 1. Get OpenRouter API Key

1. Visit [OpenRouter.ai](https://openrouter.ai/)
2. Sign up or log in
3. Go to **Keys** section
4. Generate a new API key
5. Copy the key (starts with `sk-or-v1-`)

### 2. Configure Environment Variables

1. Create a `.env` file in the `backend` folder (copy from `.env.example`)
2. Add your OpenRouter API key:

```
OPENROUTER_API_KEY=sk-or-v1-your-actual-key-here
```

### 3. Test the Integration

Run your backend server:

```bash
cd backend
python app.py
```

Visit `http://localhost:5000/` - you should see:

```json
{
  "message": "Welcome to SAVORA AI Backend API - Powered by Google Gemma via OpenRouter",
  "ai_model": "Google Gemma 2 9B"
}
```

## Model Details

- **Model**: `google/gemma-2-9b-it`
- **Provider**: OpenRouter
- **Context**: Up to 8,192 tokens
- **Cost**: ~$0.000225 per 1K tokens (very affordable)
- **Speed**: Fast response times

## Features

- Recipe generation from ingredients
- Cooking chat assistance
- Meal planning
- Nutrition information
- Cooking problem rescue

## For Forms/Applications

When asked which Google AI tool you're using, write:
**"Google Gemma 2 (via OpenRouter)"**

Your project now officially uses Google's AI technology! 🎉

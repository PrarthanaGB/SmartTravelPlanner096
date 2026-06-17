# 🤖 AI Integration Setup Guide

## Overview
SmartTravelPlanner now uses **OpenAI's GPT-3.5 Turbo** to generate intelligent, real-time travel itineraries for any destination in the world!

---

## ✅ Getting OpenAI API Key

### Step 1: Create OpenAI Account
1. Go to [https://platform.openai.com/](https://platform.openai.com/)
2. Click **"Sign up"** (or **"Log in"** if you already have an account)
3. Enter your email and create a password
4. Verify your email address

### Step 2: Get API Key
1. After logging in, go to [API Keys](https://platform.openai.com/account/api-keys)
2. Click **"Create new secret key"**
3. Copy the key (you won't see it again!)
4. Store it safely

### Step 3: Check Credits
- New users get **$5 free credits** for 3 months
- Each API call costs a small amount (usually $0.001-0.01 per request)
- View usage at [Billing Dashboard](https://platform.openai.com/account/billing/overview)

---

## 🔧 Configure Your Project

### Add API Key to Environment

**Option A: Using configure.env (Recommended)**

1. Open `backend/configure.env`
2. Replace `your_openai_api_key_here` with your actual API key:
   ```env
   OPENAI_API_KEY=sk-proj-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
   ```
3. Save the file

**Option B: Using .env file**

1. Create `backend/.env` file
2. Add:
   ```env
   OPENAI_API_KEY=your_key_here
   ```

⚠️ **IMPORTANT**: Never commit your API key to GitHub!
- Add `.env` to `.gitignore`
- Don't paste the key in public

---

## 🚀 How It Works

### AI-Powered Features

When you request an itinerary:

```
User Input: 
- Place: "Paris"
- Days: 5
- Budget: ₹100K
- Transport: Flight

↓ (sent to OpenAI API)

AI Response:
- Day-by-day activities
- Real restaurant recommendations
- Accurate hotel suggestions
- Medical facility locations
- Transport options
- Realistic pricing breakdown

↓

Displayed in interactive map with Leaflet.js
```

### Real-Time Processing
- Each request takes 2-5 seconds
- Itinerary is generated fresh, not from a template
- Works for ANY destination (not just Bengaluru/Delhi)
- Natural language responses

---

## 🧪 Testing the AI

### Test 1: Without API Key
```bash
cd backend
python app.py
```
- Go to http://localhost:5000
- Try generating an itinerary
- You'll get template-based results (Bengaluru/Delhi only)
- You'll see note: "Using template-based itinerary..."

### Test 2: With API Key
1. Add `OPENAI_API_KEY` to `configure.env`
2. Restart Flask: `python app.py`
3. Generate itinerary for **any city**
4. AI will create real recommendations!

---

## 📊 Expected API Costs

| Usage | Monthly Cost |
|-------|------------|
| 100 itineraries/month | ~$1-2 |
| 1000 itineraries/month | ~$10-20 |
| 10,000 itineraries/month | ~$100-200 |

**Free tier**: $5 credits lasts about 5,000 requests

---

## 🔒 Security Best Practices

### ✅ DO:
- Keep API key private
- Use `.env` files
- Add `.env` and `configure.env` to `.gitignore`
- Rotate keys periodically
- Monitor usage at OpenAI dashboard

### ❌ DON'T:
- Commit API keys to Git
- Share keys in emails
- Paste keys in chat/forums
- Use the same key in production and testing

---

## 🐛 Troubleshooting

### "OPENAI_API_KEY not configured"
- Check `configure.env` for the key
- Make sure you restarted Flask after adding the key
- Verify the key starts with `sk-`

### API errors or slow responses
- Check OpenAI status: [status.openai.com](https://status.openai.com)
- Verify API key is valid at [API Keys page](https://platform.openai.com/account/api-keys)
- Check usage limits at [Billing Dashboard](https://platform.openai.com/account/billing/usage)

### Getting `context_length_exceeded` error
- The destination description is too long
- Try shorter place names or simpler requests

### Rate limiting (429 error)
- You're making too many requests
- Wait a few seconds before the next request
- Upgrade to paid plan for higher limits

---

## 🚀 Performance Tips

### Speed Up Responses
- Use shorter place names ("Tokyo" vs "Tokyo's Shibuya District")
- Reduce days or budget to simpler scenarios
- Use GPT-4 in code (more powerful but pricier)

### Save on API Costs
- Cache responses (store generated itineraries)
- Batch requests (not yet implemented)
- Use GPT-3.5-turbo (cheaper than GPT-4)

---

## 📝 Using Different AI Models

To use GPT-4 (more intelligent but slower/expensive):

Edit `backend/utils/ai_helper.py`:
```python
response = client.chat.completions.create(
    model="gpt-4",  # Change from "gpt-3.5-turbo"
    ...
)
```

Cost comparison:
- **GPT-3.5-turbo**: $0.0015/1K tokens (CHEAP)
- **GPT-4**: $0.03/1K tokens (10x more expensive)

---

## 📞 Support

### Helpful Resources:
- [OpenAI API Docs](https://platform.openai.com/docs)
- [API Rate Limits](https://platform.openai.com/docs/guides/rate-limits)
- [Pricing Calculator](https://openai.com/pricing)
- [GitHub Issues](https://github.com/PrarthanaGB/SmartTravelPlanner096/issues)

---

## ✨ Next Steps

1. ✅ Get OpenAI API key
2. ✅ Add to `configure.env`
3. ✅ Restart Flask server
4. ✅ Generate itineraries for any city!
5. ✅ Monitor usage & costs

**Happy AI-powered travel planning!** 🌍✈️

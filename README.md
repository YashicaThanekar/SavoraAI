                                              🍳 Savora AI – AI-Powered Smart Recipe Generator


Savora AI is an intelligent recipe generation platform that helps users cook smarter using AI. It generates personalized recipes based on available ingredients, cuisine preferences, portion size, and taste using Google Gemini, Firebase, and a modern full-stack architecture.

---

## **Key Highlights**
- AI-powered recipe generation
- Ingredient-based smart cooking
- Voice input support
- AI cooking chatbot
- Firebase authentication and storage
- Scalable full-stack design

---

##  **Tech Stack**

### Frontend
- React (Vite)
- HTML, CSS, JavaScript
- Firebase Authentication
- Firebase Firestore

### Backend
- Python
- Flask
- Google Gemini API
- Flask-CORS
- dotenv

---

## **Project Structure**

```
SavoraAI/
├── backend/
│   ├── app.py                  # Flask API server
│   ├── .env                    # Environment variables
│   ├── requirements.txt        # Python dependencies
│   └── .env.example           # Example env file
│
├── frontend/
│   ├── index.html             # HTML entry point
│   ├── package.json           # NPM dependencies
│   ├── vite.config.js         # Vite configuration
│   └── src/
│       ├── main.jsx           # React entry point
│       ├── App.jsx            # Main app component
│       ├── firebase.js        # Firebase configuration
│       ├── styles.css         # Global styles
│       ├── pages/
│       │   ├── Home.jsx       # Main recipe generation page
│       │   ├── Login.jsx      # Authentication page
│       │   ├── History.jsx    # User recipe history
│       │   └── Favorites.jsx  # Saved favorite recipes
│       └── components/
│           ├── Navbar.jsx     # Navigation bar
│           ├── RecipeCard.jsx # Recipe display card
│           ├── Filters.jsx    # Recipe filters
│           ├── VoiceInput.jsx # Voice-to-text input
│           └── Chatbot.jsx    # AI cooking assistant
```

---

## **Features Implemented**

### Core Features
✅ AI-generated dynamic recipes  
✅ Ingredient-based recipe generation  
✅ Step-by-step cooking instructions  
✅ History of previously generated recipes  
✅ Save favorite recipes  

### **Smart Features**
✅ Multi-cuisine support (Indian, Chinese, Continental, Italian, Mexican, Thai)  
✅ Estimated cooking time  
✅ Portion-based recipe generation (1 person / 2-3 / 4-6 / Family)  
✅ Alternative ingredient suggestions  
✅ AI Chatbot for follow-up cooking questions  
✅ Voice assistant input (browser speech-to-text)  

### **Filter Features**
✅ Taste filters: Sweet / Savory / Spicy  
✅ Meal type filters: Breakfast / Lunch / Dinner / Snack  
✅ Cuisine filters: Multiple cuisines  
✅ Portion size selection  

---

## **How to Use**

1. **Login/Register**: Create an account or login with Google
2. **Enter Ingredients**: Type or speak ingredients you have
3. **Apply Filters**: Select cuisine, taste, meal type, and portion size
4. **Generate Recipe**: Click "Generate Recipe" button
5. **View Recipe**: See AI-generated recipe with steps and tips
6. **Save Favorite**: Save recipes you love
7. **Ask Chatbot**: Get help with cooking questions
8. **View History**: Access your previously generated recipes

---

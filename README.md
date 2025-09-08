# -CoffeeMate-Caf-AI-Powered-Coffee-Ordering-System
☕🍰 CoffeeMate Café – An AI-powered interactive café assistant that suggests coffee &amp; pastries, applies discounts, remembers past orders, and handles misspellings! 🚀


## 🌟 Features  
- 👤 **Personalized Experience** – Remembers your name & last order.  
- ☕ **Coffee & Pastry Suggestions** – Shows random 3 items each time.  
- 🎁 **Discounts**  
  - First-time users get **10% off** their first coffee.  
  - Special **Combo Offers (15% off)** on coffee + pastry.  
- 🧠 **Smart Memory** – Saves user history in `memory.json`.  
- 🔍 **Misspelling Correction** – Type *crossont* instead of *Croissant* – still works!  
- 💬 **Chat-like Flow** – Feels like talking to a café assistant.

## 🛠️ Tech Stack  
- **Python 3.9+**  
- **Google Generative AI (Gemini API)**  
- **dotenv** (API key management)  
- **difflib** (fuzzy matching for typos)  
- **JSON** (local memory storage)  

## ⚙️ Setup & Installation  

1. **Clone the repository**  
```bash
git clone https://github.com/your-username/CoffeeMate-Cafe.git
cd CoffeeMate-Cafe

2.env

python -m venv venv
venv\Scripts\activate   # Windows
source venv/bin/activate  # Mac/Linux

3.Add API Key
Create a .env file and add:

GEMINI_API_KEY=your_api_key_here

4.Run the app

python coffee_agent.py

<img width="1366" height="768" alt="Screenshot (75)" src="https://github.com/user-attachments/assets/58039d72-9e79-4c60-91bd-d9300e3930cd" />

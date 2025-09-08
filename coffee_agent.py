import os
import json
import random
from difflib import get_close_matches
from dotenv import load_dotenv
import google.generativeai as genai

# Load API key
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    print("⚠️ No API key found. Please set GEMINI_API_KEY in your .env file.")
    exit()

genai.configure(api_key=api_key)
model = genai.GenerativeModel("gemini-1.5-flash")

# Memory file
MEMORY_FILE = "memory.json"

def load_memory():
    if os.path.exists(MEMORY_FILE):
        with open(MEMORY_FILE, "r") as f:
            return json.load(f)
    return {}

def save_memory(data):
    with open(MEMORY_FILE, "w") as f:
        json.dump(data, f, indent=2)

memory = load_memory()

# Coffee & pastry menu with prices
coffee_menu = {
    "Espresso": 120, "Cappuccino": 150, "Latte": 160, "Mocha": 170,
    "Americano": 130, "Macchiato": 140, "Flat White": 155, "Irish Coffee": 200,
    "Affogato": 180, "Cortado": 145, "Cold Brew": 150, "Nitro Coffee": 190,
    "Caramel Macchiato": 175, "Pumpkin Spice Latte": 185, "Salted Caramel Mocha": 195
}

pastry_menu = {
    "Croissant": 100, "Muffin": 90, "Tiramisu": 180, "Cheesecake": 200,
    "Brownie": 110, "Macaron": 130, "Donut": 80, "Eclair": 150,
    "Cinnamon Roll": 140, "Cupcake": 95, "Fruit Tart": 170, "Baklava": 210
}

# Greeting
print("\n🍰☕ Welcome to CoffeeMate Café – Where Every Sip Meets a Bite! 🍩✨\n")

# Ask name
name = input("👤 What's your name? ").strip()
if name in memory:
    print(f"👋 Welcome back, {name}! Last time you enjoyed {memory[name].get('last_order', 'something delicious')}.\n")
else:
    print(f"✨ Nice to meet you, {name}! First coffee is 10% off today! 🎁\n")

# Track orders
order = {"coffee": None, "pastry": None, "total": 0}

# Initial greeting by CoffeeMate
print("🤖 CoffeeMate: Hi there! 👋 Let's pick a coffee and a pastry to start! ☕🍰")
print("💡 Note: If you pick both a coffee and a pastry, you'll get a 15% combo discount!\n")

while True:
    # Suggest random items
    coffee_suggestions = random.sample(list(coffee_menu.keys()), 3)
    pastry_suggestions = random.sample(list(pastry_menu.keys()), 3)

    print("\n📋 Coffee suggestions for today:")
    for i, c in enumerate(coffee_suggestions, 1):
        discount_info = " (10% off!)" if not memory.get(name) else ""
        print(f"{i}. {c} (₹{coffee_menu[c]}{discount_info})")

    print("\n📋 Pastry suggestions for today:")
    for i, p in enumerate(pastry_suggestions, 1):
        print(f"{i}. {p} (₹{pastry_menu[p]})")

    # Ask coffee choice
    coffee_choice = input("\n👉 Which coffee would you like? (type 'skip' to skip, 'exit' to finish): ").strip()
    if coffee_choice.lower() in ["exit", "quit"]:
        break
    if coffee_choice.lower() != "skip":
        corrected_coffee = get_close_matches(coffee_choice.title(), coffee_menu.keys(), n=1, cutoff=0.6)
        if corrected_coffee:
            coffee = corrected_coffee[0]
            order["coffee"] = coffee
            price = coffee_menu[coffee]
            # Apply first-time 10% discount if user is new
            if not memory.get(name):
                discount = round(price * 0.10, 2)
                price -= discount
                print(f"🎉 First-time discount applied! -₹{discount}")
            order["total"] += price
            print(f"✅ Added {coffee} ☕ to your order! (₹{price})")
        else:
            print("⚠️ Coffee not recognized. Skipping...")

    # Ask pastry choice
    pastry_choice = input("\n👉 Which pastry would you like? (type 'skip' to skip, 'exit' to finish): ").strip()
    if pastry_choice.lower() in ["exit", "quit"]:
        break
    if pastry_choice.lower() != "skip":
        corrected_pastry = get_close_matches(pastry_choice.title(), pastry_menu.keys(), n=1, cutoff=0.6)
        if corrected_pastry:
            pastry = corrected_pastry[0]
            order["pastry"] = pastry
            price = pastry_menu[pastry]
            order["total"] += price
            print(f"✅ Added {pastry} 🍰 to your order! (₹{price})")
        else:
            print("⚠️ Pastry not recognized. Skipping...")

    # Combo discount
    if order["coffee"] and order["pastry"]:
        original = coffee_menu[order['coffee']] + pastry_menu[order['pastry']]
        discount = round(original * 0.15, 2)
        final = original - discount
        print(f"\n🎉 Combo Offer! {order['coffee']} + {order['pastry']}")
        print(f"💰 Original: ₹{original} → Discount: ₹{discount} → Final: ₹{final}\n")
        order["total"] = final

# Save memory
if order["coffee"] or order["pastry"]:
    memory[name] = {"last_order": f"{order['coffee']} + {order['pastry']}" if order['coffee'] and order['pastry'] else order['coffee'] or order['pastry']}
    save_memory(memory)

print(f"\n👋 Thanks for visiting CoffeeMate Café, {name}! Total bill: ₹{order['total']}. Have a sweet day! ☕🍩")

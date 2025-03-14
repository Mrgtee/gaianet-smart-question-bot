import requests
import time
import random

# Ask for API Key at startup
API_KEY = input("Enter your Gaianet API Key: ").strip()

# Gaianet API URL (update if needed)
API_URL = "https://api.gaianet.com/chat"

# Random questions for the bot to ask
QUESTIONS = [
    "What is the most exciting development in AI right now?",
    "How does blockchain impact the future of finance?",
    "Can you explain quantum computing in simple terms?",
    "What are the latest trends in decentralized applications?",
    "How can AI help in medical research?",
    "What is the best way to start learning Web3?",
    "Tell me about the future of smart contracts."
]

# Follow-up questions to make it sound more human
FOLLOW_UP_QUESTIONS = [
    "That's interesting! Can you elaborate?",
    "What challenges do you see in this field?",
    "How does this compare to traditional systems?",
    "Are there any risks involved?",
    "What does the future look like for this technology?",
    "Who are the biggest players in this space?"
]

def send_message(question):
    """Send a message to Gaianet chatbot and return the response."""
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    data = {"message": question}

    try:
        response = requests.post(API_URL, json=data, headers=headers)
        
        # Debugging logs
        print(f"DEBUG: API Response Code: {response.status_code}")
        print(f"DEBUG: API Response Body: {response.text}")

        if response.status_code == 200:
            reply = response.json().get("reply", "")
            if reply:
                return reply

        print("Gaianet API Error:", response.text)  # Print API errors

    except requests.exceptions.RequestException as e:
        print("Request failed:", e)  # Print connection errors

    return "No response from Gaianet chatbot."

def chat_loop():
    """Loop to ask questions continuously until stopped."""
    print("\nGaianet Smart Question Bot running... Press Ctrl+C to stop.\n")

    while True:
        question = random.choice(QUESTIONS)
        print(f"You: {question}")

        response = send_message(question)
        print(f"Gaianet: {response}\n")

        if "sorry" not in response.lower():
            time.sleep(random.randint(10, 20))
            follow_up = random.choice(FOLLOW_UP_QUESTIONS)
            print(f"You: {follow_up}")
            response = send_message(follow_up)
            print(f"Gaianet: {response}\n")

        # Random delay to avoid spamming
        time.sleep(random.randint(15, 30))

if __name__ == "__main__":
    chat_loop()

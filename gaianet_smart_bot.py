import requests
import random
import time

API_KEY = input("Enter your Gaianet API Key: ").strip()
BASE_URL = "https://api.gaianet.com/chat"

QUESTIONS = [
    "What is the most interesting fact you know?",
    "How does blockchain work?",
    "What are the biggest threats to cybersecurity?",
    "Can AI ever be truly conscious?",
    "What are some ethical concerns about AI?",
    "What is the future of decentralized finance?",
    "How does quantum computing impact security?",
    "What are the risks of smart contracts?",
    "What is the most exciting development in AI right now?",
    "How do zero-knowledge proofs work?"
]

FOLLOW_UP_QUESTIONS = [
    "That's interesting! Can you elaborate?",
    "Why do you think that is?",
    "Can you provide an example?",
    "How does that compare to past trends?",
    "What are the potential downsides?",
    "Who benefits the most from this?"
]

def send_message(question, retries=3):
    headers = {"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"}
    data = {"message": question}

    for attempt in range(retries):
        try:
            response = requests.post(BASE_URL, json=data, headers=headers)
            if response.status_code == 200:
                reply = response.json().get("response", "").strip()
                if reply:
                    return reply
        except requests.exceptions.RequestException:
            pass
        time.sleep(3)

    return "No response from Gaianet chatbot."

def chat_loop():
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

        time.sleep(random.randint(15, 30))

if _name_ == "_main_":
    chat_loop()

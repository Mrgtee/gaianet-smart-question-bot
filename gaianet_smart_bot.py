import requests
import time
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

API_KEY = input("Enter your Gaianet API Key: ").strip()
API_URL = "https://pengu.gaia.domains/chat"  # Ensure this is the correct API endpoint

def ask_gaianet(question, max_retries=5, timeout=60):
    """Send a question to the Gaianet API and handle errors with retries."""
    headers = {"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"}
    data = {"message": question}
    
    for attempt in range(1, max_retries + 1):
        try:
            logging.info(f"Attempt {attempt} for question: {question}...")
            response = requests.post(API_URL, json=data, headers=headers, timeout=timeout)
            
            # Check for successful response
            if response.status_code == 200:
                return response.json().get("answer", "No response from Gaianet.")
            
            logging.warning(f"Unexpected response ({response.status_code}): {response.text}")
        
        except requests.exceptions.Timeout:
            logging.error("Request timed out. Retrying...")
        except requests.exceptions.ConnectionError:
            logging.error("Connection error. Retrying...")
        except Exception as e:
            logging.error(f"An unexpected error occurred: {e}")

        # Implement exponential backoff (wait 2^attempt seconds before retrying)
        wait_time = 2 ** attempt
        logging.info(f"Waiting {wait_time}s before retrying...")
        time.sleep(wait_time)

    return "Failed to get a response after multiple attempts."

# Main chat loop
if __name__ == "__main__":
    while True:
        question = input("You: ")
        if question.lower() in ["exit", "quit"]:
            break
        
        answer = ask_gaianet(question)
        print(f"Gaianet: {answer}")

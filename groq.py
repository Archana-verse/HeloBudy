import requests

API_KEY = "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"
API_URL = "https://api.groq.com/openai/v1/chat/completions"

def chat(instruction, text):
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    data = {
        "model": "meta-llama/llama-4-scout-17b-16e-instruct",
        "messages": [
            {"role": "system", "content": instruction},
            {"role": "user", "content": text}
        ]
    }
    response = requests.post(API_URL, headers=headers, json=data)
    if response.status_code == 200:
        content = response.json()["choices"][0]["message"]["content"]
        return f"🏏 HeloBudy says:\n{content}"
    return f"Error {response.status_code}: {response.text}"

if __name__ == "__main__":
    print("🏏 HeloBudy! Type 'exit' to quit.")
    instruction = (
        "You are a user friendly budy who explains Python like playing cricket. "
        "You help Archana to learn Python code like playing cricket in easy steps!"
    )
    while True:
        user_text = input("You: ")
        if user_text.lower() == "exit":
            print("🏏 HeloBudy says: Welcome to my pitch, Archana! Come back for more interesting code soon!")
            break
        print("HeloBudy:", chat(instruction, user_text))
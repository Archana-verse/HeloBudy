import requests
import speech_recognition as sr
import pyttsx3

engine = pyttsx3.init()
engine.setProperty('rate', 160)

def speak(text):
    print(f"HeloBudy: {text}")
    engine.say(text)
    engine.runAndWait()

recognizer = sr.Recognizer()

def listen():
    with sr.Microphone() as source:
        print("🎙️ Speak now...")
        audio = recognizer.listen(source)
        try:
            query = recognizer.recognize_google(audio)
            print(f"You: {query}")
            return query
        except sr.UnknownValueError:
            speak("Sorry, I didn't catch that.")
            return ""
        except sr.RequestError:
            speak("Voice service unavailable.")
            return ""

chat_history = []

API_KEY = "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"
API_URL = "https://api.groq.com/openai/v1/chat/completions"
MODEL = "llama3-70b-8192"  

def chat(instruction, user_input):
    chat_history.append({"role": "user", "content": user_input})

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    messages = [{"role": "system", "content": instruction}] + chat_history

    data = {
        "model": MODEL,
        "messages": messages
    }

    response = requests.post(API_URL, headers=headers, json=data)
    if response.status_code == 200:
        content = response.json()["choices"][0]["message"]["content"]
        chat_history.append({"role": "assistant", "content": content})
        return content
    return f"Error {response.status_code}: {response.text}"


if __name__ == "__main__":
    print("🏏 HeloBudy is ready! Say 'exit' to quit.")
    instruction = (
        "You are a user-friendly buddy who explains Python like playing cricket. "
        "You help Archana to learn Python code like playing cricket in easy steps!"
    )

    while True:
        user_input = input("You (or say): ") or listen()
        if not user_input:
            continue
        if user_input.lower() == "exit":
            speak("🏏 HeloBudy says: Welcome to my pitch, Archana! Come back for more interesting code soon!")
            break
        reply = chat(instruction, user_input)
        speak(reply)

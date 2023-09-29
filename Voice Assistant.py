#Voice Assistant By Using Python


import tkinter as tk
import speech_recognition as sr
import pyttsx3

# Initialize the recognizer and text-to-speech engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()

# Create a function for the voice assistant to listen and respond
def listen_and_respond():
    with sr.Microphone() as source:
        update_message("Listening...")
        try:
            audio = recognizer.listen(source, timeout=5)
            user_input = recognizer.recognize_google(audio, language="en-UK")
            response = respond_to_input(user_input)
            update_message(f"You said: {user_input}\nAssistant: {response}")
            speak(response)  # Speak the response
        except sr.UnknownValueError:
            update_message("Could not understand audio")
        except sr.RequestError as e:
            update_message(f"Could not request results; {e}")

# Create a function to respond to user input and speak the response
def respond_to_input(user_input):
    if "hello" in user_input:
        response = "Hello! How can I assist you?"
    elif "goodbye" in user_input:
        response = "Goodbye! Have a great day."
    elif "your name" in user_input:
        response=" I am Voice Assistant Prepared By VIRUPAKSHI. "
    elif "thank you" in user_input:
        response="You are Most Welcome. "
    elif "good morning" in user_input:
        response="Very Good morning! Have a nice day "
    elif "which language you speak" in user_input:
        response=" I speak English Langauge"
    elif "are you robot" in user_input:
        response="No! I am a Voice Assistant!"
    elif "which is your favourite language" in user_input:
        response=" My favourite language is Kannada!"
    else:
        response = "I'm not sure how to respond to that."
    speak(response)  # Speak the response
    return response

# Create a function to update the GUI message
def update_message(message):
    message_text.set(message)

# Create a function to speak text
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Create the GUI window
root = tk.Tk()
root.title("Voice Assistant - By VIRUPAKSHI")

# Create a text variable to hold the message text
message_text = tk.StringVar()
message_text.set("Assistant: ")

# Create a label for displaying messages
message_label = tk.Label(root, textvariable=message_text, font=("Arial", 12))
message_label.pack(pady=20)

# Create a button to trigger voice recognition
listen_button = tk.Button(root, text="Listen", command=listen_and_respond)
listen_button.pack(pady=10)

# Start the main GUI loop
root.mainloop()

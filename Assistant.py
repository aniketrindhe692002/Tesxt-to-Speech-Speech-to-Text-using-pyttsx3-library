import pyttsx3 
import speech_recognition as sr

def speech_to_text():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Say Something")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source, timeout=1.5)

    try:
        text=recognizer.recognize_google(audio)
        return text
    except sr.UnknownValueError:
        return "Sorry I couldn't understand anything"
    except sr.RequestError as e:
        return f"Error Connecting : {e}"
    except sr.WaitTimeoutError:
        return f"Time out for talking: {e}"


def text_to_speech(text):
    engine = pyttsx3.init()
    engine.setProperty('rate',200)
    engine.say(text)
    engine.runAndWait()

while(1):
    words = speech_to_text()
    if words == "HELLO ICAI" or words=="hello icai" or words == "hello ICAI" or words == "HELLO icai":
        word1="Hello Team DEBUG Your Asssitant is Waiting"
        word2="How can i Help you Aniket Sir"
        print(word1)
        print(word2)
        text_to_speech(word1)
        text_to_speech(word2)
    elif words == "exit" or words == "bye":
        word2="ok bye have a nice day"
        # print("ok bye have a nice day")
        text_to_speech(word2)
        exit()
    else:
        print(words)
        text_to_speech(words)
    
    
import pyttsx3
import speech_recognition as sr
import wikipedia
import webbrowser


# init pyttsx
engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")

engine.setProperty('voice', voices [1].id)  # 1 for female and 0 for male voice


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print("User said:" + query + "\n")
    except Exception as e:
        print(e)
        speak("I didn't understand. Could you please repeat ?")
        return "None"
    return query.lower()


if __name__ == '__main__':
    speak("Amigo voice assistance activated ")
    speak("This is developed by sathwik kumar")
    speak("How can i help you")
    while True:
        query = take_command()
        if 'open wikipedia' in query:
            speak("Opening Wikipedia...")
            webbrowser.open("https://en.wikipedia.org/")
            speak("Searching Wikipedia ...")
            query = query.replace("wikipedia", '')
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            speak(results)
        elif 'about you' in query:
            speak("I am amigo developed by P.Sathwik kumar")
        elif 'hi' in query:
            speak("Hello")
        elif 'open youtube' in query:
            speak("opening youtube")
            webbrowser.open("https://www.youtube.com/")
        elif 'open wikipedia' in query:
            speak("Opening Wikipedia...")
            webbrowser.open("https://www.wikipedia.org/")
        elif 'open jntu' in query:
            speak("Opening jntu...")
            webbrowser.open("https://youtu.be/dn27exmVF9A")
        elif 'open google' in query:
            speak("opening google")
            webbrowser.open("https://www.google.com/")
        elif 'open telegram' in query:
            speak("opening telegram")
            webbrowser.open("https://www.telegram.org/")

        elif 'open stackoverflow' in query:
            speak("opening stackoverflow")
            webbrowser.open("https://www.stackoverflow.com/")
        elif 'open spotify' in query:
            speak("opening spotify")
            webbrowser.open("https://www.spotify.com/")
        elif 'open instagram' in query:
            speak("opening instagram")
            webbrowser.open("https://www.instagram.com/")
        elif 'open facebook' in query:
            speak("opening facebook")
            webbrowser.open("https://www.facebook.com/")
        elif 'open whatsapp' in query:
            speak("opening whatsapp")
            webbrowser.open("https://www.whatsapp.com/")
        elif 'play music' in query:
            speak("opening music")
            webbrowser.open("https://www.spotify.com/")
        elif 'exit' in query or 'Goodbye' in query:
            speak("Goodbye! Have a nice day.")
        # else:
        #     speak("I am sorry, I don't have the capability to open that website or application.")
        exit(0)

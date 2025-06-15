import pyttsx3, datetime, webbrowser, pyautogui, wikipedia, json, subprocess, requests, time, pywhatkit
import pyjokes, psutil, speech_recognition as sr, os

# ----------------------- TTS Setup -----------------------
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('rate', 150)

def speak(text):
    print(f"JARVIS: {text}")
    engine.say(text)
    engine.runAndWait()

def set_voice(index=0):
    if index < len(voices):
        engine.setProperty('voice', voices[index].id)
        speak("Voice configured.")
    else:
        speak("Voice index out of range.")

# ----------------------- Speech Recognition -----------------------
def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        query = r.recognize_google(audio).lower()
        print(f"You said: {query}")
        return query
    except sr.UnknownValueError:
        speak("Sorry, I didn't catch that.")
        return ""
    except sr.RequestError:
        speak("Speech service is unavailable.")
        return ""

# ----------------------- Utilities -----------------------
def get_time():
    now = datetime.datetime.now().strftime("%I:%M %p")
    speak(f"The time is {now}.")

def get_date():
    now = datetime.datetime.now()
    speak(f"Today's date is {now.strftime('%B %d, %Y')}")

def wish_me():
    hour = datetime.datetime.now().hour
    if hour < 12:
        greet = "Good morning!"
    elif hour < 18:
        greet = "Good afternoon!"
    else:
        greet = "Good evening!"
    speak(f"{greet} I am Jarvis, your AI assistant.")

def send_whatsapp(phone_no, message):
    try:
        speak("Opening WhatsApp Web.")
        webbrowser.open(f"https://web.whatsapp.com/send?phone={phone_no}&text={message}")
        pyautogui.sleep(12)
        pyautogui.press('enter')
        speak("Message sent successfully.")
    except Exception as e:
        speak("Failed to send message.")
        print(f"Error: {e}")

def open_application(app_name):
    try:
        app_map = {
            "notepad": "notepad.exe",
            "chrome": "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe",
            "calculator": "calc.exe"
        }
        if app_name in app_map:
            subprocess.Popen(app_map[app_name])
            speak(f"Opening {app_name}")
        else:
            speak(f"App {app_name} not configured.")
    except Exception as e:
        speak("Couldn't open the application.")
        print(e)

def take_screenshot():
    img = pyautogui.screenshot()
    file = f"screenshot_{int(time.time())}.png"
    img.save(file)
    speak("Screenshot taken and saved.")

def get_weather(city="Delhi"):
    try:
        url = f"https://wttr.in/{city}?format=3"
        res = requests.get(url)
        speak(f"Weather update: {res.text}")
    except:
        speak("Couldn't get the weather.")

def tell_joke():
    joke = pyjokes.get_joke()
    speak(joke)

def system_status():
    battery = psutil.sensors_battery()
    speak(f"Battery is at {battery.percent}% and is {'plugged in' if battery.power_plugged else 'not plugged in'}.")

def set_timer(seconds):
    speak(f"Setting a timer for {seconds} seconds.")
    time.sleep(seconds)
    speak("Time's up!")

def calculate(expression):
    try:
        result = eval(expression)
        speak(f"The result is {result}")
    except:
        speak("I couldn't calculate that.")

def play_on_youtube(song):
    speak(f"Playing {song} on YouTube")
    pywhatkit.playonyt(song)

# ----------------------- Command Processor -----------------------
def process_command(command):
    match command:
        # Basic
        case c if "time" in c:
            get_time()
        case c if "date" in c:
            get_date()
        case c if "wikipedia" in c:
            speak("What should I search on Wikipedia?")
            topic = listen()
            try:
                summary = wikipedia.summary(topic, sentences=2)
                speak(f"According to Wikipedia, {summary}")
            except Exception:
                speak("Sorry, couldn't fetch info.")
        case c if "whatsapp" in c:
            speak("Phone number with country code?")
            phone_no = input("Phone number: ")
            speak("Message?")
            message = listen()
            send_whatsapp(phone_no, message)

        # Utility
        case c if "screenshot" in c:
            take_screenshot()
        case c if "weather" in c:
            speak("Which city?")
            city = listen()
            get_weather(city)
        case c if "joke" in c:
            tell_joke()
        case c if "battery" in c:
            system_status()
        case c if "timer" in c:
            speak("For how many seconds?")
            seconds = int(input("Seconds: "))
            set_timer(seconds)

        # Productivity
        case c if "calculate" in c:
            speak("What do you want me to calculate?")
            expr = listen()
            calculate(expr)
        case c if "note" in c:
            speak("What should I write?")
            note = listen()
            with open("jarvis_notes.txt", "a") as f:
                f.write(f"{datetime.datetime.now()}: {note}\n")
            speak("Note saved.")
        case c if "play" in c and "youtube" in c:
            speak("Which song?")
            song = listen()
            play_on_youtube(song)

        # System
        case c if "open" in c:
            for app in ["notepad", "chrome", "calculator"]:
                if app in c:
                    open_application(app)
                    break
        case c if "lock" in c:
            speak("Locking your system.")
            os.system("rundll32.exe user32.dll,LockWorkStation")
        case c if "shutdown" in c:
            speak("Shutting down. See you soon.")
            os.system("shutdown /s /t 1")
            return False
        case c if "restart" in c:
            speak("Restarting system.")
            os.system("shutdown /r /t 1")
            return False
        case c if "exit" in c or "stop" in c:
            speak("Goodbye!")
            return False

        # Default
        case _:
            speak("Sorry, I didn't understand that.")
    return True

# ----------------------- Main -----------------------
if __name__ == "__main__":
    set_voice(0)
    wish_me()
    running = True
  
while running:
    command = listen()
    if command.strip():  # only process non-empty commands
        running = process_command(command)


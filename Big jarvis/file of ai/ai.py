
import datetime
import os
import smtplib
import sys
import pyttsx3
import requests
import speech_recognition as sr
import wikipedia
import webbrowser
import random
import pause
import wolframalpha
import playsound
import pyjokes
import time
from requests import get
import socket
engine = pyttsx3.init()
engine.setProperty('rate',190)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty('volume', 1)

def voice_change(v):
    x = int(v)
    engine.setProperty('voice', voices[x].id)
    speak("here you go sir i have  changed my voice ")

def femalevoice():
    voice_change(1)

def malevoice():
    voice_change(9)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    print(audio)

def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    date = int(datetime.datetime.now().day)
    speak("Todays date is ")
    speak(date)
    speak(month)
    speak(year)


def checktime(tt):
    hour = datetime.datetime.now().hour
    if ("morning" in tt):
        if (hour >= 6 and hour < 12):
            speak("Good morning Boss")
        else:
            if (hour >= 12 and hour < 18):
                speak("it's Good afternoon boss")
            elif (hour >= 18 and hour < 24):
                speak("it's Good evening boss")
            else:
                speak("it's Goodnight sir")
    elif ("afternoon" in tt):
        if (hour >= 12 and hour < 18):
            speak("it's Good afternoon sir")
        else:
            if (hour >= 6 and hour < 12):
                speak("Good morning sir")
            elif (hour >= 18 and hour < 24):
                speak("Good evening sir")
            else:
                speak("Goodnight sir")
    else:
        speak("night sir!")


#welcome function
def wishme():
    hour = datetime.datetime.now().hour
    if (hour >= 6 and hour < 12):
        speak("Good Morning boss!")
    elif (hour >= 12 and hour < 18):
        speak("Good afternoon boss")
    elif (hour >= 18 and hour < 24):
        speak("Good evening boss")
    else:
        speak("Goodnight sir")


def WIFI():
    IPaddress=socket. gethostbyname(socket. gethostname())
    if IPaddress=="127.0.0.1":
        speak('no internet connection')
    else:
        print("Connected, with the IP address: "+ IPaddress )


def wishme_end():
    speak("signing off")
    hour = datetime.datetime.now().hour
    if (hour >= 6 and hour < 12):
        speak("Good Morning")
    elif (hour >= 12 and hour < 18):
        speak("Good afternoon")
    elif (hour >= 18 and hour < 24):
        speak("Good evening")
    else:
        speak("Goodnight.. Sweet dreams")
    quit()

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 0.5
        r.energy_threshold = 9999
        audio = r.listen(source)

    try:
        print("Recognizing...")
        voice_data = r.recognize_google(audio, language='en-in')
        print(f"User said: {voice_data}\n")

    except Exception as e:
        # print(e)
        print("Say that again please...")
        return "None"
    return voice_data

#weather condition
def weather():
    api_key = "30b2e680ad9c7790ec02fdb4f97f4573" #generate your own api key from open weather
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    city_name = ('guwahati')
    complete_url = base_url + "appid=" + api_key + "&q=" + city_name
    response = requests.get(complete_url)
    x = response.json()
    if x["cod"] != "404":
        y = x["main"]
        current_temperature = y["temp"]
        current_pressure = y["pressure"]
        current_humidiy = y["humidity"]
        z = x["weather"]
        weather_description = z[0]["description"]
        r = ("in " + city_name + " Temperature is " +
             str(int(current_temperature - 273.15)) + " degree celsius " +
             ", atmospheric pressure " + str(current_pressure) + " hpa unit" +
             ", humidity is " + str(current_humidiy) + " percent"
             " and " + str(weather_description))
        speak(r)
    else:
        speak(" City Not Found ")

def Sweather():
    api_key = "30b2e680ad9c7790ec02fdb4f97f4573" #generate your own api key from open weather
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    city_name = ('guwahati')
    complete_url = base_url + "appid=" + api_key + "&q=" + city_name
    response = requests.get(complete_url)
    x = response.json()
    if x["cod"] != "404":
        y = x["main"]
        current_temperature = y["temp"]
        current_pressure = y["pressure"]
        current_humidiy = y["humidity"]
        z = x["weather"]
        weather_description = z[0]["description"]
        r = ("outside " + " the Temperature is " +
             str(int(current_temperature - 273.15)) + " degree celsius " +
             ", atmospheric pressure " + str(current_pressure) + " hpa unit" +
             ", humidity is " + str(current_humidiy) + " percent"
             " and " + str(weather_description))
        speak(r)
    else:
        speak(" City Not Found ")


def personal():
    speak(
        "Now its time to introduce myself, I am mark , a virtual artificial intelligence and i am her to assist you to a variety of task since best i can , 24 hours a day , 7days a week, importing all  preference  from home interface , system is now fully operational"
    )


def screenshot():
    img = pyautogui.screenshot()
    img.save(
        "C:\\mark"
    )

def noint():
    IPaddress=socket. gethostbyname(socket. gethostname())
    if IPaddress=="127.0.0.1":
        speak('no internet connection')


def cpu():
    usage = str(psutil.cpu_percent())
    speak('CPU usage is at ' + usage)
    print('CPU usage is at ' + usage)

def battery():
    battery = psutil.sensors_battery()
    speak("Battery is at")
    speak(battery.percent)
    print("battery is at:" + str(battery.percent))

def jokes():
    j = pyjokes.get_joke()
    print(j)
    speak(j)

from playsound import playsound

if __name__ == "__main__":
    noint()
    while (True):
            os.system('porcupine_demo_mic --keywords hey')
            playsound('C:\\Users\\ADMIN\\Desktop\\VIRTUAL ASSISTANT\\chime.wav')
            voice_data = takeCommand().lower()

            if 'beatbox' in voice_data or 'bit box' in voice_data or 'big box' in voice_data or 'bigbox' in voice_data:
                playsound('C:\\Users\\ADMIN\\Desktop\\VIRTUAL ASSISTANT\\preview.mp3')
            if 'repeat' in voice_data:
                voice_data = voice_data.replace("repeat", "")
                voice_data = voice_data.replace("that", "")
                speak(voice_data)
                os.system('"C:\\Users\\ADMIN\\Desktop\\VIRTUAL ASSISTANT\\ASSISTANT.py"')
            if ('time' in voice_data):
                strTime = datetime.datetime.now().strftime("%I:%M:%S")
                speak(f', {strTime}')
                os.system('"C:\\Users\\ADMIN\\Desktop\\VIRTUAL ASSISTANT\\ASSISTANT.py"')
            elif ('date' in voice_data ):
                date()
                os.system('"C:\\Users\\ADMIN\\Desktop\\VIRTUAL ASSISTANT\\ASSISTANT.py"')

            elif 'i am sad' in voice_data:
                speak("i don't like it")
                os.system('"C:\\Users\\ADMIN\\Desktop\\VIRTUAL ASSISTANT\\ASSISTANT.py"')

            elif 'i am happy' in voice_data:
                speak('i love it ')
                os.system('"C:\\Users\\ADMIN\\Desktop\\VIRTUAL ASSISTANT\\ASSISTANT.py"')

            elif 'i love you' in voice_data:
                reply= 'i also like you' , 'i like it' , "i don't hate you" , 'i also love you as a friend'
                speak(random.choices(reply))
                os.system('"C:\\Users\\ADMIN\\Desktop\\VIRTUAL ASSISTANT\\ASSISTANT.py"')

            elif ("tell me about yourself" in voice_data):
                personal()
            elif ("about you" in voice_data):
                personal()
                os.system('"C:\\Users\\ADMIN\\Desktop\\VIRTUAL ASSISTANT\\ASSISTANT.py"')

            elif ("who are you" in voice_data):
                personal()
                os.system('"C:\\Users\\ADMIN\\Desktop\\VIRTUAL ASSISTANT\\ASSISTANT.py"')

            elif ("yourself" in voice_data):
                personal()
                os.system('"C:\\Users\\ADMIN\\Desktop\\VIRTUAL ASSISTANT\\ASSISTANT.py"')

            elif 'tell me the weather in' in voice_data or   "tell me today's weather in" in voice_data:
                voice_data = voice_data.replace("weather", "")
                voice_data = voice_data.replace("of", "")
                voice_data = voice_data.replace("at", "")
                voice_data = voice_data.replace("the", "")
                voice_data = voice_data.replace("in", "")
                voice_data = voice_data.replace("city", "")
                voice_data = voice_data.replace("tell", "")
                voice_data = voice_data.replace("me", "")
                voice_data = voice_data.replace("can", "")
                voice_data = voice_data.replace("you", "")
                voice_data = voice_data.replace("today's", "")
                voice_data = voice_data.replace("today's", "")

                api_key = "30b2e680ad9c7790ec02fdb4f97f4573"
                base_url = "http://api.openweathermap.org/data/2.5/weather?"
                city_name = voice_data
                complete_url = base_url + "appid=" + api_key + "&q=" + city_name
                response = requests.get(complete_url)
                x = response.json()
                if x["cod"] != "404":
                    y = x["main"]
                    current_temperature = y["temp"]
                    current_pressure = y["pressure"]
                    current_humidiy = y["humidity"]
                    z = x["weather"]
                    weather_description = z[0]["description"]
                    r = ("in " + city_name + " Temperature is " +
                        str(int(current_temperature - 273.15)) + " degree celsius " +
                        ", atmospheric pressure " + str(current_pressure) + " hpa unit" +
                        ", humidity is " + str(current_humidiy) + " percent"
                                                                " and " + str(weather_description))
                    speak(r)
                    os.system('"C:\\Users\\ADMIN\\Desktop\\VIRTUAL ASSISTANT\\ASSISTANT.py"')
                else:
                    speak(" City Not Found ")
                    os.system('"C:\\Users\\ADMIN\\Desktop\\VIRTUAL ASSISTANT\\ASSISTANT.py"')

            elif 'tell me the weather' in voice_data:
                weather()
                os.system('"C:\\Users\\ADMIN\\Desktop\\VIRTUAL ASSISTANT\\ASSISTANT.py"')
            elif 'youtube' in voice_data:
                voice_data = voice_data.replace("youtube","")
                voice_data = voice_data.replace("search","")
                voice_data = voice_data.replace("on","")
                voice_data = voice_data.replace("youtube","")
                site = 'https://youtube.com/search?q='+ voice_data
                webbrowser.open(site)
            elif 'tell me the temperature' in voice_data:
                weather()
                os.system('"C:\\Users\\ADMIN\\Desktop\\VIRTUAL ASSISTANT\\ASSISTANT.py"')

            elif "tell me today's weather" in voice_data:
                weather()
                os.system('"C:\\Users\\ADMIN\\Desktop\\VIRTUAL ASSISTANT\\ASSISTANT.py"')

            elif "tell me today's temperature" in voice_data:
                weather()
                os.system('"C:\\Users\\ADMIN\\Desktop\\VIRTUAL ASSISTANT\\ASSISTANT.py"')

            if 'wikipedia' in voice_data:
                speak('Searching Wikipedia...')
                voice_data = voice_data.replace("wikipedia", "")
                results = wikipedia.summary(voice_data, sentences=2)
                speak("According to Wikipedia")
                print(results)
                speak(results)
                os.system('"C:\\Users\\ADMIN\\Desktop\\VIRTUAL ASSISTANT\\ASSISTANT.py"')

            elif 'clock' in voice_data:
                path='F:\\digitalClock.py'
                os.startfile(path)
                os.system('"C:\\Users\\ADMIN\\Desktop\\VIRTUAL ASSISTANT\\ASSISTANT.py"')


            elif  "open website" in voice_data:
                speak("Tell me the name of the website")
                search = takeCommand().lower()
                speak('Opening' + search)
                url = 'www.' + search +'.com'
                webbrowser.open(url)
                os.system('"C:\\Users\\ADMIN\\Desktop\\VIRTUAL ASSISTANT\\ASSISTANT.py"')

            elif ("song" in voice_data or 'music' in voice_data or 'gana' in voice_data):
                speak("playing a random song")
                path ='D:\\music\\'
                files = os.listdir(path)
                d = random.choice(files)
                os.startfile('D:\\music\\'+ d)
                os.system('"C:\\Users\\ADMIN\\Desktop\\VIRTUAL ASSISTANT\\ASSISTANT.py"')


            elif ("create a reminder list" in voice_data or "reminder" in voice_data):
                speak("What is the reminder?")
                data = takeCommand()
                speak("You said to remember that" + data)
                reminder_file = open("data.txt", 'a')
                reminder_file.write('\n')
                reminder_file.write(data)
                reminder_file.close()
                os.system('"C:\\Users\\ADMIN\\Desktop\\VIRTUAL ASSISTANT\\ASSISTANT.py"')


            elif 'full form of friday' in voice_data:
                speak('Female Replacement Intelligent Digital Assistant Youth')
                os.system('"C:\\Users\\ADMIN\\Desktop\\VIRTUAL ASSISTANT\\ASSISTANT.py"')

            elif 'face' in voice_data:
                speak('opening face recognition')
                path= 'F:\\detect_face_video.py'
                os.startfile(path)
                os.system('"C:\\Users\\ADMIN\\Desktop\\VIRTUAL ASSISTANT\\ASSISTANT.py"')

            elif ("do you know anything" in voice_data or "remember" in voice_data):
                reminder_file = open("data.txt", 'r')
                speak("You said me to remember that: " + reminder_file.read())
                os.system('"C:\\Users\\ADMIN\\Desktop\\VIRTUAL ASSISTANT\\ASSISTANT.py"')



            elif ("powers" in voice_data or "help" in voice_data
                or "features" in voice_data or 'what can you do' in voice_data):
                features = ''' i can help to do lot many things like..
                i can tell you the current time and date,
                i can tell you the current weather,
                i can tell you battery and cpu usage,
                i can create the reminder list,
                i can shut down or logout or hibernate your system,
                i can tell you non funny jokes,
                i can open any website,
                i can repeat what you  you told me,
                i can search the thing on wikipedia,
                i can change my voice from male to female and vice-versa
                i have  a search engine make by my sir if you want to know something just say open search and ask the question
                i have a wake word detection i will be online if you say hey mark
                And yes one more thing, My boss is working on this system to add more features...,
                tell me what can i do for you??
                '''
                speak(features)
                os.system('"C:\\Users\\ADMIN\\Desktop\\VIRTUAL ASSISTANT\\ASSISTANT.py"')


            elif ("voice" in voice_data):
                if 'female' in voice_data:
                    femalevoice()

                else:
                    malevoice()


            elif ('i am done' in voice_data or 'bye bye mark' in voice_data
                or 'go offline mark' in voice_data or 'bye' in voice_data):
                os.system('"C:\\Users\\ADMIN\\Desktop\\VIRTUAL ASSISTANT\\ASSISTANT.py"')

            elif "how's your day going" in voice_data or 'how is your day going' in voice_data:
                speak('Wonderfull , thanks for asking me, how can i help you ')
                os.system('"C:\\Users\\ADMIN\\Desktop\\VIRTUAL ASSISTANT\\ASSISTANT.py"')

            elif 'change name' in voice_data:
                f = open("C:\\MARK\\my name.txt", "r+")
                f.seek(0)
                f.truncate()
                speak('tell me your name')
                sname = takeCommand()
                file1 = open("C:\\MARK\\my name.txt","w")
                file1.write(sname)
                file1.close()
                file_contents = f.read()
                speak ('from now i will call you sir' + file_contents)
                os.system('"C:\\Users\\ADMIN\\Desktop\\VIRTUAL ASSISTANT\\ASSISTANT.py"')

            elif 'change birthday' in voice_data:
                f = open("C:\\MARK\\birthday.txt", "r+")
                f.seek(0)
                f.truncate()
                speak('tell me the birthday date')
                sname = takeCommand()
                file1 = open("C:\\MARK\\birthday.txt","w")
                file1.write(sname)
                file1.close()
                file_contents = f.read()
                speak ('so your birthday is at'+ file_contents)

            elif 'my birthday' in voice_data:
                f = open('C:\\MARK\\birthday.txt', 'r')
                file_contents = f.read()
                speak(file_contents)
                os.system('"C:\\Users\\ADMIN\\Desktop\\VIRTUAL ASSISTANT\\ASSISTANT.py"')

            elif 'hey there' in voice_data:
                speak('hello there')
                os.system('"C:\\Users\\ADMIN\\Desktop\\VIRTUAL ASSISTANT\\ASSISTANT.py"')

            elif 'tell me my name' in voice_data:
                f = open('C:\\MARK\\my name.txt', 'r')
                file_contents = f.read()
                speak(file_contents)
                os.system('"C:\\Users\\ADMIN\\Desktop\\VIRTUAL ASSISTANT\\ASSISTANT.py"')


            elif 'shutdown' in voice_data:
                speak('system offline')
                os.system("shutdown /p")
                os.system('"C:\\Users\\ADMIN\\Desktop\\VIRTUAL ASSISTANT\\ASSISTANT.py"')

            elif 'open instagram' in voice_data:
                speak('opening Instagram')
                webbrowser.open('https://www.instagram.com/?hl=en')
                os.system('"C:\\Users\\ADMIN\\Desktop\\VIRTUAL ASSISTANT\\ASSISTANT.py"')
            elif 'full form of jarvis' in voice_data:
                speak ('Just A Rather Very Intelligent System')
                os.system('"C:\\Users\\ADMIN\\Desktop\\VIRTUAL ASSISTANT\\ASSISTANT.py"')

            elif 'hey' in voice_data:
                speak('hey')
                os.system('"C:\\Users\\ADMIN\\Desktop\\VIRTUAL ASSISTANT\\ASSISTANT.py"')

            elif 'news' in voice_data:
                speak('here you go sir')
                path='C:\\MARK\\news.py'
                os.startfile(path)
                os.system('"C:\\Users\\ADMIN\\Desktop\\VIRTUAL ASSISTANT\\ASSISTANT.py"')


            elif 'screenshot' in voice_data:
                speak('ok sir')
                screenshot()
                os.system('"C:\\Users\\ADMIN\\Desktop\\VIRTUAL ASSISTANT\\ASSISTANT.py"')

            elif 'cpu' in voice_data:
                cpu()
                os.system('"C:\\Users\\ADMIN\\Desktop\\VIRTUAL ASSISTANT\\ASSISTANT.py"')

            elif  ('there' in voice_data or 'dear' in voice_data):
                speak('For you Sir always')
                os.system('"C:\\Users\\ADMIN\\Desktop\\VIRTUAL ASSISTANT\\ASSISTANT.py"')

            elif 'battery' in voice_data:
                battery()
                os.system('"C:\\Users\\ADMIN\\Desktop\\VIRTUAL ASSISTANT\\ASSISTANT.py"')

            elif 'joke' in voice_data:
                jokes()
                os.system('"C:\\Users\\ADMIN\\Desktop\\VIRTUAL ASSISTANT\\ASSISTANT.py"')


            elif 'open location' in voice_data:
                speak('tell me the location you are looking for')
                location = takeCommand()
                url2 = 'https://google.nl/maps/place/' + location +'/&amp;'
                webbrowser.open(url2)
                speak('location on your screen boss')
                os.system('"C:\\Users\\ADMIN\\Desktop\\VIRTUAL ASSISTANT\\ASSISTANT.py"')
            elif 'close browser' in voice_data:
                try:
                    speak('as you wish')
                    os.system('TASKKILL /F /IM msedge.exe')

                except Exception as e:
                    speak("i cant do that right now")

            elif 'close all' in voice_data:
                try:
                    speak('as you wish')
                    os.system('TASKKILL /F /IM *')

                except Exception as e:
                    speak("i cant do that right now")
            elif 'close file' in voice_data:
                try:
                    speak('as you wish')
                    os.system('TASKKILL /F /IM Explorer.exe')
                    os.system('"C:\\Users\\ADMIN\\Desktop\\VIRTUAL ASSISTANT\\ASSISTANT.py"')
                except Exception as e:
                    speak("i cant do that right now")
                    os.system('"C:\\Users\\ADMIN\\Desktop\\VIRTUAL ASSISTANT\\ASSISTANT.py"')
            elif 'my location' in voice_data:
                speak('opening your home location on browser')
                loc = 'https://www.google.co.in/maps/@26.1317482,91.8018681,18.5z'
                webbrowser.open(loc)
                os.system('"C:\\Users\\ADMIN\\Desktop\\VIRTUAL ASSISTANT\\ASSISTANT.py"')

            elif 'google' in voice_data:
                voice_data = voice_data.replace("google", "")
                voice_data = voice_data.replace("it", "")
                speak('here you go ')
                url69 = 'https://google.com/search?q=' + voice_data
                webbrowser.open(url69)
                os.system('"C:\\Users\\ADMIN\\Desktop\\VIRTUAL ASSISTANT\\ASSISTANT.py"')


            elif 'switch window' in voice_data:
                pyautogui.keyDown("alt")
                pyautogui.press("tab")
                pyautogui.press("right")
                pyautogui.keyUp("alt")
                speak('window switched')
                os.system('"C:\\Users\\ADMIN\\Desktop\\VIRTUAL ASSISTANT\\ASSISTANT.py"')

            elif 'close' in voice_data:
                pyautogui.keyDown("alt")
                pyautogui.press("F4")
                pyautogui.keyUp()
                speak('application killed')
                os.system('"C:\\Users\\ADMIN\\Desktop\\VIRTUAL ASSISTANT\\ASSISTANT.py"')

            elif 'what is your name' in voice_data:
                speak('MY NAME is Mark')
                os.system('"C:\\Users\\ADMIN\\Desktop\\VIRTUAL ASSISTANT\\ASSISTANT.py"')

            elif 'whatsapp' in voice_data:
                speak('opening whatsapp')
                wpath = 'C:\\Users\\admin\\AppData\\Local\\WhatsApp\\WhatsApp.exe'
                os.startfile(wpath)
                os.system('"C:\\Users\\ADMIN\\Desktop\\VIRTUAL ASSISTANT\\ASSISTANT.py"')
            elif 'wish birthday' in voice_data:
                speak('this is for you')
                path = 'D:\\project Friday\\Y2Mate (mp3cut.net) (1).mp3'
                os.startfile(path)
                os.system('"C:\\Users\\ADMIN\\Desktop\\VIRTUAL ASSISTANT\\ASSISTANT.py"')

            elif 'tell me my birthday' in voice_data:
                speak('i remember that you told me your birthday is at 20th march')
                os.system('"C:\\Users\\ADMIN\\Desktop\\VIRTUAL ASSISTANT\\ASSISTANT.py"')

            elif 'folder' in voice_data:
                speak('tell me the name of the folder')
                path= 'C:\\Users\\ADMIN\\Desktop'
                os.chdir(path)
                Newfolder=takeCommand()
                os.makedirs(Newfolder)
                speak('i have  made a folder named' +Newfolder+'in you dekstop directry')
                os.system('"C:\\Users\\ADMIN\\Desktop\\VIRTUAL ASSISTANT\\ASSISTANT.py"')

            elif 'hello mark' in voice_data or 'lo mark' in voice_data:
                speak("hello sir how's going")
                os.system('"C:\\Users\\ADMIN\\Desktop\\VIRTUAL ASSISTANT\\ASSISTANT.py"')

            elif 'hey  mark' in voice_data:
                speak('hey sir what can i do for you')
                os.system('"C:\\Users\\ADMIN\\Desktop\\VIRTUAL ASSISTANT\\ASSISTANT.py"')

            elif 'editor' in voice_data or 'visual studio code' in voice_data:
                speak('opening code editor')
                os.startfile('C:\\Users\\ADMIN\\AppData\\Local\\Programs\\Microsoft VS Code\\code.exe')
                os.system('"C:\\Users\\ADMIN\\Desktop\\VIRTUAL ASSISTANT\\ASSISTANT.py"')

            elif 'cmd' in voice_data or 'command' in voice_data:
                os.startfile('cmd.exe')
                os.system('"C:\\Users\\ADMIN\\Desktop\\VIRTUAL ASSISTANT\\ASSISTANT.py"')

            elif 'red or blue' in voice_data:
                speak('BLue sir')
                os.system('"C:\\Users\\ADMIN\\Desktop\\VIRTUAL ASSISTANT\\ASSISTANT.py"')

            elif 'your favorite colour' in voice_data or 'tell me your favourite colour' in voice_data:
                speak('blue')
                os.system('"C:\\Users\\ADMIN\\Desktop\\VIRTUAL ASSISTANT\\ASSISTANT.py"')

            elif 'change colour' in voice_data:
                os.system('color 03')

            elif 'how are you' in voice_data:
                speak('I am fine sir ')
                os.system('"C:\\Users\\ADMIN\\Desktop\\VIRTUAL ASSISTANT\\ASSISTANT.py"')

            elif 'ip address' in voice_data:
                ip = get('https://api.ipify.org').text
                speak(f'your ip address is {ip}"')
                os.system('"C:\\Users\\ADMIN\\Desktop\\VIRTUAL ASSISTANT\\ASSISTANT.py"')

            elif 'hello' in voice_data:
                speak('hello sir')
                os.system('"C:\\Users\\ADMIN\\Desktop\\VIRTUAL ASSISTANT\\ASSISTANT.py"')

            if 'restart' in voice_data:
                os.startfile("C:\\Users\\ADMIN\\Desktop\\VIRTUAL ASSISTANT\\ASSISTANT.py")
                os.system('"C:\\Users\\ADMIN\\Desktop\\VIRTUAL ASSISTANT\\ASSISTANT.py"')

            if 'amazon order' in voice_data:
                url = 'https://www.amazon.in/gp/css/order-history?ref_=nav_orders_first'
                webbrowser.open(url)
                sys.exit


            if 'wake up' in voice_data:
                speak('Online and ready sir')
                os.system('"C:\\Users\\ADMIN\\Desktop\\VIRTUAL ASSISTANT\\ASSISTANT.py"')

            if "you can't do anything" in voice_data or 'you are nothing' in voice_data or  'you are dumb' in voice_data or 'you dont have brain' in voice_data or 'you are mad' in voice_data:
                speak("Sorry sir")
                os.system('"C:\\Users\\ADMIN\\Desktop\\VIRTUAL ASSISTANT\\ASSISTANT.py"')



            elif 'question' in voice_data:
                speak('tell me the question you want to get')
                question = takeCommand()
                speak('getting information boss')
                try:
                    try:
                        results = wikipedia.summary(question, sentences=2)
                        speak(results)
                    except:
                        client = wolframalpha.Client('QAEXLK-RY9HY2PHAT')
                        res = client.voice_data(question)
                        results = next(res.results).text
                        speak(results)
                except:
                    speak("Sorry sir i didn't get it")


            elif 'sleep' in voice_data:
                speak('As you wish')
                sys.exit

            elif 'boreing' in voice_data:
                speak('lets play some music')
            elif 'email' in voice_data:
                speak('are you the sender?')
                sender = takeCommand()

                if 'yes' in sender:
                    try:
                        speak("Please Enter Email address of Recipient.")
                        Recipient_user = input()
                        speak('What should I say? ')
                        content = takeCommand()

                        server = smtplib.SMTP('smtp.gmail.com', 587)
                        server.ehlo()
                        server.starttls()
                        server.login("youremail", 'pass')
                        server.sendmail('youremail', Recipient_user, content)
                        server.close()
                        speak('Email sent!')

                    except:
                        speak('Sorry sir i cant send this email right now!')
                pause.seconds(1)
                os.system('"C:\\Users\\ADMIN\\Desktop\\VIRTUAL ASSISTANT\\ASSISTANT.py"')
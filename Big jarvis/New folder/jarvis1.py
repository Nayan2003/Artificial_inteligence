import time
import pyttsx3
import speech_recognition as sr
import datetime
import os
import cv2 
import random
import wikipedia
from requests import get 
import webbrowser
import pywhatkit as kit
import smtplib
import sys
import pyjokes
import pyautogui
import instaloader



engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[0].id)
engine.setProperty('voices', voices[0].id)

#text to speech
def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()
    
# converted voice to text
def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("I am Listening your rubbish talking......")
        r.pause_threshold = 1
        audio = r.listen(source,timeout=1,phrase_time_limit=5) 
        
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query}")
        
    except Exception as e:
        #speak("Say that again please...")
        return "none"
    query = query.lower()
    return query

# to wish
def wish():
    hour = int(datetime.datetime.now().hour)
    
    if hour>=0 and hour<=12:
        speak("good morning...")
    
    elif hour>12 and hour<18 :
        speak("good afternun")
    
    elif hour>18 and hour<20 :
        speak("good evening...")
        
    else:
        speak("good night..")
        
    speak("i am jarvis sir please tell me how may i help you?")

#to send email
def sendEmail(to,content):
    server =smtplib.SMTP('smtp.gmail.com',587) #587 is port .. server no
    server.ehlo()
    server.starttls()
    server.login('gs020.nayan.khuje@gnkhalsa.edu.in','nayan123')
    server.sendmail('khuje.nayan@gmail.com',to, content)
    server.close()

if __name__ == "__main__":
    wish()
    while True:
    #if 1:    
        query = takecommand().lower()
        
        
        #logik building for task
        
        if "open notepad" in query:
            npath = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Accessories\\Notepad.lnk"
            os.startfile(npath)
            
        # for closing notepad
        elif "close notepad" in query:
            speak("okay sir, closing notepad")
            os.system("taskkill /f /im notepad.exe")
            
        elif "open canva" in query:
            npath = "C:\\Users\\khuje\\AppData\\Local\\Programs\\Canva\\Canva.exe"
            os.startfile(npath)
            
        # for closing canva
        elif "close canva" in query:
            speak("okay sir, closing canva")
            os.system("taskkill /f /im canva.exe")
            
        # i can add here lots of commands for oprationg my computer
        elif "open command prompt" in query:
            os.system("start cmd")
            
        elif "open cmd" in query:
            os.system("start cmd")
            
        # for closing cmd
        elif "close cmd" in query:
            speak("okay sir, closing cmd")
            os.system("taskkill /f /im cmd.exe")
            
        elif "open camera" in query:
            cap = cv2.VideoCapture(0)
            while True:
                ret, img = cap.read()
                cv2.imshow('webcam', img)
                k = cv2.waitKey(50)
                if k==27:
                    break
            cap.release()
            cv2.destroyAllWindows()
            
       
            
        elif "play music"  in query:
            music_dir = "C:\\Users\\khuje\\Desktop\\song"
            songs = os.listdir(music_dir)
            # rd = random.choice(songs)
            for song in songs :
                if song.endswith('.mp3'):
                    
                     os.startfile(os.path.join(music_dir, song))
                      
                     
        elif "ip address" in query:
            ip = get('https://api.ipify.org').text
            speak(f"your IP address is {ip}")            
            
            
        elif "wikipedia" in query:
            speak("searching wikipedia....")
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query, sentences=2)
            speak("Acording to wikipedia")
            print(results)
            speak(results)
            #print(results)
        elif "the time" in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}") 
            
        #to set alarm
        elif "set-alarm" in query:
            nn =int(datetime.date.now().hour)
            if nn==22:
                music_dir= 'D:\\jarvis alarm'
                songs = os.listdir(music_dir)
                os.startfile(os.path.join(music_dir, songs[0]))
                
        #to find a joke 
        elif "tell me a joke" in query:
            joke = pyjokes.get_joke()
            speak(joke)
        
        
        elif "open youtube"  in query:
            webbrowser.open("www.youtube.com")
        
        elif "open instagram"  in query:
            webbrowser.open("www.instagram.com")
            
        elif "open feacebook"  in query:
            webbrowser.open("www.facebook.com")
            
        elif "open google"  in query:
            speak("sir, what should i search on google")
            cm = takecommand().lower()
            webbrowser.open(f"{cm}")
            
        elif "open stack overflow"  in query:
            webbrowser.open("www.stackoverflow.com")
            
      #  elif "send massage" in query:
       #     kit.sendwhatmsg("+")
       
        elif "play songs on youtube" in query:
        
            speak("sir, what should i search on youtube")
            cm1 = takecommand().lower()        
            kit.playonyt(f"{cm1}")
           
        elif "email to nayan" in query:
            try:
                speak("what should i say?")
                content = takecommand()
                to = "khuje.nayan@gmail.com"
                sendEmail(to,content)
                speak("Email has been sent to nano")
                
            except Exception as e:
                print(e)
                speak("sorry sir, i am not able to sent email to nano ")
                
                
         #for shut down the pc       
        elif "shut down the system" in query:
            os.system("shutdown /s /t 5")
        
          #for restart the pc  
        elif "restart the system" in query:
            os.system("shutdown /r /t 5")
               
        elif "sleep the system" in query:
            os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")
                
        elif "no thanks" in query:
            speak("thanks for using me sir, have a good day.")
            sys.exit()
        
        elif "nothing" in query:
            speak("thanks for using me sir, have a good day.")
            sys.exit()
        
        elif 'switch the window' in query:
            pyautogui.keyDown("alt")
            pyautogui.press("tab")
            time.sleep(1)
            pyautogui.keyUp("alt") 
            
    ################for location
    
        elif "where i am" in query or "where we are" in query:
            speak("wait sir, let me check")
            try:
                ipAdd = get( 'https://api.ipify.org').text
                print(ipAdd)
                url = 'https://get.geojs.io/v1/ip/geo/'+ipAdd+'.json'
                geo_requests = get(url)
                geo_data = geo_requests.json()
                # print(geo_data)
                city = geo_data['city']
                # state =  geo_data['state'] 
                country = geo_data['country ']
                speak(f"sir i am not sure, but i think we are in {city} city of {country} country")
            except Exception as e:
                speak("sorry sir, Due to network issue i am not able to find where we are. ")
                pass
        
        ############# for insta gram
        
        elif "instagram profile" in query or "profile on instagram" in query:
            speak("sir please enter the user name correctly")
            name = input("Enter username here: ")
            webbrowser. open("www.instagram.com/ {name} ")
            speak(f"Sir here is the profile of the user {name}" )
            time. sleep(5)
            speak("sir would you like to download profile picture of this account. ")
            condition = takecommand() . Imger()
            if "yes" in condition:
                mod = instaloader.Instaloader() #pip install instadownloader
                mod.download_profile(name, profile_pic_on1y=True)
                speak("i am done sir, profile picture is saved in our main folder. now' i am ready")
            else:
                pass
        
        
        
        
        
        speak("sir do you have any other work")  
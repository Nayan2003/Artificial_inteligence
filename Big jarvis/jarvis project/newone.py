import time
import pyttsx3
import speech_recognition as sr
import datetime
import os
import cv2 
from bs4 import BeautifulSoup
import random
import wikipedia
import requests

import webbrowser
import pywhatkit as kit
import smtplib
import sys
import pyjokes
import pyautogui as p
import numpy as np
import instaloader



engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
#print(voices[0].id)
engine.setProperty("voices", voices[0].id)
#engine.setProperty("rate",130)

#text to speech
def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()

# wether forcast
def weather():
    speak("Checking the details for weather...")
    URL = "https://weather.com/weather/today/l/26.62,87.36?par=google&temp=c"
    header = {"User-Agent":'your user agent'}
    page = requests.get(URL, headers=header)
    soup = BeautifulSoup(page.content, 'html.parser')
    temperature = soup.find(class_="CurrentConditions--tempValue--3KcTQ").get_text()
    description = soup.find(class_="CurrentConditions--phraseValue--2xXSr").get_text()
    temp = "Sir, the temperature is " + temperature + " celcius." + ' and it is ' + description + ' outside.'
    speak(temp)
    if temperature < '20°':
        speak("It will be better if you wear woolen clothes, sir.")
    elif temperature <= '14°':
        speak("Sir, it is very cold outside. If you want to go outside, wear woolen clothes.")
    elif temperature >= '25°':
        speak("Sir, you donot need to wear woolen clothes to go outside.")    
# converted voice to text
def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("I am Listening your rubbish talking......")
        r.pause_threshold = 1
        audio = r.listen(source) 
        audio = r.listen(source,0,4)
        
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
    tt = time.strftime("%I:%M %p")
    
    if hour>=0 and hour<=12:
        speak("good morning..")
    
    elif hour>12 and hour<18 :
        speak("good afternoon..")
    
    elif hour>18 and hour<20 :
        speak("good evening..")
        
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



def TaskExecution():
    p.press('esc')
    speak("verification successful")
    speak("welcom back nayan sir")
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
            
        #wether
        elif "what's the weather" in query or 'tell me the temperature' in query or "what's the temperature" in query:
            weather()
            
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
                     
                     
      #  C:\Users\khuje\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Visual Studio Code\Visual Studio Code.lnk
        elif "open vs code" in query:
            npath = "C:\\Users\\khuje\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Visual Studio Code\\Visual Studio Code.lnk"
            os.startfile(npath)              
                     
        elif "ip address" in query:
            ip = requests.get('https://api.ipify.org').text
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
        
        #### for timer 
        elif 'timer' in query or 'stopwatch' in query:
            speak("For how many minutes?")
            timing = takecommand()
            timing =timing.replace('minutes', '')
            timing = timing.replace('minute', '')
            timing = timing.replace('for', '')
            timing = float(timing)
            timing = timing * 60
            speak(f'I will remind you in {timing} seconds')

            time.sleep(timing)
            speak('Your time has been finished sir')
                    
        #to find a joke 
        elif "tell me a joke" in query:
            joke = pyjokes.get_joke()
            speak(joke)
        
        
        elif "open youtube"  in query:
            webbrowser.open("www.youtube.com")
        
        elif "open instagram"  in query:
            webbrowser.open("www.instagram.com")
            
        elif "open facebook"  in query:
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
            p.keyDown("alt")
            p.press("tab")
            time.sleep(1)
            p.keyUp("alt") 
            
        
            
   
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
            
            
        elif "you can sleep " in query or "sleep now" in query:
            speak("okay sir, i am going to sleep you can call me anytime.")
        break 
        
       
      
        
 
    
    
if __name__ == "__main__":
    
    recognizer = cv2.face.LBPHFaceRecognizer_create() # Local Binary Patterns Histograms
    recognizer.read('trainer/trainer.yml')   #load trained model
    cascadePath = "C:\\Users\\khuje\\AppData\\Local\\Programs\\Python\\Python311\\Lib\\site-packages\\cv2\\data\\haarcascade_frontalface_default.xml"
    faceCascade = cv2.CascadeClassifier(cascadePath) #initializing haar cascade for object detection approach

    font = cv2.FONT_HERSHEY_SIMPLEX #denotes the font type


    id = 1 #number of persons you want to Recognize


    names = ['','nayan','jaya'] #names, leave first empty bcz counter starts from 0


    cam = cv2.VideoCapture(0, cv2.CAP_DSHOW) #cv2.CAP_DSHOW to remove warning
    cam.set(3, 640) # set video FrameWidht
    cam.set(4, 480) # set video FrameHeight

    # Define min window size to be recognized as a face
    minW = 0.1*cam.get(3)
    minH = 0.1*cam.get(4)

    #flag = True

    while True:

        ret, img =cam.read() #read the frames using the above created object

        converted_image = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)  #The function converts an input image from one color space to another

        faces = faceCascade.detectMultiScale( 
            converted_image,
            scaleFactor = 1.2,
            minNeighbors = 5,
            minSize = (int(minW), int(minH)),
        )

        for(x,y,w,h) in faces:

            cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 2) #used to draw a rectangle on any image

            id, accuracy = recognizer.predict(converted_image[y:y+h,x:x+w]) #to predict on every single image

            # Check if accuracy is less them 100 ==> "0" is perfect match 
            if (accuracy < 100):
                id = names[id]
                accuracy = "  {0}%".format(round(100 - accuracy))
                TaskExecution()
                
                

            else:
                id = "unknown"
                accuracy = "  {0}%".format(round(100 - accuracy))
                speak("user authentication is faild")
                break
            
            cv2.putText(img, str(id), (x+5,y-5), font, 1, (255,255,255), 2)
            cv2.putText(img, str(accuracy), (x+5,y+h-5), font, 1, (255,255,0), 1)  
        
        cv2.imshow('camera',img) 

        k = cv2.waitKey(10) & 0xff # Press 'ESC' for exiting video
        if k == 27:
            break

    # Do a bit of cleanup
    print("Thanks for using this program, have a good day.")
    cam.release()
    cv2.destroyAllWindows()
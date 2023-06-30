import pyttsx3
import speech_recognition 
import requests
from bs4 import BeautifulSoup
import datetime
import os
import pyautogui



engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
rate = engine.setProperty("rate",170)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takeCommand():
    r = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        print("Listening.....")
        r.pause_threshold = 1
        r.energy_threshold = 300
        audio = r.listen(source,0,4)

    try:
        print("Understanding..")
        query  = r.recognize_google(audio,language='en-in')
        print(f"You Said: {query}\n")
    except Exception as e:
        print("Say that again")
        return "None"
    return query

def alarm(query):
    timehere = open("Alarmtext.txt","a")
    timehere.write(query)
    timehere.close()
    os.startfile("alarm.py")


if __name__ == "__main__":
    while True:
        query = takeCommand().lower()
        if "wake up" in query:
            from GreetMe import greetMe
            greetMe()

            while True:
                query = takeCommand().lower()
                if "go to sleep" in query:
                    speak("Ok sir , You can me call anytime")
                    break
                elif "you can sleep" in query:
                    speak("Ok sir , You can me call anytime")
                    break
                
                elif "hello" in query:
                    speak("Hello sir, how are you ?")
                
                elif "introduce yourself" in query:
                    speak("Hello sir im jarvce here ,Artificial intalligence ")    
                
                elif "i am fine" in query:
                    speak("that's great, sir")
                elif "how are you" in query:
                    speak("Perfect, sir")
                elif "thank you" in query:
                    speak("you are welcome, sir")
                elif "okay" in query:
                    speak("yes sir, do you have any task for me")
                elif "yes" in query:
                    speak("whats that")
                
                #for youtube automation
                elif "pause" in query:
                    pyautogui.press("k")
                    speak("video paused")
                elif "play youtube" in query:
                    pyautogui.press("k")
                    speak("video played")
                elif "mute youtube" in query:
                    pyautogui.press("m")
                    speak("video muted")
                elif "unmute youtube" in query:
                    pyautogui.press("m")
                    speak("video unmuted")
                    
                elif "increase speed of video" in query:
                    speak("increasing speed of video.., sir..")
                    pyautogui.hotkey("shift",".")
                    
                elif "decrease speed of video" in query:
                    speak("decreasing the speed of video.., sir..")
                    pyautogui.hotkey("shift",",")
                elif "forward  video" in query:
                    speak("forwording video in 10sec")
                    pyautogui.press("l")
                elif "bacword video" in query:
                    speak("bacwording  video by 10 sec")
                    pyautogui.press("j")
                elif "forward  0%" in query:
                    speak("forwording video by 0%")
                    pyautogui.press("0")
                elif "forward  10%" in query:
                    speak("forwording video by 10%")
                    pyautogui.press("1")
                elif "forward 20%" in query:
                    speak("forwording video by 20%")
                    pyautogui.press("2")
                elif "forward 30%" in query:
                    speak("forwording video by 30 %")
                    pyautogui.press("3")
                elif "forward  40%" in query:
                    speak("forwording 40%")
                    pyautogui.press("4")
                elif "forward 50%" in query:
                    speak("forwording video by 50%")
                    pyautogui.press("5")
                elif "forward 60%" in query:
                    speak("forwording video by 60%")
                    pyautogui.press("6") 
                elif "forward 70%" in query:
                    speak("forwording video by 70 percent")
                    pyautogui.press("7")
                elif "forward 80%" in query:
                    speak("forwording video by 80%")
                    pyautogui.press("8")  
                elif "forward 90%" in query:
                    speak("forwording video by 90 percent")
                    pyautogui.press("9")

                elif "next video on youtube" in query:
                    speak("playibg next video")
                    pyautogui.hotkey("shift","n")
                elif "previous  video on youtube" in query:
                    speak("playing previous video")
                    pyautogui.hotkey("shift","p")
            
                    
                    # in youtube skiping ads 
                elif "skip ads in theater mode" in query:
                    pyautogui.click(1801,827)
                    speak("ads skiped")
                



                elif "volume up" in query:
                    from keyboard import volumeup
                    speak("Turning volume up,sir")
                    volumeup()
                elif "volume down" in query:
                    from keyboard import volumedown
                    speak("Turning volume down, sir")
                    volumedown()
                
                   
                    
                elif "open" in query:
                    from Dictapp import openappweb
                    openappweb(query)
                elif "close" in query:
                    from Dictapp import closeappweb
                    closeappweb(query)
                
                
                    
                elif "google" in query:
                    from SearchNow import searchGoogle
                    searchGoogle(query)
                elif "youtube" in query:
                    from SearchNow import searchYoutube
                    searchYoutube(query)
                elif "wikipedia" in query:
                    from SearchNow import searchWikipedia
                    searchWikipedia(query)
                    
                elif "news" in query:
                    from NewsRead import latestnews
                    latestnews()
                
                elif "calculate" in query:
                    from Calculatenumbers import WolfRamAlpha
                    from Calculatenumbers import Calc
                    query = query.replace("calculate","")
                    query = query.replace("jarvis","")
                    Calc(query)
                    
                    
                elif "temperature" in query:
                    search = query.replace("whats the","")
                    search = query.replace("what is the","")
                    search = query.replace("in","")
                    url = f"https://www.google.com/search?q={search}"
                    r  = requests.get(url)
                    data = BeautifulSoup(r.text,"html.parser")
                    temp = data.find("div", class_ = "BNeawe").text
                    speak(f"current{search} is {temp}")
                
                elif "weather" in query:
                    search = "temperature in maharastra"
                    url = f"https://www.google.com/search?q={search}"
                    r  = requests.get(url)
                    data = BeautifulSoup(r.text,"html.parser")
                    temp = data.find("div", class_ = "BNeawe").text
                    speak(f"current{search} is {temp}")
                
                elif "set an alarm" in query:
                    print("input time example:- 10 and 10 and 10")
                    speak("Set the time")
                    a = input("Please tell the time :- ")
                    alarm(a)
                    speak("Done,sir")
                    
                elif "the time" in query:
                    strTime = datetime.datetime.now().strftime("%H:%M")    
                    speak(f"Sir, the time is {strTime}")
                    
                    
                elif "finally sleep" in query:
                    speak("Going to sleep,sir, good night")
                    exit()
                    
                elif "remember that" in query:
                    rememberMessage = query.replace("remember that","")
                    rememberMessage = query.replace("jarvis","")
                    speak("You told me to remember that"+rememberMessage)
                    remember = open("Remember.txt","a")
                    remember.write(rememberMessage)
                    remember.close()
                elif "what do you remember" in query:
                    remember = open("Remember.txt","r")
                    speak("You told me to remember that" + remember.read())
                                    
                                
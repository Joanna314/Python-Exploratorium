# importing all necessary libraries
import pyttsx3
import speech_recognition as sr 
import os
import time 
from playsound import playsound
import time
from datetime import datetime
import xml.etree.ElementTree as ET
# starting pyttsx/declaring needee variables 
engine = pyttsx3.init()
engine.setProperty('rate',145)
# speaking system 
engine.say("hello I am Luna. How can I help you today. You can chat with me, order food or manage workout")
engine.runAndWait()
r=  sr.Recognizer()
with sr.Microphone() as source:
  audio= r.listen(source)
  calling = r.recognize_google(audio) 
  if calling== "Chat"or calling=="chat":
    engine.say("Oh sure. what is your name?")
    engine.runAndWait()
    w=  sr.Recognizer()
    with sr.Microphone() as source:
      audio= w.listen(source)
      name = w.recognize_google(audio)
      engine.say("hi {} how are you doing today?".format(name))
      engine.runAndWait()
      q=  sr.Recognizer()
      with sr.Microphone() as source:
        audio= q.listen(source)
        feeling = q.recognize_google(audio)
        if feeling== "happy":
          engine.say("That's fantastic {}. I'm glad you are happy. Must be enjoying space huh?".format(name)) 
          engine.runAndWait()
          engine.say("I am glad to hear you are happy. Are you satisfied with my care?")
          engine.runAndWait()
          f=  sr.Recognizer()
          with sr.Microphone() as source:
            audio= f.listen(source)
            answer= f.recognize_google(audio)
            if answer ==  "yes" or answer=="Yes":
              engine.say("That's great. Remember I am always here for you")
              engine.runAndWait()
        elif feeling == "sad":
          engine.say("Awww. It's okay {}. Remember why you came here. Millions are proud of what you have done and what you will continue to do".format(name)) 
          engine.runAndWait()
          engine.say("do you feel better now?")
          engine.runAndWait()
          g=  sr.Recognizer()
          with sr.Microphone() as source:
            audio= g.listen(source)
            answer2= g.recognize_google(audio)
            if answer2 ==  "yes" or answer=="Yes":
              engine.say("yay celebration music")
              engine.runAndWait()
              playsound("party.mp3")

        elif feeling == "mad":
          engine.say("please don't be mad {}. Enjoy what's around you and embrace this chance that not many people get. Right now, you are probably the luckiest person on earth".format(name))
          engine.runAndWait()
        elif feeling=="okay":
          engine.say("WHAT? {} you are in space and you feel okay??? I on the other hand am overjoyed!!!".format(name))
          engine.runAndWait()

  elif calling=="Workout " or calling == "Excersize" or calling=="workout":
    now = datetime.now()
    print(now)
    engine.say("what is your name?")
    engine.runAndWait()
    w=  sr.Recognizer()
    with sr.Microphone() as source:
      audio= w.listen(source)
      name = w.recognize_google(audio)
      engine.say("hi {} Get ready for your daily 30 minutes exercise".format(name))
      engine.runAndWait()
      engine.say("would you like to do a heavy or light workout today")
      engine.runAndWait()
      h=  sr.Recognizer()
      with sr.Microphone() as source:
        audio= h.listen(source)
        callingExercise= h.recognize_google(audio)
        if callingExercise== "light" or callingExercise=="Light": 
          engine.say("Hmm being lazy I see. You must be wishing you were me because robots don't need to excersize.  Either way, lets do a light exercise today. We will do a heavy workout tomorrow.")
          engine.runAndWait()

        else:
          engine.say("very good looks like you are fully charged today")
          engine.runAndWait()
            
        engine.say ("I'll play some workout music. Which one would you like? Say either, Direction, Sing , or Roar ")
        engine.runAndWait()

        z=  sr.Recognizer()
        with sr.Microphone() as source:
          audio= z.listen(source)
          song= z.recognize_google(audio)
          if song== "direction" or song=="direction":
            playsound("song4.mp3")
          if song== "sing" or song=="Sing":
            playsound ("song2.mp3")
          if song== "Roar" or song=="roar":
            playsound("song3.mp3")
            
          engine.say("Very good job. Daily exercise is vital in space. By completing your exercise today, you can ensure a better tomorrow. Looking forward for your exercise tomorrow!")
          engine.runAndWait()
      
  
  elif calling== "food" or calling == "Food":
    tree = ET.parse('data.xml')
    root = tree.getroot()
    totpeople= root[0].text
    totcans = root[1].text
    engine.say("Ok Thank you. Let me check the inventory. You currently have {} cans in the ship".format(totcans))
    engine.runAndWait()
    engine.say("How many will each person consume in a day?")
    engine.runAndWait()
    c=  sr.Recognizer()
    with sr.Microphone() as source:
      audio= c.listen(source)
      answer3= c.recognize_google(audio)
      print(totcans,totpeople,int(answer3))
      days = round(int(totcans)/int(int(answer3)*int(totpeople)))
      engine.say("based on your rate of consumption, you will have the food for another {} more days. Do you want me to order more food.".format(days))
      engine.runAndWait()
      c=  sr.Recognizer()
      with sr.Microphone() as source:
        audio= c.listen(source)
        answer4= c.recognize_google(audio)
        if answer4 == "yes" or answer4 == "Yes":
          engine.say("Ok sending order to the ground station please wait")
          engine.runAndWait()
          playsound("beep.mp3")
          time.sleep(3)
          engine.say("Okay the order is now confirmed. Please let me know when you want to order more. Have a great day")
          engine.runAndWait()
        else:
          engine.say("Okay. Please let me know when you want to order more food. Have a great day. We'll talk later")
          engine.runAndWait()
      

 


        

import cv2 
import os 
import face_recognition
import pyaudio
import speech_recognition as sr 
from playsound import playsound
import time
import pyttsx3

 # --------------------------------Declaring Variables ------------------------
engine = pyttsx3.init()
engine.setProperty('rate',145)
knownfaces_names = []
knownfaces_encodingslist = []
location_for_frame= 0 
encoding_for_frame = 0
knownfaces_locations = 0
match = []
img_counter = 0
TOLERANCE = 0.5
MODEL = "cnn"
Matchingsystem = True

# ---------------------------------Getting face encodings for each image in my knownfaces_jpegs list ----------------
cap= cv2.VideoCapture(0)
print ("camera started")


for img in os.listdir("C:/Users/noosu/Documents/python projects/PeopleIknow"):
	if img.endswith(".jpg"):
		knownface= face_recognition.load_image_file("C:/Users/noosu/Documents/python projects/PeopleIknow/" + img)
		knownface = cv2.cvtColor(knownface,cv2.COLOR_BGR2RGB)
		knownfaceencoding = face_recognition.face_encodings(knownface)[0]
		knownfaces_encodingslist.append(knownfaceencoding)
		name, ext = img.split('.')
		knownfaces_names.append(name)

print("encodings collected")


 # ----------------------------- Starting up the camera  ------------------------------------------ ---------

while True:
	ret,frame = cap.read()
	print("frame read")
	frame = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)

	location_for_frame = face_recognition.face_locations(frame)
	encoding_for_frame = face_recognition.face_encodings(frame,location_for_frame)
	print("frame encoded")
	match.clear()
	for face_encoding, face_location in zip (encoding_for_frame,location_for_frame):
		comparison = face_recognition.compare_faces(knownfaces_encodingslist, face_encoding,TOLERANCE) 
		if any(comparison):
			k= knownfaces_names[comparison.index(True)]
			match.append(k)
	print("done comparing")

	if len(location_for_frame) == 0 :
		print ("no one")
	
	else: 
		if match:
			print ("match found :",match)
			seperator = " and "
			messagematchtrue = seperator.join(match) + " is at the door"
			Matchingsystem = True 
		
		else: 
			print ("no match") 
			Matchingsystem = False
			messagematchfalse = "The person detected is not someone in your immediate family"

		engine.say("There is someone at the door")
		engine.runAndWait()
		w= sr.Recognizer()
		with sr.Microphone() as source:
			audio = w.listen(source)
			try:
				text1 = w.recognize_google(audio)
				print (text1)
				if text1 == "Who is it" or text1 == "who is it" or text1 == "Okay who is it" or text1 == "okay who is it" or text1 == "okay who's there" or text1 == "who"or text1 == "okay who":
					if Matchingsystem == True:
						engine.say(messagematchtrue)
						engine.runAndWait()
						time.sleep(25)
					elif Matchingsystem == False:
						engine.say(messagematchfalse)
						engine.say(" Do you want to save this face")
						engine.runAndWait()
						 
						with sr.Microphone() as source:
							audio = w.listen(source)
							text4 = w.recognize_google(audio)
						if  text4 == "yes" or text4 == "Yes" or text4== "ya" or text4 == "Ya" or text4 == "okay":
							engine.say("Okay shall I take the image")
							engine.runAndWait()
							with sr.Microphone() as source:
								audio = w.listen(source)
								text3 = w.recognize_google(audio)
								if text3 == "yes" or text3 == "Yes" or text3== "ya" or text3 == "Ya" or text3 == "okay":
									engine.say("Okay what is the person's name")
									engine.runAndWait()
									with sr.Microphone() as source:
										audio = w.listen(source)
										text2 = w.recognize_google(audio)
										print ("saving image")
										frame = cv2.cvtColor(frame,cv2.COLOR_RGB2BGR)
										img = "{}.jpg".format(text2)
										path = "C:/Users/noosu/Documents/python projects/PeopleIknow"
										cv2.imwrite(os.path.join(path , img), frame)
										
									
								time.sleep(25)
						else:
							engine.say("Okay. I'll go back to my routine checking")
							engine.runAndWait()
							time.sleep(25)

				elif text1 == "help" or text1 == "I do not know what to do" or text1 == "what are the instructions" or text1 == "what do I do" or text1 == "how does this work" or text1 == "what do I have to do" or text1 == "can you help me" :
					engine.say("Welcome to the instruction section. I am a J Jcube. A wifi camera. I am here to assist you with detecting the people who are outside your door. Let’s first start by reviewing the basic commands. When I detect someone, I will let you know by saying there is someone at the door. To know who is outside, all you have to do is say the command “who is it”.  Second. If I detect someone you do not know, I will tell you that the person outside is not someone in your immediate family. I will also ask you if you would like me to remember that face. You can either accept or deny. I hope I didn’t bore you. Don’t worry we are almost done. If you need any help and want to revisit the instructions section, you just have to say “I do not know what to do” or say “help”. Finally, if I don’t see anyone outside, I’ll just remain quiet.")
					engine.runAndWait()
				elif text1 == "Stop" or text1 == "stop":
					print("exiting")
					break
			

			except:
				print("ERROR")
				time.sleep(5)
				
cv2.destroyAllWindows()	
cap.release()
	

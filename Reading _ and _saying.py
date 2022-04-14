import cv2
import pytesseract 
import cv2
import os 
from gtts import gTTS
from playsound import playsound
cap= cv2.VideoCapture(0)
langu = "en"
out = gTTS(text = "Hi. I'm Marsa. I am here to help you announciate any text you desire.",lang=langu,slow = False)
out.save("Intro.mp3")
playsound("Intro.mp3")
def reading_img():

	while(True):
		ret,frame = cap.read()
		cv2.imshow("Focus your image on the text and press space bar",frame)

		if not ret:
			break
		k = cv2.waitKey(1)

		if k%256 == 27:
			print ("exiting")
			break
		elif k%256 ==32:   
			print ("saving image")
			imagename = "image_0.png"
			cv2.imwrite(imagename,frame)

			im = cv2.imread("image_0.png")

			img = cv2.resize(im, None, fx=0.5, fy=0.5)
			# 3. Convert image to grayscale
			gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
			# 4. Convert image to black and white (using adaptive threshold)
			adaptive_threshold = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 85, 11)
			config = "--psm 3"
			text = pytesseract.image_to_string(adaptive_threshold, config=config)
			return text
			break

	cap.release()
	cv2.destroyAllWindows()		

textfromimage= reading_img()
print (textfromimage)
language = "en"
output = gTTS(text = textfromimage,lang=language,slow = False)
output.save("text.mp3")
playsound("text.mp3")
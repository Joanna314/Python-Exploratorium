import pytesseract 
import cv2
import numpy as np
import pyodbc
import winsound 
from playsound import playsound
import os 
import tempfile
def read_image():
	cap= cv2.VideoCapture(0)
	while (True):
		
		try:
			ret,frame= cap.read()
			cv2.imshow("frame",frame)
			cv2.waitKey(1)
			if ret:
				
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
				print (text)
				if 1000< int(text)< 1035: 
					playsound('Grocery_Beep.mp3')
					print("barcode was read successfully")
					cap.release()
					cv2.destroyAllWindows()
					return text
					break
		except:
			print ("error with barcode. Retrying")
	cap.release()
	cv2.destroyAllWindows()

 # The AI program reads the image and sends the text into the barcode variable 
#print(barcode)
conn = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ= C:\Users\noosu\Documents\Database1.accdb;')
cursor = conn.cursor()
Totalprice = 0
price = 0
i= 1
count  = 0
##today_date = date.today().strftime('%d/%m/%Y')
itemscode = [0]
itemslist = [0]
itemsprice = [0]
f = open("demofile3.txt", "w")
while 1==1: # phase 2 of project: the barcode is used to identify product and calculate price 
	barcode= read_image()
	cursor.execute('select Subitem_Name,SubItem_Price from SubItem where subItem_ID = ?',barcode)
	row=cursor.fetchone()
	print (barcode, "-", row[0], "-", row[1])
	price = row [1]
	itemslist.append(row[0])
	itemsprice.append(row[1])
	itemscode.append(barcode)

	Totalprice = Totalprice +price
	Cont = input("Would you like to continue scanning?")
	if Cont == "No"or Cont == "no"or Cont == "N"or Cont == "n" :
		#cursor.execute("select iif(isnull(MAX(Sales_ID)),0,MAX(Sales_ID)) from Sales_table")
		cursor.execute("select MAX(Sales_ID) from Sales_table")
		row = cursor.fetchone()
		if row[0] is None:
			sid = 0
		else:
			sid = row[0]
		k= "                       Bill                           \n \n                  J AND J GROCERIES                   \n------------------------------------------------------\n"
		f.write(k)
		for number in range (1,(i + 1)):
			y= "Item {}: {}    Price : {}\n".format(count,itemslist[number],float (itemsprice[number])) 
			count +=1
			f.write(str(y))
			cursor.execute("INSERT INTO Sales_table (Sales_ID,SubItem_ID,SubItem_Quantity,SubItem_Amount,Sales_Date) VALUES (?,?,?,?,date())",(sid+1,itemscode[number],1,itemsprice[number]))
		conn.commit()
		x ="\nYour total price is {}". format(float(Totalprice))
		f.write(x) 
		z = "\nMASTER CARD ****067\n------------------------------------------------------\nThank you for shopping with us today"
		f.write(z)
		os.startfile("demofile3.txt","print")
		break
	i +=1

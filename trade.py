from PIL import Image
import pytesseract as ptt
ptt.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
import pyautogui as gui
import time 
import os
def look():
	print('HI')
	x_1_s=300
	y_1_s=295
	x_1_e=500
	y_1_e=620
	x_2_s=550
	y_2_s=295
	x_2_e=684
	y_2_e=620
	gui.click('refre.png')
	time.sleep(1)
	gui.moveTo(100, 200) 
	time.sleep(1)
	gui.screenshot('mon.png',region=(x_2_s,y_2_s,x_2_e-x_2_s,64))
	op=Image.open('mon.png')
	price = ptt.image_to_string(op)
	tic = str(price).replace(',','')
	tac=tic.replace(' ','')
	to=tac.replace('(','')
	toc=to.replace(')','')
	if price == '':
		look()
	print('The value is '+str(price))
	os.remove('mon.png')
	print('Waiittt!!!')
	check(float(toc))
def check(price):
	if price >=50000:
		print('Nice')
		sell()
		look()
	else:
		print('Not profitable ')
		look()
def sell():
	gui.click('sell1.png')
	time.sleep(1)
	gui.click('sell2.png')
	print("Sold !!")
look()
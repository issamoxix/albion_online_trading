#saving the prices in the database from the carlion market
from PIL import Image
import pytesseract as ptt
ptt.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
import pyautogui as gui
import time 
import sys
import os
import pathlib as lib
import mysql.connector
import cc
#read the content of the picture
class data:
	def __init__(self):
		self.tr=5
		self.eh=1
	def im_st(self, file1,file2):
		x=[]
		im1=Image.open(file1)
		im2=Image.open(file2)
		tt1=ptt.image_to_string(im1)
		tt2=ptt.image_to_string(im2)
		if tt1 or tt2:
			f = open('data.txt','a')
			tic = str(tt2).replace(',','')
			tac=tic.replace(' ','')
			to=tac.replace('(','')
			toc=to.replace(')','')
			f.write(str(tt1)+'\n')
			f.write(str(toc)+'\n')
			f.close()
		else:
			print('There is no Data to enter !!')
			toc=0
		x.append(tt1)
		x.append(toc)
		print(x)
		self.db(x[0],x[1],self.tr, self.eh)
	#sx , sy and sz refered to serial x y z of the image file bm1_1 bm1_2
	#there is only 2 _1 _2 but the first number after _ can change 
	# like 7_1 7_2
	def scr(self):
		x_1_s=300
		y_1_s=360-55
		x_1_e=480
		y_1_e=620
		x_2_s=590
		y_2_s=360-55
		x_2_e=684
		y_2_e=620
		for i in range(1,500):
			f_n='../pics/bm'+str(i)
			f_nl=lib.Path(str(f_n)+'/')
			#print(str(f_n)+' Checking ...')
			if f_nl.exists():
				#print('It exists !!')
				sy=i
				sx=i
			else:
				#print('It does not exist !!')
				sy=i
				sx=i
				break

		os.mkdir(f_n)
		for ii in range(1,5):
			stty=50
			if ii==1:
				stt=0
			else:
				stt=55/2
			pic1="../pics/bm"+str(sy)+"/bm"+str(sx)+'_1_'+str(ii)+'.png'
			pic2="../pics/bm"+str(sy)+"/bm"+str(sx)+'_2_'+str(ii)+'.png'
			y_1_s=y_1_s+stt*ii
			y_2_s=y_2_s+stt*ii
			bm1_1=gui.screenshot(pic1,region=(x_1_s,y_1_s,x_1_e-x_1_s,stty+20))
			bm1_2=gui.screenshot(pic2,region=(x_2_s,y_2_s,x_2_e-x_2_s,stty+20))
			print('Pic taked')
			#time.sleep(0.5)
	#this scroll function scroll a page of the market
	def scroll(self):
		for i in range(0,9):
			print(i)
			gui.scroll(-200)
	#this function enter data to the data.txt file as sorted as follow
	def en_data(self, fx,so):
		for  f in range(fx,so):
			for s in range(1,5):
				for p in range(1,3):
					file = "../pics/bm"+str(f)+"/bm"+str(f)+"_"+str(p)+"_"+str(s)+".png"
					im_st(file)
					time.sleep(1)
					print('Data entred for : '+str(file))
	def new(self):
		self.scr()
		dr=len(os.listdir('../pics/'))-1
		for i in range(1,5):
			file1 = "../pics/bm"+str(dr)+"/bm"+str(dr)+"_1_"+str(i)+".png"
			file2 = "../pics/bm"+str(dr)+"/bm"+str(dr)+"_2_"+str(i)+".png"
			self.im_st(file1,file2)
	#insert data to the database
	def db(self,item,price,tier,ench):
		db=mysql.connector.connect(host='localhost',user='root',passwd="",database='albion')
		ex=db.cursor()
		sql="INSERT INTO items (name, price, tier,ench)values(%s,%s,%s,%s)"
		val=(item,price,tier,ench)
		ex.execute(sql, val)
		db.commit()
		print(ex.rowcount, 'Data entered')
	def tier(self):
		x=gui.locateOnScreen('img/all_btn.png')
		if x:
			ck=0
			print(x)
			y=gui.center(x)
		else:
			ck=1
			x=500
			z=221
		tiers=[4,5,6,7,8]
		for i in range(0,5):
			if ck==0:
				print(1)
				# cc.clk(y.x,y.y)#new click button since the click function not working
				gui.click(y.x,y.y)
			else:
				print(2)
				
				gui.click(x,z)
			time.sleep(0.1)
			gui.click('img/t'+str(tiers[i])+'.png')
			self.tr=tiers[i]
			self.eh=0
			print('Tier '+str(self.tr))
			time.sleep(0.8)
			self.ech()
			
	def ech(self):
		x=gui.locateOnScreen('img/all_btn2.png')
		if x:
			y=gui.center(x)
			ck=0
		else:
			ck=1
			x=600
			y=220
		ench=[1,2,3,4]
		for i in range(0,4):
			self.new()
			if i ==3:
				if i == 3 and self.tr == 8:
					self.back()
				break
			print('ech'+str(self.eh))
			self.eh=ench[i]
			if ck==0:
				gui.click(y.x,y.y)
			else:
				gui.click(x,y)
			gui.moveTo(250,200)
			time.sleep(0.4)
			if ench[i]==1:
				gui.click(606,277)
			else:
				print('img/'+str(ench[i])+'.png')
				gui.click('img/'+str(ench[i])+'.png')
			gui.moveTo(250,200)
			time.sleep(1)
		if ck ==0:
			gui.click(y.x,y.y)
		else:
			gui.click(x,y)
		time.sleep(0.2)
		gui.moveTo(250, 200)
		gui.click('img/end_all.png')
	def back(self):
		print('Back Function !! ')
		x=512
		y=221
		ye=239
		gui.click(x,y)
		time.sleep(0.4)
		gui.click(x,ye)
		time.sleep(0.4)
		gui.click(700,y)
		time.sleep(0.4)
		gui.click(700,ye)


# data=data()
# data.tier()
data= data()
items=['hunter hood']
for i in items:
	cc.item(i)
	time.sleep(0.2)
	data.tier()
#all_0_normal
#checking profite
import pyautogui as gui	
from PIL import Image
import pytesseract as ptt
ptt.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
import time
import mysql.connector
import cc
class prof:
	def __init__(self):
			self.tr=0
			self.eh=0
	def machidaba(self):
			x_1_s=300
			y_1_s=360-55
			x_1_e=480
			y_1_e=620-305
			x_2_s=545
			y_2_s=360-55
			x_2_e=684
			y_2_e=620
			pic1='../bm/pic1.png'
			pic2='../bm/pic2.png'
			bm1_1=gui.screenshot(pic1,region=(x_1_s,y_1_s,x_1_e-x_1_s,50+20))
			bm1_2=gui.screenshot(pic2,region=(x_2_s,y_2_s,x_2_e-x_2_s,50+20))
			im1=Image.open(pic1)
			im2=Image.open(pic2)
			o1=ptt.image_to_string(im1)
			o2=ptt.image_to_string(im2)
			if o1 =='' or o2=='':
				oo=0
				toc=0
			else:
				tic = str(o2).replace(',','')
				tac=tic.replace(' ','')
				to=tac.replace('(','')
				toc=to.replace(')','')
				lo=o1[7:]
				smit=['Adept','Adepts','Experts',"Master's",'Grandmaster','‘’','’','‘']
				for ix in smit:
					if ix in smit:
						oo=lo.replace(ix,'')	
						break
			#this is the black market price
			print('XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX')
			print('########Black market Price##########')
			print('name: '+str(oo))
			print('price: '+str(toc))
			print('Tier: '+str(self.tr))
			print('Ench: '+str(self.eh))
			taxe=float(toc)*0.06
			print('Taxe: '+str(taxe))
			print('#########Carlion market#############')
			if oo!=0:
				dbs=mysql.connector.connect(host='localhost', user='root', passwd='',database='albion')
				ex=dbs.cursor()
				sql="SELECT * from items WHERE name REGEXP '"+str(lo)+"' AND tier="+str(self.tr)+" AND ench="+str(self.eh)+" "
				ex.execute(sql)
				row=ex.fetchall()
				if len(row)!=0:
					print(str(row[0][0])+' Price : '+str(row[0][1]))
					print('################################')
					if row[0][1] =='':
						print('No Price !!')
						profite=0
					else:
						profite=float(toc)-float(row[0][1])-float(taxe)
				else:
					profite=0
			else:
				profite=0
			if profite >= 1000:
				print('NIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIICE !!!!')
				# gui.alert(text='Tier : '+str(self.tr)+'\n Ench : '+str(self.eh)+'\n Profite : '+str(profite),title='Profite !!',button='Ok')
				file =open('../bm/prof.txt','a')
				file.write('\n ############# '+'\nCarlio PRICE => '+str(row[0][1])+'\n Tier : '+str(self.tr)+'\n Ench : '+str(self.eh)+'\n Price :'+str(toc)+'\n Profite : '+str(profite))
				file.close()
				time.sleep(1)
				# self.sell()
			print('The Profite: '+str(profite))
			print('XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX')
	def tier(self):
		# x=gui.locateOnScreen('img/all_btn.png')
		# y=gui.center(x)
		
		try:
			y =(508,220)
			tiers=[4,5,6,7,8]
			for i in range(0,5):
				gui.click(y[0],y[1])
				time.sleep(0.2)#0.4
				gui.click('../bm/t'+str(tiers[i])+'.png')
				self.tr =tiers[i]
				self.eh=0
				time.sleep(0.5)#1
				print('iiiii')
				self.ech()
		except:
			print("error")
			pass
	def ech(self):
		# x=gui.locateOnScreen('../bm/e0.png')
		
		# y=gui.center(x)
		y=(588, 220)
		print('iiiiscscsciii')
		ench=[1,2,3,4]
		for i in range(0,4):
			self.machidaba()
			self.eh=ench[i]
			if i ==3:
				break
			gui.click(y[0],y[1])
			gui.moveTo(250,200)
			time.sleep(0.2)#0.4
			gui.click('../bm/'+str(ench[i])+'.png')
			gui.moveTo(250,200)
			time.sleep(0.5)#1
		gui.click(y.x,y.y)
		time.sleep(0.05)#0.2
		gui.moveTo(250, 200)
		gui.click('../bm/0_e.png')
	def sell(self):
		gui.click('img/sell1.png')
		time.sleep(1)
		gui.click('img/sell2.png')
		print("Sold !!")
# cc.item()
issam=prof()
issam.tier()

import pyautogui as gui
import time
import alb
import test
# for i in range(0,2):
# 	print('Click')
# 	gui.doubleClick('sear.png')
# gui.click(button='right')
#from Black_m to the market
def mr():
	for i in range(1,15):
		print('One step')
		time.sleep(0.4)
		#goin to the market
		gui.click(x=861,y=381,button='right')
	x = input('m/b: ')
	start(x)
def bm():
	for i in range(1,15):
		print('Step ')
		time.sleep(0.4)
		#goin to the black market
		gui.click(x=261,y=320,button='right')
		gui.click()
	o=gui.locateOnScreen('me.png',confidence=0.5)
	op = gui.center(o)
	gui.click(op.x,op.y)
	x = input('m/b: ')
	start(x)
def start(x):
	if x=='m':
		mr()
	elif x=='b':
		bm()

def go_to_market():
	cor=[[781,565],[999,439],[905,159]]
	for i in range(0,3):	
		print(cor[i])
		if i ==1:
			for r in range(0,5):
				print(r)
				if r==4:
					gui.click(877,439,button='right')
					break
				gui.click(cor[i][0],cor[i][1],button='right')
				time.sleep(1)
		else:
			gui.click(cor[i][0],cor[i][1],button='right')
		time.sleep(2)
	time.sleep(10)
	u,p=627,59
	gui.click(u,p,button='right')
	time.sleep(2)
	gui.click(u,p)
	time.sleep(10)
	kho=alb.data()
	kho.tier()
	time.sleep(1)
	prog()
def prog():
	cor=[[407,707],[947,547]]
	for i in range(0,2):
		if i ==0:
			for o in range(0,2):
				gui.click(cor[i][0],cor[i][1],button='right')
				time.sleep(1)
			time.sleep(1)
		else:
			gui.click(cor[i][0],cor[i][1],button='right')
			time.sleep(1)
	time.sleep(10)
	go_to_black()
def go_to_black():
	cor =[[31,383],[119,39]]
	for i in range(0,2):
		if i ==0:
			for po in range(0,3):
				gui.click(cor[i][0],cor[i][1],button='right')
				time.sleep(2)
		else:
			gui.click(cor[i][0],cor[i][1],button='right')
		time.sleep(1)
	gui.click(193,139)
	print('Finished First Travelle ')
	time.sleep(2)
	issam=test.prof()
	issam.tier()
	time.sleep(10)
	go_to_market()
go_to_market()

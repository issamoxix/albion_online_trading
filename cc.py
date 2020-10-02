import pyautogui as gui
# from PIL import Image
import time
import pytesseract as ptt
ptt.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def clk(x,y):
    gui.mouseDown(x,y);
    gui.mouseUp(x,y)
def item(item,b_m):
    gui.click(276,220)
    clk(276,220)
    gui.write(item) 
    if b_m==1:
        gui.press('backspace')
        clk(429,181)
def ench():
    ench_0_pos = (590, 262)
    x=590
    y=262
    for i in range(1,5):
        time.sleep(1)
        print(i)
        gui.moveTo(x,y)
        y+=15
# (x=111, y=36)
# (x=237, y=67)

import pyautogui as gui

def clk(x,y):
    gui.mouseDown(x,y);
    gui.mouseUp(x,y)
def item(item):
    gui.click(276,220)
    clk(276,220)
    gui.write(item) 

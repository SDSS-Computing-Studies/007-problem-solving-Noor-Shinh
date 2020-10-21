import pyautogui as p
import time
times=[]
upgrade=[]
curTime=time.time()
C=True
times=curTime + 5
upgrade=curTime + 4

while C==True:
    p.click(218,398)
    
    curTime=time.time()
    if curTime>times:
        x=p.locateCenterOnScreen("Temple.PNG", confidence=0.8)
        p.click(x)
        y=p.locateCenterOnScreen("Bank.PNG", confidence=0.8)
        p.click(y)
        z=p.locateCenterOnScreen("Factory.PNG", confidence=0.8)
        p.click(z)
        a=p.locateCenterOnScreen("Mine.PNG", confidence=0.8)
        p.click(a)
        b=p.locateCenterOnScreen("Farm.PNG", confidence=0.8)
        p.click(b)
        c=p.locateCenterOnScreen("Gran.PNG", confidence=0.8)
        p.click(c)
        d=p.locateCenterOnScreen("Cursor.PNG", confidence=0.8)
        p.click(d)

        times=curTime + 60
    if curTime>upgrade:
        p.click(1153,220)  
        upgrade=curTime + 239  
 
    


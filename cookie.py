import pyautogui as p
import time
times=[]
upgrade=[]
golden=[]
curTime=time.time()
C=True
times=curTime + 5
upgrade=curTime + 4
golden=curTime + 3

while C==True:
    p.click(218,398)
    
    curTime=time.time()
    if curTime>times:
        n=p.locateCenterOnScreen("Wizard.PNG", confidence=0.8)
        p.click(n)
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

        times=curTime + 300
    if curTime>upgrade:
        z=p.locateCenterOnScreen("Store.PNG", confidence=0.8)
        p.moveTo(z)
        p.move(-100,70)
        p.click()
        upgrade=curTime + 280 
     
    if curTime>golden:
        m=p.locateCenterOnScreen("Gold.PNG", confidence=0.8)
        p.click(m)
        print("x")
        golden = curTime+5
    


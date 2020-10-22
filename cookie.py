import pyautogui as p
import time
#These 3 tuples store time in order for other functions to work. Curtime allows the program to store/apply a timer
times=[]
upgrade=[]
golden=[]
curTime=time.time()
#Makes C=True to create an infinite loop 
C=True
#These 3 lines add 5 4 and 3 seconds to current time respectively. This allows them to run their respective functions immediately 
times=curTime + 5
upgrade=curTime + 4
golden=curTime + 3
#C==True allows the function to run forever because C is always =True
while C==True:
    #This funtion finds the coordinates of the main cookie
    p.click(218,398)
    #Resets the time value so that the next functions can work
    curTime=time.time()
    if curTime>times:
        #Every 5 minutes the prgram will cycle through every available building from most to least valueable and buys them if possible
        #It does this by finding the building using image processing then storing its location as a coordinate for the p.click function to then use
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
        #Every 200 seconds this function will attempt to buy an upgrade by finding the store then movng down 70 pixels and 100 pixels to the left
        z=p.locateCenterOnScreen("Store.PNG", confidence=0.8)
        p.moveTo(z)
        p.move(-100,70)
        p.click()
        upgrade=curTime + 280 
     
    if curTime>golden:
        #Every 5 seconds this function searches for a golden cookie, if one is found it clicks it. If not the program runs on with no interuption
        m=p.locateCenterOnScreen("Gold.PNG", confidence=0.8)
        p.click(m)
        golden = curTime+5
    

    


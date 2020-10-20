import pyautogui as p
import time
times=[]
events=[]
curTime=time.time()
C=True
times=curTime + 5
events.append(p.click(1290,320))
while C==True:
    p.click(226,325)
    time.sleep(0.1)
    curTime=time.time()
    if curTime>times:
        p.click(1290,340)
        times=curTime + 5

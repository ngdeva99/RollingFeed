import pyautogui
import time

print("winthin ten seconds position your cursor to the first window")
time.sleep(10)

k=list(pyautogui.position())
count=0

no_of_participants=8 #no of students taking the exam
time_interval=3 #time for each screen share
time_for_one_cycle=no_of_participants*time_interval
exam_time=48 #in seconds
no_of_cycles=exam_time//time_for_one_cycle #48/16=3

cycle_count=0

while cycle_count<no_of_cycles:
    x=k[0]
    y=k[1]
    
    for i in range(no_of_participants):
        pyautogui.moveTo(x,y,duration=time_interval) 
        pyautogui.click(button='left',clicks=1)
        x=x-100
    
    cycle_count+=1
import pywhatkit
import webbrowser
import time
from pynput.mouse import Button, Controller
mouse = Controller()
import time
from pynput.keyboard import Key, Controller
keyboard = Controller()
import os 

#opening whatsapp
print ("OPENING WHATSAPP")
os.startfile("C:\Program Files\Google\Chrome\Application\chrome.exe")
link1 = "https://web.whatsapp.com/"
chrome_path = '"C:\Program Files\Google\Chrome\Application\chrome.exe" %s'
webbrowser.get(chrome_path).open(link1)



print("CLICKING CLASS GROUP")
#clicking our class group in whatsapp
time.sleep(18)
# Set pointer position
mouse.position = (206, 288)
# Press and release
mouse.press(Button.left)
mouse.release(Button.left)



print("CLICKING THE LINK (tough task)")
#CLICKING OUR LINK (THE TOUGH TASK)
mouse.position = (532, 558)#configure this according to your screen 
time.sleep(2)
mouse.press(Button.left)
mouse.release(Button.left)



print("TURNING OFF THE CAM AND MIC")
#now we start clicking 
import time
from pynput.keyboard import Key, Controller
keyboard = Controller()
time.sleep(30)#here instead of 30 you can put whatever number u want but it will take it as sec only 
#presing d
keyboard.press(Key.ctrl_l)
keyboard.press('d')
keyboard.press('e')
#realeasing 
keyboard.release(Key.ctrl_l)
keyboard.release('d')
keyboard.release('e')
time.sleep(3)



print("JOINING")
#JOINING
from pynput.mouse import Button, Controller
mouse = Controller()
# Set pointer position
mouse.position = (988, 432)
# Press and release
mouse.press(Button.left)
mouse.release(Button.left)



print("auto closing")
#auto closing 
time.sleep(15)#wewant3300 seconds in there because our class is oen hour and we can leave a 5 mins early so 55 mins = 3300secs
keyboard.press(Key.ctrl_l)  
keyboard.press('w')
keyboard.release(Key.ctrl_l)
keyboard.release('w')


#thi is gonna close the whatsapp tab after desired time 

pywhatkit.close_tab(wait_time = 3)

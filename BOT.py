import pywhatkit
pywhatkit.sendwhatmsg( "enter your no","testing pls ignore", 23, 53)#here we have to enter our group or chat name,text if we wnat to sent to them, and tehn finaly we ahve to mention the time its gonna work 
link = input("ENTER YOUR LINK HERE :=")

#thi is gonna close the tab after desired time 
pywhatkit.close_tab(wait_time = 30)


#now we are gonna open a new tab of chrome with the recieved link
import webbrowser
url = link
chrome_path = '"C:\Program Files\Google\Chrome\Application\chrome.exe" %s'
webbrowser.get(chrome_path).open(url)

#now we start clicking shitts

import time
from pynput.keyboard import Key, Controller
keyboard = Controller()


time.sleep(10)
#presing d
keyboard.press(Key.ctrl_l)
keyboard.press('d')
keyboard.press('e')

#realeasing 
keyboard.release(Key.ctrl_l)
keyboard.release('d')
keyboard.release('e')


'''
#clicking join now 
from selenium import webdriver
driver = webdriver.Chrome('S:\APPS\PROGRAMMING\chromedriver.exe')
time.sleep(5)
driver.implicitly_wait(2000)
driver.find_element_by_css_selector('div.uArJ5e.UQuaGc.Y5sE8d.uyXBBb.xKiqt').click()

#for the time being we have installed a extenstion called https://chrome.google.com/webstore/detail/auto-join-for-google-meet/ajfokipknlmjhcioemgnofkpmdnbaldi


'''

#auto closing 
time.sleep(20)#wewant3300 seconds in there because our class is oen hour and we can leave a 5 mins early so 55 mins = 3300secs
keyboard.press(Key.ctrl_l)
keyboard.press('w')
keyboard.release(Key.ctrl_l)
keyboard.release('w')

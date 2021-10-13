def GOOGLEMEET():
    import pywhatkit
    import webbrowser
    import time

#opening whatsapp
    link1 = "https://web.whatsapp.com/"
    url = link1
    chrome_path = '"C:\Program Files\Google\Chrome\Application\chrome.exe" %s'
    webbrowser.get(chrome_path).open(url)


#clicking our class group in whatsapp
    time.sleep(4)
    from pynput.mouse import Button, Controller
    mouse = Controller()
# Set pointer position
    mouse.position = (206, 288)
# Press and release
    mouse.press(Button.left)
    mouse.release(Button.left)

    link = input("ENTER YOUR LINK HERE:==")

#thi is gonna close the tab after desired time 
    pywhatkit.close_tab(wait_time = 3)


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
    time.sleep(3)


#JOINING
    from pynput.mouse import Button, Controller
    mouse = Controller()
# Set pointer position
    mouse.position = (974, 498)
# Press and release
    mouse.press(Button.left)
    mouse.release(Button.left)

#auto closing 
    time.sleep(30)#wewant3300 seconds in there because our class is oen hour and we can leave a 5 mins early so 55 mins = 3300secs
    keyboard.press(Key.ctrl_l)  
    keyboard.press('w')
    keyboard.release(Key.ctrl_l)
    keyboard.release('w')


GOOGLEMEET
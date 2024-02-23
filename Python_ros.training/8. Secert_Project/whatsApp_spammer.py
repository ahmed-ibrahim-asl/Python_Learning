import pyautogui
import keyboard

import time

################################################################
PhoneNumber_List = [
    "",
]

################################################################

################################################################
Message = f"""السلام عليكم👋
مبروك، لقد تم قبولك للمشاركة بتدريب ros المجاني
يرجى الإنضمام لجروب الواتس أب من خلال الرابط التالي
https://chat.whatsapp.com/GupwkoemWG2HrxqGF980f6
"""
################################################################
for PhoneNumber in PhoneNumber_List:
    counter = 0

    # location of addressbar
    pyautogui.click(493, 57)

    pyautogui.hotkey('ctrl', 'a')
    pyautogui.press('backspace')
    time.sleep(1)
    pyautogui.typewrite(f"wa.me/{PhoneNumber}")
    pyautogui.press('enter')
    time.sleep(3)

    # go to click "Continue To chat"
    pyautogui.click(808, 354)

    time.sleep(3)
    # click on use WhatsApp Web
    pyautogui.click(788, 427)

    time.sleep(25)
    # Navigate to "Type a message"
    pyautogui.click(751, 1362)

    for line in Message.split('\n'):
        keyboard.write(line.strip())
        time.sleep(0.5)
        pyautogui.keyDown('shift')
        pyautogui.press('enter')
        pyautogui.keyUp('shift')

    pyautogui.press('enter')
    print(f"{counter} Done: " + PhoneNumber)
    counter += 1

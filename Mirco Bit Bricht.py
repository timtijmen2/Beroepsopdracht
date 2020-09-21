from microbit import *
import time
alfabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", " ", "#"]
Letter = 0
Bricht = ""
while True:
    if Letter == 26:
        display.show("_")
    else:
        display.show(alfabet[Letter])
    if button_a.is_pressed():
        Letter += 1
        time.sleep(0.2)
        if Letter == 28:
            Letter = 0
    elif button_b.is_pressed():
        
        if Letter == 27:
            display.scroll(Bricht)
            time.sleep(1)
        else:
            Bricht += alfabet[Letter]
            display.show("+")
            time.sleep(1)
        
import time
import keyboard

valMin = 65
valMax = 91

val1 = valMin
val2 = valMin
val3 = valMin
val4 = valMin

time.sleep(3)

for i in range(100000000):
    keyboard.write(chr(val1)+chr(val2)+chr(val3)+chr(val4))
    time.sleep(0.5)
    keyboard.press_and_release('enter')
    keyboard.press_and_release('enter')
    val1 = val1+1
    if val1 == 91:
        val1 = 97
    if val1 == 122:
        val1 = 65
        val2 = val2 + 1
    if val2 == 91:
        val2 = 97
    if val2 == 122:
        val2 = 65
        val3 = val3+1
    if val3 == 91:
        val3 = 97
    if val3 == 122:
        val3 = 65
        val4 = val4+1
    if keyboard.is_pressed('esc'):
        exit(0)

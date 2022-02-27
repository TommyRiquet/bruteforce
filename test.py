import time
import keyboard
from tkinter import *

valMin = 65
valMax = 91





class BruteForce:
    def __init__(self,test):
        self.delay = 1

        frame = Frame(window)
        self.Val = StringVar()
        labelVal = Label(frame, textvariable=self.Val, font=('Arial', 15), fg='black')
        labelVal.pack()
        btnStart = Button(frame, text="Start", font=('Arial', 12), command=self.runBruteForce)
        btnStart.pack()
        frame.pack()

    def printVal(self, val):
        self.Val.set(val)

    def runBruteForce(self):
        self.val1 = valMin
        self.val2 = valMin
        self.val3 = valMin
        self.val4 = valMin

        for i in range(100):
            window.after(self.delay, self.printVal, chr(self.val1)+chr(self.val2)+chr(self.val3)+chr(self.val4))

            """keyboard.write(chr(val1)+chr(val2)+chr(val3)+chr(val4))"""
            keyboard.press_and_release('enter')
            keyboard.press_and_release('enter')
            time.sleep(self.delay)
            self.val1 = self.val1+1
            if self.val1 == 91:
                self.val1 = 97
            if self.val1 == 122:
                self.val1 = 65
                self.val2 = self.val2 + 1
            if self.val2 == 91:
                self.val2 = 97
            if self.val2 == 122:
                self.val2 = 65
                self.val3 = self.val3+1
            if self.val3 == 91:
                self.val3 = 97
            if self.val3 == 122:
                self.val3 = 65
                self.val4 = self.val4+1
            if keyboard.is_pressed('esc'):
                exit(0)
                window.close()



if __name__ == '__main__':
    window = Tk()
    window.title('BruteForce')
    window.geometry('300x300')
    window.resizable(False, False)

    bruteforce = BruteForce(window)
    window.mainloop()

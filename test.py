import time
import keyboard
import tkinter as tk

valMin = 65
valMax = 91


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.delay = 3
        self.speed = 0
        self.iteration = 1000000
        self.isOn = False
        self.password = ''
        self.cpt = 0

        self.resizable(False, False)
        self.geometry("300x300")

        self.Val = tk.StringVar()
        self.nbrPassword = tk.StringVar()

        tk.Label(self, text='Mot de passe : ').grid(row=2, column=1)
        tk.Label(self, textvariable=self.Val).grid(row=2, column=4)

        tk.Label(self, text='Numéro : ').grid(row=3, column=1)
        tk.Label(self, textvariable=self.nbrPassword).grid(row=3, column=4)

        self.btnStart = tk.Button(self, text="Start", font=('Arial', 12), command=self.runBruteForce).grid(row=6, column=3)
        self.btnStop = tk.Button(self, text="Stop", font=('Arial', 12), command=self.stopBruteForce).grid(row=6, column=4)



    def runBruteForce(self):
        self.val1 = valMin
        self.val2 = valMin
        self.val3 = valMin
        self.val4 = valMin
        self.isOn = True

        time.sleep(self.delay)
        while self.isOn:
            self.password = chr(self.val1)+chr(self.val2)+chr(self.val3)+chr(self.val4)
            self.Val.set(self.password)
            self.nbrPassword.set(self.cpt)
            app.update()
            keyboard.write(self.password)
            keyboard.press_and_release('enter')
            keyboard.press_and_release('enter')
            if self.speed != 0:
                time.sleep(self.speed)

            self.cpt = self.cpt+1
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

    def stopBruteForce(self):
        self.isOn = False


if __name__ == '__main__':
    app = App()
    app.mainloop()

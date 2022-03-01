import time
import tkinter as tk
import rarfile


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.resizable(False, False)
        self.geometry("300x300")
        self.title('BruteForce')
        self.filename = 'flag.rar'

        self.speed = 0
        self.isSearching = False
        self.password = ''
        self.nbr_essai = 0

        self.val1 = 48
        self.val2 = 48
        self.val3 = 48
        self.val4 = 48

        self.Val = tk.StringVar()
        self.nbrPassword = tk.StringVar()

        tk.Label(self, text='Mot de passe : ').grid(row=2, column=1)
        tk.Label(self, textvariable=self.Val).grid(row=2, column=4)

        tk.Label(self, text='Numéro : ').grid(row=3, column=1)
        tk.Label(self, textvariable=self.nbrPassword).grid(row=3, column=4)

        self.btnStart = tk.Button(self, text="Start", font=('Arial', 12), command=self.runBruteForce).grid(row=6,
                                                                                                           column=3)
        self.btnStop = tk.Button(self, text="Stop", font=('Arial', 12), command=self.stopBruteForce).grid(row=6,
                                                                                                          column=4)

    def runBruteForce(self):

        self.isSearching = True

        with rarfile.RarFile(self.filename) as rf:

            while self.isSearching:
                self.password = chr(self.val1) + chr(self.val2) + chr(self.val3) + chr(self.val4)
                self.Val.set(self.password)
                self.nbrPassword.set(self.nbr_essai)
                self.update()
                try:
                    rf.extractall(pwd=self.password)
                    print("Password Found : "+self.password)
                    self.isSearching = False
                except rarfile.BadRarFile:

                    # [48-57][65-90][97-122]
                    self.nbr_essai = self.nbr_essai + 1
                    self.val1 = self.val1 + 1
                    if self.val1 == 58:
                        self.val1 = 65
                    if self.val1 == 91:
                        self.val1 = 97
                    if self.val1 == 123:
                        self.val1 = 65
                        self.val2 = self.val2 + 1

                    if self.val2 == 58:
                        self.val2 = 65
                    if self.val2 == 91:
                        self.val2 = 97
                    if self.val2 == 122:
                        self.val2 = 65
                        self.val3 = self.val3 + 1

                    if self.val3 == 58:
                        self.val3 = 65
                    if self.val3 == 91:
                        self.val3 = 97
                    if self.val3 == 122:
                        self.val3 = 65
                        self.val4 = self.val4 + 1
                    if self.val4 == 123:
                        print('LIMIT')

    def stopBruteForce(self):
        self.isSearching = False


if __name__ == '__main__':
    app = App()
    app.mainloop()

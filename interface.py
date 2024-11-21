from tkinter import *
from tkinter import ttk
from img import root_logo

class Main_window(Tk):
    logo_root = root_logo.pegar_logo()

    def __init__(self, screenName = None, baseName = None, className = "Tk", useTk = True, sync = False, use = None):
        super().__init__(screenName, baseName, className, useTk, sync, use)
        self.geometry("600x300")
        self.title("Teste")
        [self.wm_iconbitmap(self.logo_root) for controle in range(1)]
        print("contando")
        self.mainloop()

tela = Main_window()

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

class Window_Notebook(ttk.Notebook):
    def __init__(self, master = None, *, class_ = "", cursor = "", height = 0, name = ..., padding = ..., style = "", takefocus = ..., width = 0):
        self.criar_janela_opcao()
        super().__init__(master, class_=class_, cursor=cursor, height=height, name=name, padding=padding, style=style, takefocus=takefocus, width=width)

    def criar_janela_opcao(self):
        frame_opcao_notebook = ttk.Frame(self)
        frame_opcao_notebook.pack(fill="both", expand=True)
        ttk.Label(self, text="Hello world!").grid(column=0, row=0)
        self.add(frame_opcao_notebook, text="opções")

tela_inicial = Main_window()
tela_notebook = Window_Notebook(tela_inicial)

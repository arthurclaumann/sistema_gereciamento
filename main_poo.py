import tkinter as tk
import sqlite3
import pandas as pd

class App:
    def __init__(self):
        self.janela = self.cria_janela()
        self.janela.mainloop()

    def cria_janela(self):
        janela = tk.Tk()
        janela.title('Sistema de Gereciamento')
        janela.geometry('650x450')
        janela.resizable(True,True)
        return janela

    

    # def configuracao_janela(self):

app = App()
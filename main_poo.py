import tkinter as tk
import sqlite3
from typing import Any
import pandas as pd

class App:
    def __init__(self):
        self.janela = self.cria_janela()
        self.cria_menu()
        self.exibir_cadastro()
        self.janela.mainloop()


    def cria_janela(self):
        janela = tk.Tk()
        janela.title('Sistema de Gereciamento')
        janela.geometry('650x450')
        janela.resizable(True,True)
        return janela

    def cria_menu(self):
        self.menu = tk.Menu(self.janela)
        self.janela.config(menu = self.menu)

        self.menu_gerenciamento = tk.Menu(self.menu)
        self.menu.add_cascade(label = 'Menu de Gerenciamento', menu = self.menu_gerenciamento)
        
        self.criacao_menu_ordem_servico(self.menu, self.menu_gerenciamento)
    # def configuracao_janela(self):


    def criacao_menu_ordem_servico(self, menu, menu_gerenciamento):
        # OS
        menu_ordem_servico = tk.Menu(menu_gerenciamento)
        menu_gerenciamento.add_cascade(label = 'Ordem de Serviço', menu = menu_ordem_servico)

        menu_os = tk.Menu(menu_ordem_servico)
        menu_ordem_servico.add_cascade(label = 'Ordem de Serviço', menu = menu_os)

        menu_voucher_despesa = tk.Menu(menu_ordem_servico)
        menu_ordem_servico.add_cascade(label = 'Voucher/Despesa', menu = menu_voucher_despesa)

        menu_voucher_emitidos = tk.Menu(menu_ordem_servico)
        menu_ordem_servico.add_cascade(label = 'Vouchers Emitidos', menu = menu_voucher_emitidos)

        # menu_fecha_os = tk.Menu(menu_ordem_servico)
        def fecha_os():
            pass
        menu_ordem_servico.add_command(label = 'Fechar OS', command = fecha_os)

        # menu_os_aberta = tk.Menu(menu_ordem_servico)
        def os_abertas():
            pass
        menu_ordem_servico.add_command(label = 'OS abertas', command = os_abertas)

        # menu_os_fechada = tk.Menu(menu_ordem_servico)
        def os_fechada():
            pass
        menu_ordem_servico.add_command(label = 'OS fechadas', command = os_fechada)

        # menu_relat_carro = tk.Menu(menu_ordem_servico)
        def relatorio_carro():
            pass
        menu_ordem_servico.add_command(label = 'Relatório Carros', command = relatorio_carro)

    def exibir_cadastro(self):
        self.cadastro_frame = tk.Frame(self.janela)
        self.cadastro_frame.pack()


app = App()
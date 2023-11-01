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
        
        self.cria_menu_ordem_servico(self.menu, self.menu_gerenciamento)
        self.cria_menu_financeiro(self.menu, self.menu_gerenciamento)
        self.menu_gerenciamento.add_separator()


    def cria_menu_ordem_servico(self, menu, menu_gerenciamento):
        # OS
        menu_ordem_servico = tk.Menu(menu_gerenciamento)
        menu_gerenciamento.add_cascade(label = 'Ordem de Serviço', menu = menu_ordem_servico)

        menu_os = tk.Menu(menu_ordem_servico)
        menu_ordem_servico.add_cascade(label = 'Ordem de Serviço', menu = menu_os)
        
        menu_voucher_despesa = tk.Menu(menu_ordem_servico)
        menu_ordem_servico.add_cascade(label = 'Voucher/Despesa', menu = menu_voucher_despesa)

        menu_voucher_emitidos = tk.Menu(menu_ordem_servico)
        menu_ordem_servico.add_cascade(label = 'Vouchers Emitidos', menu = menu_voucher_emitidos)
        menu_ordem_servico.add_separator()

        # menu_fecha_os = tk.Menu(menu_ordem_servico)
        def fecha_os():
            pass
        menu_ordem_servico.add_command(label = 'Fechar OS', command = fecha_os)
        menu_ordem_servico.add_separator()

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

    def cria_menu_financeiro(self, menu, menu_gerenciamento):
        menu_financeiro = tk.Menu(menu_gerenciamento)
        menu_gerenciamento.add_cascade(label = 'Financeiro', menu = menu_financeiro)

        menu_movimentacao = tk.Menu(menu_financeiro)
        menu_financeiro.add_cascade(label = 'Movimentação', menu = menu_movimentacao)   
                             

        menu_contas_pagar = tk.Menu(menu_financeiro)
        menu_financeiro.add_cascade(label = 'Contas a pagar', menu = menu_contas_pagar)   

        menu_baixa_contas_pagar = tk.Menu(menu_financeiro)
        menu_financeiro.add_cascade(label = 'Baixar contas a pagar', menu = menu_baixa_contas_pagar)   
                             

        menu_contas_receber = tk.Menu(menu_financeiro)
        menu_financeiro.add_cascade(label = 'Contas a receber', menu = menu_contas_receber)   
                             

        menu_baixar_conta_receber= tk.Menu(menu_financeiro)
        menu_financeiro.add_cascade(label = 'Baixar contas a receber', menu = menu_baixar_conta_receber)   
        menu_financeiro.add_separator()
                             

        menu_plano_contas = tk.Menu(menu_financeiro)
        menu_financeiro.add_cascade(label = 'Plano contas', menu = menu_plano_contas)   
                             

        menu_financiamento = tk.Menu(menu_financeiro)
        menu_financeiro.add_cascade(label = 'Financiamento', menu = menu_financiamento)   
        menu_financeiro.add_separator()
                             

        menu_emissao_fatura = tk.Menu(menu_financeiro)
        menu_financeiro.add_cascade(label = 'Emissão faturas', menu = menu_emissao_fatura)   


        menu_imprime_fatura = tk.Menu(menu_financeiro)
        menu_financeiro.add_cascade(label = 'Imprime faturas', menu = menu_imprime_fatura)   

        menu_baixa_fatura = tk.Menu(menu_financeiro)
        menu_financeiro.add_cascade(label = 'Baixar faturas', menu = menu_baixa_fatura) 
        menu_financeiro.add_separator()

        menu_emissao_fatura_extra = tk.Menu(menu_financeiro)
        menu_financeiro.add_cascade(label = 'Emissão faturas extras', menu = menu_emissao_fatura_extra)   

        menu_imprime_fatura_extra = tk.Menu(menu_financeiro)
        menu_financeiro.add_cascade(label = 'Imprime fatura', menu = menu_imprime_fatura_extra)   

        menu_baixa_fatura_extra = tk.Menu(menu_financeiro)
        menu_financeiro.add_cascade(label = 'Baixar faturas extra', menu = menu_baixa_fatura_extra)   
        menu_financeiro.add_separator()

        menu_relatorio_movimentacao = tk.Menu(menu_financeiro)
        menu_financeiro.add_cascade(label = 'Relat. Movimentação', menu = menu_relatorio_movimentacao)   

        menu_relatorio_lucratividade = tk.Menu(menu_financeiro)
        menu_financeiro.add_cascade(label = 'Relat. Lucratividade', menu = menu_relatorio_lucratividade)   

        menu_relatorio_contas_pagar= tk.Menu(menu_financeiro)
        menu_financeiro.add_cascade(label = 'Relat. Contas Pagar', menu = menu_relatorio_contas_pagar)   
                             
                                            
    def exibir_cadastro(self):
        self.cadastro_frame = tk.Frame(self.janela)
        self.cadastro_frame.pack()


app = App()
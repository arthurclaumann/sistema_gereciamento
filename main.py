import tkinter as tk
import sqlite3
import pandas as pd
["Ordens Serviço", "Financeiro", "Cadastro", "Apoio", "Parâmetros"]

# def mostrar_cadastro(opcao):
#     # Limpar o frame atual
#     for widget in cadastro_frame.winfo_children():
#         widget.destroy()

#     if opcao == "Ordens Serviço":
#         menu_ordem_servico = tk.Menu(menu_gerenciamento)
#         menu_gerenciamento.add_cascade(label='Ordens de Serviço', menu=menu_ordem_servico)

#         label = tk.Label(cadastro_frame, text='Ordens Serviço')
#         label.grid(column=0, row=0, columnspan=3, padx=10, pady=10)

#         entry = tk.Entry(cadastro_frame)
#         entry.grid(column=2, row=0, columnspan=3, padx=10, pady=10)


# Configuração da janela principal
janela = tk.Tk()
janela.title("Sistema de Gerenciamento")
janela.geometry('650x450')

# Criar um menu
menu = tk.Menu(janela)
janela.config(menu=menu, background='gray')

## Opções do menu
menu_gerenciamento = tk.Menu(menu)

menu.add_cascade(label="Menu Geral do Sistema", menu=menu_gerenciamento)

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




# Financeiro
menu_financeiro = tk.Menu(menu_gerenciamento)
menu_gerenciamento.add_cascade(label = 'Financeiro', menu = menu_financeiro)

# Cadastro
menu_cadastro= tk.Menu(menu_gerenciamento)
menu_gerenciamento.add_cascade(label = 'Cadastro', menu = menu_cadastro)

# Apoio
menu_apoio= tk.Menu(menu_gerenciamento)
menu_gerenciamento.add_cascade(label = 'Apoio', menu = menu_apoio)

# Parametros
menu_parametros= tk.Menu(menu_gerenciamento)
menu_gerenciamento.add_cascade(label = 'Parâmetros', menu = menu_parametros)

# Sair
menu_gerenciamento.add_command(label = 'Sair', command= janela.destroy)


# opcoes = ["Ordens Serviço", "Financeiro", "Cadastro", "Apoio", "Parâmetros"]
# for opcao in opcoes:
#     menu_gerenciamento.add_command(label=opcao, command=lambda opcao=opcao: mostrar_cadastro(opcao))


# # Frame para exibir os formulários de cadastro
cadastro_frame = tk.Frame(janela)
cadastro_frame.pack()

janela.mainloop()

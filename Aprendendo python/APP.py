import tkinter as tk

# Função para adicionar despesas ou receitas
def adicionar_transacao():
    descricao = descricao_entry.get()
    valor = float(valor_entry.get())
    if tipo_transacao.get() == "Despesa":
        valor *= -1  # Converte despesa para valor negativo
    transacoes_listbox.insert(tk.END, f"{descricao}: R${valor:.2f}")
    atualizar_saldo(valor)

# Função para atualizar o saldo
def atualizar_saldo(valor):
    saldo_atual = float(saldo_label.cget("text")[8:]) + valor
    saldo_label.config(text=f"Saldo: R${saldo_atual:.2f}")

# Configuração da janela principal
janela = tk.Tk()
janela.title("Aplicativo de Contabilidade")

# Criação de widgets
descricao_label = tk.Label(janela, text="Descrição:")
descricao_entry = tk.Entry(janela)
valor_label = tk.Label(janela, text="Valor (R$):")
valor_entry = tk.Entry(janela)
tipo_transacao = tk.StringVar()
tipo_transacao.set("Receita")
tipo_transacao_label = tk.Label(janela, text="Tipo de Transação:")
tipo_transacao_menu = tk.OptionMenu(janela, tipo_transacao, "Receita", "Despesa")
adicionar_botao = tk.Button(janela, text="Adicionar Transação", command=adicionar_transacao)
saldo_label = tk.Label(janela, text="Saldo: R$0.00")
transacoes_label = tk.Label(janela, text="Transações:")
transacoes_listbox = tk.Listbox(janela)

# Posicionamento dos widgets
descricao_label.pack()
descricao_entry.pack()
valor_label.pack()
valor_entry.pack()
tipo_transacao_label.pack()
tipo_transacao_menu.pack()
adicionar_botao.pack()
saldo_label.pack()
transacoes_label.pack()
transacoes_listbox.pack()

# Loop principal da aplicação
janela.mainloop()

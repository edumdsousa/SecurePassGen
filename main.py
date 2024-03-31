import tkinter as tk
from tkinter import ttk
import random
import string
import tkinter.messagebox as messagebox

def gerar_senha():
    comprimento = int(comprimento_entrada.get())
    caracteres = string.ascii_letters + string.digits + string.punctuation
    senha = ''.join(random.choice(caracteres) for _ in range(comprimento))
    senha_entrada.delete(0, tk.END)
    senha_entrada.insert(0, senha)

def salvar_senha():
    senha = senha_entrada.get()
    origem = origem_entrada.get()
    with open("config.conf", "a") as arquivo:
        arquivo.write(f'{origem}"{senha}\n')  # Modificado para adicionar aspas
    messagebox.showinfo("Sucesso", "Senha salva com sucesso!")

def copiar_senha(event):
    # Obter a linha selecionada
    item = tree.focus()
    # Obter os valores da linha selecionada
    valores = tree.item(item, 'values')
    # Se houver valores e eles não estiverem vazios
    if valores and valores[1]:
        senha = valores[1]
        # Copiar a senha para a área de transferência
        root.clipboard_clear()
        root.clipboard_append(senha)
        root.update()
        messagebox.showinfo("Sucesso", "Senha copiada para a área de transferência!")

def gerenciar_senhas_salvas():
    # Nova janela
    janela_gerenciar = tk.Toplevel(root)
    janela_gerenciar.title("Senhas Salvas")

    # Treeview para exibir senhas salvas
    global tree
    tree = ttk.Treeview(janela_gerenciar, columns=('Referência', 'Senha'), show='headings')
    tree.heading('Referência', text='Referência')
    tree.heading('Senha', text='Senha')
    tree.column('Senha', stretch=True)  # Ajuste automático do tamanho da coluna

    # Lê senhas salvas do arquivo e adiciona ao Treeview
    with open("config.conf", "r") as arquivo:
        for linha in arquivo:
            index_aspas = linha.find('"')
            referencia = linha[:index_aspas]
            senha = linha[index_aspas+1:].strip()
            tree.insert('', 'end', values=(referencia, senha))

    tree.pack(fill='both', expand=True)

    # Adicionar evento de duplo clique para copiar a senha
    tree.bind('<Double-1>', copiar_senha)

root = tk.Tk()
root.title("Gerador de Senha Segura")
root.configure(bg="#f0f0f0")  # Cor de fundo
root.iconbitmap(bitmap="icone.ico") #icone

# Impede o redimensionamento da janela
root.resizable(False, False)

# Personalização de cores
cor_botao = "#4caf50"
cor_botao_salvar = "#2196f3"
cor_texto = "#333333"

# Widgets
comprimento_label = tk.Label(root, text="Quantidade de Dígitos:", bg="#f0f0f0", fg=cor_texto)
comprimento_entrada = tk.Entry(root)
gerar_botao = tk.Button(root, text="Gerar Senha", command=gerar_senha, bg=cor_botao, fg="white")
senha_entrada = tk.Entry(root)
origem_label = tk.Label(root, text="Referência:", bg="#f0f0f0", fg=cor_texto)
origem_entrada = tk.Entry(root, width=50)  # Aumentando o tamanho do campo de entrada
salvar_botao = tk.Button(root, text="Salvar", command=salvar_senha, bg=cor_botao_salvar, fg="white")
gerenciar_botao = tk.Button(root, text="Gerenciar Senhas Salvas", command=gerenciar_senhas_salvas, bg="#ff9800", fg="white")

# Layout
comprimento_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")
comprimento_entrada.grid(row=0, column=1, padx=10, pady=10, sticky="ew")
gerar_botao.grid(row=1, column=0, columnspan=2, padx=10, pady=10, sticky="ew")
senha_entrada.grid(row=2, column=0, columnspan=2, padx=10, pady=10, sticky="ew")
origem_label.grid(row=3, column=0, padx=10, pady=10, sticky="w")
origem_entrada.grid(row=3, column=1, padx=10, pady=10, sticky="ew")
salvar_botao.grid(row=4, column=0, columnspan=2, padx=10, pady=10, sticky="ew")
gerenciar_botao.grid(row=5, column=0, columnspan=2, padx=10, pady=10, sticky="ew")

# Centralizar widgets verticalmente
for i in range(6):
    root.grid_rowconfigure(i, weight=1)

root.mainloop()

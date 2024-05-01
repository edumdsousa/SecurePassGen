import tkinter as tk
from tkinter import ttk
import random
import string
import tkinter.messagebox as messagebox
import os
import subprocess

# Dicionário para armazenar os trees de cada aba
trees = {}

# Função para gerar senha
def gerar_senha(comprimento_entrada, senha_entrada):
    comprimento = int(comprimento_entrada.get())
    caracteres = string.ascii_letters + string.digits + string.punctuation
    senha = ''.join(random.choice(caracteres) for _ in range(comprimento))
    senha_entrada.delete(0, tk.END)
    senha_entrada.insert(0, senha)

# Função para salvar senha
def salvar_senha(nome_arquivo, senha_entrada, origem_entrada):
    senha = senha_entrada.get()
    origem = origem_entrada.get()
    with open(nome_arquivo, "a") as arquivo:
        arquivo.write(f'{origem}"{senha}\n')  # Modificado para adicionar aspas
    messagebox.showinfo("Sucesso", "Senha salva com sucesso!")

# Função para editar senha
def editar_senha(nome_arquivo):
    # Fechar a janela de gerenciamento de senhas
    janela_gerenciar.destroy()
    # Abrir o arquivo onde as senhas estão salvas
    try:
        # Abrir o arquivo com o bloco de notas
        subprocess.Popen(['notepad', nome_arquivo])
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao abrir o arquivo: {e}")

# Função para copiar senha
def copiar_senha(event, tree):
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
        # Fechar a janela do gerenciador de senhas
        janela_gerenciar.destroy()

# Função para gerenciar senhas salvas
def gerenciar_senhas_salvas(nome_arquivo):
    global janela_gerenciar
    # Nova janela
    janela_gerenciar = tk.Toplevel(root)
    janela_gerenciar.title("Senhas Salvas")
    janela_gerenciar.iconbitmap(bitmap="icone.ico")

    # Frame principal
    frame_principal = ttk.Frame(janela_gerenciar, padding="20")
    frame_principal.pack(fill='both', expand=True)

    # Treeview para exibir senhas salvas
    style = ttk.Style()
    style.configure("Treeview", background="#F0F0F0", fieldbackground="#F0F0F0", foreground="black")
    tree = ttk.Treeview(frame_principal, columns=('Referência', 'Senha'), show='headings', style="Treeview")
    tree.heading('Referência', text='Referência')
    tree.heading('Senha', text='Senha')
    tree.column('Senha', stretch=True)  # Ajuste automático do tamanho da coluna

    # Lê senhas salvas do arquivo e adiciona ao Treeview
    with open(nome_arquivo, "r") as arquivo:
        for linha in arquivo:
            index_aspas = linha.find('"')
            referencia = linha[:index_aspas]
            senha = linha[index_aspas+1:].strip()
            tree.insert('', 'end', values=(referencia, senha))

    tree.pack(fill='x', expand=True)

    # Esticar o botão para ocupar todo o frame horizontalmente
    editar_botao = ttk.Button(frame_principal, text="Editar Senha", style="TButton", command=lambda: editar_senha(nome_arquivo))
    editar_botao.pack(fill='x', pady=10)

    # Adicionar evento de duplo clique para copiar a senha
    tree.bind('<Double-1>', lambda event: copiar_senha(event, tree))

    # Armazenar o tree no dicionário
    trees[nome_arquivo] = tree

# Função para criar uma nova aba
def criar_aba(nome_visual, nome_arquivo):
    aba = ttk.Frame(notebook, padding="20")
    notebook.add(aba, text=nome_visual)

    # Widgets
    comprimento_label = ttk.Label(aba, text="Quantidade de Dígitos:", style="TLabel")
    comprimento_entrada = ttk.Entry(aba)
    gerar_botao = ttk.Button(aba, text="Gerar Senha", style="TButton", command=lambda: gerar_senha(comprimento_entrada, senha_entrada))
    senha_entrada = ttk.Entry(aba)
    origem_label = ttk.Label(aba, text="Referência:", style="TLabel")
    origem_entrada = ttk.Entry(aba, width=50)
    salvar_botao = ttk.Button(aba, text="Salvar", style="TButton", command=lambda: salvar_senha(nome_arquivo, senha_entrada, origem_entrada))
    gerenciar_botao = ttk.Button(aba, text="Gerenciar Senhas Salvas", style="TButton", command=lambda: gerenciar_senhas_salvas(nome_arquivo))

    # Layout
    comprimento_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")
    comprimento_entrada.grid(row=0, column=1, padx=10, pady=10, sticky="ew")
    gerar_botao.grid(row=1, column=0, columnspan=2, padx=10, pady=10, sticky="ew")
    senha_entrada.grid(row=2, column=0, columnspan=2, padx=10, pady=10, sticky="ew")
    origem_label.grid(row=3, column=0, padx=10, pady=10, sticky="w")
    origem_entrada.grid(row=3, column=1, padx=10, pady=10, sticky="ew")
    salvar_botao.grid(row=4, column=0, columnspan=2, padx=10, pady=10, sticky="ew")
    gerenciar_botao.grid(row=5, column=0, columnspan=2, padx=10, pady=10, sticky="ew")

    # Configuração do estilo
    style = ttk.Style()
    style.configure('TButton', foreground='white', background='#007BFF', font=('Arial', 10))
    style.map('TButton', background=[('active', '#0056B3')])
    style.configure('TLabel', foreground='#007BFF', font=('Arial', 10))

# Configuração da janela principal
root = tk.Tk()
root.title("Gerador de Senha Segura")
root.iconbitmap(bitmap="icone.ico")
root.iconbitmap(default="icone.ico")

# Carregar um estilo mais moderno para os widgets
style = ttk.Style()
style.theme_use('clam')

# Widgets
notebook = ttk.Notebook(root)
notebook.pack(fill='both', expand=True)

# Criação das abas
abas = [("Layer1", "Layer1.conf"), ("Layer2", "Layer2.conf"), ("Layer3", "Layer3.conf"), ("Layer4", "Layer4.conf"), ("Layer5", "Layer5.conf")]
for nome_visual, nome_arquivo in abas:
    criar_aba(nome_visual, nome_arquivo)

# Configuração do fundo
root.configure(bg="#F0F0F0")

# Laço principal
root.mainloop()

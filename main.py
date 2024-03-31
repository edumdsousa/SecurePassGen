import tkinter as tk
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
        arquivo.write(f'{origem} {senha}\n')  
    messagebox.showinfo("Sucesso", "Senha salva com sucesso!")

root = tk.Tk()
root.title("Gerador de Senha Segura")
root.iconbitmap(bitmap="icone.ico")
root.configure(bg="#f0f0f0")  # Cor de fundo
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
origem_entrada = tk.Entry(root, width=20)
salvar_botao = tk.Button(root, text="Salvar", command=salvar_senha, bg=cor_botao_salvar, fg="white")

# Layout
comprimento_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")
comprimento_entrada.grid(row=0, column=1, padx=10, pady=10, sticky="ew")
gerar_botao.grid(row=1, column=0, columnspan=2, padx=10, pady=10, sticky="ew")
senha_entrada.grid(row=2, column=0, columnspan=2, padx=10, pady=10, sticky="ew")
origem_label.grid(row=3, column=0, padx=10, pady=10, sticky="w")
origem_entrada.grid(row=3, column=1, padx=10, pady=10, sticky="ew")
salvar_botao.grid(row=4, column=0, columnspan=2, padx=10, pady=10, sticky="ew")

# Centralizar widgets verticalmente
root.grid_rowconfigure(0, weight=1)
root.grid_rowconfigure(1, weight=1)
root.grid_rowconfigure(2, weight=1)
root.grid_rowconfigure(3, weight=1)
root.grid_rowconfigure(4, weight=1)

root.mainloop()

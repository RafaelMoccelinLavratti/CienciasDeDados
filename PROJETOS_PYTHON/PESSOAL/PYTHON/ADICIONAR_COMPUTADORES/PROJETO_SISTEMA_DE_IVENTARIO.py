import tkinter as tk
from tkinter import messagebox

# Função para adicionar um novo computador ao inventário
def adicionar_computador():
    nome = nome_entry.get()
    tipo = tipo_entry.get()
    numero_serie = numero_serie_entry.get()

    if nome and tipo and numero_serie:
        inventario_listbox.insert(tk.END, f"Nome: {nome}, Tipo: {tipo}, Número de Série: {numero_serie}")
        nome_entry.delete(0, tk.END)
        tipo_entry.delete(0, tk.END)
        numero_serie_entry.delete(0, tk.END)
    else:
        messagebox.showerror("Erro", "Por favor, preencha todos os campos.")

# Função para remover um computador selecionado do inventário
def remover_computador():
    selected_index = inventario_listbox.curselection()
    if selected_index:
        inventario_listbox.delete(selected_index)

# Configuração da janela principal
root = tk.Tk()
root.title("Inventário de Computadores")

# Campos de entrada
nome_label = tk.Label(root, text="Nome:")
nome_label.pack()
nome_entry = tk.Entry(root)
nome_entry.pack()

tipo_label = tk.Label(root, text="Tipo:")
tipo_label.pack()
tipo_entry = tk.Entry(root)
tipo_entry.pack()

numero_serie_label = tk.Label(root, text="Número de Série:")
numero_serie_label.pack()
numero_serie_entry = tk.Entry(root)
numero_serie_entry.pack()

# Botões
adicionar_button = tk.Button(root, text="Adicionar Computador", command=adicionar_computador)
adicionar_button.pack()

remover_button = tk.Button(root, text="Remover Computador Selecionado", command=remover_computador)
remover_button.pack()

# Lista de inventário
inventario_listbox = tk.Listbox(root)
inventario_listbox.pack()

# Executar a aplicação
root.mainloop()

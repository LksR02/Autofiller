import tkinter as tk
from tkinter import filedialog, messagebox

def insert_text_in_dat_file(file_path, text, line_number, column_number):
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
        
        # Garante que a linha existe, adicionando linhas vazias se necessário
        while len(lines) < line_number:
            lines.append('\n')
        
        line = lines[line_number - 1].rstrip('\n')
        
        # Garante que a coluna existe, adicionando espaços em branco se necessário
        if column_number > len(line):
            line += ' ' * (column_number - len(line))
        
        # Insere o texto na posição desejada
        lines[line_number - 1] = line[:column_number] + text + line[column_number:] + '\n'
        
        with open(file_path, 'w') as file:
            file.writelines(lines)
        
        messagebox.showinfo("Sucesso", f"Texto inserido com sucesso no arquivo {file_path}")
    except Exception as e:
        messagebox.showerror("Erro", f"Ocorreu um erro ao inserir o texto: {e}")

def browse_file():
    file_path = filedialog.askopenfilename(filetypes=[("DAT files", "*.dat")])
    entry_file_path.delete(0, tk.END)
    entry_file_path.insert(0, file_path)

def on_submit():
    try:
        file_path = entry_file_path.get()
        text = entry_text.get()
        line_number = int(entry_line_number.get())
        column_number = int(entry_column_number.get())
        insert_text_in_dat_file(file_path, text, line_number, column_number)
    except ValueError:
        messagebox.showerror("Erro", "Certifique-se de inserir valores numéricos para a linha e a coluna.")

# Configuração da interface gráfica
root = tk.Tk()
root.title("Inserir Texto em Arquivo .dat")

tk.Label(root, text="Caminho do arquivo .dat:").grid(row=0, column=0, padx=10, pady=5)
entry_file_path = tk.Entry(root, width=50)
entry_file_path.grid(row=0, column=1, padx=10, pady=5)
tk.Button(root, text="Procurar", command=browse_file).grid(row=0, column=2, padx=10, pady=5)

tk.Label(root, text="Texto a ser inserido:").grid(row=1, column=0, padx=10, pady=5)
entry_text = tk.Entry(root, width=50)
entry_text.grid(row=1, column=1, padx=10, pady=5)

tk.Label(root, text="Número da linha:").grid(row=2, column=0, padx=10, pady=5)
entry_line_number = tk.Entry(root, width=10)
entry_line_number.grid(row=2, column=1, padx=10, pady=5, sticky='w')

tk.Label(root, text="Número da coluna:").grid(row=3, column=0, padx=10, pady=5)
entry_column_number = tk.Entry(root, width=10)
entry_column_number.grid(row=3, column=1, padx=10, pady=5, sticky='w')

tk.Button(root, text="Inserir Texto", command=on_submit).grid(row=4, column=0, columnspan=3, pady=10)

root.mainloop()

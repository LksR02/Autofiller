import tkinter as tk
from tkinter import filedialog, messagebox

def modify_lines(file_path):
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
        
        # Garante que o arquivo tem pelo menos 80 linhas
        while len(lines) < 80:
            lines.append('\n')
        
        # Define a nova linha 80 conforme a tabela
        new_line_80 = " " * 100  # Cria uma linha vazia com 100 espaços
        new_line_80 = new_line_80[:0] + "SIST" + new_line_80[4:]  # Coluna 1
        new_line_80 = new_line_80[:7] + "12" + new_line_80[9:]    # Coluna 8
        new_line_80 = new_line_80[:10] + "12" + new_line_80[12:]  # Coluna 11
        new_line_80 = new_line_80[:14] + "0" + new_line_80[15:]   # Coluna 15
        new_line_80 = new_line_80[:16] + "RD 2" + new_line_80[20:]  # Coluna 17
        lines[79] = new_line_80 + "\n"  # Substitui a linha 80
        
        # Garante que o arquivo tem pelo menos 392 linhas
        while len(lines) < 392:
            lines.append('\n')
        
        # Define a nova linha 393 conforme a nova tabela
        new_line_393 = " " * 100  # Cria uma linha vazia com 100 espaços
        new_line_393 = new_line_393[:0] + "UT" + new_line_393[2:]   # Coluna 1
        new_line_393 = new_line_393[:4] + "999" + new_line_393[7:]  # Coluna 5
        new_line_393 = new_line_393[:9] + "RD 2" + new_line_393[13:] # Coluna 10
        new_line_393 = new_line_393[:22] + "12" + new_line_393[24:]  # Coluna 23
        new_line_393 = new_line_393[:25] + "2" + new_line_393[26:]   # Coluna 26
        new_line_393 = new_line_393[:28] + "4" + new_line_393[29:]   # Coluna 29
        new_line_393 = new_line_393[:31] + "0" + new_line_393[32:]   # Coluna 32
        new_line_393 = new_line_393[:33] + "0" + new_line_393[34:]   # Coluna 34
        new_line_393 = new_line_393[:36] + "F" + new_line_393[37:]   # Coluna 37
        new_line_393 = new_line_393[:54] + "0.0" + new_line_393[57:] # Coluna 55
        new_line_393 = new_line_393[:63] + "52.5" + new_line_393[67:] # Coluna 64
        lines.insert(392, new_line_393 + "\n")  # Insere abaixo da linha 392
        
        with open(file_path, 'w') as file:
            file.writelines(lines)
        
        messagebox.showinfo("Sucesso", "Linhas 80 e 393 modificadas com sucesso!")
    except Exception as e:
        messagebox.showerror("Erro", f"Ocorreu um erro: {e}")

def browse_file():
    file_path = filedialog.askopenfilename(filetypes=[("DAT files", "*.dat")])
    if file_path:
        modify_lines(file_path)

# Interface gráfica
root = tk.Tk()
root.withdraw()
browse_file()

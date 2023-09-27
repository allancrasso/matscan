import os
import openpyxl
import tkinter as tk
from tkinter import messagebox

def validar_ra(ra, arquivo_xlsx):
    script_dir = os.path.dirname(os.path.abspath(__file__))
    arquivo_xlsx_path = os.path.join(script_dir, arquivo_xlsx + ".xlsx")

    workbook = openpyxl.load_workbook(arquivo_xlsx_path)
    sheet = workbook.active

    for row in sheet.iter_rows(values_only=True):
        if row[0] == ra:
            workbook.close()
            return True

    workbook.close()
    return False

def verificar_ra():
    ra = ra_entry.get().strip()  # Remove espaços em branco do início e do final
    ra_entry.delete(0, tk.END)   # Limpa a entrada
    if ra.lower() == "exit":
        root.quit()
    elif validar_ra(ra, arquivo_xlsx):
        messagebox.showinfo("Resultado", "RA validado com sucesso!")
    else:
        messagebox.showerror("Resultado", "RA inválido!")

def ativar_verificacao_automatica():
    ra = ra_entry.get().strip()  # Remove espaços em branco do início e do final
    if ra:  # Verifica se o campo não está vazio
        verificar_ra()  # Chama a função verificar_ra() se o campo não estiver vazio
    root.after(500, ativar_verificacao_automatica)  # Agenda a próxima chamada após 0,5 segundos

# Nome do arquivo XLSX com os RAs válidos (sem a extensão)
arquivo_xlsx = "Ras"

# Cria a janela principal
root = tk.Tk()
root.title("Validação de RA")

# Rótulo e entrada para digitar o RA
ra_label = tk.Label(root, text="Digite o RA ou 'exit' para sair:")
ra_label.pack()
ra_entry = tk.Entry(root)
ra_entry.pack()

# Botão para verificar o RA
verificar_button = tk.Button(root, text="Verificar", command=verificar_ra)
verificar_button.pack()

# Ativar verificação automática após 0,5 segundos
root.after(500, ativar_verificacao_automatica)

root.mainloop()





import os
import openpyxl


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


arquivo_xlsx = "Ras"


while True:
   
    ra = input("Digite o RA ou 'exit' para sair: ")

    if ra.lower() == "exit":
        break  

    
    if validar_ra(ra, arquivo_xlsx):
        print("RA validado com sucesso!")
    else:
        print("RA inválido!")


import openpyxl
import pygame
import datetime
import win32com.client as win32

# Carregue o arquivo Excel
workbook = openpyxl.load_workbook('alunos.xlsx')
sheet = workbook.active  # Ou selecione a planilha desejada

# Defina a lista de alunos
alunos = []

# Itere pelas linhas a partir da segunda linha (min_row=2)
for row in sheet.iter_rows(min_row=2, values_only=True):
    qr = row
    alunos.append((qr))

# Função para procurar uma informação na lista de alunos
def procurar_informacao(informacao_procurada):
    linhas_com_informacao = []

    for row_num, (qr) in enumerate(alunos, start=2):
        if informacao_procurada.upper() in str(qr).upper():
            
            linhas_com_informacao.append(row_num)

    # Verifique se há linhas encontradas
    if linhas_com_informacao:
        linha_validada = linhas_com_informacao[0]
        print("Linha com a informação procurada:", linha_validada)
        
        # Acesse o emailResp na linha validada
        email_resp = alunos[linha_validada - 2][4]
        nome_aluno = alunos[linha_validada - 2][1]
        classe_aluno = alunos[linha_validada - 2][0]
        ra_aluno = alunos[linha_validada - 2][2]


        def tocar_musica():
            # Inicialize o mixer de áudio (necessário antes de reproduzir som)
            pygame.mixer.init()

            # Carregue o arquivo de áudio
            pygame.mixer.music.load("C:\\Users\\ENZOVITORIANOPUTTINI\\Desktop\\Projeto_TCC\\sounds\\aprovado.mp3")

            # Reproduza o som
            pygame.mixer.music.play()

            # Mantenha o programa em execução até que o som termine de tocar    
            pygame.time.wait(5000)# Aguarde 3 segundos (ou o tempo que desejar)

            def enviar_email():
                agora = datetime.datetime.now()

                # Acesso a diferentes partes da data e hora
                ano = agora.year
                mes = agora.month
                dia = agora.day
                hora = agora.strftime("%H:%M:%S")



                # criar a integração com o outlook
                outlook = win32.Dispatch('outlook.application')

                # criar um email
                email = outlook.CreateItem(0)


                # configurar as informações do seu e-mail
                email.To = F"{email_resp}"
                email.Subject = "Entrada do Aluno Autorizada"
                email.HTMLBody = f"""
                <p>Olá, um aluno(a) com o seu email cadastrado teve a entrada autorizada pelo nosso sistema de validação!</p>
                <p> </p>
                <p> </p>

                <p>O aluno: {nome_aluno}.</p>
                <p>Da sala: {classe_aluno}</p>
                <p>Portador do RA: {ra_aluno}.</p>
                <p>Teve a sua entrada autorizada as {hora} do dia {dia}/{mes}/{ano}.</p>

                
                <p> </p>
                <p> </p>
                <p>Lembre-se, esse email foi gerado de forma automatica, favor não responder!</p>
                """

                email.Send()
                print("Email Enviado")

            enviar_email()
        
        print("Valor do emailResp na linha", linha_validada, ":", email_resp)

        tocar_musica()
        

    else:
        print("Nenhuma linha com a informação procurada foi encontrada")

         # Inicialize o mixer de áudio (necessário antes de reproduzir som)
        pygame.mixer.init()

        # Carregue o arquivo de áudio
        pygame.mixer.music.load("C:\\Users\\ENZOVITORIANOPUTTINI\\Desktop\\Projeto_TCC\\sounds\\reprovado.mp3")

        # Reproduza o som
        pygame.mixer.music.play()

        # Mantenha o programa em execução até que o som termine de tocar
        pygame.time.wait(3000)# Aguarde 3 segundos (ou o tempo que desejar)

# Solicite a informação ao usuário
informacao_procurada = input("Digite a informação que você está procurando: ")

# Procure a informação na lista de alunos
procurar_informacao(informacao_procurada)

# Feche o arquivo do Excel
workbook.close()

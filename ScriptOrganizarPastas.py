import os
from tkinter.filedialog import askdirectory

caminho = askdirectory(title="Selecione uma pasta")

lista_arquivos = os.listdir(caminho)

locais = {
    "Imagens":[".png",".jpg",],
    "Planilhas":[".csv",".xlsx",".xlsm"],
    "Aplicativos":[".exe"],
    "Documentos":[".pdf",".docx"],
    "Videos":[".mp4",".braw"],
    "Python":[".py"],
    "Winrar":[".rar",".zip"]
}

for arquivo in lista_arquivos:
    #01 . Arquivo.pdf
   
    nome, extensao = os.path.splitext(arquivo)
    for pasta in locais:
        if extensao in locais[pasta]:
            if not os.path.exists(f"{caminho}/{pasta}"):
                os.mkdir(f"{caminho}/{pasta}")
            os.rename(f"{caminho}/{arquivo}", f"{caminho}/{pasta}/{arquivo}")
            
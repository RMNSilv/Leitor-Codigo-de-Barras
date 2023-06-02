#Instalcao das bibliotecas que serao usadas ao longo do programa


!pip install pyzbar #Biblioteca para leitura de Codigo de barras
!pip install pdf2image #Biblioteca para converter PDF para imagem
!pip install poppler #Biblioteca para renderizar e manipular PDF


#Importacao das funcoes a serem utilizadas

from pyzbar.pyzbar import decode #funcao que decodifica e ler codigo de barras
from pdf2image import convert_from_path #Funcao que obtera PDF a partir de um caminho para depois converter em imagem
import os #Funcao para manipular arquivos
import numpy as np

#Comando para listar arquivos em um diretorio, neste caso, sera apenas PDF
pdfs = [i for i in os.listdir() if ".pdf" in i]

pdf_path = pdfs[0]

#Funcao criada para leitura do codigo de barras

def leitura_codbar(pdf_path):
    #A funcao convert_from_path busca os arquivos PDFs no caminho informado (pdf_path) 
    #e converte em imagem e tras uma lista de arquivos em imagem
    pages = convert_from_path(pdf_path)

    #Atribuicao da imagem anterior a uma variavel
    img = pages[0]


    #Decodificacao da imagem para se obter o codigo de barras
    deteccodbar = decode(img)
    deteccodbar

    #Condicional para verificar a presenca de codigo de barras
    #na decodificacao da imagem
    if not deteccodbar:
        return False
    else:

    
        for codbar in deteccodbar:
            codbar=deteccodbar[1] #utiliza-se somente o segundo codigo de barras da lista, pois primeiro eh do tipo QRCODE
            if codbar.data !="" and codbar.type =='I25': #Obtem somente o codigo de barras do tipo I25
                codbar_=codbar.data.decode('utf-8') #Decodificar para especificacao utf-8
                return codbar_          

leitura_codbar(pdf_path)

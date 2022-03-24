#Gerador de senhas
import random
import string
from tkinter import *
import os
opção=0
opção2=0
tamanho=0
name=''
senha=""

def Abrir_TXT():
    os.startfile("senhas11.txt")
def senha_gerador():
    name = Nome.get()
    tamanho=int(Tamanho1.get())
    print(name)
    print(tamanho)
    name=Nome.get()
    options = string.ascii_letters + string.digits
    maiuscula = "ABCDEFGHIJKMNOPQRSTUVWXYZ"
    Minuscula = "abcdefghijkmnopqrstuvwxyz"
    numero = string.digits
    caracteres_especiais="!@#$%&*"
    senha=""
    digit1 = random.choice(maiuscula)
    digit2 = random.choice(Minuscula)
    digit3 = random.choice(numero)
    digit4 = random.choice(caracteres_especiais)
    senha = digit1 + digit2 + digit3 + digit4
    for i in range(4,tamanho):
        digit5=random.choice(options)
        senha = senha + digit5
    print(senha)
    name_txt['text'] = name
    senha_gerada['text'] = senha
    return senha ,name
def Visualizar_senhas():
    with open('senhas11.txt', 'r') as arquivo:
       valor = arquivo.read()
       texto_senhas['text']=valor

def Salvar_senha( senha_gerada ,name_txt):
    name_txt=name_txt['text']
    senha_gerada=senha_gerada['text']
    with open('senhas11.txt', 'a') as arquivo:
        for valor in name_txt:
            arquivo.write(str(valor))
        arquivo.write("\n")
        for valor in senha_gerada:
            arquivo.write(str(valor))
        arquivo.write("\n")
    print("Senha salva")

def chamar_senha():
    Salvar_senha(senha_gerada, name_txt)
#INTERFACE GRAFICA

janela=Tk()
janela.configure(background="white")
janela.title("Gerador de senhas")
janela.geometry("500x300")

#img_background=PhotoImage(file="download (1).png")
#lab_fundo=label(janela,image=img_background)
#lab_fundo.pack()
janela.resizable(width=1,height=1)
texto_visualizar = Button(janela, text="GERENCIADOR DE SENHAS",bg="red")
texto_visualizar.grid(column=50, row=0, padx=1, pady=1)

botao_visualizarTXT=Button(janela, text="       AbrirTXT       ", command=Abrir_TXT)
botao_visualizarTXT.grid(column=50, row=1, padx=30, pady=1)

botao_visualizar=Button(janela, text="Visualizar Senhas", command=Visualizar_senhas)
botao_visualizar.grid(column=50, row=2, padx=10, pady=1)

texto_senhas=Label(janela, text="SENHAS")
texto_senhas.grid(column=50, row=3, padx=1, pady=1)

texto_gerar = Label(janela, text="         ")
texto_gerar.grid(column=10, row=0, padx=20, pady=20)

texto_gerar = Label(janela, text="         ")
texto_gerar.grid(column=0, row=0, padx=20, pady=20)

texto_gerar = Button(janela, text="     GERE A SENHA     ",bg="red")
texto_gerar.grid(column=0, row=0, padx=0, pady=0)

texto_plat = Label(janela, text="Insira a plataforma da senha")
texto_plat.grid(column=0, row=1, padx=0, pady=0)

Nome= Entry(janela)
Nome.place()
Nome.grid(column=0, row=2, padx=10, pady=1)


texto_Tamanho= Label(janela, text="insira o tamanho da senha")
texto_Tamanho.grid(column=0, row=3, padx=10, pady=1)

name_txt=Label(janela, text="Plataforma")
name_txt.grid(column=0, row=7, padx=0, pady=0)


senha_gerada=Label(janela, text="senha")
senha_gerada.grid(column=0, row=8, padx=0, pady=0)


Tamanho1= Entry(janela)
Tamanho1.place()
Tamanho1.grid(column=0, row=5, padx=10, pady=1)
criar=Button(janela, text="       Gerar Senha       ", bg="white",  command=senha_gerador)
criar.grid(column=0, row=6, padx=1, pady=5)

salvar_senha=Button(janela, text="Salvar Senha", bg="white", command=chamar_senha)
salvar_senha.grid(column=0, row=9, padx=10, pady=1)

janela.mainloop()

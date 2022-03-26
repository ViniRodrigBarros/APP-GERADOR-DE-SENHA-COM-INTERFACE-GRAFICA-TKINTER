#Gerador de senhas
import random
import string
from tkinter import *
from tkinter import scrolledtext
from tkinter.scrolledtext import ScrolledText
import os
opção=0
opção2=0
tamanho=0
name=''
senha=""

def Abrir_TXT():
    os.startfile("senhas11.txt")

def Visualizar_senhas():
    with open('senhas11.txt', 'r') as arquivo:
       valor = arquivo.read()
       texto_senhas['text']=valor



def abrir_janela_visualizar_senha():
    janela_S_Senha=Toplevel()
    janela_S_Senha.title('Visualizar senhas')
    janela_S_Senha.geometry("700x300")
    scrolltxt = scrolledtext.ScrolledText(janela_S_Senha)

    with open('senhas11.txt', 'r') as arquivo:
        valor = arquivo.read()
        texto_senhas['text'] = valor
    scrolltxt.insert('1.0',valor)

    scrolltxt.grid( )

    janela_S_Senha.mainloop()
def abrir_gerar_senha():
    def Salvar_senha(senha_gerada, name_txt):
        name_txt = name_txt['text']
        senha_gerada = senha_gerada['text']
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
    def senha_gerador():

        name = Nome.get()
        tamanho = int(Tamanho1.get())
        print(name)
        print(tamanho)
        name = Nome.get()
        options = string.ascii_letters + string.digits
        maiuscula = "ABCDEFGHIJKMNOPQRSTUVWXYZ"
        Minuscula = "abcdefghijkmnopqrstuvwxyz"
        numero = string.digits
        caracteres_especiais = "!@#$%&*"
        senha = ""
        digit1 = random.choice(maiuscula)
        digit2 = random.choice(Minuscula)
        digit3 = random.choice(numero)
        digit4 = random.choice(caracteres_especiais)
        senha = digit1 + digit2 + digit3 + digit4
        for i in range(4, tamanho):
            digit5 = random.choice(options)
            senha = senha + digit5
        print(senha)
        name_txt['text'] = name
        senha_gerada['text'] = senha
        return senha, name
    #JANELA 2
    janela_gerar=Toplevel()
    janela_gerar.title('  GERAR SENHA  ')
    janela_gerar.geometry("170x270")
    texto_gerar = Button(janela_gerar, text="     GERE A SENHA     ", bg="red")
    texto_gerar.grid(column=0, row=0, padx=10, pady=10)

    texto_plat = Label(janela_gerar, text="Insira a plataforma da senha")
    texto_plat.grid(column=0, row=1, padx=0, pady=0)

    Nome = Entry(janela_gerar)
    Nome.place()
    Nome.grid(column=0, row=2, padx=10, pady=1)

    texto_Tamanho = Label(janela_gerar, text="insira o tamanho da senha")
    texto_Tamanho.grid(column=0, row=3, padx=10, pady=1)

    Tamanho1 = Entry(janela_gerar)
    Tamanho1.place()
    Tamanho1.grid(column=0, row=4, padx=10, pady=1)
    criar = Button(janela_gerar, text="       Gerar Senha       ", bg="white", command=senha_gerador)
    criar.grid(column=0, row=5, padx=1, pady=5)
    name_txt=Label(janela_gerar, text="Plataforma")
    name_txt.grid(column=0, row=6, padx=0, pady=0)
    senha_gerada = Label(janela_gerar, text="senha")
    senha_gerada.grid(column=0, row=7, padx=0, pady=0)

    salvar_senha = Button(janela_gerar, text="Salvar Senha", bg="white", command=chamar_senha)
    salvar_senha.grid(column=0, row=8, padx=10, pady=1)


#INTERFACE GRAFICA

janela=Tk()
janela.configure(background="white")
janela.title("GDS")
janela.geometry("150x150")

#img_background=PhotoImage(file="download (1).png")
#lab_fundo=label(janela,image=img_background)
#lab_fundo.pack()

#JANELA 1
janela.resizable(width=1,height=1)
texto_visualizar = Button(janela, text="GERADOR DE SENHAS",bg="red")
texto_visualizar.grid(column=0, row=0, padx=12, pady=10)

botao_visualizarTXT=Button(janela, text="       Abrir TXT       ", command=Abrir_TXT)
botao_visualizarTXT.grid(column=0, row=2, padx=0, pady=0)

botao_visualizar=Button(janela, text="Visualizar Senhas", command=abrir_janela_visualizar_senha)
botao_visualizar.grid(column=0, row=3, padx=0, pady=0)

botao_visualizar=Button(janela, text="    Gerar Senha    ", command=abrir_gerar_senha)
botao_visualizar.grid(column=0, row=4, padx=0, pady=0)


texto_senhas=Label(janela, text="SENHAS")


texto_gerar = Label(janela, text="         ")
texto_gerar.grid(column=1, row=0, padx=20, pady=20)


janela.mainloop()

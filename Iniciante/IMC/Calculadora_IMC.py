from tkinter import *


def calcular():
    try:
        peso = float(e_peso.get().replace(',', '.'))
        altura = float(e_altura.get().replace(',', '.'))
    except ValueError:
        l_resultado_texto['text'] = 'Digite valores válidos!'
    else:
        imc = peso / altura ** 2

        if imc < 18.5:
            l_resultado_texto['text'] = 'Seu IMC: Abaixo do peso'
        elif 18.5 <= imc < 25:
            l_resultado_texto['text'] = 'Seu IMC: Peso normal'
        elif 25 <= imc < 30:
            l_resultado_texto['text'] = 'Seu IMC: Sobrepeso'
        else:
            l_resultado_texto['text'] = 'Seu IMC: Obesidade'

        l_resultado['text'] = f'{imc:.1f}'.replace('.', ',')


# cores
cor0 = '#FFFFFF' # branco
cor1 = '#1C1C1C' # cinza
cor2 = '#0078d4' # azul

# ----TELA----
janela = Tk()
janela.title('IMC')
janela.geometry('300x180')
janela.configure(bg=cor2)
janela.resizable(width=False, height=False)

# ----DIVIDIR JANELA----
frame_topo = Frame(janela, width=300, height=40, bg=cor0, relief='flat', padx=10, pady=10)
frame_topo.grid(row=0, column=0, padx=0, pady=0, sticky='nw')
frame_baixo = Frame(janela, width=300, height=140, bg=cor0, relief='flat', padx=10, pady=5)
frame_baixo.grid(row=1, column=0, padx=0, pady=10, sticky='NSWE')

# ----TOPO----
l_nome = Label(text='Calculadora de IMC', relief='flat', width=26, height=1, bg=cor0, font='Arial 15')
l_nome.place(x=0, y=2)

# ----BAIXO----
l_peso = Label(frame_baixo, text='Insira seu peso', bg=cor0, width=11, height=2, font='Ivy 10')
l_peso.grid(row=1, column=1, columnspan=1, padx=5, pady=0, sticky='N')
e_peso = Entry(frame_baixo, width=7, justify='center', relief='solid')
e_peso.grid(row=1, column=2, columnspan=1, rowspan=1, padx=5, pady=0)

l_altura = Label(frame_baixo, text='Insira sua altura', bg=cor0, width=11, height=2, font='Ivy 10')
l_altura.grid(row=2, column=1, columnspan=1, padx=5, pady=0, sticky='N', rowspan=1)
e_altura = Entry(frame_baixo, width=7, justify='center', relief='solid')
e_altura.grid(row=2, column=2, columnspan=1, rowspan=1, padx=5, pady=0)

l_resultado = Label(frame_baixo, width=5, height=0, bg=cor2, anchor='center', padx=0, pady=1, text='0.0',
                    font='Ivy 15 bold', relief='flat')
l_resultado.grid(row=1, column=3, rowspan=2, columnspan=1, sticky='NSWE', padx=10, pady=1)

l_resultado_texto = Label(frame_baixo, font='Ivy 10 bold', text='', padx=0, pady=0, bg=cor0, anchor='center',
                          width=20, height=0, fg=cor2)
l_resultado_texto.grid(row=3, column=1, columnspan=3, sticky='n')

botao = Button(frame_baixo, command=calcular, text='Calcular', width=39, bg=cor2, fg=cor0, font='Ivy 9 bold')
botao.grid(row=4, column=1, columnspan=3, sticky='n', padx=0, pady=0)

janela.mainloop()

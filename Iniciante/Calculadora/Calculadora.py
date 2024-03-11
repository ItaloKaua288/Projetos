from tkinter import *

todos_os_valores = ''


def adicionar(num):
    global todos_os_valores
    if l_resultado['text'] == '|':
        l_resultado['text'] = ''
    if num != '%':
        todos_os_valores += num
        l_resultado['text'] = todos_os_valores
    else:
        l_resultado['text'] += '%'
        todos_os_valores += '/100'


def calcular():
    global todos_os_valores
    resultado1 = f'{eval(todos_os_valores)}'
    l_resultado['text'] = str(resultado1[:9])
    todos_os_valores = l_resultado['text']


def limpar():
    global todos_os_valores
    l_resultado['text'] = ''
    todos_os_valores = ''


# ---cores---
cor0 = '#eceff1'  # branco
cor1 = '#38576b'  # azul
cor2 = '#ffab40'  # laranja
cor3 = '#000000'  # preto

# ---janela---
janela = Tk()
janela.title('Calculadora')
janela.geometry('227x350')
janela.resizable(width=False, height=False)
janela.configure(bg=cor3)

# ---divisão de tela---
frame_topo = Frame(janela, width=221, height=50, bg=cor1)
frame_topo.grid(row=0, column=0, padx=2, pady=0, sticky='NSWE')
frame_baixo = Frame(janela, width=220, height=300, bg='#000000', pady=1, padx=1)
frame_baixo.grid(row=1, column=0)

# ---resultado/calculo---

# ---botões---
button_c = Button(frame_baixo, text='C', width=8, height=1, relief='flat', font='Ivi 13 bold', command=limpar)
button_c.grid(row=1, column=1, columnspan=2, padx=1, pady=1, sticky='NSWE')

button_porcent = Button(frame_baixo, text='%', width=3, height=2, relief='flat', font='Ivi 13 bold',
                        command=lambda m='%': adicionar(m))
button_porcent.grid(row=1, column=3, columnspan=1, padx=1, pady=1, sticky='NSWE')

button_divisao = Button(frame_baixo, text='/', width=3, height=2, relief='flat', bg=cor2, font='Ivi 13 bold',
                        command=lambda m='/': adicionar(m))
button_divisao.grid(row=1, column=4, columnspan=1, padx=1, pady=1, sticky='NSWE')

button_7 = Button(frame_baixo, text='7', width=3, height=2, relief='flat', font='Ivi 13 bold',
                  command=lambda m='7': adicionar(m))
button_7.grid(row=2, column=1, padx=1, pady=1, sticky='NSWE')

button_8 = Button(frame_baixo, text='8', width=3, height=2, relief='flat', font='Ivi 13 bold',
                  command=lambda m='8': adicionar(m))
button_8.grid(row=2, column=2, padx=1, pady=1, sticky='NSWE')

button_9 = Button(frame_baixo, text='9', width=3, height=2, relief='flat', font='Ivi 13 bold',
                  command=lambda m='9': adicionar(m))
button_9.grid(row=2, column=3, padx=1, pady=1, sticky='NSWE')

button_mult = Button(frame_baixo, text='x', width=3, height=2, relief='flat', bg=cor2, font='Ivi 13 bold',
                     command=lambda m='*': adicionar(m))
button_mult.grid(row=2, column=4, padx=1, pady=1, sticky='NSWE')

button_4 = Button(frame_baixo, text='4', width=3, height=2, relief='flat', font='Ivi 13 bold',
                  command=lambda m='4': adicionar(m))
button_4.grid(row=3, column=1, padx=1, pady=1, sticky='NSWE')

button_5 = Button(frame_baixo, text='5', width=3, height=2, relief='flat', font='Ivi 13 bold',
                  command=lambda m='5': adicionar(m))
button_5.grid(row=3, column=2, padx=1, pady=1, sticky='NSWE')

button_6 = Button(frame_baixo, text='6', width=3, height=2, relief='flat', font='Ivi 13 bold',
                  command=lambda m='6': adicionar(m))
button_6.grid(row=3, column=3, padx=1, pady=1, sticky='NSWE')

button_sub = Button(frame_baixo, text='-', width=3, height=2, relief='flat', bg=cor2, font='Ivi 13 bold',
                    command=lambda m='-': adicionar(m))
button_sub.grid(row=3, column=4, padx=1, pady=1, sticky='NSWE')

button_1 = Button(frame_baixo, text='1', width=3, height=2, relief='flat', font='Ivi 13 bold',
                  command=lambda m='1': adicionar(m))
button_1.grid(row=4, column=1, padx=1, pady=1, sticky='NSWE')

button_2 = Button(frame_baixo, text='2', width=3, height=2, relief='flat', font='Ivi 13 bold',
                  command=lambda m='2': adicionar(m))
button_2.grid(row=4, column=2, padx=1, pady=1, sticky='NSWE')

button_3 = Button(frame_baixo, text='3', width=3, height=2, relief='flat', font='Ivi 13 bold',
                  command=lambda m='3': adicionar(m))
button_3.grid(row=4, column=3, padx=1, pady=1, sticky='NSWE')

button_adi = Button(frame_baixo, text='+', width=3, height=2, relief='flat', bg=cor2, font='Ivi 13 bold',
                    command=lambda m='+': adicionar(m))
button_adi.grid(row=4, column=4, padx=1, pady=1, sticky='NSWE')

button_0 = Button(frame_baixo, text='0', width=8, height=1, relief='flat', font='Ivi 13 bold',
                  command=lambda m='0': adicionar(m))
button_0.grid(row=5, column=1, columnspan=2, padx=1, pady=1, sticky='NSWE')

button_ponto = Button(frame_baixo, text='.', width=3, height=2, relief='flat', font='Ivi 14 bold',
                      command=lambda m='.': adicionar(m))
button_ponto.grid(row=5, column=3, columnspan=1, padx=1, pady=1, sticky='NSWE')

button_igual = Button(frame_baixo, text='=', width=3, height=2, relief='flat', bg=cor2, font='Ivi 13 bold',
                      command=calcular)
button_igual.grid(row=5, column=4, columnspan=1, padx=1, pady=1, sticky='NSWE')

l_barra = Label(frame_baixo, width=31, height=1, bg=cor1, relief='flat')
l_barra.grid(row=6, column=1, columnspan=4, pady=1, padx=1)

# --Frame topo---
l_resultado = Label(frame_topo, bg=cor1, relief='flat', text='|', font='Ivi 17', anchor='e', fg=cor0)
l_resultado.place(x=15, y=6, width=200, height=40)

janela.mainloop()

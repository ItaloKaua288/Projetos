from datetime import datetime
from tkinter import Tk, Frame, Label, Button, ttk
from tkcalendar import DateEntry
from dateutil.relativedelta import relativedelta


def calcular():
    atual = datetime.today().date()
    data_convertida = datetime(int(e_nascimento.get().split("/")[2]), int(e_nascimento.get().split('/')[1]),
                               int(e_nascimento.get().split('/')[0]))
    l_ano['text'] = relativedelta(atual, data_convertida).years
    l_mes['text'] = relativedelta(atual, data_convertida).months
    l_dias['text'] = relativedelta(atual, data_convertida).days


# ---CORES---
cor0 = '#424242'  # cinza
cor1 = '#303030'  # cinza escuro
cor2 = '#DFB025'  # dourado
cor3 = '#FFFFFF'  # branco

# ---Janela---
janela = Tk()
janela.geometry('250x300')
janela.resizable(width=False, height=False)
janela.title('Calculadora de Idade')

# ---DIVIDIR JANELA---
frame_topo = Frame(janela, bg=cor1, width=250, height=100)
frame_topo.grid(row=0, column=0, padx=0, pady=0, sticky='NSWE')
frame_baixo = Frame(janela, bg=cor0, width=250, height=200)
frame_baixo.grid(row=1, column=0, padx=0, pady=0, sticky='NSWE')

# ---TITULO---
l_nome = Label(frame_topo, bg=cor1, width=12, height=1, text='CALCULADORA', font='Ivy 12 bold', fg=cor3)
l_nome.place(x=60, y=20)
l_nome = Label(frame_topo, bg=cor1, width=10, height=1, text='DE IDADE', font='Arial 25 bold', fg=cor2)
l_nome.place(x=22, y=50)

# ---Labels de baixo---
l_nascimento = Label(frame_baixo, bg=cor0, fg=cor3, text='Data de nascimento', width=15, height=5, font='Ivy 10')
l_nascimento.place(x=15, y=0)
e_nascimento = DateEntry(frame_baixo, background='darkblue', foreground='white', date_pattern='mm/dd/y', borderwidth=2)
e_nascimento.place(x=140, y=32, width=80, height=20)

l_ano = Label(frame_baixo, bg=cor0, fg=cor3, text='0', width=4, height=1, font='Arial 25')
l_ano.place(x=24, y=90)
l_ano_texto = Label(frame_baixo, bg=cor0, fg=cor3, text='anos', width=4, height=1, font='Arial 10')
l_ano_texto.place(x=45, y=130)

l_mes = Label(frame_baixo, bg=cor0, fg=cor3, text='0', width=4, height=1, font='Arial 25')
l_mes.place(x=84, y=90)
l_mes_texto = Label(frame_baixo, bg=cor0, fg=cor3, text='meses', width=4, height=1, font='Arial 10')
l_mes_texto.place(x=104, y=130)

l_dias = Label(frame_baixo, bg=cor0, fg=cor3, text='0', width=4, height=1, font='Arial 25')
l_dias.place(x=144, y=90)
l_dias_texto = Label(frame_baixo, bg=cor0, fg=cor3, text='dias', width=4, height=1, font='Arial 10')
l_dias_texto.place(x=164, y=130)

b_botao = Button(frame_baixo, text='Calcular Idade', bg=cor0, fg=cor3, relief='raised', command=calcular)
b_botao.place(x=80, y=165)

janela.mainloop()

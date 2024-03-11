from tkinter import Frame, Label, Tk, Button
from PIL import Image, ImageTk


def botoes(des=False):
    """
        Função que cria e destroi os botões
    :param des: True para destruir e reiniciar e False para apenas criar os botões
    """
    global img_0
    global img_1
    global img_2
    global b_0
    global b_1
    global b_2
    global b_3
    b_3.destroy()
    if not des:
        img_0 = Image.open('imagens/pedra.png')
        img_0 = img_0.resize((50, 50), Image.LANCZOS)
        img_0 = ImageTk.PhotoImage(img_0)
        b_0 = Button(frame_baixo, width=60, height=65, image=img_0, bg=cor1, command=lambda m='Pedra': jogo(m))
        b_0.place(x=15, y=60)

        img_1 = Image.open('imagens/papel.png')
        img_1 = img_1.resize((50, 50), Image.LANCZOS)
        img_1 = ImageTk.PhotoImage(img_1)
        b_1 = Button(frame_baixo, width=60, height=65, image=img_1, bg=cor1, command=lambda m='Papel': jogo(m))
        b_1.place(x=95, y=60)

        img_2 = Image.open('imagens/tesoura.png')
        img_2 = img_2.resize((50, 50), Image.LANCZOS)
        img_2 = ImageTk.PhotoImage(img_2)
        b_2 = Button(frame_baixo, width=60, height=65, image=img_2, bg=cor1, command=lambda m='Tesoura': jogo(m))
        b_2.place(x=175, y=60)
    else:
        b_0.destroy()
        b_1.destroy()
        b_2.destroy()
        b_3 = Button(frame_baixo, text='Jogar', bg=cor1, fg=cor0, font='Ivy 15 bold', width=18, command=iniciar)
        b_3.place(x=15, y=140, height=30)


def iniciar():
    """
        Inicia o jogo e limpa o placar
    """
    l_jogador['text'] = '0'
    l_pc['text'] = '0'
    l_resultado_text['text'] = ''
    botoes()


def jogo(i):
    """
        Função que faz todo o calculo do jogo
    :param i: A escolha do jogador
    """
    from random import choice
    escolhas = ['Pedra', 'Papel', 'Tesoura']
    pc = choice(escolhas)
    l_pc_esc['text'] = pc
    if i == 'Pedra' and pc == 'Tesoura':
        l_jogador['text'] = int(l_jogador['text']) + 10
    elif i == 'Pedra' and pc == 'Papel':
        l_pc['text'] = int(l_pc['text']) + 10
    elif i == 'Papel' and pc == 'Pedra':
        l_jogador['text'] = int(l_jogador['text']) + 10
    elif i == 'Papel' and pc == 'Tesoura':
        l_pc['text'] = int(l_pc['text']) + 10
    elif i == 'Tesoura' and pc == 'Pedra':
        l_pc['text'] = int(l_pc['text']) + 10
    else:
        l_jogador['text'] = int(l_jogador['text']) + 10
    if l_jogador['text'] == 30:
        l_resultado_text['text'] = 'Você venceu!'
        l_resultado_text['fg'] = cor4
        botoes(des=True)
    elif l_pc['text'] == 30:
        l_resultado_text['text'] = 'Pc venceu!'
        l_resultado_text['fg'] = cor5
        botoes(des=True)


# cores
cor0 = "#FFFFFF"  # white / branca
cor1 = "#333333"  # black / preta
cor2 = "#fcc058"  # orange / laranja
cor4 = "#34eb3d"   # green / verde
cor5 = "#e85151"   # red / vermelha
cor6 = '#1C1C1C'

janela = Tk()
janela.title('Jokenpô')
janela.geometry('260x280')
janela.resizable(width=False, height=False)
janela.configure(bg=cor0)

# divisão
frame_cima = Frame(janela, width=250, height=90, bg=cor6)
frame_cima.grid(row=0, padx=5)
frame_meio = Frame(janela, width=260, height=5, bg=cor2)
frame_meio.grid(row=1)
frame_baixo = Frame(janela, width=260, height=185, bg=cor1)
frame_baixo.grid(row=2)

# botões

b_3 = Button(frame_baixo, text='Jogar', bg=cor1, fg=cor0, font='Ivy 15 bold', width=18, command=iniciar)
b_3.place(x=15, y=140, height=30)

l_pc_esc = Label(frame_baixo, width=1, height=1, bg=cor1, fg=cor0, text='', font='Ivy 13 bold')
l_pc_esc.place(x=180, y=10, width=60)

l_resultado_text = Label(frame_baixo, width=1, height=1, bg=cor1, fg=cor0, font='Arial 13', text='')
l_resultado_text.place(x=15, y=10, width=100)

# placar
l_jogador = Label(frame_cima, width=1, height=1, text='0', font='Arial 40 bold', bg=cor6, fg=cor0)
l_jogador.place(x=30, y=15, height=50, width=60)
l_jogador_nome = Label(frame_cima, width=1, height=1, text='Você', font='Arial 10 bold', bg=cor6, fg=cor0)
l_jogador_nome.place(x=40, y=60, height=15, width=35)

l_pc = Label(frame_cima, width=1, height=1, text='0', font='Arial 40 bold', bg=cor6, fg=cor0)
l_pc.place(x=160, y=15, height=50, width=60)
l_pc_nome = Label(frame_cima, width=1, height=1, text='Pc', font='Arial 10 bold', bg=cor6, fg=cor0)
l_pc_nome.place(x=180, y=60, height=15, width=20)

l_div = Label(frame_cima, width=1, height=1, text=':', font='Arial 40 bold', bg=cor6, fg=cor0)
l_div.place(x=95, y=10, height=50, width=60)

janela.mainloop()

from tkinter import Tk, Label, Frame, Button, Entry, ttk
import sqlite3 as sq

banco = sq.connect('dados.db')
try:
    with banco:
        cursor = banco.cursor()
        cursor.execute('CREATE TABLE Tarefas (id INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT)')
except:
    pass

def destroy():
    try:
        e_tarefa.destroy()
        b_adicionar.destroy()
        b_remover2.destroy()
        b_atualizar2.destroy()
        e_atualizar.destroy()
    except:    
        pass

def inserir_tarefa(i):
    with banco:
        cursor = banco.cursor()
        query = 'INSERT INTO Tarefas (nome) VALUES (?)'
        cursor.execute(query, i)
    mostrar()

def remover_tarefa(i):
    with banco:
        cursor = banco.cursor()
        query = 'DELETE FROM Tarefas WHERE id=?'
        cursor.execute(query, i)
    mostrar()

def atualizar_tarefa(i):
    with banco:
        cursor = banco.cursor()
        query = 'UPDATE Tarefas SET nome=? WHERE id=?'
        cursor.execute(query, i)
    mostrar()

def novo():
    def adicionar():
        inserir_tarefa([e_tarefa.get().strip()])
        
    global b_adicionar, e_tarefa
    l_legenda['text'] = 'Insira uma nova tarefa'
    destroy()

    e_tarefa = Entry(f_baixo, justify='center', font='Arial 15', relief='solid')
    e_tarefa.place(x=1, y=137, width=287)

    b_adicionar = Button(f_baixo, text='ADICIONAR', font='Ivy 10 bold', bg=co1, fg=co2, command=adicionar, activebackground=co1)
    b_adicionar.place(x=1, y=164, width=287)  

def remover():
    def remove():
        global tree
        tree_dados = tree.focus()
        tree_dicionario = tree.item(tree_dados)
        tree_lista = tree_dicionario['values']
        valor = tree_lista[0]
        remover_tarefa([valor])
    
    global b_remover2
    destroy()

    l_legenda['text'] = 'Selecione a tarefa que será removida'

    b_remover2 = Button(f_baixo, text='REMOVER', font='Ivy 10 bold', bg=co1, fg=co2, command=remove, activebackground=co1)
    b_remover2.place(x=1, y=164, width=287) 

def atualizar():
    def atualize():
        global tree
        tree_dados = tree.focus()
        tree_dicionario = tree.item(tree_dados)
        tree_lista = tree_dicionario['values']
        valor = tree_lista[0]
        atualizar_tarefa([e_atualizar.get().strip(), valor])
    
    global e_atualizar, b_atualizar2
    destroy()

    l_legenda['text'] = 'Selecione a tarefa que será atualizada'

    e_atualizar = Entry(f_baixo, justify='center', font='Arial 15', relief='solid')
    e_atualizar.place(x=1, y=137, width=287)

    b_atualizar2 = Button(f_baixo, text='ATUALIZAR', font='Ivy 10 bold', bg=co1, fg=co2, command=atualize, activebackground=co1)
    b_atualizar2.place(x=1, y=164, width=287)

def mostrar():
    def ver_dados():
        lista = []
        with banco:
            cursor = banco.cursor()
            cursor.execute('SELECT * FROM Tarefas')
            rows = cursor.fetchall()
            for row in rows:
                lista.append(row)
        return lista
    
    tarefas = ['id', 'Tarefas']
    lista = ver_dados()
    global tree

    tree = ttk.Treeview(f_direira, columns=tarefas, show='')
    vsb = ttk.Scrollbar(f_direira, orient='vertical', command=tree.yview)
    hsb = ttk.Scrollbar(f_direira, orient='horizontal', command=tree.xview)

    tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set, height=8)
    tree.grid(row=1, column=0, rowspan=1, sticky='nswe')
    vsb.grid(row=1, column=1, sticky='ns')
    hsb.grid(row=2, column=0, sticky='we')

    tree.column(0, width=10, anchor='center')
    f_direira.grid_rowconfigure(0, weight=1)
    
    h = [1, 190]
    n = 0
    for col in tarefas:
        tree.column(col, width=h[n], anchor='nw')
        n += 1

    for item in lista:
        tree.insert('', 'end', values=item)

# cores
co0 = "#000000"  # preta
co1 = "#59656F"  # cinza escuro
co2 = "#feffff"  # branca
co3 = "#0074eb"  # azul
co4 = "#f04141"  # vermelho
co5 = "#59b356"  # verde
co6 = "#cdd1cd"  # cinza claro

# janela
janela = Tk()
janela.title('Lista de Tarefas')
janela.geometry('500x225')
janela.resizable(width=False, height=False)
janela.configure(bg=co2)

f_cima = Frame(janela, width=290, height=1, bg=co0)
f_cima.grid(row=0, column=0, sticky='n')
f_baixo = Frame(janela, width=290, height=192)
f_baixo.grid(row=1, column=0)
f_direira = Frame(janela, width=210, height=225, bg=co2)
f_direira.grid(row=0, column=1, rowspan=2)

# frame cima
b_novo = Button(f_cima, text='NOVO', font='Ivy 12 bold', bg=co3, fg=co2, width=8, command=novo, activebackground=co3)
b_novo.grid(row=0, column=0)

b_remover = Button(f_cima, text='REMOVER', font='Ivy 12 bold', bg=co4, fg=co2, width=9, command=remover, activebackground=co4)
b_remover.grid(row=0, column=1)

b_atualizar = Button(f_cima, text='ATUALIZAR', font='Ivy 12 bold', bg=co5, fg=co2, width=9, command=atualizar, activebackground=co5)
b_atualizar.grid(row=0, column=2)

# frame baixo

l_legenda = Label(f_baixo, text='Escolha uma das opções acima', font='Arial 10', width=35, height=7)
l_legenda.place(x=0, y=10)

# frame direita
l_titulo = Label(f_direira, text='Tarefas', font='Arial 15', bg=co2, height=1)
l_titulo.grid(row=0, column=0, sticky='NSWE')

mostrar()

janela.mainloop()

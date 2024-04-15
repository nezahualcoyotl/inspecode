import string
import tkinter as tk
from lib2to3.pgen2.token import STRING
from tkinter import *
from distutils.cmd import Command
from tkinter import COMMAND, messagebox, ttk
from turtle import bgcolor
#ventana = Tk()
#ventana.title("Calculadora")

#e_texto = Entry(ventana, font=("Calibri 20"))
#e_texto.grid(row = 0, column = 0, columnspan =4, padx = 50, pady = 5)

'''def show_selection():
     #Obtener la opción seleccionada.
    selection = combo.get()
    messagebox.showinfo(
       message=f"La opción seleccionada es: {selection}",
        title="Selección"
    )
    txt1.delete(0,'end')
    txt2.delete(0,'end')'''

'''def fnCompara(event):
    BOARD = combo.get()
    WIRING = txt1.get()
    USB = txt2.get()
    txt1.delete(0,'end')
    txt2.delete(0,'end')
    if BOARD == 'P88390DW010':
        if WIRING == 'VTSMXP88572DW010':
            messagebox.showinfo(
            message=f"La opción seleccionada es: {BOARD}, {WIRING}",
            title="Selección"
            )
        else:
            messagebox.showinfo(
                message=f"La combinacion no es correcta, favor de verificar",
                title="Selección"   
                )
    elif BOARD == 'P88490DW000':
        if WIRING == 'VTSMXP88572DW000':
            if USB == '96125-P1610WK':
                messagebox.showinfo(
                message=f"La opción seleccionada es: {BOARD}, {WIRING}",
                title="Selección"
                )
            else:
                messagebox.showinfo(
                message=f"La combinacion no es correcta, favor de verificar",
                title="Selección"   
            )
        else:
            messagebox.showinfo(
            message=f"La combinacion no es correcta, favor de verificar",
            title="Selección"   
            )
    elif BOARD == 'P88490DW010':
        if WIRING == 'VTSMXP88572DW010':
            if USB == '96125-P1610WK':
                msgOk = ttk.Label(main_window, text="Ok")
                msgOk .place(x=370, y=85, width=160, height=30)
                msgOk = ttk.Label(main_window, text="Ok")
                msgOk .place(x=370, y=120, width=160, height=30)
            else:
                msgNoOk = ttk.Label(main_window, text="No Ok")
                msgNoOk .place(x=370, y=120, width=160, height=30)
                msgOk = ttk.Label(main_window, text="Ok")
                msgOk .place(x=370, y=85, width=160, height=30)
        else:
            msgNoOk = ttk.Label(main_window, text="No Ok")
            msgNoOk .place(x=370, y=85, width=160, height=30)'''

def fnValidaBoard(event):
    BOARD = StringVar()
    BOARD = combo.get()
    BOARD = BOARD[22:33]
    BOARDS = ['P88390DW010', 'P88390DW010', 'P88490DW010']
    if BOARD in BOARDS:
        msgOk = ttk.Label(main_window, text="Ok")
        msgOk .place(x=370, y=50, width=160, height=30)
        event.widget.tk_focusNext().focus()
    else:
        msgNoOk = ttk.Label(main_window, text="Valor incorrecto")
        msgNoOk .place(x=370, y=50, width=160, height=30)
        combo.bind('<Return>', fnValidaBoard)
        combo.delete(0,'end')
def fnCompara1(event):
    BOARD = StringVar()
    BOARD = combo.get()
    BOARD = BOARD[22:33]
    WIRING = StringVar()
    WIRING = txt1.get()
    WIRING = WIRING[0:16]
    if BOARD == 'P88390DW010':
        if WIRING == 'VTSMXP88572DW010':
            msgOk = ttk.Label(main_window, text="Ok")
            msgOk .place(x=370, y=85, width=160, height=30)
            event.widget.tk_focusNext().focus()
        else:
            msgNoOk = ttk.Label(main_window, text="No Ok")
            msgNoOk .place(x=370, y=85, width=160, height=30)
            txt1.bind('<Return>', fnCompara1)
            txt1.delete(0,'end')
            
    elif BOARD == 'P88490DW000':
        if WIRING == 'VTSMXP88572DW000':
            msgOk = ttk.Label(main_window, text="Ok")
            msgOk .place(x=370, y=85, width=160, height=30)
            event.widget.tk_focusNext().focus()
        else:
            msgNoOk = ttk.Label(main_window, text="No Ok")
            msgNoOk .place(x=370, y=85, width=160, height=30)
            txt1.bind('<Return>', fnCompara1)
            txt1.delete(0,'end')
    elif BOARD == 'P88490DW010':
        if WIRING == 'VTSMXP88572DW010':
            msgOk = ttk.Label(main_window, text="Ok")
            msgOk .place(x=370, y=85, width=160, height=30)
            event.widget.tk_focusNext().focus()
        else:
            msgNoOk = ttk.Label(main_window, text="No Ok")
            msgNoOk .place(x=370, y=85, width=160, height=30)
            txt1.bind('<Return>', fnCompara1)
            txt1.delete(0,'end')
def fnCompara2(event):
    BOARD = StringVar()
    BOARD = combo.get()
    BOARD = BOARD[22:33]
    USB = StringVar()
    USB = txt2.get()
    USB = USB[0:16]
    if BOARD == 'P88390DW010':
        if USB == 'yyy':
            msgOk = ttk.Label(main_window, text="Ok")
            msgOk .place(x=370, y=120, width=160, height=30)
            txt1.delete(0,'end')
            txt2.delete(0,'end')
            combo.delete(0,'end')
            event.widget.tk_focusNext().focus()
        else:
            msgNoOk = ttk.Label(main_window, text="No Ok")
            msgNoOk .place(x=370, y=120, width=160, height=30)
            txt2.bind('<Return>', fnCompara2)
            txt2.delete(0,'end')
    elif BOARD == 'P88490DW000':
        if USB == '96125-P1610WK':
            msgOk = ttk.Label(main_window, text="Ok")
            msgOk .place(x=370, y=120, width=160, height=30)
            event.widget.tk_focusNext().focus()
            txt1.delete(0,'end')
            txt2.delete(0,'end')
            combo.delete(0,'end')
            event.widget.tk_focusNext().focus()
        else:
            msgNoOk = ttk.Label(main_window, text="No Ok")
            msgNoOk .place(x=370, y=120, width=160, height=30)
            txt2.bind('<Return>', fnCompara2)
            txt2.delete(0,'end')
            txt1.delete(0,'end')
            txt2.delete(0,'end')
            combo.delete(0,'end')
            event.widget.tk_focusNext().focus()
    elif BOARD == 'P88490DW010':
        if USB == '96125-P1610WK':
            msgOk = ttk.Label(main_window, text="Ok")
            msgOk .place(x=370, y=120, width=160, height=30)
            event.widget.tk_focusNext().focus()
            txt1.delete(0,'end')
            txt2.delete(0,'end')
            combo.delete(0,'end')
            event.widget.tk_focusNext().focus()
        else:
            msgNoOk = ttk.Label(main_window, text="No Ok")
            msgNoOk .place(x=370, y=120, width=160, height=30)
            txt2.bind('<Return>', fnCompara2)
            txt2.delete(0,'end')

main_window = tk.Tk()
main_window.config(width=600, height=400)
main_window.title("Validacion")

'''combo = ttk.Combobox(
    state="readonly",
    values=["P88390DW010", "P88490DW000", "P88490DW010"]
)
combo.place(x=210, y=50, width=150, height=30)'''

combo = ttk.Entry()
combo.place(x=210, y=50, width=150, height=30)
combo.bind('<Return>', fnValidaBoard)

txt1 = ttk.Entry() #Crear caja de texto
txt1.place(x=210, y=85, width=150, height=30)# Posicionarla en la ventana
txt1.bind('<Return>', fnCompara1)
txt2 = ttk.Entry()
txt2.place(x=210, y=120, width=150, height=30) # Posicionarla en la ventana
txt2.bind('<Return>', fnCompara2)

lbl1 = ttk.Label(main_window, text="BOARD ASSY-FR BACK:")
lbl1 .place(x=50, y=50, width=160, height=30)
lbl2 = ttk.Label(main_window, text="WIRING HARNESS-FR BACK:")
lbl2 .place(x=50, y=85, width=160, height=30)
lbl3 = ttk.Label(main_window, text="USB CHARGER-FR BACK:")
lbl3 .place(x=50, y=120, width=160, height=30)

#lbl1 = Label(main_window, text="Board Assy-fr back:", bg="grey" )
#lbl1.place(x=50, y=50)

main_window.mainloop()
#import string
#Instalar pip3 install qrcode
#Instalar pip3 install pillow
import tkinter as tk
from lib2to3.pgen2.token import STRING
from tkinter import *
from distutils.cmd import Command
from tkinter import COMMAND, messagebox, ttk
from turtle import bgcolor

main_window = tk.Tk()
main_window.config(width=600, height=400)
main_window.title("Generador QR")

def fnCompara3(event):
    event.widget.tk_focusNext().focus()
def fnCompara1(event):
    wiring1 = StringVar()
    wiring1 = wiring.get()
    wiring1 = wiring1[12:16]
    usb1 = StringVar()
    usb1 = usb.get()
    usb1 = usb1[6:13]
    if (wiring1 == 'W010') and (usb1 == 'P1610WK'):
        messagebox.showinfo(
        message=f"La opción seleccionada es: [)>06VAYGDP88490DW010SET220930S121A1000001MYC",
        title="Selección"
        )
        event.widget.tk_focusNext().focus()
    elif (wiring1 == 'W010') and (usb1 == 'P1600WK'):
        messagebox.showinfo(
        message=f"La opción seleccionada es: [)>06VAYGDP88390DW010SET220929S121A1000022MYC",
        title="Selección"
        )
    elif (wiring1 == 'W000') and (usb1 == 'P1610WK'):
        messagebox.showinfo(
        message=f"La opción seleccionada es: [)>06VAYGDP88490DW000SET220930S121A1000001MYC",
        title="Selección"
        )
    else:
        messagebox.showinfo(
        message=f"Favor de introducir una combinacion valida",
        title="Error"
        )
        event.widget.tk_focusNext().focus()
        #msgNoOk = ttk.Label(main_window, text="Valor incorrecto")
        #msgNoOk .place(x=370, y=50, width=160, height=30)
        #combo.bind('<Return>', fnValidaBoard)
        #combo.delete(0,'end')
    #msgOk = ttk.Label(main_window, text="Ok")
    #msgOk .place(x=370, y=85, width=160, height=30)
    #event.widget.tk_focusNext().focus()

def fnCompara2(event):
    usb1 = StringVar()
    usb1 = usb.get()
    usb1 = usb1[9:13]
    messagebox.showinfo(
        message=f"La opción seleccionada es: {usb1}",
        title="Selección"
    )
    #msgOk = ttk.Label(main_window, text="Ok")
    #msgOk .place(x=370, y=85, width=160, height=30)
    #event.widget.tk_focusNext().focus()

lbl1 = ttk.Label(main_window, text="WIRING HARNESS-FR BACK:")
lbl1 .place(x=50, y=50, width=160, height=30)
lbl2 = ttk.Label(main_window, text="USB CHARGER-FR BACK:")
lbl2 .place(x=50, y=85, width=160, height=30)

wiring = ttk.Entry() #Crear caja de texto
wiring.place(x=210, y=50, width=150, height=30)# Posicionarla en la ventana
wiring.bind('<Return>', fnCompara3)
usb = ttk.Entry()
usb.place(x=210, y=85, width=150, height=30) # Posicionarla en la ventana
usb.bind('<Return>', fnCompara1)



main_window.mainloop()
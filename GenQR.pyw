#import string
# Instalar pip3 install qrcode
# Instalar pip3 install pillow
# <gs> -> group separator \0x1D for GS chr(29)
# <rs> -> record separator \0x1E for RS chr(30)
# <eot> -> end of transmission \0x04 for EOT chr(4)

#\x1d - GS, Separador de grupo, código ASCII 29 (Hex 1D)
#\x1e - RS, Separador de registro, código ASCII 30 (Hex 1E)
#\x04 - EOT, Fin de transmisión, código ASCII 04 (Hex 04)


import os
import tkinter as tk
from ast import Global
from contextlib import ContextDecorator
from datetime import date, datetime
from distutils.cmd import Command
"from lib2to3.pgen2.token import STRING"
from pathlib import Path
from stringprep import c22_specials
from time import strftime
from tkinter import *
from tkinter import COMMAND, messagebox, ttk
from turtle import bgcolor
import win32print
import win32api
import tempfile
import cv2
import numpy as np
import qrcode
from PIL import Image, ImageDraw, ImageWin
from pylibdmtx.pylibdmtx import decode, encode
import win32ui
import win32print
import win32con
import win32print
import win32ui
import pyzbar.pyzbar as pyzbar

main_window = tk.Tk()
main_window.config(width=600, height=400)
main_window.title("Generador Data Matrix")

lbl1 = ttk.Label(main_window, text="WIRING HARNESS-FR BACK:")
lbl1 .place(x=50, y=50, width=160, height=30)
lbl2 = ttk.Label(main_window, text="USB CHARGER-FR BACK:")
lbl2 .place(x=50, y=85, width=160, height=30)
wiring = ttk.Entry()  # Crear caja de texto
wiring.place(x=210, y=50, width=150, height=30)  # Posicionarla en la ventana
usb = ttk.Entry()
usb.place(x=210, y=85, width=150, height=30)  # Posicionarla en la ventana


date = datetime.now()
today = date.strftime('%d.%m.%y')

fileCount = 'C:/Users/Master Mind/Desktop/Validacion_QR/Proyecto_Imprimir_etiqueta/etiquetas/contw01010'+today+'.txt'
if (os.path.exists(fileCount) == False):
    open("file", "w")
    f = open(fileCount, "w")
    f.write("1000000")
    f = open(fileCount, "r")
else:
    f = open(fileCount, "r")

fcount = open(fileCount, "r")
contador = fcount.read()

fileCountW01000 = 'C:/Users/Master Mind/Desktop/Validacion_QR/Proyecto_Imprimir_etiqueta/etiquetas/contW01000'+today+'.txt'
if (os.path.exists(fileCountW01000) == False):
    open("file", "w")
    f = open(fileCountW01000, "w")
    f.write("1000000")
    f = open(fileCountW01000, "r")
else:
    f = open(fileCountW01000, "r")

fcountW01000 = open(fileCountW01000, "r")
contadorW01000 = fcountW01000.read()

fileCountW00010 = 'C:/Users/Master Mind/Desktop/Validacion_QR/Proyecto_Imprimir_etiqueta/etiquetas/contW00010'+today+'.txt'
if (os.path.exists(fileCountW00010) == False):
    open("file", "w")
    f = open(fileCountW00010, "w")
    f.write("1000000")
    f = open(fileCountW00010, "r")
else:
    f = open(fileCountW00010, "r")

fileCountW00010 = open(fileCountW00010, "r")
contadorW00010 = fileCountW00010.read()


def fnCompara1(event):
    event.widget.tk_focusNext().focus()


def fnCompara2(event):
    wiring1 = StringVar()
    wiring1 = wiring.get()
    wiring1 = wiring1[12:16]
    usb1 = StringVar()
    usb1 = usb.get()
    usb1 = usb1[6:13]
    print(wiring1)
    print(usb1)
    lblerror = Label(main_window, text="")
    lblerror .place(x=150, y=0+150, width=200, height=60)
    if (wiring1 == 'W010') and (usb1 == 'P1610WK'):
        event.widget.tk_focusNext().focus()
        d = datetime.now()
        today1 = d.strftime('%d.%m.%y')
        today2 = d.strftime('%y%m%d')
        img = 255*np.ones((203, 203, 3), np.uint8)
        font = cv2.FONT_HERSHEY_DUPLEX = 2
        fontScale = .72
        fontColor = (0, 0, 0)
        global contador
        print(contador)
    # Crea el codigo datamatrix
        cv2.putText(img, '88390DW010', (15, 40), font, fontScale, fontColor)
        cv2.putText(img, 'TAESUNG', (15, 75), font, fontScale, fontColor)
        cv2.putText(img, 'BOARD ASSY FR', (15, 110),
                    font, fontScale, fontColor)
        cv2.putText(img, 'BACK RH(PWR)', (15, 145), font, fontScale, fontColor)
        cv2.putText(img, today1, (15, 175), font, fontScale, fontColor)
        cv2.imwrite('datos.bmp', img)
        createdmtx = '[)>'+chr(30)+'06'+chr(29)+'VAYGD'+chr(29)+'P88490DW010'+chr(29)+'S'+chr(29)+'E'+chr(
            29)+'T' + today2+'S121A'+str(contador)+''+chr(29)+'MY'+chr(29)+'C'+chr(29)+chr(30)+chr(4)
        encoded = encode(createdmtx.encode('utf8'))
        img = Image.frombytes(
            'RGB', (encoded.width, encoded.height), encoded.pixels)
        img.save('dmtx.bmp')
    # print(decode(Image.open('dmtx.bmp')))
        img1 = cv2.imread('datos.bmp')
        virat_img = cv2.imread('dmtx.bmp')
        borderoutput = cv2.copyMakeBorder(
            virat_img, 7, 7, 7, 7, cv2.BORDER_CONSTANT, value=[255, 255, 255])
        cv2.imwrite('dmtx.bmp', borderoutput)
        img2 = cv2.imread('dmtx.bmp')
        imgresize = cv2.resize(img2, (203, 203))
        dimenqr = img1.shape
        dimenInfo = img2.shape
        print('qr Dimension    : ', dimenqr)
        print('Info dimentions  :', dimenInfo)
        im_v = cv2.hconcat([img1, imgresize])
        ruta = 'C:/Users/Master Mind/Desktop/Validacion_QR/Proyecto_Imprimir_etiqueta/etiquetas'
        #cv2.imshow('sea_image.jpg', im_v)
        contador = int(contador) + 1
    # Crea un archivo en la ruta y guarda el valor del contador
        fC = 'C:/Users/Master Mind/Desktop/Validacion_QR/Proyecto_Imprimir_etiqueta/etiquetas/contW010'+today+'.txt'
        f2 = open(fC, "w+")
        f2.write(str(contador))
        f2.close()
        cv2.imwrite(os.path.join(ruta, 'etiqueta.bmp'), im_v)
    # Manda a imprimir
        # http://timgolden.me.uk/python/win32_how_do_i/print.html
        # Constants for GetDeviceCaps
        #
        #
        # HORZRES / VERTRES = printable area
        #
        HORZRES = 8
        VERTRES = 10
        #
        # LOGPIXELS = dots per inch
        #
        LOGPIXELSX = 88
        LOGPIXELSY = 90
        #
        # PHYSICALWIDTH/HEIGHT = total area
        #
        PHYSICALWIDTH = 110
        PHYSICALHEIGHT = 111
        #
        # PHYSICALOFFSETX/Y = left / top margin
        #
        PHYSICALOFFSETX = 112
        PHYSICALOFFSETY = 113

        printer_name = win32print.GetDefaultPrinter()
        file_name = "C:/Users/Master Mind/Desktop/Validacion_QR/Proyecto_Imprimir_etiqueta/etiquetas/etiqueta.bmp"

        #
        # You can only write a Device-independent bitmap
        #  directly to a Windows device context; therefore
        #  we need (for ease) to use the Python Imaging
        #  Library to manipulate the image.
        #
        # Create a device context from a named printer
        #  and assess the printable size of the paper.
        #
        hDC = win32ui.CreateDC()
        hDC.CreatePrinterDC(printer_name)
        printable_area = hDC.GetDeviceCaps(HORZRES), hDC.GetDeviceCaps(VERTRES)
        printer_size = hDC.GetDeviceCaps(
            PHYSICALWIDTH), hDC.GetDeviceCaps(PHYSICALHEIGHT)
        printer_margins = hDC.GetDeviceCaps(
            PHYSICALOFFSETX), hDC.GetDeviceCaps(PHYSICALOFFSETY)

        #
        # Open the image, rotate it if it's wider than
        #  it is high, and work out how much to multiply
        #  each pixel by to get it as big as possible on
        #  the page without distorting.
        #
        bmp = Image.open(file_name)
        #if bmp.size[0] > bmp.size[1]:bmp = bmp.rotate(90)

        ratios = [1.0 * printable_area[0] / bmp.size[0],
                  1.0 * printable_area[1] / bmp.size[1]]
        scale = min(ratios)

        #
        # Start the print job, and draw the bitmap to
        #  the printer device at the scaled size.
        #
        hDC.StartDoc(file_name)
        hDC.StartPage()

        dib = ImageWin.Dib(bmp)
        scaled_width, scaled_height = [int(scale * i) for i in bmp.size]
        x1 = int((printer_size[0] - scaled_width) / 2)
        y1 = int((printer_size[1] - scaled_height) / 2)
        x2 = x1 + scaled_width
        y2 = y1 + scaled_height
        dib.draw(hDC.GetHandleOutput(), (x1, y1, x2, y2))

        hDC.EndPage()
        hDC.EndDoc()
        hDC.DeleteDC()
        usb.delete(0, tk.END)
        wiring.delete(0, tk.END)
        event.widget.tk_focusNext().focus()
        cv2.waitKey(0)
    elif (wiring1 == 'W010') and (usb1 == 'P1600WK'):
        event.widget.tk_focusNext().focus()
        d = datetime.now()
        today1 = d.strftime('%d.%m.%y')
        today2 = d.strftime('%y%m%d')
        img = 255*np.ones((203, 203, 3), np.uint8)
        font = cv2.FONT_HERSHEY_DUPLEX = 2
        fontScale = .72
        fontColor = (0, 0, 0)
        global contadorW01000
        print(contadorW01000)
    # Crea el codigo datamatrix
        cv2.putText(img, '88390DW010', (15, 40), font, fontScale, fontColor)
        cv2.putText(img, 'TAESUNG', (15, 75), font, fontScale, fontColor)
        cv2.putText(img, 'BOARD ASSY FR', (15, 110),
                    font, fontScale, fontColor)
        cv2.putText(img, 'BACK LH(PWR)', (15, 145), font, fontScale, fontColor)
        cv2.putText(img, today1, (15, 175), font, fontScale, fontColor)
        cv2.imwrite('datos.bmp', img)
        createdmtx = '[)>'+chr(30)+'06'+chr(29)+'VAYGD'+chr(29)+'P88490DW010'+chr(29)+'S'+chr(29)+'E'+chr(
            29)+'T' + today2+'S121A'+str(contadorW01000)+''+chr(29)+'MY'+chr(29)+'C'+chr(29)+chr(30)+chr(4)
        encoded = encode(createdmtx.encode('utf8'))
        img = Image.frombytes(
            'RGB', (encoded.width, encoded.height), encoded.pixels)
        img.save('dmtx.bmp')
    # print(decode(Image.open('dmtx.bmp')))
        img1 = cv2.imread('datos.bmp')
        virat_img = cv2.imread('dmtx.bmp')
        borderoutput = cv2.copyMakeBorder(
            virat_img, 7, 7, 7, 7, cv2.BORDER_CONSTANT, value=[255, 255, 255])
        cv2.imwrite('dmtx.bmp', borderoutput)
        img2 = cv2.imread('dmtx.bmp')
        imgresize = cv2.resize(img2, (203, 203))
        im_v = cv2.hconcat([img1, imgresize])
        ruta = 'C:/Users/Master Mind/Desktop/Validacion_QR/Proyecto_Imprimir_etiqueta/etiquetas'
    #cv2.imshow('sea_image.jpg', im_v)
        contadorW01000 = int(contadorW01000) + 1
    # Crea un archivo en la ruta y guarda el valor del contador
        fC = 'C:/Users/Master Mind/Desktop/Validacion_QR/Proyecto_Imprimir_etiqueta/etiquetas/contW01000'+today+'.txt'
        f2 = open(fC, "w+")
        f2.write(str(contadorW01000))
        f2.close()
        cv2.imwrite(os.path.join(ruta, 'etiqueta.bmp'), im_v)
        # http://timgolden.me.uk/python/win32_how_do_i/print.html
        # Constants for GetDeviceCaps
        #
        #
        # HORZRES / VERTRES = printable area
        #
        HORZRES = 8
        VERTRES = 10
        #
        # LOGPIXELS = dots per inch
        #
        LOGPIXELSX = 88
        LOGPIXELSY = 90
        #
        # PHYSICALWIDTH/HEIGHT = total area
        #
        PHYSICALWIDTH = 110
        PHYSICALHEIGHT = 111
        #
        # PHYSICALOFFSETX/Y = left / top margin
        #
        PHYSICALOFFSETX = 112
        PHYSICALOFFSETY = 113

        printer_name = win32print.GetDefaultPrinter()
        file_name = "C:/Users/Master Mind/Desktop/Validacion_QR/Proyecto_Imprimir_etiqueta/etiquetas/etiqueta.bmp"

        #
        # You can only write a Device-independent bitmap
        #  directly to a Windows device context; therefore
        #  we need (for ease) to use the Python Imaging
        #  Library to manipulate the image.
        #
        # Create a device context from a named printer
        #  and assess the printable size of the paper.
        #
        hDC = win32ui.CreateDC()
        hDC.CreatePrinterDC(printer_name)
        printable_area = hDC.GetDeviceCaps(HORZRES), hDC.GetDeviceCaps(VERTRES)
        printer_size = hDC.GetDeviceCaps(
            PHYSICALWIDTH), hDC.GetDeviceCaps(PHYSICALHEIGHT)
        printer_margins = hDC.GetDeviceCaps(
            PHYSICALOFFSETX), hDC.GetDeviceCaps(PHYSICALOFFSETY)

        #
        # Open the image, rotate it if it's wider than
        #  it is high, and work out how much to multiply
        #  each pixel by to get it as big as possible on
        #  the page without distorting.
        #
        bmp = Image.open(file_name)
        #if bmp.size[0] > bmp.size[1]:bmp = bmp.rotate(90)

        ratios = [1.0 * printable_area[0] / bmp.size[0],
                  1.0 * printable_area[1] / bmp.size[1]]
        scale = min(ratios)

        #
        # Start the print job, and draw the bitmap to
        #  the printer device at the scaled size.
        #
        hDC.StartDoc(file_name)
        hDC.StartPage()

        dib = ImageWin.Dib(bmp)
        scaled_width, scaled_height = [int(scale * i) for i in bmp.size]
        x1 = int((printer_size[0] - scaled_width) / 2)
        y1 = int((printer_size[1] - scaled_height) / 2)
        x2 = x1 + scaled_width
        y2 = y1 + scaled_height
        dib.draw(hDC.GetHandleOutput(), (x1, y1, x2, y2))

        hDC.EndPage()
        hDC.EndDoc()
        hDC.DeleteDC()
        usb.delete(0, tk.END)
        wiring.delete(0, tk.END)
        event.widget.tk_focusNext().focus()
        cv2.waitKey(0)
    elif (wiring1 == 'W000') and (usb1 == 'P1610WK'):
        event.widget.tk_focusNext().focus()
        d = datetime.now()
        today1 = d.strftime('%d.%m.%y')
        today2 = d.strftime('%y%m%d')
        img = 255*np.ones((203, 203, 3), np.uint8)
        font = cv2.FONT_HERSHEY_DUPLEX = 2
        fontScale = .72
        fontColor = (0, 0, 0)
        global contadorW00010
        print(contadorW00010)
    # Crea el codigo datamatrix
        cv2.putText(img, '88490DW000', (15, 40), font, fontScale, fontColor)
        cv2.putText(img, 'TAESUNG', (15, 75), font, fontScale, fontColor)
        cv2.putText(img, 'BOARD ASSY FR', (15, 110),
                    font, fontScale, fontColor)
        cv2.putText(img, 'BACK RH(MNL)', (15, 145), font, fontScale, fontColor)
        cv2.putText(img, today1, (15, 175), font, fontScale, fontColor)
        cv2.imwrite('datos.bmp', img)
        createdmtx = '[)>'+chr(30)+'06'+chr(29)+'VAYGD'+chr(29)+'P88490DW010'+chr(29)+'S'+chr(29)+'E'+chr(
            29)+'T' + today2+'S121A'+str(contadorW00010)+''+chr(29)+'MY'+chr(29)+'C'+chr(29)+chr(30)+chr(4)
        encoded = encode(createdmtx.encode('utf8'))
        img = Image.frombytes(
            'RGB', (encoded.width, encoded.height), encoded.pixels)
        img.save('dmtx.bmp')
    # print(decode(Image.open('dmtx.bmp')))
        img1 = cv2.imread('datos.bmp')
        virat_img = cv2.imread('dmtx.bmp')
        borderoutput = cv2.copyMakeBorder(
            virat_img, 7, 7, 7, 7, cv2.BORDER_CONSTANT, value=[255, 255, 255])
        cv2.imwrite('dmtx.bmp', borderoutput)
        img2 = cv2.imread('dmtx.bmp')
        imgresize = cv2.resize(img2, (203, 203))
        im_v = cv2.hconcat([img1, imgresize])
        ruta = 'C:/Users/Master Mind/Desktop/Validacion_QR/Proyecto_Imprimir_etiqueta/etiquetas'
    #cv2.imshow('sea_image.jpg', im_v)
        contadorW00010 = int(contadorW00010) + 1
    # Crea un archivo en la ruta y guarda el valor del contador
        fC = 'C:/Users/Master Mind/Desktop/Validacion_QR/Proyecto_Imprimir_etiqueta/etiquetas/contW00010'+today+'.txt'
        f2 = open(fC, "w+")
        f2.write(str(contadorW00010))
        f2.close()
        cv2.imwrite(os.path.join(ruta, 'etiqueta.bmp'), im_v)
        # http://timgolden.me.uk/python/win32_how_do_i/print.html
        # Constants for GetDeviceCaps
        #
        #
        # HORZRES / VERTRES = printable area
        #
        HORZRES = 8
        VERTRES = 10
        #
        # LOGPIXELS = dots per inch
        #
        LOGPIXELSX = 88
        LOGPIXELSY = 90
        #
        # PHYSICALWIDTH/HEIGHT = total area
        #
        PHYSICALWIDTH = 110
        PHYSICALHEIGHT = 111
        #
        # PHYSICALOFFSETX/Y = left / top margin
        #
        PHYSICALOFFSETX = 112
        PHYSICALOFFSETY = 113

        printer_name = win32print.GetDefaultPrinter()
        file_name = "C:/Users/Master Mind/Desktop/Validacion_QR/Proyecto_Imprimir_etiqueta/etiquetas/etiqueta.bmp"

        #
        # You can only write a Device-independent bitmap
        #  directly to a Windows device context; therefore
        #  we need (for ease) to use the Python Imaging
        #  Library to manipulate the image.
        #
        # Create a device context from a named printer
        #  and assess the printable size of the paper.
        #
        hDC = win32ui.CreateDC()
        hDC.CreatePrinterDC(printer_name)
        printable_area = hDC.GetDeviceCaps(HORZRES), hDC.GetDeviceCaps(VERTRES)
        printer_size = hDC.GetDeviceCaps(
            PHYSICALWIDTH), hDC.GetDeviceCaps(PHYSICALHEIGHT)
        printer_margins = hDC.GetDeviceCaps(
            PHYSICALOFFSETX), hDC.GetDeviceCaps(PHYSICALOFFSETY)

        #
        # Open the image, rotate it if it's wider than
        #  it is high, and work out how much to multiply
        #  each pixel by to get it as big as possible on
        #  the page without distorting.
        #
        bmp = Image.open(file_name)
        #if bmp.size[0] > bmp.size[1]:bmp = bmp.rotate(90)

        ratios = [1.0 * printable_area[0] / bmp.size[0],
                  1.0 * printable_area[1] / bmp.size[1]]
        scale = min(ratios)

        #
        # Start the print job, and draw the bitmap to
        #  the printer device at the scaled size.
        #
        hDC.StartDoc(file_name)
        hDC.StartPage()

        dib = ImageWin.Dib(bmp)
        scaled_width, scaled_height = [int(scale * i) for i in bmp.size]
        x1 = int((printer_size[0] - scaled_width) / 2)
        y1 = int((printer_size[1] - scaled_height) / 2)
        x2 = x1 + scaled_width
        y2 = y1 + scaled_height
        dib.draw(hDC.GetHandleOutput(), (x1, y1, x2, y2))

        hDC.EndPage()
        hDC.EndDoc()
        hDC.DeleteDC()
        usb.delete(0, tk.END)
        wiring.delete(0, tk.END)
        event.widget.tk_focusNext().focus()
        cv2.waitKey(0)
    else:
        usb.delete(0, tk.END)
        wiring.delete(0, tk.END)
        lblerror = Label(main_window, text="Verifique los datos escaneados")
        lblerror .place(x=150, y=0+150, width=200, height=60)
        event.widget.tk_focusNext().focus()


def concatenarimagenes():
    img1 = cv2.imread('datos.bmp')
    img2 = cv2.imread('QR.bmp')
    im_v = cv2.hconcat([img1, img2])

    ruta = 'C:/Users/Master Mind/Desktop/Validacion_QR/Proyecto_Imprimir_etiqueta/etiquetas'

    cv2.imshow('sea_image.jpg', im_v)
    cv2.imwrite(os.path.join(ruta, 'etiqueta.bmp'), im_v)
    cv2.waitKey(0)


def w01010wk(contador):
    d = datetime.now()
    today1 = d.strftime('%d.%m.%y')
    today2 = d.strftime('%y%m%d')
    img = 255*np.ones((203, 203, 3), np.uint8)
    font = cv2.FONT_HERSHEY_DUPLEX = 2
    fontScale = .72
    fontColor = (0, 0, 0)

    cv2.putText(img, '88390DW010', (15, 40), font, fontScale, fontColor)
    cv2.putText(img, 'TAESUNG', (15, 75), font, fontScale, fontColor)
    cv2.putText(img, 'BOARD ASSY FR', (15, 110), font, fontScale, fontColor)
    cv2.putText(img, 'BACK LH(PWR)', (15, 145), font, fontScale, fontColor)
    cv2.putText(img, today1, (15, 175), font, fontScale, fontColor)
    cv2.imwrite('datos.bmp', img)
    createdmtx = '[)>'+chr(30)+'06'+chr(29)+'VAYGD'+chr(29)+'P88490DW010'+chr(29)+'S'+chr(29)+'E'+chr(
        29)+'T'+today2+'S121A'+str(contador)+''+chr(29)+'MY'+chr(29)+'C'+chr(29)+chr(30)+chr(4)
    encoded = encode(createdmtx.encode('utf8'))
    img = Image.frombytes(
        'RGB', (encoded.width, encoded.height), encoded.pixels)
    img.save('dmtx.bmp')
    print(decode(Image.open('dmtx.bmp')))
    img1 = cv2.imread('datos.bmp')
    img2 = cv2.imread('dmtx.bmp')
    imgresize = cv2.resize(img2, (203, 203))
    im_v = cv2.hconcat([img1, imgresize])
    ruta = 'C:/Users/Master Mind/Desktop/Validacion_QR/Proyecto_Imprimir_etiqueta/etiquetas'
    #cv2.imshow('sea_image.jpg', im_v)
    contador = contador + 1
    cv2.imwrite(os.path.join(ruta, 'etiqueta.bmp'), im_v)
    cv2.waitKey(0)


def w01000wk():
    print('Ejemplo dimentions  :')


def w00010wk():
    print('Ejemplo dimentions  :')


wiring.bind('<Return>', fnCompara1)
usb.bind('<Return>', fnCompara2)
wiring.focus()

main_window.mainloop()

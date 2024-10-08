import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
from utils.limitar_entrada import limitar_entrada
from utils.verificacion import verificar_pin

#Valores iniciales
user_pin = "1234"
saldo = 1000

def consultar_saldo():
    messagebox.showinfo("Consultar Saldo", f"Saldo disponible: {saldo}")

def depositar_saldo():
    window_depo = tk.Toplevel()
    window_depo.title("Cajero Automatico")
    window_depo.configure(background='lightblue')
    window_depo.resizable(False, False)
    window_depo.geometry('300x200')
    window_depo.iconbitmap('src/icon/cajero-automatico.ico')

    cantidad_label = tk.Label(window_depo, text= "Cantidad a depositar", font=('Arial', 10, 'bold'))

    frame_depositar = tk.Frame(window_depo, bg='lightgrey', bd=2, relief='groove')
    entry_depositar = tk.Entry(frame_depositar, bg="cyan",justify="center")

    def depositar_dinero():
        try:
            global saldo
            cantidad = float(entry_depositar.get())
            if cantidad < 0:
                raise ValueError("No se permiten números negativos.")
            else:
                saldo += cantidad
                messagebox.showinfo("Éxito", f"Has depositado ${cantidad}\nNuevo saldo: ${saldo}")
                window_depo.destroy()

        except ValueError as e:
                messagebox.showerror("Error", f"Entrada inválida: {e}")

    btn_depositar = tk.Button(frame_depositar, text="Depositar", compound='left',padx=10 ,image=imagen_monedaTK, borderwidth=4, relief="raised", command=depositar_dinero)

    cantidad_label.pack(pady=30, fill='x')
    frame_depositar.pack(expand= True, ipadx= 20)
    entry_depositar.pack(pady=5)
    btn_depositar.pack(pady=5, ipady= 10)

def retirar_saldo():
    window_retiro = tk.Toplevel()
    window_retiro.title("Cajero Automatico")
    window_retiro.configure(background='lightblue')
    window_retiro.resizable(False, False)
    window_retiro.geometry('300x200')
    window_retiro.iconbitmap('src/icon/cajero-automatico.ico')

    retiro_label = tk.Label(window_retiro, text= "Cantidad a retirar", font=('Arial', 10, 'bold'))

    retiro_frame = tk.Frame(window_retiro, bg='lightgrey', bd=2, relief='groove')
    entry_retiro = tk.Entry(retiro_frame, bg="cyan",justify="center")

    def retirar_dinero():
        try:
            global saldo
            cantidad = float(entry_retiro.get())
            if cantidad > 0:
                if cantidad > saldo:
                    messagebox.showerror("Error","Saldo insuficiente")
                else:
                    saldo -= cantidad
                    messagebox.showinfo("Éxito", f"Has retirado ${cantidad}\nSaldo restante: ${saldo}")
                    window_retiro.destroy()
            else:
                raise ValueError("No se permiten numeros negativos")
        except ValueError as e:
            messagebox.showerror("Error", f"Entrada inválida: {e}")

    btn_retiro = tk.Button(retiro_frame, text= "Retirar", compound='left', image= imagen_monedaTK ,font=('Arial', 10, 'bold'), command=retirar_dinero)

    retiro_label.pack(pady=30, fill='x')

    retiro_frame.pack(expand= True, ipadx= 20)
    entry_retiro.pack(pady=5)
    btn_retiro.pack(pady=5, ipady= 10, ipadx= 20)

def menu_principal():
    window_menu = tk.Toplevel()
    window_menu.title("Cajero Automatico")
    window_menu.configure(background='lightblue')
    window_menu.resizable(False, False)
    window_menu.geometry('500x350')
    window_menu.iconbitmap('src/icon/cajero-automatico.ico')

    menu_label = tk.Label(window_menu, text= "Bienvenido", font=('Arial', 25, 'bold'), pady=10)
    
    frame_btn = tk.Frame(window_menu, bg = 'lightgrey', bd = '3', relief='groove')
    
    btn_consultar = tk.Button(frame_btn, text="Consultar", compound='left', padx=10, image=imagen_consultaTK, borderwidth=4, relief="raised", command=consultar_saldo)
    btn_depositar = tk.Button(frame_btn, text= "Depositar", compound='left',padx=10 ,image=imagen_depositoTK, borderwidth=4, relief="raised", command=depositar_saldo)
    opcion_label = tk.Label(frame_btn, text= "Elige una opcion", font=('Arial', 10, 'bold'), bg= 'lightgrey')
    btn_retirar = tk.Button(frame_btn, text="Retirar", compound='left', padx=10, image=imagen_retiroTK, borderwidth=4, relief="raised", command=retirar_saldo)

    menu_label.pack(side='top', fill='x')

    frame_btn.pack(ipadx=45, expand=True)
    btn_consultar.pack(pady=5, fill= 'x')
    btn_depositar.pack(side= 'left', expand=True, pady=5, fill= 'x')
    opcion_label.pack(side= 'left', expand=True, pady= 5)
    btn_retirar.pack(side= 'left', expand=True, pady=5, fill= 'x')

#Creacion de ventana principal
window_pin = tk.Tk()
window_pin.title('Cajero Automatico')
window_pin.configure(background='lightblue')
window_pin.resizable(False, False)
window_pin.geometry('500x350')
window_pin.iconbitmap('src/icon/cajero-automatico.ico')

#Generacion de imagenes
imagen_entrar = Image.open('src/images/entrar.png') 
imagen_entrar_redimensionar = imagen_entrar.resize((30,30)) 
imagen_entrarTK = ImageTk.PhotoImage(imagen_entrar_redimensionar)

imagen_cajero = Image.open('src/images/cajero-automatico.png')
imagen_cajero_redimensionar = imagen_cajero.resize((75,75))
imagen_cajeroTK = ImageTk.PhotoImage(imagen_cajero_redimensionar)

imagen_moneda = Image.open('src/images/moneda.png')
image_moneda_redimensionar = imagen_moneda.resize((30, 30))
imagen_monedaTK = ImageTk.PhotoImage(image_moneda_redimensionar)

imagen_deposito = Image.open('src/images/deposito-de-efectivo.png')
imagen_deposito_redimensionar=imagen_deposito.resize((35,35))
imagen_depositoTK = ImageTk.PhotoImage(imagen_deposito_redimensionar)

imagen_retiro = Image.open('src/images/retiro-de-efectivo.png')
imagen_retiro_redimensionar=imagen_retiro.resize((35,35))
imagen_retiroTK = ImageTk.PhotoImage(imagen_retiro_redimensionar)

imagen_consulta = Image.open('src/images/consulta-de-efectivo.png')
imagen_consulta_redimensionar=imagen_consulta.resize((35,35))
imagen_consultaTK = ImageTk.PhotoImage(imagen_consulta_redimensionar)

#Registro para validar entrada
validar_entrada = window_pin.register(limitar_entrada)

#Creacion de un frame
frame_principal = tk.Frame(window_pin, bg='lightgrey', bd=2, relief='groove')

#Creacion de widgets
nombre_label = tk.Label(window_pin, text="Cajero automático",font=("Arial", 25, "bold"), relief="groove", compound="left", padx=10, image=imagen_cajeroTK)
caja_texto = tk.Entry(frame_principal, bg="cyan",justify="center", show="*", validate="key", validatecommand=(validar_entrada, '%P'))
entrar_boton = tk.Button(frame_principal, text="Ingresar", compound="left",padx=10 ,image=imagen_entrarTK, borderwidth=4, relief="raised", command=lambda:verificar_pin(caja_texto, window_pin, menu_principal, user_pin))
texto_label = tk.Label(window_pin, text="Creado por Edgar Jared Garcia Mercado", font=("Arial", 10, "bold"))

#Mostrar en pantalla los widgets
nombre_label.pack(side='top', fill='x')

frame_principal.pack(ipadx=40, expand=True)
caja_texto.pack(side='top', pady=10)
entrar_boton.pack(side='bottom', pady=10)

texto_label.pack(side='bottom')

window_pin.mainloop()
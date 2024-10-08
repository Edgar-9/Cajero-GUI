from tkinter import messagebox

#Verificacion de PIN ingresado en la caja de texto
def verificar_pin(caja_texto, window_pin, menu_principal, user_pin):
    pin_ingresado = caja_texto.get()
    if pin_ingresado == user_pin:
        window_pin.withdraw()
        menu_principal()
    elif pin_ingresado == "":
        messagebox.showwarning("Advertencia","El campo no debe estar vacio")
    elif len(pin_ingresado) < 4:
        messagebox.showwarning("Advertencia", "El campo debe tener 4 digitos")
    else:
        messagebox.showerror("Error", "PIN incorrecto")
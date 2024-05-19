import tkinter as tk
from tkinter import ttk
import customtkinter as ctk
from PIL import Image, ImageTk

from assets.utils import *

# Constants for styling
FONT_TYPE = "Arial"
ENTRE_TEXT = 15
BODY = 25
SUBBODY = 20
BUTTON = 40
HEADER = 20
FOOTER = 12
PADDING = 10
IMAGE_PATH = "src/assets/logo-fgc.png"  # Replace with your image path
x= "Samya"
pages=["main_menu"]
# Create the main application window
root = tk.Tk()
root.title("FGC - Ferrocarrils de la Generalitat de Catalunya")
root.geometry("400x400+0+500")  # Set the window size

def refresh():
    for widget in button_frame.winfo_children():
        widget.destroy()


def recarregaTM():
    print("Recarregar T-Mobilitat")

def ahead_behind_buttons():
    pass

def carregarTM():
    refresh()
    # Mostra el nom de l'usuari i la informació de la T-Mobilitat
    header = ctk.CTkLabel(
        button_frame, text=f"Títol - T-jove FM/FN general", text_color='black', font=(FONT_TYPE, BODY))
    header.grid(row=0, column=0, padx=20, pady=(20,20), sticky="nw")

def frame_tincTM():
    recarrega = False
    refresh()
    if recarrega:
        # Mostra el nom de l'usuari i la informació de la T-Mobilitat
        header = ctk.CTkLabel(
            button_frame, text=f"Títol - T-jove FM/FN general", text_color='black', font=(FONT_TYPE, BODY))
        header.grid(row=0, column=0, padx=20, pady=(20,20), sticky="nw")

        vigencia = ctk.CTkLabel(
            button_frame, text=f"Vigencia", text_color='gray', font=(FONT_TYPE, BODY))
        vigencia.grid(row=1, column=0, padx=20, pady=(0,0), sticky="nw")
        vigencia = ctk.CTkLabel(
            button_frame, text=f"Vàlid fins 31/12/2021", text_color='black', font=(FONT_TYPE, BODY))
        vigencia.grid(row=2, column=0, padx=20, pady=(0,ENTRE_TEXT), sticky="nw")

        trestant = ctk.CTkLabel(
            button_frame, text=f"Temps restant", text_color='gray', font=(FONT_TYPE, BODY))
        trestant.grid(row=1, column=1, padx=20, pady=(0,0), sticky="nw")
        trestant = ctk.CTkLabel(
            button_frame, text=f"64 dies restants", text_color='black', font=(FONT_TYPE, BODY))
        trestant.grid(row=2, column=1, padx=20, pady=(0,ENTRE_TEXT), sticky="nw")

        viatges = ctk.CTkLabel(
            button_frame, text=f"Viatges", text_color='gray', font=(FONT_TYPE, BODY))
        viatges.grid(row=3, column=0, padx=20, pady=(0,0), sticky="nw")
        viatges = ctk.CTkLabel(
            button_frame, text=f"Ilimitats", text_color='black', font=(FONT_TYPE, BODY))
        viatges.grid(row=4, column=0, padx=20, pady=(0,ENTRE_TEXT), sticky="nw")

        estat = ctk.CTkLabel(
            button_frame, text=f"Estat", text_color='gray', font=(FONT_TYPE, BODY))
        estat.grid(row=3, column=1, padx=20, pady=(0,0), sticky="nw")
        estat = ctk.CTkLabel(
            button_frame, text=f"Actiu", text_color='black', font=(FONT_TYPE, BODY))
        estat.grid(row=4, column=1, padx=20, pady=(0,ENTRE_TEXT), sticky="nw")

        zprimerav = ctk.CTkLabel(
            button_frame, text=f"Zona primera validació", text_color='gray', font=(FONT_TYPE, BODY))
        zprimerav.grid(row=5, column=0, padx=20, pady=(0,0), sticky="nw")
        zprimerav = ctk.CTkLabel(
            button_frame, text=f"Zona 7", text_color='black', font=(FONT_TYPE, BODY))
        zprimerav.grid(row=6, column=0, padx=20, pady=(0,ENTRE_TEXT), sticky="nw")
    
        zones = ctk.CTkLabel(
            button_frame, text=f"Zones", text_color='gray', font=(FONT_TYPE, BODY))
        zones.grid(row=5, column=1, padx=20, pady=(0,0), sticky="nw")
        zones = ctk.CTkLabel(
            button_frame, text=f"6", text_color='black', font=(FONT_TYPE, BODY))
        zones.grid(row=6, column=1, padx=20, pady=(0,40), sticky="nw")

        b_recarregaTM = ctk.CTkButton(
            button_frame, text="Recarrega", height=80, fg_color="#d0deb0", 
            text_color='gray', font=(FONT_TYPE, BUTTON), hover=False
        )
        b_recarregaTM.grid(row=7, column=0, columnspan=2, padx=5, pady=5, sticky="nsew")

    else:
        header = ctk.CTkLabel(
            button_frame, text=f"Resum de compra", text_color='black', font=(FONT_TYPE, BODY))
        header.grid(row=0, column=0, padx=20, pady=(20,20), sticky="nw")

        vigencia = ctk.CTkLabel(
            button_frame, text=f"Número de viatges", text_color='gray', font=(FONT_TYPE, BODY))
        vigencia.grid(row=1, column=0, padx=20, pady=(0,0), sticky="nw")
        vigencia = ctk.CTkLabel(
            button_frame, text=f"Ilimitats", text_color='black', font=(FONT_TYPE, BODY))
        vigencia.grid(row=2, column=0, padx=20, pady=(0,ENTRE_TEXT), sticky="nw")

        trestant = ctk.CTkLabel(
            button_frame, text=f"Validesa", text_color='gray', font=(FONT_TYPE, BODY))
        trestant.grid(row=1, column=1, padx=20, pady=(0,0), sticky="nw")
        trestant = ctk.CTkLabel(
            button_frame, text=f"90 dies des de la \nprimera validació", text_color='black', font=(FONT_TYPE, BODY))
        trestant.grid(row=2, column=1, padx=20, pady=(0,ENTRE_TEXT), sticky="nw")

        viatges = ctk.CTkLabel(
            button_frame, text=f"Títol", text_color='gray', font=(FONT_TYPE, BODY))
        viatges.grid(row=3, column=0, padx=20, pady=(ENTRE_TEXT,ENTRE_TEXT), sticky="nw")
        viatges = ctk.CTkLabel(
            button_frame, text=f"T-jove FM/FN general", text_color='black', font=(FONT_TYPE, BODY+4))
        viatges.grid(row=4, column=0, padx=20, pady=(0,ENTRE_TEXT), sticky="nw")

        viatges = ctk.CTkLabel(
            button_frame, text=f"Preu", text_color='gray', font=(FONT_TYPE, BODY))
        viatges.grid(row=3, column=1, padx=20, pady=(ENTRE_TEXT,ENTRE_TEXT), sticky="nw")
        viatges = ctk.CTkLabel(
            button_frame, text=f"34,15 €", text_color='black', font=(FONT_TYPE, BODY+4))
        viatges.grid(row=4, column=1, padx=20, pady=(0,40), sticky="nw")

        b_recarregaTM = ctk.CTkButton(
            button_frame, text="Pagar", height=80, fg_color="#97d700",
            hover_color="#79ac20", text_color='black', font=(FONT_TYPE, BUTTON),
            command=pagar
        )
        b_recarregaTM.grid(row=6, column=0, columnspan=2, padx=5, pady=(5,5), sticky="nsew")

def comprarTM():
    refresh()
    gi = Get_info()
    all_tickets = gi.get_tickets("Lleida - La Pobla de Segur")

    def update_price(event=None):     
        price = gi.get_ticket("Lleida - La Pobla de Segur", str(tticket.get()), int(zones.get()), int(quant.get()))
        preu_value.configure(text=f"{price:.2f} €")
        print(str(tticket.get()), int(zones.get()), quant.get())

    header = ctk.CTkLabel(
        button_frame, text=f"Compra", text_color='black', font=(FONT_TYPE, BODY))
    header.grid(row=0, column=0, padx=20, pady=(20, 20), sticky="nw")

    t = ctk.CTkLabel(
        button_frame, text=f"Tipus de bitllet", text_color='gray', font=(FONT_TYPE, BODY))
    t.grid(row=1, column=0, padx=20, pady=(0, 0), sticky="nw")
    tticket = ctk.CTkComboBox(
        button_frame, values=all_tickets, text_color='black', width=250, font=(FONT_TYPE, BODY))
    tticket.grid(row=2, column=0, padx=20, pady=(0, ENTRE_TEXT), sticky="nw")

    z = ctk.CTkLabel(
        button_frame, text=f"Zones", text_color='gray', font=(FONT_TYPE, BODY))
    z.grid(row=1, column=1, padx=20, pady=(ENTRE_TEXT, 0), sticky="nw")
    zones = ctk.CTkComboBox(
        button_frame, values=['1', '2', '3', '4', '5'], text_color='black', font=(FONT_TYPE, BODY))
    zones.grid(row=2, column=1, padx=20, pady=(0, 40), sticky="nw")
    
    q = ctk.CTkLabel(
        button_frame, text=f"Quantitat", text_color='gray', font=(FONT_TYPE, BODY))
    q.grid(row=3, column=1, padx=20, pady=(0, 0), sticky="nw")
    quant = ctk.CTkComboBox(
        button_frame, values=['1', '2', '3', '4', '5'], text_color='black', font=(FONT_TYPE, BODY))
    quant.grid(row=4, column=1, padx=20, pady=(0, 40), sticky="nw")
    
    p = ctk.CTkLabel(
        button_frame, text=f"Preu", text_color='gray', font=(FONT_TYPE, BODY + 4))
    p.grid(row=3, column=0, padx=20, pady=(0, 0), sticky="nw")
    preu_value = ctk.CTkLabel(
        button_frame, text="0,00 €", text_color='black', font=(FONT_TYPE, BODY + 4))
    preu_value.grid(row=4, column=0, padx=20, pady=(0, 40), sticky="nw")

    # Bind the update_price function to the Combobox events
    tticket.bind("<<ComboboxSelected>>", update_price)
    zones.bind("<<ComboboxSelected>>", update_price)
    quant.bind("<<ComboboxSelected>>", update_price)

    b_recarregaTM = ctk.CTkButton(
        button_frame, text="Pagar", height=80, fg_color="#97d700",
        hover_color="#79ac20", text_color='black', font=(FONT_TYPE, BUTTON),
        command=pagar
    )
    b_recarregaTM.grid(row=7, column=0, columnspan=3, padx=5, pady=(5, 5), sticky="nsew")


def frame_ajuda():
    pass

def recarregaTM():
    refresh()

    header = ctk.CTkLabel(
        button_frame, text=f"Resum de compra", text_color='black', font=(FONT_TYPE, BODY))
    header.grid(row=0, column=0, padx=20, pady=(20,20), sticky="nw")

    vigencia = ctk.CTkLabel(
        button_frame, text=f"Número de viatges", text_color='gray', font=(FONT_TYPE, BODY))
    vigencia.grid(row=1, column=0, padx=20, pady=(0,0), sticky="nw")
    vigencia = ctk.CTkLabel(
        button_frame, text=f"Ilimitats", text_color='black', font=(FONT_TYPE, BODY))
    vigencia.grid(row=2, column=0, padx=20, pady=(0,ENTRE_TEXT), sticky="nw")

    trestant = ctk.CTkLabel(
        button_frame, text=f"Validesa", text_color='gray', font=(FONT_TYPE, BODY))
    trestant.grid(row=1, column=1, padx=20, pady=(0,0), sticky="nw")
    trestant = ctk.CTkLabel(
        button_frame, text=f"90 dies des de la \nprimera validació", text_color='black', font=(FONT_TYPE, BODY))
    trestant.grid(row=2, column=1, padx=20, pady=(0,ENTRE_TEXT), sticky="nw")

    viatges = ctk.CTkLabel(
        button_frame, text=f"Títol", text_color='gray', font=(FONT_TYPE, BODY))
    viatges.grid(row=3, column=0, padx=20, pady=(ENTRE_TEXT,ENTRE_TEXT), sticky="nw")
    viatges = ctk.CTkLabel(
        button_frame, text=f"T-jove FM/FN general", text_color='black', font=(FONT_TYPE, BODY+4))
    viatges.grid(row=4, column=0, padx=20, pady=(0,ENTRE_TEXT), sticky="nw")

    viatges = ctk.CTkLabel(
        button_frame, text=f"Preu", text_color='gray', font=(FONT_TYPE, BODY))
    viatges.grid(row=3, column=1, padx=20, pady=(ENTRE_TEXT,ENTRE_TEXT), sticky="nw")
    viatges = ctk.CTkLabel(
        button_frame, text=f"34,15 €", text_color='black', font=(FONT_TYPE, BODY+4))
    viatges.grid(row=4, column=1, padx=20, pady=(0,40), sticky="nw")

    b_recarregaTM = ctk.CTkButton(
        button_frame, text="Pagar", height=80, fg_color="#97d700",
        hover_color="#79ac20", text_color='black', font=(FONT_TYPE, BUTTON),
        command=pagar
    )
    b_recarregaTM.grid(row=6, column=0, columnspan=2, padx=5, pady=(5,5), sticky="nsew")


def pagar():
    refresh()
    success_message = ctk.CTkLabel(
        button_frame, text="Payment Successful!", text_color='green', font=(FONT_TYPE, BODY))
    success_message.grid(row=0, column=0, padx=20, pady=(20, 20), sticky="nw")


def novaTM():
    refresh()

    header = ctk.CTkLabel(
        button_frame, text=f"Nova T-Mobilitat", text_color='black', font=(FONT_TYPE, BODY))
    header.grid(row=0, column=0, padx=20, pady=(20,20), sticky="nw")

    tticket = ctk.CTkLabel(
        button_frame, text=f"Nom", text_color='gray', font=(FONT_TYPE, BODY))
    tticket.grid(row=1, column=0, padx=20, pady=(0,0), sticky="nw")
    tticket = ctk.CTkEntry(
        button_frame, text_color='black',width=250, font=(FONT_TYPE, BODY))
    tticket.grid(row=2, column=0, padx=20, pady=(0,ENTRE_TEXT), sticky="nw")

    zones = ctk.CTkLabel(
        button_frame, text=f"Cognoms", text_color='gray', font=(FONT_TYPE, BODY))
    zones.grid(row=1, column=1, padx=20, pady=(0,0), sticky="nw")
    tticket = ctk.CTkEntry(
        button_frame, text_color='black',width=250, font=(FONT_TYPE, BODY))
    tticket.grid(row=2, column=1, padx=20, pady=(0,ENTRE_TEXT), sticky="nw")

    zones = ctk.CTkLabel(
        button_frame, text=f"Tipus de document", text_color='gray', font=(FONT_TYPE, BODY))
    zones.grid(row=3, column=0, padx=20, pady=(0,0), sticky="nw")

    tticket = ctk.CTkComboBox(
        button_frame, values=['DNI', 'NIE'], text_color='black',width=250, font=(FONT_TYPE, BODY))
    tticket.grid(row=4, column=0, padx=20, pady=(0,ENTRE_TEXT), sticky="nw")

    zones = ctk.CTkLabel(
        button_frame, text=f"Número de document", text_color='gray', font=(FONT_TYPE, BODY))
    zones.grid(row=3, column=1, padx=20, pady=(0,0), sticky="nw")
    tticket = ctk.CTkEntry(
        button_frame, text_color='black',width=250, font=(FONT_TYPE, BODY))
    tticket.grid(row=4, column=1, padx=20, pady=(0,ENTRE_TEXT), sticky="nw")

    zones = ctk.CTkLabel(
        button_frame, text=f"Data de naixement", text_color='gray', font=(FONT_TYPE, BODY))
    zones.grid(row=5, column=0, padx=20, pady=(0,0), sticky="nw")
    tticket = ctk.CTkEntry(
        button_frame, text_color='black',width=250, font=(FONT_TYPE, BODY))
    tticket.grid(row=6, column=0, padx=20, pady=(0,10), sticky="nw")

    b_recarregaTM = ctk.CTkButton(
        button_frame, text="Següent", height=80, fg_color="#97d700",
        hover_color="#79ac20", text_color='black', font=(FONT_TYPE, BUTTON),
        command=pagar
    )
    b_recarregaTM.grid(row=7, column=0, columnspan=2, padx=5, pady=(5,5), sticky="nsew")


def frame_noTincTM():
    # Clear the existing widgets in the button frame
    refresh()

    new_button1 = ctk.CTkLabel(
        button_frame, text=f"Que t'agradaria fer?", text_color='black', height=80, font=(FONT_TYPE, BODY))
    new_button1.grid(row=0, column=0, columnspan=2, padx=5, pady=5, sticky="nsew")

    # Add new button options
    new_button1 = ctk.CTkButton(
        button_frame, text="Crear nova\nT-Mobilitat", height=180, fg_color="#97d700",
        hover_color="#79ac20", text_color='black', font=(FONT_TYPE, BUTTON),
        command=novaTM)
    new_button1.grid(row=1, column=0, padx=5, pady=5, sticky="nsew")
    
    new_button2 = ctk.CTkButton(
        button_frame, text="Comprar títol\nsenzill", height=180, fg_color="#97d700",
        hover_color="#79ac20", text_color='black', font=(FONT_TYPE, BUTTON),
        command=comprarTM)
    new_button2.grid(row=1, column=1, padx=5, pady=5, sticky="nsew")

def reset_main_menu():
    # Clear the existing widgets in the button frame
    for widget in button_frame.winfo_children():
        widget.destroy()
    
    # Add the original buttons back
    b_tincTM = ctk.CTkButton(
        button_frame, text="Carregar\nT-Mobilitat", height=180, fg_color="#97d700",
        hover_color="#79ac20", text_color='black', font=(FONT_TYPE, BUTTON),
        command=frame_tincTM
    )
    b_tincTM.grid(row=0, column=0, padx=5, pady=5, sticky="nsew")

    b_noTincTM = ctk.CTkButton(
        button_frame, text="Nou Títol", height=180, fg_color="#97d700",
        hover_color="#79ac20", text_color='black', font=(FONT_TYPE, BUTTON),
        command=lambda: print("Nou Títol")
    )
    b_noTincTM.grid(row=0, column=1, padx=5, pady=5, sticky="nsew")

    b_ajuda = ctk.CTkButton(
        button_frame, text="✨Ajuda", height=80, fg_color="#049d84",
        hover_color="#047c70", text_color='black', font=(FONT_TYPE, BUTTON),
        command=lambda: print("Ajuda")
    )
    b_ajuda.grid(row=1, column=0, columnspan=2, padx=5, pady=5, sticky="nsew")


def main_menu():
    button_frame.grid(row=1, column=0, columnspan=2, sticky="nsew")
    button_frame.columnconfigure(0, weight=1)
    button_frame.columnconfigure(1, weight=1)
    '''button_frame.rowconfigure(0, weight=1)
    button_frame.rowconfigure(1, weight=1)'''

    # Initial buttons
    b_tincTM = ctk.CTkButton(
        button_frame, text="Tinc la\nT-Mobilitat", height=250, fg_color="#97d700",
        hover_color="#79ac20", text_color='black', font=(FONT_TYPE, BUTTON),
        command=frame_tincTM)
    b_tincTM.grid(row=0, column=0, padx=5, pady=5, sticky="nsew")

    b_noTincTM = ctk.CTkButton(
        button_frame, text="Nou Títol", height=250, fg_color="#97d700",
        hover_color="#79ac20", text_color='black', font=(FONT_TYPE, BUTTON),
        command=frame_noTincTM
    )
    b_noTincTM.grid(row=0, column=1, padx=5, pady=5, sticky="nsew")

    b_ajuda = ctk.CTkButton(
        button_frame, text="✨Ajuda", height=80, fg_color="#049d84",
        hover_color="#047c70", text_color='black', font=(FONT_TYPE, BUTTON),
        command=frame_ajuda
    )
    b_ajuda.grid(row=1, column=0, columnspan=2, padx=5, pady=5, sticky="nsew")


# HEADER FRAME
header_frame = ttk.Frame(root, padding=(PADDING, PADDING, 0, 5))
header_frame.grid(row=0, column=0, columnspan=2, sticky="ew")

# HEADER IMAGE
img = Image.open(IMAGE_PATH)
img = img.resize((int(img.width / 1.6), int(img.height / 1.6)))  # Resize the image if necessary
photo = ImageTk.PhotoImage(img)
img_label = tk.Label(header_frame, image=photo)
img_label.pack(side="left", padx=(20, 50))

# HEADER TEXT
header_label = ttk.Label(header_frame, text="Nou Sistema de venda de títols de transport", font=(FONT_TYPE, HEADER))
header_label.pack(side="left", padx=(10, 10))

# MAIN MENU BUTTONS
button_frame = ttk.Frame(root, padding=PADDING)

main_menu()

# FOOTER FRAME
footer_frame = ttk.Frame(root, padding=(5, PADDING, 0, PADDING))
footer_frame.grid(row=2, column=0, columnspan=2, sticky="ew")

# FOOTER LABEL
footer_label = ctk.CTkLabel(
    footer_frame, text="Aplicació dissenyada a la UAB The Hack per Samya, Yeray, Gabriel i Bruno",
    text_color='gray', font=(FONT_TYPE, FOOTER)
)
footer_label.pack()

# Ensure the main window and grid resize properly
root.grid_rowconfigure(1, weight=1)
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)

# Start the Tkinter main loop
root.mainloop()

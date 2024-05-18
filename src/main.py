import tkinter as tk
from tkinter import ttk
import customtkinter as ctk
from PIL import Image, ImageTk

from assets.utils import *

# Constants for styling
FONT_TYPE = "Arial"
BODY = 30
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

def ahead_behind_buttons():
    pass

def frame_tincTM():
    pass

def frame_ajuda():
    pass
def refresh():
    for widget in button_frame.winfo_children():
        widget.destroy()
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
        command=lambda: carregarTM
    )
    new_button1.grid(row=1, column=0, padx=5, pady=5, sticky="nsew")
    
    new_button2 = ctk.CTkButton(
        button_frame, text="Comprar títol\nSenzill", height=180, fg_color="#97d700",
        hover_color="#79ac20", text_color='black', font=(FONT_TYPE, BUTTON),
        command=lambda: abandonarTM
    )
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
    button_frame.rowconfigure(0, weight=1)
    button_frame.rowconfigure(1, weight=1)

    # Initial buttons
    b_tincTM = ctk.CTkButton(
        button_frame, text="Tinc la\nT-Mobilitat", height=180, fg_color="#97d700",
        hover_color="#79ac20", text_color='black', font=(FONT_TYPE, BUTTON),
        command=frame_tincTM
    )
    b_tincTM.grid(row=0, column=0, padx=5, pady=5, sticky="nsew")

    b_noTincTM = ctk.CTkButton(
        button_frame, text="Nou Títol", height=180, fg_color="#97d700",
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
header_frame = ttk.Frame(root, padding=PADDING)
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
footer_frame = ttk.Frame(root, padding=PADDING)
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

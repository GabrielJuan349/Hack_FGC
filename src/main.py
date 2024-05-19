import tkinter as tk
from tkinter import ttk
import customtkinter as ctk
from PIL import Image, ImageTk

from assets.utils import *
from rpi.recognizer import Recognizer
from rpi.server_communication import ServerCommunication

# Constants for styling
FONT_TYPE = "Arial"
ENTRE_TEXT = 15
BODY = 25
SUBBODY = 20
BUTTON = 40
HEADER = 20
FOOTER = 12
PADDING = 10
IMAGE_PATH = "assets/logo-fgc.png"  # Replace with your image path
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
    recarrega = True
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
        button_frame, values=['1', '2'], text_color='black', font=(FONT_TYPE, BODY))
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

    def comprarTMresume():
        gi = Get_info()
        all_tickets = gi.get_tickets("Lleida - La Pobla de Segur")    
        price = gi.get_ticket("Lleida - La Pobla de Segur", str(tticket.get()), int(zones.get()), int(quant.get()))
        print(str(tticket.get()), int(zones.get()), quant.get())

        p = ctk.CTkLabel(
            button_frame, text=f"Preu", text_color='gray', font=(FONT_TYPE, BODY + 4))
        p.grid(row=3, column=0, padx=20, pady=(0, 0), sticky="nw")
        preu_value = ctk.CTkLabel(
            button_frame, text=f"{price} €", text_color='black', font=(FONT_TYPE, BODY + 4))
        preu_value.grid(row=4, column=0, padx=20, pady=(0, 40), sticky="nw")

        b_recarregaTM = ctk.CTkButton(
            button_frame, text="Pagar", height=80, fg_color="#97d700",
            hover_color="#79ac20", text_color='black', font=(FONT_TYPE, BUTTON),
            command=pagar
        )
        b_recarregaTM.grid(row=7, column=0, columnspan=3, padx=5, pady=(5, 5), sticky="nsew")

    b_recarregaTM = ctk.CTkButton(
        button_frame, text="Resum", height=80, fg_color="#97d700",
        hover_color="#79ac20", text_color='black', font=(FONT_TYPE, BUTTON),
        command=comprarTMresume
    )
    b_recarregaTM.grid(row=7, column=0, columnspan=3, padx=5, pady=(5, 5), sticky="nsew")

    def comprarTMresume():
        gi = Get_info()
        all_tickets = gi.get_tickets("Lleida - La Pobla de Segur")    
        price = gi.get_ticket("Lleida - La Pobla de Segur", str(tticket.get()), int(zones.get()), int(quant.get()))
        print(str(tticket.get()), int(zones.get()), quant.get())

        p = ctk.CTkLabel(
            button_frame, text=f"Preu", text_color='gray', font=(FONT_TYPE, BODY + 4))
        p.grid(row=3, column=0, padx=20, pady=(0, 0), sticky="nw")
        preu_value = ctk.CTkLabel(
            button_frame, text=f"{price} €", text_color='black', font=(FONT_TYPE, BODY + 4))
        preu_value.grid(row=4, column=0, padx=20, pady=(0, 40), sticky="nw")

        b_recarregaTM = ctk.CTkButton(
            button_frame, text="Pagar", height=80, fg_color="#97d700",
            hover_color="#79ac20", text_color='black', font=(FONT_TYPE, BUTTON),
            command=comprarTMresume
        )
        b_recarregaTM.grid(row=7, column=0, columnspan=3, padx=5, pady=(5, 5), sticky="nsew")


def play_audio_from_base64(audio_base64, type="mp3"):
    import base64
    import pydub
    from pydub import AudioSegment
    from pydub.playback import play

    # Convert the base64 audio to a .wav file
    audio_data = base64.b64decode(audio_base64)
    if type == "wav":
        with open("audio.wav", "wb") as file:
            file.write(audio_data)
    else:
        with open("audio.mp3", "wb") as file:
            file.write(audio_data)

    # Play the audio
    if type == "wav":
        audio = AudioSegment.from_wav("audio.wav")
    else:
        audio = AudioSegment.from_mp3("audio.mp3")
    
    play(audio)

recognizer = Recognizer(duration=2)


waiting_response = False

def listen_to_user(options, onlistencallback, onstopcallback):
    print("Listening to user...")
    base64_audio = recognizer.recognize_speech_from_mic(onlistencallback=onlistencallback, onstopcallback=onstopcallback)

    print("Sending audio to the server...")
    
    # play_audio_from_base64(base64_audio, type="wav")

    print("Audio has been played")

    global waiting_response
    waiting_response = True
    # Example usage
    server_communication = ServerCommunication({'host': 'http://127.0.0.1:8000', 'endpoint': 'call_gemini'})

    response = server_communication.call_server(frame="frame", location="location",
                                                audio=base64_audio, options=options)
    
    print(response)
    waiting_response = False

    return response

stop_listening = False

def my_mainloop():

    options = {
    }
    global info_text

    def onlistencallback():
        print("Listening...")
        info_text.configure(text="Listening to you.")
        # text = ctk.CTkLabel(
        #             button_frame, text="Listening to you.", text_color='black', font=(FONT_TYPE, BODY))
        
        # # put on the middle of the screen
        # text.place(x=20, y=20)
        stop_listening = True

    def onstopcallback():
        print("Stopped listening...")
        info_text.configure(text="Stopped listening.")
        # text = ctk.CTkLabel(
        #             button_frame, text="Stopped listening.", text_color='black', font=(FONT_TYPE, BODY))
        
        # # put on the middle of the screen
        # text.place(x=20, y=20)
        stop_listening = False

    if not stop_listening:

        response = listen_to_user(options, onlistencallback, onstopcallback)

        if waiting_response:
            print("Waiting for response")
            root.after(10, my_mainloop)

        if response is None:
            print("Error")
            # add an error message to the screen

            text = ctk.CTkLabel(
                button_frame, text="Error", text_color='red', font=(FONT_TYPE, BODY))
            text.place(x=20, y=20)

            root.after(10, my_mainloop)  # run again after 1000ms (1s)


        if "audio" not in response or response["audio"] is None:
            print("Error")
            # add an error message to the screen

            text = ctk.CTkLabel(
                button_frame, text="Error", text_color='red', font=(FONT_TYPE, BODY))
            text.place(x=20, y=20)

            root.after(10, my_mainloop)  # run again after 1000ms (1s)

            return

        else:

            print("Playing audio")
            print(response)

            # text = ctk.CTkLabel(
            #     button_frame, text="Playing", text_color='red', font=(FONT_TYPE, BODY))
            # text.place(x=20, y=190)

            text = ctk.CTkLabel(
                button_frame, text=response["plain_text"], text_color='black', font=(FONT_TYPE, BODY))
            text.place(x=20, y=200)

            play_audio_from_base64(response["audio"])

            if response["action"] != "just_talk":
                if response["action"] == "go_to_payment":
                    recarregaTM()

        root.after(10, my_mainloop)  # run again after 1000ms (1s)
    
    else:
        print("I am listening already")
        root.after(10, my_mainloop)
        
            
 

def frame_ajuda():
    import requests
    
    options = {
    }
    # make get request to the server to poke the AI so it starts speaking
    response = requests.post("http://127.0.0.1:8000/poke", json=options)
    
    # play the audio
    json = response.json()

    if json["audio"] is None:
        print("Error")
        # add an error message to the screen

        text = ctk.CTkLabel(
            button_frame, text="Error", text_color='red', font=(FONT_TYPE, BODY))
        text.place(x=20, y=20)

    # text = ctk.CTkLabel(
    #         button_frame, text="Playing", text_color='red', font=(FONT_TYPE, BODY))
    # text.place(x=0, y=350)

    play_audio_from_base64(json["audio"])

    root.after(200, my_mainloop)
    # 
    
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
        button_frame, text="Gracies per la seva compra!", text_color='green', font=(FONT_TYPE, BUTTON))
    success_message.grid(row=0, column=0, padx=20, pady=(20, 20), sticky="nswe")

def nouSoci():
    refresh()
    success_message = ctk.CTkLabel(
        button_frame, text="Gracies per fer-te\nla T-Mobilitat!", text_color='green', font=(FONT_TYPE, BUTTON))
    success_message.grid(row=0, column=0, padx=20, pady=(20, 20), sticky="nswe")


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
        command=nouSoci
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

info_text = None

def main_menu():
    refresh()
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

    global info_text

    info_text = ctk.CTkLabel(
                    button_frame, text="Listening to you.", text_color='black', font=(FONT_TYPE, BODY))
    
    # put on the middle of the screen
    info_text.place(x=20, y=350)


# HEADER FRAME
header_frame = ttk.Frame(root, padding=(PADDING, PADDING, 0, 5))
header_frame.grid(row=0, column=0, columnspan=2, sticky="ew")

# HEADER IMAGE
img = Image.open(IMAGE_PATH)
img = img.resize((int(img.width / 1.6), int(img.height / 1.6)))  # Resize the image if necessary
photo = ImageTk.PhotoImage(img)
img_label = ctk.CTkButton(header_frame, image=photo, text="", fg_color="white", hover_color="white", command=main_menu)
img_label.pack(side="left", padx=(20, 50))

# HEADER TEXT
header_label = tk.Label(header_frame, text="Nou Sistema de venda de títols de transport", font=(FONT_TYPE, HEADER))
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

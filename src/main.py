import tkinter as tk
from tkinter import ttk

# Create the main application window
root = tk.Tk()
root.title("Tkinter Layout Example")
root.geometry("400x400")  # Set the window size

# Create the header frame
header_frame = ttk.Frame(root, padding="10")
header_frame.grid(row=0, column=0, columnspan=2, sticky="ew")

# Add a label to the header frame
header_label = ttk.Label(header_frame, text="Header", font=("Arial", 16))
header_label.pack()

# Create the grid of buttons (2x2)
button_frame = ttk.Frame(root, padding="10")
button_frame.grid(row=1, column=0, columnspan=2, sticky="nsew")

# Configure the grid layout in the button frame
button_frame.columnconfigure(0, weight=1)
button_frame.columnconfigure(1, weight=1)
button_frame.rowconfigure(0, weight=1)
button_frame.rowconfigure(1, weight=1)

# Add buttons to the button frame
button1 = ttk.Button(button_frame, text="Button 1")
button1.grid(row=0, column=0, padx=5, pady=5, sticky="nsew")

button2 = ttk.Button(button_frame, text="Button 2")
button2.grid(row=0, column=1, padx=5, pady=5, sticky="nsew")

button3 = ttk.Button(button_frame, text="Button 3")
button3.grid(row=1, column=0, padx=5, pady=5, sticky="nsew")

button4 = ttk.Button(button_frame, text="Button 4")
button4.grid(row=1, column=1, padx=5, pady=5, sticky="nsew")

# Create the footer frame
footer_frame = ttk.Frame(root, padding="10")
footer_frame.grid(row=2, column=0, columnspan=2, sticky="ew")

# Add a label to the footer frame
footer_label = ttk.Label(footer_frame, text="Footer", font=("Arial", 12))
footer_label.pack()

# Ensure the main window and grid resize properly
root.grid_rowconfigure(1, weight=1)
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)

# Start the Tkinter main loop
root.mainloop()

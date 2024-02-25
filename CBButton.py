import tkinter as tk
import random
from tkinter import ttk

def copy_to_clipboard(text):
    root.clipboard_clear()
    root.clipboard_append(text)
    root.update()

def create_button(text):
    button_color = "#{:06x}".format(random.randint(0, 0xFFFFFF)) # Generate random color in #RRGGBB format
    button = tk.Button(main_frame, text=text, command=lambda: copy_to_clipboard(text), bg=button_color)
    button.pack(pady=5)
    buttons.append(button)

def add_button():
    text = entry.get()
    if text:
        create_button(text)
        entry.delete(0, tk.END) # Clear the entry field

def clear_buttons():
    for button in buttons:
        button.destroy()
    buttons.clear()

root = tk.Tk()
root.title("Copy text to clipboard")

main_frame = tk.Frame(root)
main_frame.pack(padx=20, pady=20)

entry_label = tk.Label(main_frame, text="Button text:")
entry_label.pack()

entry = tk.Entry(main_frame, width=30)
entry.pack(pady=5)

add_button_button = tk.Button(main_frame, text="Add button", command=add_button)
add_button_button.pack(pady=5)

clear_buttons_button = tk.Button(main_frame, text="Clear all buttons", command=clear_buttons)
clear_buttons_button.pack(pady=5)

buttons = []

root.mainloop()

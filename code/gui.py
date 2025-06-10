# gui.py
# Interfaz gráfica principal con Tkinter, actualizada para respetar saltos de línea.

import tkinter as tk
from tkinter import scrolledtext, messagebox
from translator import Translator
import file_handler

def run_gui():
    root = tk.Tk()
    root.title("MorsePy - Traductor sin diccionarios")
    root.geometry("900x500")
    root.resizable(True, True)

    translator = Translator()

    def translate_text_to_morse():
        # Traduce línea por línea
        text = input_box.get("1.0", tk.END)
        result = translator.text_to_morse(text)
        output_box.delete("1.0", tk.END)
        output_box.insert(tk.END, result)

    def translate_morse_to_text():
        # Traduce línea por línea
        morse = input_box.get("1.0", tk.END)
        result = translator.morse_to_text(morse)
        output_box.delete("1.0", tk.END)
        output_box.insert(tk.END, result)

    def load_file():
        content = file_handler.load_text()
        if content:
            input_box.delete("1.0", tk.END)
            input_box.insert(tk.END, content)

    def save_file():
        content = output_box.get("1.0", tk.END)
        if file_handler.save_text(content):
            messagebox.showinfo("Éxito", "Archivo guardado correctamente.")

    def limpiar_entrada_salida():
        input_box.delete("1.0", tk.END)
        output_box.delete("1.0", tk.END)

    # Layout
    top_frame = tk.Frame(root)
    top_frame.pack(fill=tk.X, pady=5)

    button_frame = tk.Frame(top_frame)
    button_frame.pack(anchor="center")

    btn_style = {"padx": 6, "pady": 3}

    tk.Button(button_frame, text="📁 Cargar archivo", command=load_file).pack(side=tk.LEFT, **btn_style)
    tk.Button(button_frame, text="🔤 Texto a Morse", command=translate_text_to_morse).pack(side=tk.LEFT, **btn_style)
    tk.Button(button_frame, text="📡 Morse a Texto", command=translate_morse_to_text).pack(side=tk.LEFT, **btn_style)
    tk.Button(button_frame, text="💾 Guardar", command=save_file).pack(side=tk.LEFT, **btn_style)
    tk.Button(button_frame, text="🧼 Limpiar", command=limpiar_entrada_salida).pack(side=tk.LEFT, **btn_style)
    tk.Button(button_frame, text="❌ Salir", command=root.destroy).pack(side=tk.LEFT, **btn_style)

    middle_frame = tk.Frame(root)
    middle_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)

    input_frame = tk.Frame(middle_frame)
    input_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(0, 5))

    tk.Label(input_frame, text="Entrada", font=('Arial', 10, 'bold')).pack(anchor="w")
    input_box = scrolledtext.ScrolledText(input_frame, wrap=tk.WORD)
    input_box.pack(fill=tk.BOTH, expand=True)

    output_frame = tk.Frame(middle_frame)
    output_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=(5, 0))

    tk.Label(output_frame, text="Salida", font=('Arial', 10, 'bold')).pack(anchor="w")
    output_box = scrolledtext.ScrolledText(output_frame, wrap=tk.WORD)
    output_box.pack(fill=tk.BOTH, expand=True)

    root.mainloop()
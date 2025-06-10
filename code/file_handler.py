# file_handler.py
# Módulo para abrir y guardar archivos desde la interfaz gráfica.

from tkinter import filedialog

def load_text():
    """
    Permite seleccionar un archivo .txt y leer su contenido.
    """
    filepath = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
    if filepath:
        with open(filepath, 'r', encoding='utf-8') as file:
            return file.read()
    return ""

def save_text(text):
    """
    Permite al usuario guardar el resultado en un archivo .txt.
    """
    filepath = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
    if filepath:
        with open(filepath, 'w', encoding='utf-8') as file:
            file.write(text)
        return True
    return False
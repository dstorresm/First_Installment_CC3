# file_handler.py
from tkinter import filedialog

def load_text():
    """
    Abre un cuadro de diálogo para seleccionar un archivo de texto (.txt) y carga su contenido.
    Retorna el contenido del archivo como una cadena.
    Si no se selecciona archivo, retorna una cadena vacía.
    """
    filepath = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
    if filepath:
        with open(filepath, 'r', encoding='utf-8') as file:
            return file.read()
    return ""

def save_text(text):
    """
    Abre un cuadro de diálogo para guardar el texto en un archivo .txt.
    Escribe el contenido recibido en el archivo seleccionado.
    Retorna True si el archivo se guardó correctamente, False en caso contrario.
    """
    filepath = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
    if filepath:
        with open(filepath, 'w', encoding='utf-8') as file:
            file.write(text)
        return True
    return False
# gui.py
# MorsePy - Traductor Morse con GUI

import tkinter as tk
from tkinter import scrolledtext, messagebox
import morse_compiler as morse_dict
import file_handler
import speech_recognition as sr
import unicodedata

def run_gui():
    """
    Inicializa y ejecuta la interfaz gráfica de usuario para el traductor MorsePy.
    Permite traducir entre texto y código Morse, cargar y guardar archivos, 
    limpiar campos, y transcribir audio a texto usando reconocimiento de voz.
    """

    root = tk.Tk()
    root.title("MorsePy - Traductor Morse")
    root.geometry("900x500")
    root.resizable(True, True)

    recognizer = sr.Recognizer()
    mic = sr.Microphone()
    stop_listening = {"value": None}

    # --- Función para detectar símbolos no válidos ---
    def detect_invalid_symbols(text):
        """
        Detecta y retorna los símbolos no válidos en el texto de entrada.
        """
        allowed = "abcdefghijklmnopqrstuvwxyz0123456789.,-()/ "
        raw = unicodedata.normalize('NFD', text.lower().replace('ñ', 'n'))
        ascii_text = raw.encode('ascii', 'ignore').decode('utf-8')
        removed = ''.join(c for c in text if c.lower() not in allowed and not c.isspace() and not c.isalnum())
        return removed

    def translate_text_to_morse():
        """
        Traduce el texto de entrada a código Morse y lo muestra en la salida.
        Advierte si se eliminaron símbolos no válidos.
        """
        text = input_box.get("1.0", tk.END).strip()
        removed = detect_invalid_symbols(text)
        result = morse_dict.compile_to_morse(text)
        output_box.delete("1.0", tk.END)
        output_box.insert(tk.END, result)
        if removed:
            messagebox.showwarning("Símbolos ignorados", f"Se eliminaron estos símbolos no válidos: {removed}")

    def translate_morse_to_text():
        """
        Traduce el código Morse de entrada a texto y lo muestra en la salida.
        """
        morse = input_box.get("1.0", tk.END).strip()
        result = morse_dict.compile_from_morse(morse)
        output_box.delete("1.0", tk.END)
        output_box.insert(tk.END, result)

    def load_file():
        """
        Carga el contenido de un archivo de texto en el área de entrada.
        """
        content = file_handler.load_text()
        if content:
            input_box.delete("1.0", tk.END)
            input_box.insert(tk.END, content)

    def save_file():
        """
        Guarda el contenido del área de salida en un archivo de texto.
        """
        content = output_box.get("1.0", tk.END)
        if file_handler.save_text(content):
            messagebox.showinfo("Éxito", "Archivo guardado correctamente.")

    def start_audio_transcription():
        """
        Inicia la transcripción de audio a texto usando el micrófono y reconocimiento de voz.
        El texto reconocido se inserta en el área de entrada.
        """
        def callback(recognizer, audio):
            try:
                text = recognizer.recognize_google(audio, language='es-ES')
                input_box.insert(tk.END, text + " ")
            except sr.UnknownValueError:
                pass
            except sr.RequestError as e:
                messagebox.showerror("Error de reconocimiento", f"API falló: {e}")

        try:
            with mic as source:
                recognizer.adjust_for_ambient_noise(source)
            stop_listening["value"] = recognizer.listen_in_background(mic, callback)
            messagebox.showinfo("Grabando", "Se ha iniciado la grabación. Puedes hablar...")
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo iniciar el micrófono:\n{e}")

    def stop_audio_transcription():
        """
        Detiene la transcripción de audio si está activa.
        """
        if stop_listening["value"]:
            stop_listening["value"](wait_for_stop=False)
            stop_listening["value"] = None
            messagebox.showinfo("Grabación detenida", "La grabación de voz ha sido detenida.")
        else:
            messagebox.showwarning("No activo", "La grabación no está en curso.")

    def limpiar_entrada_salida():
        """
        Limpia tanto el área de entrada como la de salida.
        """
        input_box.delete("1.0", tk.END)
        output_box.delete("1.0", tk.END)

    # --- GUI Layout ---

    # Top frame con botones centrados
    top_frame = tk.Frame(root)
    top_frame.pack(fill=tk.X, pady=5)

    button_frame = tk.Frame(top_frame)
    button_frame.pack(anchor="center")

    btn_style = {"padx": 6, "pady": 3}

    tk.Button(button_frame, text="📁 Cargar archivo", command=load_file).pack(side=tk.LEFT, **btn_style)
    tk.Button(button_frame, text="🔤 Texto a Morse", command=translate_text_to_morse).pack(side=tk.LEFT, **btn_style)
    tk.Button(button_frame, text="📡 Morse a Texto", command=translate_morse_to_text).pack(side=tk.LEFT, **btn_style)
    tk.Button(button_frame, text="🎤 Iniciar Audio", command=start_audio_transcription).pack(side=tk.LEFT, **btn_style)
    tk.Button(button_frame, text="🛑 Finalizar Audio", command=stop_audio_transcription).pack(side=tk.LEFT, **btn_style)
    tk.Button(button_frame, text="💾 Guardar", command=save_file).pack(side=tk.LEFT, **btn_style)
    tk.Button(button_frame, text="🧼 Limpiar", command=limpiar_entrada_salida).pack(side=tk.LEFT, **btn_style)
    tk.Button(button_frame, text="❌ Salir", command=root.destroy).pack(side=tk.LEFT, **btn_style)

    # Middle frame para entrada/salida
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
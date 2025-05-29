MorsePy: Traductor de Código Morse con Interfaz Gráfica y Reconocimiento de Voz

📖 Descripción

MorsePy es una aplicación de escritorio desarrollada en Python que permite traducir entre texto natural y código Morse de forma precisa. Cuenta con una interfaz gráfica intuitiva basada en Tkinter, validación de entrada mediante máquinas de estado, limpieza automática de acentos y símbolos no soportados, y transcripción por voz en tiempo real usando Google Speech Recognition.

🚀 Características Principales

Traducción Texto → Morse con limpieza de tildes y símbolos.

Traducción Morse → Texto, incluyendo soporte para puntuación básica.

Entrada por voz sin límite de tiempo: lo hablado se transcribe al panel de entrada.

Lectura desde archivos .txt y guardado de resultados.

Limpieza rápida del contenido de entrada y salida.

Interfaz gráfica adaptable, centrada y con botones organizados.

Módulo de compilación con lexer, parser y máquina de estados.

📁 Estructura del Proyecto

morsepy/
├── main.py                 # Lanza la interfaz gráfica
├── gui.py                  # Interfaz gráfica con Tkinter
├── morse_compiler.py       # Módulo principal de traducción
├── morse_dict.py           # Diccionario básico (alternativo)
├── file_handler.py         # Manejador de archivos
├── audio_module.py         # Grabación y decodificación de audio (no usado en GUI final)
├── README.md               # Este archivo
└── requirements.txt        # Librerías necesarias

🔧 Requisitos

Python >= 3.9

Librerías necesarias: pip install SpeechRecognition sounddevice pyaudio numpy
En Windows: pip install pipwin pipwin install pyaudio

⚖️ Uso

Ejecuta el programa con: python main.py

Usa los botones para:

Escribir texto y traducir a Morse.

Dictar por micrófono (sin límite de tiempo).

Leer o guardar archivos .txt.

Convertir Morse a texto.

Limpiar todo el contenido.

✉️ Contacto y Licencia

Proyecto educativo con fines didácticos. Uso libre.
Desarrollado por: David Santiago Torres Mendieta, Universidad Distrital Francisco José de Caldas, Ingeniería de Sistemas
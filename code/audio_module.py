# audio_module.py
# Reconocimiento de audio básico para convertir a código Morse

import numpy as np
import sounddevice as sd

def record_audio(duration=3, fs=44100):
    """
    Graba audio desde el micrófono durante un tiempo determinado.
    Args:
        duration (int): Duración de la grabación en segundos (por defecto 3).
        fs (int): Frecuencia de muestreo en Hz (por defecto 44100).
    Returns:
        np.ndarray: Array unidimensional con los datos de audio grabados.
    """
    print("Grabando audio...")
    audio = sd.rec(int(duration * fs), samplerate=fs, channels=1)
    sd.wait()
    return audio.flatten()

def detect_morse_from_audio(audio, threshold=0.02, short_pulse=2000):
    """
    Detecta señales de código Morse a partir de un array de audio.
    Args:
        audio (np.ndarray): Array de audio grabado.
        threshold (float): Umbral para considerar si hay sonido.
        short_pulse (int): Número de muestras para distinguir punto de raya.
    Returns:
        str: Cadena con la secuencia Morse detectada ('.' para punto, '-' para raya).
    """
    morse = ""
    sound_on = False
    count = 0
    for sample in audio:
        if abs(sample) > threshold:
            count += 1
            sound_on = True
        else:
            if sound_on:
                if count < short_pulse:
                    morse += '.'
                else:
                    morse += '-'
                sound_on = False
                count = 0
            morse += ' '  # separador entre señales
    return morse.strip()
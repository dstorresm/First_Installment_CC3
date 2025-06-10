# lexer.py
# Analizador léxico: identifica caracteres válidos en texto y morse.
import re

class Lexer:
    """
    Analizador léxico.
    Detecta patrones válidos en el texto o en el morse según gramáticas básicas.
    """

    def __init__(self):
        # Gramática para texto natural: letras, números, puntuación básica y espacio
        self.text_pattern = re.compile(r'^[a-zA-Z0-9.,\-()/ ]+$')
        # Gramática para código Morse: puntos, rayas, espacio y separador "/"
        self.morse_pattern = re.compile(r'^[\.\- /]+$')

    def validate_text(self, text):
        """
        Verifica si el texto cumple con la gramática definida.
        """
        return bool(self.text_pattern.fullmatch(text))

    def validate_morse(self, morse):
        """
        Verifica si el morse cumple con la gramática definida.
        """
        return bool(self.morse_pattern.fullmatch(morse))
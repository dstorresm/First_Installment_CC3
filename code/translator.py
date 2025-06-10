# translator.py
# Controlador principal que ahora permite caracteres especiales "sin modificar"
# en la traducción en ambas direcciones.

from lexer import Lexer
from semantic import Semantic
import unicodedata

class Translator:
    """
    Traducción bidireccional que:
    - Convierte ñ → n y elimina tildes
    - Respeta saltos de línea
    - Copia caracteres especiales tal cual sin traducirlos
    """

    def __init__(self):
        self.lexer = Lexer()
        self.semantic = Semantic()

    def clean_text(self, text):
        """
        Elimina tildes y reemplaza ñ por n.
        Mantiene caracteres especiales sin modificar.
        """
        text = text.lower().replace('ñ', 'n')
        # Elimina tildes usando normalización
        text = unicodedata.normalize('NFD', text).encode('ascii', 'ignore').decode('utf-8')
        return text.upper()

    def text_to_morse(self, text):
        """
        Traduce texto a morse línea por línea.
        Copia caracteres especiales directamente sin intentar traducirlos.
        """
        lines = text.splitlines()
        translated_lines = []

        for line in lines:
            cleaned_line = self.clean_text(line.strip())
            if not cleaned_line:
                translated_lines.append('')
                continue

            morse_line = []
            for char in cleaned_line:
                # Verifica si el carácter es válido para traducir a morse
                if self.lexer.validate_text(char):
                    morse_char = self.semantic.char_to_morse(char)
                    if morse_char:
                        morse_line.append(morse_char)
                else:
                    # Carácter especial, lo deja igual
                    morse_line.append(char)
            translated_lines.append(' '.join(morse_line))

        return '\n'.join(translated_lines)

    def morse_to_text(self, morse):
        """
        Traduce morse a texto, línea por línea.
        Copia caracteres especiales directamente sin intentar traducirlos.
        """
        lines = morse.splitlines()
        translated_lines = []

        for line in lines:
            cleaned_line = line.strip()
            if not cleaned_line:
                translated_lines.append('')
                continue

            words = cleaned_line.split(' / ')
            text_words = []
            for word in words:
                letters = word.strip().split()
                word_text = ''
                for letter in letters:
                    # Si es un carácter especial, lo dejamos igual
                    if not all(c in '.-/' for c in letter):
                        word_text += letter
                    else:
                        word_text += self.semantic.morse_to_char(letter)
                text_words.append(word_text)
            translated_lines.append(' '.join(text_words))

        return '\n'.join(translated_lines)

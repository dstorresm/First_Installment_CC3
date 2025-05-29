# morse_dict.py
# Diccionario de traducción Morse <-> Texto

# Diccionario que asocia cada carácter permitido con su representación en código Morse.
MORSE_CODE_DICT = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
    'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
    'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
    'Z': '--..', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
    '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.',
    '0': '-----', ',': '--..--', '.': '.-.-.-', '?': '..--..', '/': '-..-.',
    '-': '-....-', '(': '-.--.', ')': '-.--.-', ' ': '/'
}

# Diccionario inverso para decodificar de Morse a texto.
INVERSE_MORSE_CODE_DICT = {v: k for k, v in MORSE_CODE_DICT.items()}

def text_to_morse(text):
    """
    Convierte una cadena de texto a código Morse.
    Solo traduce los caracteres presentes en el diccionario MORSE_CODE_DICT.
    Los caracteres no reconocidos se omiten.
    """
    return ' '.join(MORSE_CODE_DICT.get(c.upper(), '') for c in text if c.upper() in MORSE_CODE_DICT)

def morse_to_text(morse):
    """
    Convierte una cadena en código Morse a texto.
    Separa las palabras por ' / ' y los caracteres por espacios.
    Los códigos no reconocidos se omiten.
    """
    return ' '.join(''.join(INVERSE_MORSE_CODE_DICT.get(code, '') for code in word.split()) for word in morse.split(' / '))
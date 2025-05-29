# morse_compiler.py

import unicodedata
import re

# Diccionario Morse: Asocia cada carácter permitido con su representación en código Morse.
MORSE_CODE_DICT = {
    'A': '.-',    'B': '-...',  'C': '-.-.',  'D': '-..',   'E': '.',
    'F': '..-.',  'G': '--.',   'H': '....',  'I': '..',    'J': '.---',
    'K': '-.-',   'L': '.-..',  'M': '--',    'N': '-.',    'O': '---',
    'P': '.--.',  'Q': '--.-',  'R': '.-.',   'S': '...',   'T': '-',
    'U': '..-',   'V': '...-',  'W': '.--',   'X': '-..-',  'Y': '-.--',
    'Z': '--..',
    '0': '-----', '1': '.----', '2': '..---','3': '...--', '4': '....-',
    '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.',
    '.': '.-.-.-', ',': '--..--', '?': '..--..', '-': '-....-', '/': '-..-.',
    '(': '-.--.', ')': '-.--.-', ' ': '/'
}

# Diccionario inverso: Permite decodificar de Morse a texto.
INVERSE_MORSE_CODE_DICT = {v: k for k, v in MORSE_CODE_DICT.items()}

# --- Paso 1: Normalización ---
def normalize_text(text):
    """
    Normaliza el texto de entrada:
    - Convierte a minúsculas y reemplaza 'ñ' por 'n'.
    - Elimina acentos y caracteres especiales.
    - Filtra solo los caracteres permitidos.
    - Devuelve el texto en mayúsculas.
    """
    text = text.lower().replace('ñ', 'n')
    text = unicodedata.normalize('NFD', text)
    text = text.encode('ascii', 'ignore').decode('utf-8')
    allowed_chars = "abcdefghijklmnopqrstuvwxyz0123456789.,-()/ "
    filtered_text = ''.join(c for c in text if c in allowed_chars)
    return filtered_text.upper()

# --- Paso 2: Lexer ---
def lexer(text):
    """
    Convierte el texto en una lista de tokens.
    Cada carácter permitido se agrega como token, los espacios como ' ', y los no permitidos como '[INVALID]'.
    """
    tokens = []
    for char in text.upper():
        if char in MORSE_CODE_DICT:
            tokens.append(char)
        elif char.isspace():
            tokens.append(' ')
        else:
            tokens.append('[INVALID]')
    return tokens

# --- Paso 3: Máquina de estado para validación léxica ---
class MorseStateMachine:
    """
    Máquina de estados finitos para validar la secuencia de tokens.
    Cambia a estado 'error' si encuentra un token inválido.
    """
    def __init__(self):
        self.state = 'start'
    
    def validate(self, tokens):
        for token in tokens:
            if token == '[INVALID]':
                self.state = 'error'
                break
        if self.state != 'error':
            self.state = 'valid'
        return self.state

# --- Paso 4: Gramática generativa (parser básico) ---
def parse_grammar(tokens):
    """
    Valida la secuencia de tokens usando una expresión regular.
    Solo permite letras, números y signos de puntuación definidos.
    """
    pattern = re.compile(r'^([A-Z0-9 .,?\-/()]|\s)+$')
    joined = ''.join(tokens).replace('[INVALID]', '')
    return bool(pattern.fullmatch(joined))

# --- Paso 5: Compilación texto → morse ---
def compile_to_morse(text):
    """
    Convierte texto normalizado a código Morse.
    Realiza normalización, tokenización, validación y compilación.
    Devuelve el código Morse o un mensaje de error si hay caracteres inválidos.
    """
    normalized = normalize_text(text)
    tokens = lexer(normalized)
    fsm = MorseStateMachine()
    state = fsm.validate(tokens)

    if state != 'valid' or not parse_grammar(tokens):
        return "Error: Entrada contiene caracteres no válidos o estructura incorrecta."

    morse = []
    for token in tokens:
        if token == ' ':
            morse.append('/')
        else:
            morse.append(MORSE_CODE_DICT.get(token, ''))
    return ' '.join(morse)

# --- Paso 6: Compilación morse → texto ---
def compile_from_morse(morse):
    """
    Convierte código Morse a texto.
    Separa palabras y caracteres, decodifica cada uno y maneja errores de formato.
    Devuelve el texto decodificado o un mensaje de error si el código es inválido.
    """
    try:
        words = morse.strip().split(' / ')
        decoded = []
        for word in words:
            chars = word.split()
            decoded.append(''.join(INVERSE_MORSE_CODE_DICT.get(c, '?') for c in chars))
        return ' '.join(decoded)
    except Exception:
        return "Error: Código Morse inválido o mal estructurado."
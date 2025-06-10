# semantic.py
# Analizador semántico: convierte texto a morse y viceversa sin usar diccionarios.

class Semantic:
    """
    Analizador semántico que asocia letras, números y símbolos con
    su equivalente en código Morse (y viceversa) sin usar diccionarios.
    """

    def char_to_morse(self, char):
        """
        Traduce un carácter a código Morse manualmente.
        """
        char = char.upper()
        if char == 'A': return '.-'
        if char == 'B': return '-...'
        if char == 'C': return '-.-.'
        if char == 'D': return '-..'
        if char == 'E': return '.'
        if char == 'F': return '..-.'
        if char == 'G': return '--.'
        if char == 'H': return '....'
        if char == 'I': return '..'
        if char == 'J': return '.---'
        if char == 'K': return '-.-'
        if char == 'L': return '.-..'
        if char == 'M': return '--'
        if char == 'N': return '-.'
        if char == 'O': return '---'
        if char == 'P': return '.--.'
        if char == 'Q': return '--.-'
        if char == 'R': return '.-.'
        if char == 'S': return '...'
        if char == 'T': return '-'
        if char == 'U': return '..-'
        if char == 'V': return '...-'
        if char == 'W': return '.--'
        if char == 'X': return '-..-'
        if char == 'Y': return '-.--'
        if char == 'Z': return '--..'
        if char == '1': return '.----'
        if char == '2': return '..---'
        if char == '3': return '...--'
        if char == '4': return '....-'
        if char == '5': return '.....'
        if char == '6': return '-....'
        if char == '7': return '--...'
        if char == '8': return '---..'
        if char == '9': return '----.'
        if char == '0': return '-----'
        if char == '.': return '.-.-.-'
        if char == ',': return '--..--'
        if char == '?': return '..--..'
        if char == '-': return '-....-'
        if char == '/': return '-..-.'
        if char == '(': return '-.--.'
        if char == ')': return '-.--.-'
        if char == ' ': return '/'
        return ''  # Ignora otros caracteres

    def morse_to_char(self, morse_char):
        """
        Traduce una secuencia Morse a su carácter equivalente.
        """
        if morse_char == '.-': return 'A'
        if morse_char == '-...': return 'B'
        if morse_char == '-.-.': return 'C'
        if morse_char == '-..': return 'D'
        if morse_char == '.': return 'E'
        if morse_char == '..-.': return 'F'
        if morse_char == '--.': return 'G'
        if morse_char == '....': return 'H'
        if morse_char == '..': return 'I'
        if morse_char == '.---': return 'J'
        if morse_char == '-.-': return 'K'
        if morse_char == '.-..': return 'L'
        if morse_char == '--': return 'M'
        if morse_char == '-.': return 'N'
        if morse_char == '---': return 'O'
        if morse_char == '.--.': return 'P'
        if morse_char == '--.-': return 'Q'
        if morse_char == '.-.': return 'R'
        if morse_char == '...': return 'S'
        if morse_char == '-': return 'T'
        if morse_char == '..-': return 'U'
        if morse_char == '...-': return 'V'
        if morse_char == '.--': return 'W'
        if morse_char == '-..-': return 'X'
        if morse_char == '-.--': return 'Y'
        if morse_char == '--..': return 'Z'
        if morse_char == '.----': return '1'
        if morse_char == '..---': return '2'
        if morse_char == '...--': return '3'
        if morse_char == '....-': return '4'
        if morse_char == '.....': return '5'
        if morse_char == '-....': return '6'
        if morse_char == '--...': return '7'
        if morse_char == '---..': return '8'
        if morse_char == '----.': return '9'
        if morse_char == '-----': return '0'
        if morse_char == '.-.-.-': return '.'
        if morse_char == '--..--': return ','
        if morse_char == '..--..': return '?'
        if morse_char == '-....-': return '-'
        if morse_char == '-..-.': return '/'
        if morse_char == '-.--.': return '('
        if morse_char == '-.--.-': return ')'
        if morse_char == '/': return ' '
        return '?'  # Marca caracteres no reconocidos
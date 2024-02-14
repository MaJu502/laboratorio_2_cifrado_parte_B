# Universidad del Valle de Guatemala
# Cifrado de información
# Laboratorio#2

def word_to_binary(word):
    ascii_repr = []
    
    for letra in word:
        ascii_repr.append(ord(letra))
    
    binary = ""
    
    for num in ascii_repr:
        binary += int_to_binary(num)
    
    return binary
        
def int_to_binary(num):
    if num == 0:
        return '0'
    
    binary = ''
    while num > 0:
        residuo = num % 2
        binary = str(residuo) + binary
        num //= 2
    
    binary = binary.zfill(8)

    return binary

def binary_to_int(binary):
    decimal = 0
    longitud = len(binary)

    for i in range(longitud):
        bit = int(binary[longitud - i - 1])
        decimal += bit * (2 ** i)
        
    return decimal
    
def binary_to_word(binary):
    bloques = []
    
    for i in range(0, len(binary), 8):
        bloque = binary[i:i+8]
        bloques.append(bloque.zfill(8))
    
    word = ""
    for block in bloques:
        word += chr(binary_to_int(block))
        
    return word

def binary_to_base64(binary):
    caracteres_base64 = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
    lista_caracteres_base64 = list(caracteres_base64)
    
    bloques = []
    
    for i in range(0, len(binary), 6):
        bloque = binary[i:i+6]
        bloques.append(bloque + '0' * (6 - len(bloque)))

    binaries = []
    for bloque in bloques:
        binaries.append(binary_to_int(bloque))
    
    base64 = ""
    for i in binaries:
        base64 += lista_caracteres_base64[i]
        
    return base64
    
def base64_to_binary(base64):
    caracteres_base64 = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
    lista_caracteres_base64 = list(caracteres_base64)
    
    num64 = []
    
    for letra in base64:
        num64.append(lista_caracteres_base64.index(letra))

    binary = ""
    for num in num64:
        binary += int_to_binary(num)[2:]
    
    return binary

# ex1 = "Esto es una prueba"
# ex2 = "Texto de ejemplo"

# # Inciso 1
# wordA = word_to_binary(ex1)
# wordA1 = word_to_binary(ex2)

# # Inciso 2
# wordB = binary_to_word(wordA)
# wordB1 = binary_to_word(wordA1)

# # Inciso 3
# wordC = binary_to_base64(wordA)
# wordC1 = binary_to_base64(wordA1)

# # Inciso 4
# wordD = binary_to_word(base64_to_binary(wordC))
# wordD1 = binary_to_word(base64_to_binary(wordC1))

# print()
# print("------------------------------------------------")
# print("--> Inciso 1\n")
# print(f"'{ex1}' se traduce a este binario:\n\n{wordA}")
# print()
# print(f"'{ex2}' se traduce a este binario:\n\n{wordA1}")
# print("\n------------------------------------------------")
# print("--> Inciso 2\n")
# print(f"'{wordA}' se traduce a este texto:\n\n'{wordB}'")
# print()
# print(f"'{wordA1}' se traduce a este texto:\n\n'{wordB1}'")
# print("\n------------------------------------------------")
# print("--> Inciso 3\n")
# print(f"'{ex1}' se traduce a esta base64:\n\n'{wordC}'")
# print()
# print(f"'{ex2}' se traduce a esta base64:\n\n'{wordC1}'")
# print("\n------------------------------------------------")
# print("--> Inciso 4\n")
# print(f"'{wordC}' se traduce a este texto:\n\n'{wordD}'")
# print()
# print(f"'{wordC1}' se traduce a este texto:\n\n'{wordD1}'")
# print("\n------------------------------------------------\n")



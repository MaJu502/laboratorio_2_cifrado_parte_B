# Universidad del Valle de Guatemala
# Cifrado de información
# Laboratorio#2

import base64
import io
from tools import *
from PIL import Image

def change_with_xor(text, key):    
    newKey = key
    
    if(len(key) > len(text)):
        return
    
    if(len(key) < len(text)):
        newKey = (key * (len(text) // len(key))) + key[:len(text) % len(key)]        
        
    binary_text = word_to_binary(text)
    binary_key = word_to_binary(newKey)
    
    if len(binary_text) != len(binary_key):
        longitud_maxima = max(len(binary_text), len(binary_key))
        binary_text = binary_text.zfill(longitud_maxima)
        binary_key = binary_key.zfill(longitud_maxima)
    
    xor_encrypt = ''
    for bit1, bit2 in zip(binary_text, binary_key):
        if bit1 != bit2:
            xor_encrypt += '1'
        else:
            xor_encrypt += '0'
    
    return xor_encrypt
    
def imagen_a_bits(ruta_imagen):
    with open(ruta_imagen, "rb") as img_file:
        img_bytes = img_file.read()
        
    base64_encoded = base64.b64encode(img_bytes).decode('utf-8')
    return base64_encoded

def binario_a_imagen(binario, ruta_guardar):
    lado = int(len(binario)**0.5)
    imagen = Image.new("RGB", (lado, lado))
    
    for y in range(lado):
        for x in range(lado):
            bit = int(binario[y * lado + x])
            color = (bit * 255, bit * 255, bit * 255)
            imagen.putpixel((x, y), color)

    imagen.save(ruta_guardar)

ruta_imagen = 'imagen_xor.png'
bits_imagen = imagen_a_bits(ruta_imagen)

text = bits_imagen
key = "cifrados para encontrar su valor"

print(binario_a_imagen(change_with_xor(text, key), "test.png"))
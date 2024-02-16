# Universidad del Valle de Guatemala
# Cifrado de la información
# Laboratorio#2 B

import shutil
from PIL import Image
import base64
import io

shutil.unpack_archive('imagen_xor.png.zip', '.')

with open('imagen_xor.png', "rb") as a:
    codificado_base64 = base64.b64encode(a.read()).decode('utf-8')

def xor_data(x, y):
    llave_binario = [ord(char) for char in y]
    xor_result = []

    for i in range(len(x)):
        xor_result.append(x[i] ^ llave_binario[i % len(llave_binario)])

    return bytes(xor_result)

imagen_ejemplo = base64.b64decode(codificado_base64)

llave = "cifrados"
xor_result = xor_data(imagen_ejemplo, llave)

image_result = Image.open(io.BytesIO(xor_result))

image_result_path = 'imagen_resultado_ejercicio_6.png'
image_result.save(image_result_path)
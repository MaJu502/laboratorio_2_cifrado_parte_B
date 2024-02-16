# Universidad del Valle de Guatemala
# Cifrado de la información
# Laboratorio#2 B

import cv2
import numpy as np
import base64
from PIL import Image
import io

with open('foto.png', "rb") as img_file:
    foto_base64 = base64.b64encode(img_file.read()).decode('utf-8')

with open('lock.png', "rb") as lock_file:
    lock_base64 = base64.b64encode(lock_file.read()).decode('utf-8')

def xor_data(x, y):
    xor_result = bytearray()

    for i in range(len(x)):
        xor_result.append(x[i] ^ y[i % len(y)])

    return bytes(xor_result)

imagen_original = base64.b64decode(foto_base64)
imagen_llave = base64.b64decode(lock_base64)

imagen_original_pil = Image.open(io.BytesIO(imagen_original))
imagen_llave_pil = Image.open(io.BytesIO(imagen_llave))

if imagen_original_pil.size != imagen_llave_pil.size:
    print("Las imágenes tienen dimensiones diferentes")
    exit()

imagen_original_array = np.array(imagen_original_pil)
imagen_llave_array = np.array(imagen_llave_pil)

resultado_xor = np.bitwise_xor(imagen_original_array, imagen_llave_array)
cv2.imwrite('imagen_resultado_ejercicio_8.png', resultado_xor)

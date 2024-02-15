# XOR bit a bit
def convertir_letra_binario(x):
    a = ord(x)

    binario = ''
    while a > 0:
        residuo = a % 2
        binario = str(residuo) + binario
        a = a // 2
    temp = 8 - len(binario)

    retorno = ''
    for i in range(temp):
        retorno = retorno + '0'
    retorno = retorno + binario
    return retorno

def convertir_binario_letra(x):
    valor_decimal = 0

    for i in range(8):
        valor_decimal += int(x[i]) * (2 ** (len(x) - i - 1))


    letra = chr(valor_decimal)
    return letra

def codificar_binario(x):
    retorno = ""
    for i in x:
        retorno += convertir_letra_binario(i)
    return retorno

def decodificar_binario(x):
    retorno = ""
    for i in range(0, len(x), 8):
        retorno += convertir_binario_letra(x[i:i+8])
    return retorno

def verificar_largo_llave_xor(x,y):
    retorno = ""
    temp = 0

    for _ in range(len(x)):
        retorno += y[temp]
        temp = (temp + 1) % len(y) # modulo para asegurar que no sea más larga de la palabra

    return retorno

def coder_xor(x, y):
    y = verificar_largo_llave_xor(x, y)

    input_binario = codificar_binario(x)
    y_binario = codificar_binario(y)

    # XOR bit a bit
    result_binario = ''
    for i in range(len(input_binario)):
        temp = 0
        if input_binario[i] == '0' and y_binario[i] == '1':
            temp = 1
        elif input_binario[i] == '1' and y_binario[i] == '0':
            temp = 1

        result_binario = result_binario + str(temp)

    print(result_binario)
    result_texto = decodificar_binario(result_binario)

    return result_texto

# Ejemplo de uso
x = "Demagogo"
y = "carro"
result = coder_xor(x, y)
print("Resultado XOR:", result)
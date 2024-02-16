# Universidad del Valle de Guatemala
# Cifrado de la información
# Laboratorio#2 B

import matplotlib.pyplot as plt

# Se uso una función similar para el lab1
def frecuency(data, n):
    probabilities = {}
    total_count = len(data) - n + 1
    
    for i in range(total_count):
        subsequence = data[i:i+n]
        probabilities[subsequence] = probabilities.get(subsequence, 0) + 1
    
    for key, value in probabilities.items():
        probabilities[key] = value / total_count
    
    return probabilities


def plot_histogram(probabilities, title, filename=None):
    plt.bar(probabilities.keys(), probabilities.values())
    plt.title(title)
    plt.xlabel("Ocurrencia")
    plt.ylabel("Probabilidad")
    if filename:
        plt.savefig(filename, format="png")
    plt.show()

def main():
    # El texto es: Hola mundo
    bit_string = "01001000011011110110110001100001001000000110110101110101011011100110010001101111"
    
    single_probabilities = frecuency(bit_string, 1)
    plot_histogram(single_probabilities, "Distribución de bits individuales", "Bits_individuales.png")

    bigram_probabilities = frecuency(bit_string, 2)
    plot_histogram(bigram_probabilities, "Distribución de bigramas", "Bigramas.png")

    trigram_probabilities = frecuency(bit_string, 3)
    plot_histogram(trigram_probabilities, "Distribución de trigramas", "Trigramas.png")

if __name__ == "__main__":
    main()

import numpy as np
import numpy.random as npr

def questao_4():
    # A função `npr.randint` retorna uma array de n elementos que são números
    # inteiros entre os valores fornecidos
    array_aleatoria_1 = npr.randint(0, 10, 8)
    array_aleatoria_2 = npr.randint(0, 10, 8)
    print(f"Quinta array: {array_aleatoria_1}")
    print(f"Sexta array: {array_aleatoria_1}")

    # A função np.intersect1d retorna uma array com a interesecção entre duas
    # arrays unidimensionais. O argumento return_indices, quando verdadeiro, faz
    # a função retornar mais duas arrays extras contendo os índices de cada item
    # nas duas arrays inciais.
    interseccao, indices_1, indices_2 = np.intersect1d(
        array_aleatoria_1,
        array_aleatoria_2,
        return_indices = True
    )
    print(f"Elementos comuns das duas arrays: {interseccao}")
    print("Índices correspondentes dos elementos comuns:")
    for index in range(indices_1.shape[0]):
        print(f"{indices_1[index]} - {indices_2[index]}")
    print("\n")
    return array_aleatoria_1, array_aleatoria_2

def questao_5():
    array_5, array_6 = questao_4()

    # A função np.hstack concatena as duas arrays horizontalmente
    array_7 = np.hstack((array_5, array_6))
    print(f"Sétima array: {array_7}")

    # As funções np.mean, np.std e np.var retornam respectivamente a média,
    # desvio padrão e variância de uma array unidimensional
    print(f"Medidas estatísticas da sétima array:\nMédia: {np.mean(array_7)}\n"\
          f"Desvio Padrão:  {np.std(array_7)}\nVariância: {np.var(array_7)}")

    # Define uma função que recebe um inteiro e retorna -1 ou 1 de acordo com
    # a paridade dele
    def ver_paridade(numero):
        if numero % 2:
            return -1
        else:
            return 1

    # A função vectorize faz uma funcao aceitar um vetor e faz ela retornar outro
    # vetor com os elementos modificados pela fucao original
    ver_paridade_vetorizada = np.vectorize(ver_paridade)
    vetor_7 = ver_paridade_vetorizada(array_7)
    print(f"Sétima array modificada: {vetor_7}", end = "\n\n")

questao_5()

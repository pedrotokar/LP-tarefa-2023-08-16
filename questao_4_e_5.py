import numpy as np
import numpy.random as npr

def questao_4():
    # A função `npr.randint` retorna uma array de n elementos que são números
    # inteiros entre os valores fornecidos
    array_aleatoria_1 = npr.randint(0, 10, 8)
    array_aleatoria_2 = npr.randint(0, 10, 8)

    # A função np.intersect1d retorna uma array com a interesecção entre duas
    # arrays unidimensionais. O argumento return_indices, quando verdadeiro, faz
    # a função retornar mais duas arrays extras contendo os índices de cada item
    # nas duas arrays inciais.
    interseccao = np.intersect1d(
        array_aleatoria_1,
        array_aleatoria_2,
        return_indices = True
    )

    return array_aleatoria_1, array_aleatoria_2, interseccao

def questao_5():
    array_5, array_6, interseccao = questao_4()

    # A função np.hstack concatena as duas arrays horizontalmente
    array_7 = np.hstack((array_5, array_6))
    print(array_7)

    # As funções np.mean, np.std e np.var retornam respectivamente a média,
    # desvio padrão e variância de uma array unidimensional
    estatisticas = {
        "media": np.mean(array_7),
        "desvio-padrao":  np.std(array_7),
        "variancia": np.var(array_7)
    }

    # Define uma função que recebe um inteiro e retorna -1 ou 1 de acordo com
    # a paridade dele
    def ver_paridade(numero):
        if numero % 2:
            return -1
        else:
            return 1

    ver_paridade_vetorizada = np.vectorize(ver_paridade)
    return ver_paridade_vetorizada(array_7)



print(questao_4())
print(questao_5())

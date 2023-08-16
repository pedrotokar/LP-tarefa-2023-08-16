import numpy as np
import numpy.random as npr

def questao_4():
    # A função `npr.randint` retorna uma array de n elementos que são números
    # inteiros entre os valores fornecidos
    array_aleatoria_1 = npr.randint(0, 10, 8)
    array_aleatoria_2 = npr.randint(0, 10, 8)

    # A função `np.intersect1d` retorna uma array com a interesecção entre duas
    # arrays unidimensionais. O argumento return_indices, quando verdadeiro, faz
    # a função retornar mais duas arrays extras contendo os índices de cada item
    # nas duas arrays inciais.
    interseccao = np.intersect1d(
        array_aleatoria_1,
        array_aleatoria_2,
        return_indices = True
    )
    print(interseccao)

    return array_aleatoria_1, array_aleatoria_2, interseccao

def questao_5():
    pass

print(questao_4())
print(questao_5())

import numpy as np

def questao_1():
    # Criação de array de 9 elementos:
    array_1 = np.arange(1,10) 
    array_2 = np.arange(11,20)
    # Soma dos elementos dos arrays elemento a elemento:
    array_3 = array_1 + array_2
    print(array_3)
    return array_3

def questao_2():
    # Redimensionamento do array_3 com formato 3X3:
    array_redimensionado = questao_1().reshape(3,3)
    # Modifição do dtype do array para o tipo float:
    array_redimensionado = array_redimensionado.astype(float)
    # Matriz transposta:
    array_redimensionado = array_redimensionado.T
    print(array_redimensionado)
    return array_redimensionado

def questao_3():
    # Criação de array de 6 elementos:
    array_4 = np.arange(1,7)
    # Redimensionamento do array_4 com formato 2X3:
    array_4 = array_4.reshape(2,3)
    # Multiplicação entre matrizes:
    array_4 = np.dot(array_4, questao_2())
    print(array_4)
    return array_4
import numpy as np
import numpy.random as npr

def questao_6():
    vetor_A = npr.randint(10, size = (3,3))
    vetor_B = npr.randint(10, size = (3,3))
    print(f"Vetor A: \n", vetor_A)
    print(f"Vetor B: \n", vetor_B)
    print(f"Produto vetorial: \n", np.cross(vetor_A, vetor_B))

def questao_7():
    ndarray_8 = npr.randint(10, size = (3,3)) # Gera matriz 3x3 com valores aleatórios
    matriz_identidade = np.identity(3) # Gera uma matriz identidade 3x3
    determinante = np.linalg.det(ndarray_8) # Calcula o determinante
    inversa = np.linalg.inv(ndarray_8) # Calcula a inversa
    print(f"Matriz inicial: \n", ndarray_8)
    print(f"Determinante: \n", determinante)
    print(f"Inversa: \n", inversa)
    # A multiplicação terá valores próximos a 0 ao invés de 0, pois os floats não são exatos.
    print("Multiplicação da matriz inicial pela inversa: \n", np.dot(inversa, ndarray_8))
    np.allclose(np.dot(inversa, ndarray_8), matriz_identidade)
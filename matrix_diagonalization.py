import numpy as np

def diagonalizar(matriz, expoente):    
    autovalores, autovetores = np.linalg.eig(matriz)
    print(f'Auto Valores: \n {autovalores} \n')
    print(f'Auto Valores: \n {autovetores} \n')
    matriz_d = autovetores @ np.diag(autovalores**expoente) @ np.linalg.inv(autovetores)
    print(f'Matriz Diagonalizada elevada a {expoente}: \n {matriz_d}')

matriz = np.array([[0.2, 0.8], [0.9, 0.1]])
diagonalizar(matriz, 4)

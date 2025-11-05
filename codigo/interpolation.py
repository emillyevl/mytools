# Python 3
import numpy as np
from scipy.interpolate import interp1d


class interpolater:

    def evaluate(self, X):
        raise NotImplementedError

    def __call__(self,  X):
        return self.evaluate(X)


class VandermondeMatrix(interpolater):
    def __init__(self, x, y):
        # 1. VALIDAÇÃO DOS DADOS (garante que para todo x exite um y)
        if len(x) != len(y):
            raise RuntimeError(f"Dimensions must be equal len(x) = {len(x)} != len(y) = {len(y)}")
        
        # 2. ARMAZENAMENTO DOS DADOS
        self.data = [x, y]           # Armazena os pontos (x, y)
        self._degree = len(x) - 1    # Grau do polinômio interpolador
        
        # 3. CONSTRUÇÃO E RESOLUÇÃO DO SISTEMA
        self._buildMatrix()          # Constrói a matriz do sistema
        self._poly = np.linalg.solve(self.matrix, self.data[1])  # Resolve o sistema. _poly armazena os coeficientes do polinômio interpolador

    def _buildMatrix(self):
        self.matrix = np.ones([self._degree+1, self._degree+1])
        for i, x in enumerate(self.data[0]):
            self.matrix[i, 1:] = np.multiply.accumulate(np.repeat(x, self._degree))
    
    def evaluate(self, X):
        r = 0.0
        for c in self._poly[::-1]:
            r = c+r*X
        return r

    
class Lagrange(interpolater):
    def __init__(self, x, y):
        if len(x) != len(y):
            raise RuntimeError(f"Dimensions must be equal len(x) = {len(x)} != len(y) = {len(y)}")
        
        self.data = [x, y]          
        self._degree = len(x) - 1   

    def evaluate(self, X):
        r = 0.0
        for i in range(self._degree+1):
            Li = np.ones_like(X)
            for j in range(self._degree+1):
                if j != i:
                    Li *= (X - self.data[0][j])/(self.data[0][i] - self.data[0][j])
            r += self.data[1][i]*Li
        
        return r
        

def random_sample(intv, N):
    r = np.random.uniform(intv[0], intv[1], N-2)
    r.sort()
    return np.array([intv[0]] + list(r) + [intv[1]])

def error_pol(f, P, intv, n = 1000):
    x = random_sample(intv, n)
    vectError = np.abs(f(x)-P(x))
    return np.sum(vectError)/n, np.max(vectError)


if __name__ == '__main__':
    import matplotlib.pyplot as plt

    DataX = [10.7       , 11.075     , 11.45      , 11.825     , 12.2       , 12.5]
    DataY = [-0.25991903,  0.04625002,  0.16592075,  0.13048074,  0.13902777, 0.2]

    Pvm = VandermondeMatrix(DataX, DataY)

    Plg = Lagrange(DataX, DataY)

    # Vandermonde Matrix

    Xv = np.linspace(min(DataX)-0.2, max(DataX)+0.2, 100)
    Yv = Pvm(Xv)

    # Lagrange
    Xl = np.linspace(min(DataX), max(DataX), 100)
    Yl = interp1d(DataX, DataY, kind='quadratic')(Xl)

    _, ax = plt.subplots(1)
    ax.plot(Xv,Yv, color ='blue')
    ax.plot(Xl,Yl, '--', color='red')

    ax.legend(['Vandermonde Matrix', 'Lagrange']) 

    ax.axis('equal')
    ax.plot(DataX, DataY, 'o')
    plt.show()
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d

class interpolater:
    def evaluate(self, X):
        raise NotImplementedError

    def __call__(self, X):
        return self.evaluate(X)

class Linear(interpolater):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.interpolator = interp1d(x, y, kind='linear', fill_value="extrapolate")

    def evaluate(self, X):
        return self.interpolator(X)
    
class polinomial(interpolater):
    def __init__(self, x, y, order=2):
        self.x = x
        self.y = y
        self.interpolator = interp1d(x, y, kind=order, fill_value="extrapolate")

    def evaluate(self, X):
        return self.interpolator(X)
    
if __name__ == "__main__":
    import matplotlib.pyplot as plt

    DataX = [200 , 400 , 600 , 800 , 1000 , 1200, 1400]
    DataY = [15  , 9   , 5   , 3   , -2   , -5  , -15]

    k = Linear(DataX, DataY)

    X = np.linspace(min(DataX), max(DataX), 1000000)
    Y = k(X)

    print(k(700))
    
    valores_x = []
    for x, y in zip(X, Y):
        if abs(y) < 0.00002:  
            valores_x.append(x)
    print(f"linear: {max(valores_x):.2f}")

    p = polinomial(DataX, DataY)
    Z = p(X)

    valores_xz = []
    for x, z in zip(X, Z):
        if abs(z) < 0.00002:  
            valores_xz.append(x)
    print(f"polinomial: {max(valores_xz):.2f}")


    _, ax = plt.subplots(1)
    ax.plot(X,Y, color ='blue')
    ax.plot(X,Z, color ='red')

    ax.legend(['Interpolação linear', 'Interpolação polinomial']) 

    ax.set_xlim(min(DataX)-100, max(DataX)+100)
    ax.set_ylim(min(DataY)-6, max(DataY)+5)

    ax.plot(DataX, DataY, 'o')
    plt.show()
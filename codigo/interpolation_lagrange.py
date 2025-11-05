import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d

class interpolater:

    def evaluate(self, X):
        raise NotImplementedError

    def __call__(self,  X):
        return self.evaluate(X)
    
#class Langrange:

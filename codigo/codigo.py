class numerica:

    def __init__(self, numero):
        self.numero = numero

    def __add__(self, otro):
        return numerica(self.numero + otro.numero)
    
    def __mul__(self, otro):
        return numerica('%.3f'%(self.numero * otro.numero))
    
    def __div__(self, otro):
        return numerica(self.numero / otro.numero)
    
    def __str__(self):
        return str(self.numero)
    
if __name__ == "__main__":
    a = numerica(1234567) #100.000
    b = numerica(0.009)
    c = a * b
    print(c)# This code defines a class 'numerica' that encapsulates a numeric value and overloadss the addition, multiplication, and division operators.




#100000 m, 0.001 m.
# 
#         
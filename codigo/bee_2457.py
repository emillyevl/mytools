numero_nos = int(input())

numeros = list(map(int, input().split()))

arestas = []

for i in range(numero_nos-1):
    x, y = input().split()
    edges = (int(x), int(y))
    arestas.append(edges)


            
    #print(numeros[i])



print(arestas)
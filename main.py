from builder import builder
from math import e

weights = [0,1,4],[2,-2,-7],[-23,3,9]
biases = [1,2,3]

inputs = [3,2,1]
Out = 0

for i in weights:
    for j in i:
        I = j * inputs[i.index(j)] + biases[i.index(j)]
        Sigmified = (1/(1+e**(-I)))/len(i)
        Out = Sigmified + Out
    print(Out)
    Out = 0





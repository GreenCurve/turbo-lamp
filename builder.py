import csv

class Node():
    def __init__(self,coef,bias):
        self.coef = coef
        self.bias = bias

        #with open('Brainstalks.csv','r') as f:
            #csvFile = csv.reader(f)
            #Layer = csvFile[layer]

        with open('Brainstalks.csv', 'a', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(str(self.coef) + str(self.bias))


def builder(C,B):
    NodeOne = Node(C,B)

import csv
from math import sqrt


class Punto:
    def __init__(self,X:int,Y:int)-> None:
        self.coord_X = X
        self.coord_Y = Y
    
    def getCords(self) -> list:
        return [self.coord_X,self.coord_Y]
        
class Cluster:
    
    def __init__(self, puntosCluster) -> None:
        self.puntos = puntosCluster

    def agregarPunto(self,punto:Punto) -> None:
        if isinstance(punto, Punto):
            self.puntos.append(punto)
    
    def getPoints(self):
        return self.puntos
            
def euclidianDistance(cord1:list, cord2:list) -> float:
    return sqrt( pow((cord1[0]-cord2[0]),2) + pow((cord1[1] - cord2[1]),2) )

def singleLinkage(Cluster1:Cluster, Cluster2:Cluster) ->float:
    tmpPuntosCluster1 = Cluster1.getPoints()
    tmpPuntosCluster2 = Cluster2.getPoints()
    res = [] #Array para guardar los tmp de cada ciclo
    for punto1 in tmpPuntosCluster1:
        tmp = 100000000.0
        for punto2 in tmpPuntosCluster2:
            x = euclidianDistance(punto1.getCords(),punto2.getCords())
            if(x < tmp): tmp = x
        res.append(tmp)
    return min(res)             
            
         
def averageLinkage(Cluster1,Cluster2):
    return None

def completeLinkage(Cluster1, Cluster2):
    return None
            
if __name__ == "__main__":
    puntosCluster1 = []
    puntosCluster2 = []
    with open('puntos.csv') as csv_file: #Cargamos DataSet
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                print(f"Headers: {row[0]}, {row[1]}")
                line_count += 1
            elif line_count >= 3:
                puntosCluster2.append(Punto(float(row[0]),float(row[1])))
                line_count += 1
            else:
                puntosCluster1.append(Punto(float(row[0]),float(row[1])))
                line_count += 1
    clusters = [Cluster(puntosCluster1),Cluster(puntosCluster2)]
    
    print(singleLinkage(clusters[0],clusters[1]))
    
    
            
            
class Point:
    def __init__(self,x,y,value):
        self.x=x
        self.y=y
        self.value=value
    def coord(self):
        return [self.x,self.y,self.value]

class Line:
    def __init__(self, lista):
        self.coeficientes = []
        for elemento in lista:
            self.coeficientes.append(elemento)
        self.cadena=self.chain()
        self.chain()
        self.fit=0


    def chain(self):
        cadena=""
        grado = len(self.coeficientes)-1
        for elemento in self.coeficientes:
            cadena=cadena+"+"+str(elemento)+"*x**"+str(grado)
            grado=grado-1
        return cadena

    def toString(self):
        return self.cadena

    def solve(self,x):
        #return self.x3*x**3 + self.x2*x**2 + self.x1*x + self.x0
        sol=0
        grado= len(self.coeficientes)-1
        for elemento in self.coeficientes:
            sol=sol+elemento*(x**grado)
            grado=grado-1
        return sol

    def setFit(self,n):
        self.fit=n

    def getFit(self):
        return self.fit
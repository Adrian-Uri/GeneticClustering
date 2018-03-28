from Funciones import *
from Clases import *

z=0
stop=700
psize=50
tsize=5
equaciones=[]
puntos=[]
equacionesDef=[]
init(equaciones,puntos,psize)
mejor=equaciones[0]
torneos = torneo(equaciones, tsize)

while(mejor.getFit()<stop and mejor.getFit()<200):
    #print(mejor.chain())

    for sistema in torneos:
        sistema.sort(key=lambda equacion:equacion.fit, reverse=True)
    eqsDef=[]
    for elemento in torneos:
        for i in range(1,5):
            actual=elemento.pop()
            eqsDef.append(actual)

    evaluate(eqsDef,puntos)
    #Aqui tengo en eqsDef a los progenitores

    eqsDef=crossover(eqsDef)
    eqsDef=mutacion(eqsDef)

    for j in range(0, len(eqsDef)):
        for i in range(0, len(eqsDef[j].coeficientes)):
            num = bin(eqsDef[j].coeficientes[i])
            posi = random.randint(0, 1)
            if (posi > 0):
                numRand = random.randint(-100, 100)

                eqsDef[j].coeficientes[i] = eqsDef[j].coeficientes[i] + numRand




    evaluate(eqsDef,puntos)
    eqsDef.sort(key=lambda equacion:equacion.fit, reverse=True)
    if(eqsDef[0].getFit()>mejor.getFit()):
        mejor=eqsDef[0]
        drawGraph(mejor.chain(), range(-10, 10),"b")

    while(len(eqsDef)<psize):
        eqsDef.append(Line([random.randint(-100,100),random.randint(-100,100),random.randint(-100,100),random.randint(-100,100),random.randint(-100,100)]))
    print(mejor.getFit())
    print(z)
    torneos=torneo(eqsDef,tsize)
    z=z+1
    stop=stop-1

print("####################################3")
print(mejor.chain())
print(fitnessFunct(mejor, puntos))


drawGraph(mejor.chain(),range(-10,10),"r")
for elemento in puntos:
     drawPoint([elemento.coord()])

draw.show()
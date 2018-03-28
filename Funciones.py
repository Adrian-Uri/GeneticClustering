from Clases import *
import matplotlib.pyplot as draw
import random
import numpy as np





def init(indiv,points,psize):
    """
    Inicializes the values for the first population and the set of points
    :param indiv:
    :param points:
    """
    for elemento in range(1,psize):
        indiv.append(Line([random.randint(-100,100),random.randint(-100,100),random.randint(-100,100),random.randint(-100,100),random.randint(-100,100)]))


    for num in range(0, 100):
        points.append(Point(random.uniform(-10, 10), random.uniform(-0, 10000), 1))
    for num in range(0, 100):
        points.append(Point(random.uniform(-10, 10), random.uniform(-10000, 0), -1))


def drawGraph(formula, range, color):
    """
    Draws the function
    :param formula: Line
    :param range:
    :param color: string

    """
    x=np.array(range)
    print(formula)
    y=eval(formula)
    draw.plot(x,y,color)


def drawPoint(listasa):
    """
    Draws the points according to its value
    :param listasa:
        List of points, given as [,,,,,]
    """
    list_of_lists = listasa
    x_list = [x for [x, y, v] in list_of_lists]
    y_list = [y for [x, y, v] in list_of_lists]
    v_list = [v for [x,y,v] in list_of_lists]
    if(v_list==[1]):
        draw.plot(x_list, y_list,'g^') #bs ro g^
    else:
        draw.plot(x_list, y_list, 'ro')  # bs ro g^


def infSup(point,equacion):
    """
    Checks if points are above or below the function
    :param point: Point
    :param equacion: Line
    :return: boolean
        returns true if the point is above the function

    """
    sol=equacion.solve(point.x)
    if sol>point.y:
        return False
    else:
        return True


def fitnessFunct(equacion,listPoints):
    """
    Determine how good a solution is
    :param equacion: Line
    :param listPoints: list(Point)
    :return: int
        Returns the value of the fitness for that function and set of points
    """
    positive=0
    for element in listPoints:
        if infSup(element,equacion):
            positive=positive+element.value
        if not infSup(element,equacion) and element.value<0:
            positive = positive - element.value

    return positive


def evaluate(eqs,points):
    """
    Evaluates the fitness of every function
    :param eqs: list[Line]
    :param points: list[Point]
    """
    for elemento in eqs:
        elemento.setFit(fitnessFunct(elemento,points))


def torneo(ranking,tsize):
    """
    Creates the tournaments
    :param ranking:
        List of functions
    :param tsize:
    :return:
    List of lists with the divided population
    """
    splited = [ranking[i::tsize] for i in range(tsize)]
    return splited


def crossover(progenitores):
    """
    Performs the crossover
    :param progenitores:
    :return: list(Line)
        The "offspring"
    """
    nuevos=[]
    while(len(progenitores)):
        p1=progenitores.pop()
        p2=progenitores.pop()
        for elemento in range(0,len(p1.coeficientes)):
            posi=random.randint(0,1)
            if(posi>0):
                aux=p1.coeficientes[elemento]
                p1.coeficientes[elemento]=p2.coeficientes[elemento]
                p2.coeficientes[elemento]=aux

        nuevos.append(Line(p1.coeficientes))
        nuevos.append(Line(p2.coeficientes))
    return nuevos


def binarizar(decimal):
    """
    Turns number into binary(finaly not used)
    :param decimal:
    :return:
        String with the number in binary
    """
    binario = ''
    while decimal // 2 != 0:
        binario = str(decimal % 2) + binario
        decimal = decimal // 2
    return str(decimal) + binario


def mutacion(eqsDef):
    """
    Performs mutation
    :param eqsDef:
    :return: list(Line)
        Mutated functions
    """
    for j in range(0,len(eqsDef)):
        for i in range(0,len(eqsDef[j].coeficientes)):
            num=bin(eqsDef[j].coeficientes[i])
            posi = random.randint(0, 1)
            if(posi>0):
                numRand=random.randint(-100,100)
                #print(eqsDef[j].coeficientes[i])
                eqsDef[j].coeficientes[i]=eqsDef[j].coeficientes[i] + numRand
                #print(eqsDef[j].coeficientes[i])
    return eqsDef
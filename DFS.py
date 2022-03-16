import copy


def printNode(node):
    print(node[0],node[1],node[2])
    print(node[3],node[4],node[5])
    print(node[6],node[7],node[8])
    global nodeNumber
    print('Nodo:', nodeNumber)
    print('Profundidad:', len(node[9:]))
    print('Movimiento(s):', node[9:])
    print('------')
    nodeNumber += 1

def checkFinal(node):
    if node[:9]==finalNode:
        printNode(node)
        return True
    global insertIndex
    if node[:9] not in visitedList:
        printNode(node)
        stack.insert(insertIndex, node)
        insertIndex += 1
        visitedList.append(node[:9])
    return False

if __name__ == '__main__':

    print("Este programa encuentra la solución al 8-puzzle mediante la búsqueda de profundidad.")

    print("Ingrese el estado inicial del juego: ")

    p1i=int(input("Ingrese la posición 1 del estado inicial: "))
    p2i=int(input("Ingrese la posición 2 del estado inicial: "))
    p3i=int(input("Ingrese la posición 3 del estado inicial: "))
    p4i=int(input("Ingrese la posición 4 del estado inicial: "))
    p5i=int(input("Ingrese la posición 5 del estado inicial: "))
    p6i=int(input("Ingrese la posición 6 del estado inicial: "))
    p7i=int(input("Ingrese la posición 7 del estado inicial: "))
    p8i=int(input("Ingrese la posición 8 del estado inicial: "))
    p9i=int(input("Ingrese la posición 9 del estado inicial: "))

    print("Ingrese el estado final del juego: ")

    p1f=int(input("Ingrese la posición 1 del estado final: "))
    p2f=int(input("Ingrese la posición 2 del estado final: "))
    p3f=int(input("Ingrese la posición 3 del estado final: "))
    p4f=int(input("Ingrese la posición 4 del estado final: "))
    p5f=int(input("Ingrese la posición 5 del estado final: "))
    p6f=int(input("Ingrese la posición 6 del estado final: "))
    p7f=int(input("Ingrese la posición 7 del estado final: "))
    p8f=int(input("Ingrese la posición 8 del estado final: "))
    p9f=int(input("Ingrese la posición 9 del estado final: "))

    depth = int(input("Ingrese la profundidad máxima: "))


    finalNode = [p1f, p2f, p3f, p4f, p5f, p6f, p7f, p8f, p9f]
    startNode = [p1i, p2i, p3i, p4i, p5i, p6i, p7i, p8i, p9i]

    
    found = False
    nodeNumber = 0
    visitedList = []
    stack = []
    stack.append(startNode)
    visitedList.append(startNode)
    printNode(startNode)

    i=0
    while (not found and not len(stack)==0 and i <depth):
        
        i=i+1
        currentNode = stack.pop(0)
        blankIndex = currentNode.index(0)
        insertIndex = 0
        if blankIndex!=0 and blankIndex!=1 and blankIndex!=2:
            upNode = copy.deepcopy(currentNode)
            upNode[blankIndex] = upNode[blankIndex-3]
            upNode[blankIndex-3] = 0
            upNode.append('arriba')
            found = checkFinal(upNode)
        if blankIndex!=0 and blankIndex!=3 and blankIndex!=6 and found==False:
            leftNode = copy.deepcopy(currentNode)
            leftNode[blankIndex] = leftNode[blankIndex-1]
            leftNode[blankIndex-1] = 0
            leftNode.append('izquierda')
            found = checkFinal(leftNode)
        if blankIndex!=6 and blankIndex!=7 and blankIndex!=8 and found==False:
            downNode = copy.deepcopy(currentNode)
            downNode[blankIndex] = downNode[blankIndex+3]
            downNode[blankIndex+3] = 0
            downNode.append('abajo')
            found = checkFinal(downNode)
        if blankIndex!=2 and blankIndex!=5 and blankIndex!=8 and found==False:
            rightNode = copy.deepcopy(currentNode)
            rightNode[blankIndex] = rightNode[blankIndex+1]
            rightNode[blankIndex+1] = 0
            rightNode.append('derecha')
            found = checkFinal(rightNode)
        if i==depth:
            print("Alcanzaste el límite de profundidad")

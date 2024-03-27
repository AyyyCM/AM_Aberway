#! /bin/python

from aberway_background_code import create, update, main_loop
import time

ColourFlip = False
import math
    
screen, bg, lineList, nodeList = create(ColourFlip)
update(None, screen, bg, lineList, nodeList, None, None, None, None, 0)


# --- SET THESE VALUES TO AN EXAMPLE ---
startPos = 0
listOfNodesToPass = [10,11,14]
length = 676.75
error = 0.06

def path_update():
    ListOfNodeId = [] #set the value of this to the nodes that your path takes
    start = time.time_ns() # for timing your algorithm
    # ---------- ---------- YOUR CODE GOES HERE ---------- ----------
    #def floyd(g):
    g = [0,10]
    k = 0
    i = 0
    j = 0
    weights=[0,0]

    lengthDict = {}
    for v in range(len(nodeList)):#make verts
        lengthDict[v] = {}
        for n in nodeList[v][3]: #make connecteds
            lengthDict[v][n] = {}

    def lengthCalculator(v,n):
        x = nodeList[v][0][0] - nodeList[n][0][0]
        y = nodeList[v][0][1] - nodeList[n][0][1]
        length = round(math.sqrt((abs(x)**2)+(abs(y)**2)),2) #distance
        return length

    for k in nodeList[startPos][3]:
        print(k)
        for i in nodeList[k][3]:
            print(i)
            for j in nodeList[i][3]:
                #edge = (i, j)
                lengthDict[i][j] = lengthCalculator(i,j)
                # print(j)
                # #print(ListOfNodeId)
                # length = lengthCalculator(i,k) + lengthCalculator(k,j)
                # if length < lengthCalculator(i,j):
                #     weightest = lengthCalculator(i,j)
                #     ListOfNodeId.append(j)
                #     print(ListOfNodeId)
    print(lengthDict)
    print(ListOfNodeId)




    # ---------- ---------- ---------- ---------- ---------- ---------- ----------
    end = time.time_ns()
    update(ListOfNodeId, screen, bg, lineList, nodeList, startPos, listOfNodesToPass, length, error, end - start)

path_update()
main_loop()

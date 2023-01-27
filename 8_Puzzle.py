import copy 
import random
io=open('inp+out.txt','a')
def childStates(stateCurr):
    nextPStates=[]
    tempStates=[]
    x=-1
    y=-1
    for i in range(3):
        if(x!=-1):
            break
        for j in range(3):
            if(stateCurr[i][j]=='B'):
                x=i
                y=j
                break    
    if(x>0):
        tempStates=copy.deepcopy(stateCurr)
        tempStates[x][y],tempStates[x-1][y]=tempStates[x-1][y],tempStates[x][y]
        nextPStates.append(tempStates)
    if(x<2):
        tempStates=copy.deepcopy(stateCurr)
        tempStates[x][y],tempStates[x+1][y]=tempStates[x+1][y],tempStates[x][y]
        nextPStates.append(tempStates)
    if(y>0):
        tempStates=copy.deepcopy(stateCurr)
        tempStates[x][y],tempStates[x][y-1]=tempStates[x][y-1],tempStates[x][y]
        nextPStates.append(tempStates)
    if(y<2):
        tempStates=copy.deepcopy(stateCurr)
        tempStates[x][y],tempStates[x][y+1]=tempStates[x][y+1],tempStates[x][y]
        nextPStates.append(tempStates)
    return nextPStates

def runDFS(initState,endState):
    stack=[]
    stack.append(initState)
    parent = {str(stack): None}
    visited = 0
    while stack:
        top = stack[len(stack)-1]
        stack.pop(len(stack)-1)
        visited+=1
        if(top==endState):
            # print("Noice!This 8-puzzle game is solved!!! \nThe number of states traversed is ",visited,"\n")
            return visited
            break
        for newState in childStates(top):
            if(str(newState) not in parent):
                stack.append(newState)
                parent[str(newState)]=top
    if visited==181441:
        return visited
        print("Sorry! This 8-puzzle can't be solved\n")    

def runBFS(initState,endState):
    queue=[]
    queue.append(initState)
    parent = {str(queue): None}
    visited = 0
    while queue:
        stateCurr=queue[0]
        queue.pop(0)
        visited+=1
        if(stateCurr==endState):
            # print("Noice!This 8-puzzle game is solved!!! \nThe number of states traversed is ",visited,"\n")
            return visited
            break
        for newState in childStates(stateCurr):
            if(str(newState) not in parent):
                queue.append(newState)
                parent[str(newState)]=stateCurr
    if visited==181441:
        return visited
        # print("Sorry! This 8-puzzle can't be solved  \n")    

initList=[1,2,3,4,5,6,7,8,'B']
for l in range(40):
    random.shuffle(initList)
    for alpha in range(9):
        io.write(str(initList[alpha]))
    io.write(",")
    initState=[[],[],[]]
    n=0
    print("The Initial Matrix is : \n")
    # initList=[3,2,1,4,5,6,8,7,'B']
    for i in range(3):
        for j in range(3):
            print(initList[n],end=" ")
            initState[i].append(initList[n])
            n+=1
        print("\n")
    endState=[[1,2,3],[4,5,6],[7,8,'B']]
    print("*************************This is for BFS*************************\n")
    if runBFS(initState,endState)==181441:
        print("Sorry! This 8-puzzle can't be solved  \n") 
    elif runBFS(initState,endState)<181441:
        print("Noice!This 8-puzzle game is solved!!! \nThe number of states traversed is ",runBFS(initState,endState),"\n")
    io.write(str(runBFS(initState,endState)))
    io.write(",")
    print("\n**************************This is for DFS*************************\n")
    if runDFS(initState,endState)==181441:
        print("Sorry! This 8-puzzle can't be solved  \n")         
    elif runDFS(initState,endState)<181441:
        print("Noice!This 8-puzzle game is solved!!! \nThe number of states traversed is ",runDFS(initState,endState),"\n") 
    io.write(str(runDFS(initState,endState)))
    io.write("\n")
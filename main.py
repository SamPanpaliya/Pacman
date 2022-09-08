from pyMaze import maze,agent,COLOR
def DFS(m):
    start=(m.rows,m.cols)
    explored=[start]
    frontier=[start]
    dfsPath={}
    while len(frontier)>0:
        current_cell=frontier.pop()
        if current_cell==(1,1):
            break
        for direction in 'WNSE':
            if m.maze_map[current_cell][direction]==True:
                if direction=='E':
                    childCell=(current_cell[0],current_cell[1]+1)
                elif direction=='W':
                    childCell=(current_cell[0],current_cell[1]-1)
                elif direction=='S':
                    childCell=(current_cell[0]+1,current_cell[1])
                elif direction=='N':
                    childCell=(current_cell[0]-1,current_cell[1])
                if childCell in explored:
                    continue
                explored.append(childCell)
                frontier.append(childCell)
                dfsPath[childCell]=current_cell
    fwdPath={}
    cell=(1,1)
    while cell!=start:
        fwdPath[dfsPath[cell]]=cell
        cell=dfsPath[cell]
    return fwdPath
if __name__ == "__main__":
    m=maze(7,15)
    m.CreateMaze()
    path=DFS(m)
    a=agent(m,footprints=True)
    m.tracePath({a:path})
    m.run()


# In[ ]:





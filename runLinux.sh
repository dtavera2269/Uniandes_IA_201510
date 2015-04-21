cd search/
# Si lo quiero jugar , el "-2" es para que use python 2.7
#python2 pacman.py

#Prueba de que el agente funciona
#python2 pacman.py -l tinyMaze -p SearchAgent -a fn=tinyMazeSearch

# 1) Test DFS 
#python2 pacman.py -l tinyMaze -p SearchAgent -a fn=dfs
#python2 pacman.py -l mediumMaze -p SearchAgent -a fn=dfs
#python2 pacman.py -l bigMaze -z .5 -p SearchAgent -a fn=dfs

# 2) Test BFS
#python2 pacman.py -l mediumMaze -p SearchAgent -a fn=bfs
#python2 pacman.py -l bigMaze -p SearchAgent -a fn=bfs -z .5
#python2 eightpuzzle.py

# 3) Test UCS
#python2 pacman.py -l mediumMaze -p SearchAgent -a fn=ucs
#python2 pacman.py -l mediumDottedMaze -p StayEastSearchAgent
#python2 pacman.py -l mediumScaryMaze -p StayWestSearchAgent

# 4) Test A*
#python2 pacman.py -l bigMaze -z .5 -p SearchAgent -a fn=ucs
#python2 pacman.py -l bigMaze -z .5 -p SearchAgent -a fn=astar,heuristic=manhattanHeuristic

# 5) Test Finding All the Corners
#python2 pacman.py -l tinyCorners -p SearchAgent -a fn=bfs,prob=CornersProblem
#python2 pacman.py -l mediumCorners -p SearchAgent -a fn=bfs,prob=CornersProblem

# 6) Test Corners Problem: Heuristic
#python2 pacman.py -l mediumCorners -p AStarCornersAgent -z 0.5

# 7) Test Eating All The Dots
#python2 pacman.py -l testSearch -p AStarFoodSearchAgent
#python2 pacman.py -l trickySearch -p AStarFoodSearchAgent

# 8) Suboptimal Search
#python2 pacman.py -l bigSearch -p ClosestDotSearchAgent -z .5 
#python2 pacman.py -l bigSearch -p ClosestDotSearchAgent -z .5
python2 autograder.py
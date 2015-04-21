cd search/
:: Si lo quiero jugar , el "-2" es para que use python 2.7
::py -2 pacman.py

::Prueba de que el agente funciona
::py -2 pacman.py -l tinyMaze -p SearchAgent -a fn=tinyMazeSearch

:: 1) Test DFS 
::py -2 pacman.py -l tinyMaze -p SearchAgent -a fn=dfs
py -2 pacman.py -l mediumMaze -p SearchAgent -a fn=dfs
::py -2 pacman.py -l bigMaze -z .5 -p SearchAgent -a fn=dfs

:: 2) Test BFS
::py -2 pacman.py -l mediumMaze -p SearchAgent -a fn=bfs
::py -2 pacman.py -l bigMaze -p SearchAgent -a fn=bfs -z .5
::py -2 eightpuzzle.py

:: 3) Test UCS
::py -2 pacman.py -l mediumMaze -p SearchAgent -a fn=ucs
::py -2 pacman.py -l mediumDottedMaze -p StayEastSearchAgent
::py -2 pacman.py -l mediumScaryMaze -p StayWestSearchAgent

:: 4) Test A*
::py -2 pacman.py -l bigMaze -z .5 -p SearchAgent -a fn=ucs
::py -2 pacman.py -l bigMaze -z .5 -p SearchAgent -a fn=astar,heuristic=manhattanHeuristic

:: 5) Test Finding All the Corners
::py -2 pacman.py -l tinyCorners -p SearchAgent -a fn=bfs,prob=CornersProblem
::py -2 pacman.py -l mediumCorners -p SearchAgent -a fn=bfs,prob=CornersProblem

:: 6) Test Corners Problem: Heuristic
::py -2 pacman.py -l mediumCorners -p AStarCornersAgent -z 0.5

:: 7) Test Eating All The Dots
::py -2 pacman.py -l testSearch -p AStarFoodSearchAgent
::py -2 pacman.py -l trickySearch -p AStarFoodSearchAgent

:: 8) Suboptimal Search
::py -2 pacman.py -l bigSearch -p ClosestDotSearchAgent -z .5 
::py -2 pacman.py -l bigSearch -p ClosestDotSearchAgent -z .5
py -2 autograder.py
pause
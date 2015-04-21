# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """
    "*** YOUR CODE HERE ***"
    #util.raiseNotDefined()
    
    estados=util.Stack() #Un estado es un objeto (<nodo, camino>)
    visitados=[]
    
    src=problem.getStartState()
    estados.push((src, []))
    #visitados.append(src)
    while not estados.isEmpty():
        
        nodo, camino = estados.pop()
        if problem.isGoalState(nodo):
            return camino

        if not nodo in visitados:
            visitados.append(nodo)
            for hijo, direccion, paso in problem.getSuccessors(nodo):
                estados.push((hijo, camino+[direccion]))
    return []
    
    """ 
    #Aqui queda la implementacion iterativa, tambien sirve
    visitados=[]
    camino=[]

    src=problem.getStartState()
    return iter_dfs(visitados, src, camino, problem)

def iter_dfs(visitados, nodo, camino, problem):
    visitados.append(nodo)
    if problem.isGoalState(nodo):
        return camino

    for hijo, direccion, paso in problem.getSuccessors(nodo):
        if not hijo in visitados:
            rta = iter_dfs(visitados, hijo, camino+[direccion], problem)
            if len(rta)>0:
                return rta
    return []
    """

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    #util.raiseNotDefined()
    estados=util.Queue() #Un estado es un objeto (<nodo, camino>)
    visitados=[]
    
    src=problem.getStartState()
    estados.push((src, []))
    #visitados.append(src)
    while not estados.isEmpty():
        
        nodo, camino = estados.pop()
        if problem.isGoalState(nodo):
            return camino

        if not nodo in visitados:
            visitados.append(nodo)
            for hijo, direccion, paso in problem.getSuccessors(nodo):
                estados.push((hijo, camino+[direccion]))
    return []
    """
    estados=util.Queue() #Un estado es un objeto (<nodo, camino>)
    visitados=[] #Esto se conserva para poder probar eightpuzzle.py
    
    src=problem.getStartState()
    estados.push((src, []))
    visitados.append(src)
    while not estados.isEmpty():
        nodo, camino = estados.pop()
        if problem.isGoalState(nodo):
            return camino
        for hijo, direccion, paso in problem.getSuccessors(nodo):
            if not hijo in visitados:
                visitados.append(hijo)
                estados.push((hijo, camino+[direccion]))

    return []
    """

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    #util.raiseNotDefined()
    estados=util.PriorityQueue() #Un estado es un objeto (<nodo, camino>)
    visitados=[]
    
    src=problem.getStartState()
    estados.push((src, []),0)
    
    while not estados.isEmpty():
        nodo, camino = estados.pop()
        
        if problem.isGoalState(nodo):
                return camino
        visitados.append(nodo)

        for hijo, direccion, paso in problem.getSuccessors(nodo):
            if not hijo in visitados:
                aux=camino+[direccion]
                estados.push((hijo, aux), problem.getCostOfActions(aux))
    return []

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    #util.raiseNotDefined()
    
    estados=util.PriorityQueue() #Un estado es un objeto (<nodo, camino>)
    visitados=[]
    
    src=problem.getStartState()
    estados.push((src, []),0)
    visitados.append(src)
    while not estados.isEmpty():
        nodo, camino = estados.pop()
        
        if problem.isGoalState(nodo):
                return camino
        for hijo, direccion, paso in problem.getSuccessors(nodo):
            if not hijo in visitados:
                visitados.append(hijo)
                aux=camino+[direccion]
                estados.push((hijo, aux), problem.getCostOfActions(aux))
    return []
    """
    print type(problem).__name__
    src=problem.getStartState()
    fin=src

    frontera=util.PriorityQueue()
    frontera.push(src,0)

    camino=[]
    came_from = {}
    cost_so_far = {}
    came_from[src] = None
    cost_so_far[src] = 0
    return []

    while not frontera.isEmpty():
        actual=frontera.pop()

        if problem.isGoalState(actual):
            fin=actual
            break

        for hijo, direccion, paso in problem.getSuccessors(nodo):
            nuevoCosto=problem.getCostOfActions(aux)
    """

def reconstruct_path(came_from, start, goal, camino):
    current = goal
    path = [current]
    while current != start:
        current = came_from[current]
        path.append(current)
    return path

# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch

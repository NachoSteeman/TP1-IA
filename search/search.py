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
from game import Directions
from typing import List

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
        return self.startState

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



def tinyMazeSearch(problem: SearchProblem) -> List[Directions]:
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem: SearchProblem) -> List[Directions]:
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """
    "*** YOUR CODE HERE ***"

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    
    
    pila = util.Stack()
    visitados = set()

    # Guardamos tuplas de (estado, camino_de_acciones)
    pila.push((problem.getStartState(), []))
    encontrado = False

    camino_final = []

    while not pila.isEmpty() and not encontrado:
        nodo, direcciones = pila.pop()

        if problem.isGoalState(nodo):
            encontrado = True 
            camino_final = direcciones

        elif nodo not in visitados:
            visitados.add(nodo)

            for vecino, dir, costo in problem.getSuccessors(nodo):
                if vecino not in visitados:
                    pila.push((vecino, direcciones + [dir]))

    return camino_final


def breadthFirstSearch(problem: SearchProblem) -> List[Directions]:
    """Search the shallowest nodes in the search tree first."""
    
    cola = util.Queue()
    visitados = set()
    
    cola.push((problem.getStartState(), []))
    encontrado = False 
    
    camino_final = []

    while not cola.isEmpty() and not encontrado: 
        node, direcciones = cola.pop()

        if problem.isGoalState(node):
            encontrado = True
            camino_final = direcciones

        elif node not in visitados:
            visitados.add(node)

            for vecino, accion, costo in problem.getSuccessors(node):
                if vecino not in visitados:
                    cola.push((vecino, direcciones + [accion]))
            
    return camino_final



def uniformCostSearch(problem: SearchProblem) -> List[Directions]:
    """Search the node of least total cost first."""
    priority = lambda elem: elem[2] # node = (state, dir, path_cost)

    frontier = util.PriorityQueueWithFunction(priority)
    reached = {}
    g_initial_state_cost = 0
    goal_path = []

    frontier.push((problem.getStartState(), [], g_initial_state_cost))

    goal = False 
    while not frontier.isEmpty() and not goal: 
        state, path, path_cost = frontier.pop()

        if problem.isGoalState(state):
            goal = True
            goal_path = path

        else:
            for child_state, dir, child_cost in problem.getSuccessors(state):
                g_child_cost = path_cost + child_cost

                if ((child_state not in reached) or (reached[child_state] > g_child_cost)):
                    reached[child_state] = g_child_cost 
                    frontier.push((child_state, path + [dir], g_child_cost))

    return goal_path

def nullHeuristic(state, problem=None) -> float:
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

# - TODO: cambiar reached[child] = f_cost por g_cost (fijarse si es lo mismo)
def aStarSearch(problem: SearchProblem, heuristic=nullHeuristic) -> List[Directions]:
    """Search the node that has the lowest combined cost and heuristic first."""
    priority = lambda elem: elem[2] + heuristic(elem[0], problem)

    frontier = util.PriorityQueueWithFunction(priority)
    reached = {}
    g_initial_state_cost = 0
    goal_path = []

    frontier.push((problem.getStartState(), [], g_initial_state_cost))

    goal = False 
    while not frontier.isEmpty() and not goal: 
        state, path, path_cost = frontier.pop()

        if problem.isGoalState(state):
            goal = True
            goal_path = path

        else:
            for child_state, dir, child_cost in problem.getSuccessors(state):
                g_child_cost = path_cost + child_cost
                f_child_cost = g_child_cost + heuristic(child_state, problem)

                if ((child_state not in reached) or (reached[child_state] > f_child_cost)):
                    reached[child_state] = f_child_cost
                    frontier.push((child_state, path + [dir], g_child_cost))

    return goal_path

# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch

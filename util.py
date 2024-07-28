class Node:
    """
    Class representing a node in the search tree.
    """
    def __init__(self, state, parent, action):
        self.state = state    # The state represented by the node
        self.parent = parent  # The parent node
        self.action = action  # The action that led to this node


class StackFrontier:
    """
    Stack-based frontier for DFS (Depth-First Search).
    """
    def __init__(self):
        self.frontier = []

    def add(self, node):
        """
        Add a node to the frontier.
        """
        self.frontier.append(node)

    def contains_state(self, state):
        """
        Check if the frontier contains a state.
        """
        return any(node.state == state for node in self.frontier)

    def empty(self):
        """
        Check if the frontier is empty.
        """
        return len(self.frontier) == 0

    def remove(self):
        """
        Remove a node from the frontier.
        """
        if self.empty():
            raise Exception("empty frontier")
        else:
            node = self.frontier[-1]
            self.frontier = self.frontier[:-1]
            return node


class QueueFrontier(StackFrontier):
    """
    Queue-based frontier for BFS (Breadth-First Search), inherits from StackFrontier.
    Uses FIFO (First-In-First-Out) principle where the first node added is the first to be removed.
    """
    def remove(self):
        """
        Remove a node from the frontier using FIFO (First-In-First-Out).
        FIFO ensures that nodes are explored in the order they were added.
        """
        if self.empty():
            raise Exception("empty frontier")
        else:
            node = self.frontier[0]
            self.frontier = self.frontier[1:]
            return node

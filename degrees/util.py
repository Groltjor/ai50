class Nodo():
    def __init__(self, state, parent, action):
        self.state = state
        self.parent = parent
        self.action = action


class FronteraStack():
    def __init__(self):
        self.frontier = []

    def add(self, nodo):
        self.frontier.append(nodo)

    def check_state(self, state):
        return any(nodo.state == state for nodo in self.frontier)

    def empty(self):
        return len(self.frontier) == 0

    def remove(self):
        if self.empty():
            raise Exception("empty frontier")
        else:
            nodo = self.frontier[-1]
            self.frontier = self.frontier[:-1]
            return nodo


class QueueFrontier(FronteraStack):

    def remove(self):
        if self.empty():
            raise Exception("empty frontier")
        else:
            nodo = self.frontier[0]
            self.frontier = self.frontier[1:]
            return nodo

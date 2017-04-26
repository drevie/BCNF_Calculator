""" This class is a list of functional dependencies """


class FuncDepList:

    def __init__(self):
        self.functionalDependencyList = []
        self.dependencyIterator = -1

    def insert(self, F):
        self.functionalDependencyList.append(F)

    def getNext(self):
        self.dependencyIterator += 1
        return self.functionalDependencyList[self.dependencyIterator]

    def reset(self):
        self.dependencyIterator = -1

    def count(self):
        return len(self.functionalDependencyList)

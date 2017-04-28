""" This class is a list of functional dependencies """


class FuncDepList:

    def __init__(self):
        self.functionalDependencyList = []
        self.dependencyIterator = -1

    def insert(self, F):
        self.functionalDependencyList.append(F)

    def getNext(self):
        self.dependencyIterator = self.dependencyIterator + 1
        return self.functionalDependencyList[self.dependencyIterator]

    def reset(self):
        self.dependencyIterator = -1

    def count(self):
        return len(self.functionalDependencyList)

    def end(self):
        if len(self.functionalDependencyList) == (self.dependencyIterator + 1):
            return True

        else:
            return False

    def print(self):
        for i in range(len(self.functionalDependencyList)):
            print(str(self.functionalDependencyList[i].left) + " -> " + str(self.functionalDependencyList[i].right))

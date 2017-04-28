""" This class stores all of the relations """


class DB:

    def __init__(self):
        self.relationList = []
        self.relationIterator = -1

    def insert(self, A):
        self.relationList.append(A)

    def getNext(self):
        self.dependencyIterator += 1
        return self.relationList[self.relationIterator]

    def reset(self):
        self.relationIterator = -1

    def count(self):
        return len(self.relationList)

    def end(self):
        if len(self.relationList) == (self.relationIterator + 1):
            return True

        else:
            return False

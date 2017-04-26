
class FunctionalDependency:

    def __init__(self, functionalDependencyRow):
        self.depdency = []
        self.left = []
        self.right = []

        self.leftFlag = True
        for i in range(len(functionalDependencyRow)):

            if(functionalDependencyRow[i] == '->'):
                self.leftFlag = False
                continue

            if(self.leftFlag):
                self.left.append(functionalDependencyRow[i])

            else:
                self.right.append(functionalDependencyRow[i])

            self.depdency.append(functionalDependencyRow[i])


from itertools import chain, combinations
from copy import copy
""" Class to contain a functional dependency """

# Note that we seperate the dependency into its left and right side to make computations on it easier


class FunctionalDependency:

    def __init__(self, functionalDependencyRow, dependencyList):
        self.dependencyList = dependencyList
        self.dependency = []
        self.left = []
        self.right = []

        self.leftFlag = True
        for i in range(len(functionalDependencyRow)):

            if(functionalDependencyRow[i] == '->'):
                self.leftFlag = False
                continue

            self.dependency.append(functionalDependencyRow[i])

            if(self.leftFlag):
                self.left.append(functionalDependencyRow[i])

            else:
                self.right.append(functionalDependencyRow[i])

    def lhs(self):
        return self.left

    def rhs(self):
        right = copy(self.right)
        # print("Printing Left Side before operations " + str(self.left))
        # print("Printing Right Side before operations " + str(self.right))

        # AXIOM 1
        for i in range(len(self.left)):
            if(self.left[i] in right):
                continue
            else:
                right.append(self.left[i])

        # print("Printing Left Side after axiom 1 " + str(self.left))
        # print("Printing Right Side after axiom 1 " + str(self.right))

        # AXIOM 2
        axiom_2_list = []
        changedFlag = True

        while(changedFlag):

            changedFlag = False

            for i in range(len(self.dependencyList.functionalDependencyList)):

                if(set(self.dependencyList.functionalDependencyList[i].left) < set(right)):
                    axiom_2_list.append(self.dependencyList.functionalDependencyList[i].right)
                else:
                    continue

            for i in range(len(axiom_2_list)):
                for j in range(len(axiom_2_list[i])):
                    if(axiom_2_list[i][j] in right):
                        continue
                    else:
                        changedFlag = True
                        right.append(axiom_2_list[i][j])

        # print("Printing Left Side after axiom 2" + str(self.left))
        # print("Printing Right Side after axiom 2" + str(self.right))

        return right

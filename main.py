import Relation
import Stack
import FunctionalDependency
import FuncDepList

global FunctionalDependencyList
global RelationsList


def readFile(filename):
    # We must open the file for reading
    relationList = []

    if(filename):
        try:
            inputFile = open(filename, "r")
            for line in inputFile:
                relation = line.split()
                relationList.append(relation)

        except Exception as e:
            print("Error opening the input file: %s %s" % (filename, repr(e)))

    else:
        print("Error: No filename given")

    return relationList


def getDependencies(inputList):
    FunctionalDependencyList = FuncDepList.FuncDepList()

    for i in range(len(inputList)):
        if(i == 0):
            continue

        else:
            f = FunctionalDependency.FunctionalDependency(inputList[i])
            FunctionalDependencyList.insert(f)

    return FunctionalDependencyList


if __name__ == "__main__":
    global Relations
    global DependencyList

    inputList = readFile("inputFile.txt")

    # NOW GET THE RELATIONS AND THE FUNCTIONAL DEPENDENCIES
    Relations = inputList[0]
    DependencyList = getDependencies(inputList)

    print("printing relations")
    print(str(Relations) + '\n')

    print("printing dependencies")
    D1 = DependencyList.getNext()
    D2 = DependencyList.getNext()
    D3 = DependencyList.getNext()

    print("D1: left= " + str(D1.left) + " right= " + str(D1.right))
    print("D2: left= " + str(D2.left) + " right= " + str(D2.right))
    print("D3: left= " + str(D3.left) + " right= " + str(D3.right))

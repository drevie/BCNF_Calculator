from FuncDepList import FuncDepList
from copy import copy
from itertools import combinations
from Stack import Stack
from DB import DB
global DependencyList


class FD:
    def __init__(self, lhs, rhs):
        self.left = lhs
        self.right = rhs

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

            for i in range(len(DependencyList.functionalDependencyList)):

                if(set(DependencyList.functionalDependencyList[i].left) < set(right)):
                    axiom_2_list.append(DependencyList.functionalDependencyList[i].right)
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


def readFile(filename):
    print(".... readFile ....")

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


def generateFDs(List):
    print(".... generateFDs ....")

    F_List = FuncDepList()

    for i in range(len(List)):

        left = []
        right = []

        if i == 0:
            continue
        else:
            leftFlag = True
            for j in range(len(List[i])):
                if(List[i][j] == '->'):
                    leftFlag = False
                    continue

                if(leftFlag):
                    left.append(List[i][j])
                else:
                    right.append(List[i][j])

        fd = FD(left, right)
        F_List.insert(fd)

    return F_List


def generate_all_pairs(R):
    print(R)
    print(".... generate all pairs ....")
    combos = []
    for r in range(0, len(R) + 1):
        for subset in combinations(R, r):
            if(subset):
                fd = FD(subset, '')
                combos.append(fd)

    return combos


def generate_all_possible_fd(L, FDs):
    print(".... generate all fds ....")
    for combination in L:
        FDs.reset()
        while(not FDs.end()):
            FD = FDs.getNext()
            # print("FD Left = " + str(FD.left) + " COMBO LEF = " + str(combination.left))
            if(set(FD.left) < set(combination.left) or (set(FD.left) == set(combination.left))):
                combination.right = list(set(FD.right) | set(combination.right))
                # print("Combination")
                # print(combination.right)
    return L


def clean_all_fd(L):
    print(".... cleaning empty sets ....")
    deleteList = []
    for combo in L:
        if combo.right == '':
            deleteList.append(combo)

    for combo in deleteList:
        L.remove(combo)

    return L


def get_closure(L):
    for fd in L:
        fd.right = fd.rhs()
    return L


def get_all_non_trivial(L):
    print(".... getting all non trivial ....")
    non_trivial = []

    for combo in L:
        if(set(combo.left) & set(combo.right)):
            continue
        else:
            non_trivial.append(combo)

    return non_trivial


def break_down_dependencies(L):
    insertList = []
    for fd in L:
        print(str(fd.left) + "->" + str(fd.right))
        for r in range(0, len(fd.right) + 1):
            for subset in combinations(fd.right, r):
                if(subset):
                    if(subset != fd.right):
                        new_FD = FD(fd.left, subset)
                        insertList.append(new_FD)

    for fd in insertList:
        L.append(fd)

    return L


def clean_non_trivial(L):
    print(".... clean non trivial ....")

    for fd in L:
        fd.right = list(set(fd.right) - set(fd.left))

    deleteList = []
    for fd in L:
        if fd.right:
            continue
        else:
            deleteList.append(fd)

    for fd in deleteList:
        L.remove(fd)


def decomposition(R, L):
    db = DB()
    S = Stack()

    S.push(R)
    while(not S.isEmpty()):
        A = S.pop()
        violation = False
        L.reset()
        while(not L.end() and not violation):
            F = L.getNext()

            if(BCNF_Violation(F, A, True)):
                violation = True

        if(not violation):
            # print("We're inserting A into the DB")
            db.insert(A)
        else:
            # print("We are pushing smaller stuff onto the stack")
            S.push(list(set(F.lhs()) | set(F.rhs())))
            subtractSet = set(F.rhs()) - set(F.lhs())
            S.push(list(set(A) - subtractSet))

            
            print("Relationship: " + str(A))
            print("Printing stack push 1")
            print(str(list(set(F.lhs()) | set(F.rhs()))))
            print("Printing stack push 2")
            print(list(set(A) - subtractSet))


    return db


def BCNF_Violation(F, A, printFlag):

    if(printFlag):
        print("A = " + str(A))
        print("F = " + str(F.lhs()) + "->" + str(F.rhs()))

    # print("set(F.lhs) <= set(A) = " + str(set(F.lhs()) <= set(A)))
    # print("not (set(A) <= (set(F.rhs()) | set(F.lhs()))) = " + str(not (set(A) <= (set(F.rhs()) | set(F.lhs())))))

    if(set(F.lhs()) <= set(A) and not (set(A) <= (set(F.rhs()) | set(F.lhs())))):
        subtractSet = set(F.rhs()) - set(F.lhs())
        if(set(A) - subtractSet == set(A)):
            print("Announcement FAQ #2")
            return False

        print("F = " + str(F.lhs()) + "->" + str(F.rhs()))
        print("BCNF Violation")
        return True

    else:
        if printFlag:
            print("BCNF NON Violation")
            #
        return False


if __name__ == "__main__":
    global DependencyList

    print(".... __main__ ....")

    inputList = readFile("inputFile.txt")
    f_list = generateFDs(inputList)

    DependencyList = f_list

    All_Combinations = generate_all_pairs(inputList[0])
    All_FDs = generate_all_possible_fd(All_Combinations, DependencyList)
    All_FDs = clean_all_fd(All_FDs)
    All_FDs = get_closure(All_FDs)
    all_fds = All_FDs
    All_FDs = generate_all_possible_fd(All_FDs, DependencyList)
    clean_non_trivial(All_FDs)
    Non_Trivial_FDs = get_all_non_trivial(All_FDs)

    print('\n' + "---------- Part 1 ----------")
    print("Number of Non Trivial FDS = " + str(len(Non_Trivial_FDs)))
    print("All Non Trivial FDS: ")
    for fd in Non_Trivial_FDs:
        print(str(fd.left) + " -> " + str(fd.right))

    print("... Press enter to continue to part 2")
    input()

    L = FuncDepList()
    print('\n' + "---------- Part 2 ----------")
    for entry in inputList:
        if entry == inputList[0]:
            continue
        left = []
        right = []
        leftFlag = True
        for i in range(len(entry)):
            if(entry[i] == "->"):
                leftFlag = False
                continue
            if(leftFlag):
                left.append(entry[i])
            else:
                right.append(entry[i])
        fd = FD(left, right)
        BCNF_Violation(fd, inputList[0], True)
        fd.BCNF_Violation = True
        L.insert(fd)

    print("... Press enter to continue to part 3")
    input()

    print('\n' + "---------- Part 3 ----------")
    db = decomposition(inputList[0], L)

    print("DB RELATION LIST")
    for r in db.relationList:
        print(r)

    print("... Press enter to end program")
    input()

    print(".... end __main___ ....")

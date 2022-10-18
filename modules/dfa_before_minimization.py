def get_edge(inputString):
    saver = []
    # remove newline on input
    for i in inputString.split("\r\n"):
        # split one line by whitespace
        temp = list(str(i).split(" "))
        # add to saver
        saver.append(temp)
    for i in saver:
        # remove the alphabet (only edge)
        i.pop(1)
    return saver


def get_edge_label(inputString):
    edgeSaver = []
    # remove newline on input
    for i in inputString.split("\r\n"):
        # split one line by whitespace
        temp = list(str(i).split(" "))
        # add to edgeSaver
        edgeSaver.append(temp)
    # solve problem when missing label..
    # ..when a state can go to another state with
    # ..two or more alphabets
    pairEdge = get_edge(inputString)
    labelSaver = []
    for i in pairEdge:
        temp = []
        for j in edgeSaver:
            if (i[0] == j[0]) and (i[1] == j[2]):
                temp.append(j[1])
        temp.sort()
        labelSaver.append(list(temp))
    dictResult = {}
    for key in pairEdge:
        temp = ", ".join(labelSaver.pop(0))
        dictResult[tuple(key)] = temp
    return dictResult


def split_sort_string(inputString):
    result = inputString.split(", ")
    result.sort()
    return result


def get_state(inputString):
    return split_sort_string(inputString)


def get_alphabet(inputString):
    return split_sort_string(inputString)


def get_initial(inputString):
    return split_sort_string(inputString)


def get_final(inputString):
    return split_sort_string(inputString)


def get_transition_table(state, alphabet, inputString):
    edgeSaver = []
    # remove newline on input
    for i in inputString.split("\r\n"):
        # split one line by whitespace
        temp = list(str(i).split(" "))
        # add to edgeSaver
        edgeSaver.append(temp)
    labelSaver = []
    for i in edgeSaver:
        # temp contains the alphabet
        temp = i.pop(2)
        # add temp to labelSaver
        labelSaver.append(temp)
    temp = []
    for i in edgeSaver:
        # change from list to tuple
        temp.append(tuple(i))
    # make nested tuple (2D)
    tupleEdge = tuple(temp)
    # make dictionary
    dictResult = {}
    # pair the edge with the alphabet
    for key in tupleEdge:
        dictResult[key] = labelSaver.pop(0)
    # get list from alphabet and state
    aList = get_alphabet(alphabet)
    sList = get_state(state)
    # saver for save the result
    saver = []
    # temp for saving temporary result for each state
    temp = []
    for i in sList:
        temp.append(i)
        for j in aList:
            temp.append(dictResult[(i, j)])
        saver.append(list(temp))
        temp.clear()
    return saver


def get_detailed_description(inputString):
    # saver for save the result
    saver = []
    # temp for saving temporary result for each state
    temp = []
    # remove newline on input
    for i in inputString.split("\r\n"):
        # split one line by whitespace and assign to variable
        qStart, a, qEnd = str(i).split(" ")
        # add some symbol according to delta
        getString = "\u03B4(" + qStart + ", " + a + ") = " + qEnd + ","
        temp.append(getString)
        saver.append(list(temp))
        temp.clear()
    # sort the list, so the result will be sorted
    saver.sort()
    return saver

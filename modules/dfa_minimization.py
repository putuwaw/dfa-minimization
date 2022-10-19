listEdge = []


def split_sort_string(inputString):
    result = inputString.split(", ")
    result.sort()
    return result


def get_list_edge(inputString):
    saver = []
    # remove newline on input
    for i in inputString.split("\r\n"):
        # split one line by whitespace
        temp = list(str(i).split(" "))
        # add to saver
        saver.append(temp)
    return saver


def get_pair_edge(inputString):
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


def delta(stateStart, alphabet):
    global listEdge
    for i in listEdge:
        if (i[0] == stateStart) and (i[1] == alphabet):
            return i[2]


def get_key(first, second):
    global listEdge
    temp = []
    for i in listEdge:
        if (i[0] == first) and (i[2] == second):
            temp.append(i[1])
    return temp


def table_filling_method(state, alpha, trans, init, f, idx):
    global listEdge
    listEdge = get_list_edge(trans)

    states = split_sort_string(state)
    alphabets = split_sort_string(alpha)
    if (idx == 4):
        return alphabets
    pairEdge = get_pair_edge(trans)
    initial = split_sort_string(init)
    final = split_sort_string(f)

    listTable = []
    for i in range(len(states) - 1):
        for j in range(i+1, len(states)):
            temp = []
            temp.append(states[i])
            temp.append(states[j])
            temp.append(False)
            listTable.append(list(temp))

    # 0th iteration
    for i in listTable:
        if (i[2] == False):
            if (i[0] in final and i[1] not in final):
                i[2] = True
            if (i[0] not in final and i[1] in final):
                i[2] = True

    # n-th iteration
    isChange = True
    while (isChange):
        isChange = False
        for i in listTable:
            if (i[2] == False):
                for j in alphabets:
                    temp = []
                    temp.append(delta(i[0], j))
                    temp.append(delta(i[1], j))
                    temp.append(True)
                    temp2 = []
                    temp2.append(delta(i[1], j))
                    temp2.append(delta(i[0], j))
                    temp2.append(True)
                    if (temp in listTable) or (temp2 in listTable):
                        isChange = True
                        i[2] = True

    # list of blank states
    noTable = []
    for i in listTable:
        if (i[2] == False):
            noTable.append(i)

    # list of states that have been paired
    resultPairEdge = []
    for i in pairEdge:
        tempList = [i[0], i[1]]
        for j in noTable:
            if (i[0] in j) and (i[1] in j):
                newString = j[0] + j[1]
                tempList[0] = newString
                tempList[1] = newString
            elif (i[0] in j):
                newString = j[0] + j[1]
                tempList[0] = newString
            elif (i[1] in j):
                newString = j[0] + j[1]
                tempList[1] = newString
        if (list(tempList) not in resultPairEdge) and (tempList != []):
            resultPairEdge.append(list(tempList))
    if (idx == 1):
        return resultPairEdge
    # label for resultPairEdge
    labelPairEdge = []
    for j in resultPairEdge:
        if (len(states[0]) == 1):
            for k in j[0]:
                temp = []
                for l in j[1]:
                    tempRes = get_key(k, l)
                    for i in tempRes:
                        if (i not in temp):
                            temp.append(i)
                            temp.sort()
            labelPairEdge.append((temp))
        elif (len(states[0]) == 2):
            for k in range(0, len(j[0]), 2):
                temp = []
                for l in range(0, len(j[1]), 2):
                    tempRes = get_key(j[0][k:k+2], j[1][l:l+2])
                    for i in tempRes:
                        if (i not in temp):
                            temp.append(i)
                            temp.sort()
            labelPairEdge.append((temp))
    # Dictionary for transition diagram image
    resultDict = {}
    for i in range(len(resultPairEdge)):
        strTemp = ", ".join(labelPairEdge[i])
        resultDict[tuple(resultPairEdge[i])] = strTemp
    if (idx == 2):
        return resultDict
    # States result minimization
    minimStates = []
    for i in resultPairEdge:
        if (i[0] not in minimStates):
            minimStates.append(i[0])
    if (idx == 3):
        return minimStates
    # list for tabel transition
    transTable = []
    for i in minimStates:
        temp = []
        temp.append(i)
        # for every list
        for j in alphabets:
            # for every alphabets
            for k in range(len(resultPairEdge)):
                # if state found and alphabets in list final
                if (resultPairEdge[k][0] == i) and (j in labelPairEdge[k]):
                    temp.append(resultPairEdge[k][1])
        transTable.append(list(temp))
    if (idx == 7):
        return transTable
    # Initial states result minimization
    minimInitial = []
    for i in minimStates:
        for j in initial:
            if (j in i):
                minimInitial.append(i)
    if (idx == 5):
        return minimInitial
    # Final states result minimization
    minimFinal = []
    for i in minimStates:
        for j in final:
            if (j in i) and (i not in minimFinal):
                minimFinal.append(i)
    if (idx == 6):
        return minimFinal
    # List for detailed description
    prepListDetail = []
    minimListDetail = []
    for i in range(len(resultPairEdge)):
        for j in range(len(labelPairEdge[i])):
            prepListDetail.append(resultPairEdge[i][0])
            prepListDetail.append(labelPairEdge[i][j])
            prepListDetail.append(resultPairEdge[i][1])
    for i in range(0, len(prepListDetail), 3):
        qStart = prepListDetail[i]
        alfa = prepListDetail[i+1]
        qFinal = prepListDetail[i+2]
        temp = []
        getString = "\u03B4(" + qStart + ", " + alfa + ") = " + qFinal + ","
        temp.append(getString)
        minimListDetail.append(list(temp))
    if (idx == 8):
        return minimListDetail

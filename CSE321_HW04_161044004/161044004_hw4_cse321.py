'''
    CSE 321
    Introduction to Algorithm Design
    Homework 04
    Omer CEVIK
    161044004
'''
__author__ = 'Omer CEVIK'

#################################################################################
#                          QUESTION    1     BEGIN                              #
#################################################################################

def question1partB(A):

    for i in range(1,len(A)):
        for j in range(1,len(A[i])):
            for k in range(i+1,len(A)):
                for l in range(j+1,len(A[i])):
                    if not A[i][j] + A[k][l] <= A[i][l] + A[k][j]:
                        return [A[k][j], k, j] if A[i][l] > A[k][j] else [A[i][l], i, l]

    return ["It","is","Special Array"]

def question1partC(A):

    Result = []
    for row in A:
        IndexArray = [0] * len(row)
        i = 0
        while i < len(row):
            IndexArray[i] = i
            i += 1

        quickSort(row, 0, len(row)-1, IndexArray)

        Result.append(['Element : ' + str(row[0]),'Index : ' + str(IndexArray[0])])

    return Result

def partition(A, start, end, IndexArray):

    i = start - 1

    pivot = A[end]

    for j in range(start , end):

        if A[j] <= pivot:
            i = i+1
            A[i],A[j] = A[j],A[i]
            IndexArray[i],IndexArray[j] = IndexArray[j],IndexArray[i]

    A[i+1],A[end] = A[end],A[i+1]
    IndexArray[i+1],IndexArray[end] = IndexArray[end],IndexArray[i+1]

    return i+1

def quickSort(A, start, end, IndexArray):

    if start < end:
        startPivot = partition(A, start, end, IndexArray)

        quickSort(A, start, startPivot-1, IndexArray)
        quickSort(A, startPivot+1, end, IndexArray)

#################################################################################
#                          QUESTION    1     END                                #
#################################################################################

#-------------------------------------------------------------------------------#

#################################################################################
#                          QUESTION    2     BEGIN                              #
#################################################################################

def question2(A, B, k):

    return findKthElement(A, B, len(A)-1, len(B)-1, 0, 0, k)

def findKthElement(A, B, rightSubArrayLengthOfA, rightSubArrayLengthOfB, leftSubArrayLengthOfA, leftSubArrayLengthOfB, k):

    if (leftSubArrayLengthOfA <= rightSubArrayLengthOfA and leftSubArrayLengthOfB <= rightSubArrayLengthOfB):

        midOfA = (leftSubArrayLengthOfA + rightSubArrayLengthOfA) // 2
        midOfB = (leftSubArrayLengthOfB + rightSubArrayLengthOfB) // 2

        newMidA = midOfA - leftSubArrayLengthOfA + 1
        newMidB = midOfB - leftSubArrayLengthOfB + 1

        if (newMidA + newMidB > k and A[midOfA] > B[midOfB]):
            rightSubArrayLengthOfA = midOfA - 1
        elif (newMidA + newMidB > k and A[midOfA] <= B[midOfB]):
            rightSubArrayLengthOfB = midOfB - 1
        elif (newMidA + newMidB <= k and A[midOfA] < B[midOfB]):
            leftSubArrayLengthOfA = midOfA + 1
            k -= newMidA
        elif(newMidA + newMidB <= k and A[midOfA] >= B[midOfB]):
            leftSubArrayLengthOfB = midOfB + 1
            k -= newMidB

        return findKthElement(A, B, rightSubArrayLengthOfA, rightSubArrayLengthOfB, leftSubArrayLengthOfA, leftSubArrayLengthOfB, k)

    return A[leftSubArrayLengthOfA + k - 1] if leftSubArrayLengthOfA <= rightSubArrayLengthOfA else B[leftSubArrayLengthOfB + k - 1]


#################################################################################
#                          QUESTION    2     END                                #
#################################################################################

#-------------------------------------------------------------------------------#

#################################################################################
#                          QUESTION    3     BEGIN                              #
#################################################################################

def question3(A):

    return findMaxSubArraySum(A, 0, len(A)-1)


def findMaxSubArraySum(A, start, end) :

    if (start == end) :
        return A[start]

    middle = (start + end) // 2

    leftSubSet = findMaxSubArraySum(A, start, middle)
    rightSubSet = findMaxSubArraySum(A, middle+1, end)
    sumSubSet = divideAndConquerSum(A, start, middle, end)

    return max(leftSubSet, rightSubSet, sumSubSet)

def divideAndConquerSum(A, start, middle, end) :

    sumOfArray = 0
    sumOfLeftSubArray = sumOfRightSubArray = float("-inf")

    index = middle
    while(index > start - 1):
        sumOfArray += A[index]

        if (sumOfArray > sumOfLeftSubArray):
            sumOfLeftSubArray = sumOfArray
        index -= 1

    sumOfArray = 0

    index = middle + 1

    while(index < end + 1):
        sumOfArray += A[index]

        if (sumOfArray > sumOfRightSubArray):
            sumOfRightSubArray = sumOfArray
        index += 1

    return sumOfLeftSubArray + sumOfRightSubArray;


#################################################################################
#                          QUESTION    3     END                                #
#################################################################################

#-------------------------------------------------------------------------------#

#################################################################################
#                          QUESTION    4     BEGIN                              #
#################################################################################

def question4(G):

    V = len(G)

    colorArr = [-1] * V

    colorArr[0] = 1

    queue = [0]

    while queue:

        u = queue.pop()

        if G[u][u] == 1:
            return False;

        for v in range(V):

            if G[u][v] == 1 and colorArr[v] == -1:
                colorArr[v] = 1 - colorArr[u]
                queue.append(v)

            elif G[u][v] == 1 and colorArr[v] == colorArr[u]:
                return False
    return True

#################################################################################
#                          QUESTION    4     END                                #
#################################################################################

#-------------------------------------------------------------------------------#

#################################################################################
#                          QUESTION    5     BEGIN                              #
#################################################################################

def question5(C, P):

    maxGain = [float("-inf"),float("-inf")]
    if len(P) == 1:
        return ["There is no day", "to make money"]

    divideAndConquerMax(C[:len(C)-1], P[1::], maxGain, 0, len(C)-1)
    return [maxGain[0], maxGain[1]+1]

def divideAndConquerMax(C, P, maxGain, start, end):

    if end == start:
        return

    mid = (end + start)//2
    gain = P[mid] - C[mid]

    if gain > maxGain[0]:
        maxGain[0] = gain
        maxGain[1] = end

    divideAndConquerMax(C, P, maxGain, start, mid)
    divideAndConquerMax(C, P, maxGain, mid + 1, end)



#################################################################################
#                          QUESTION    5     END                                #
#################################################################################


#-------------------------------------------------------------------------------#


#-----------------------          TESTS         --------------------------------#

#----------------------        QUESTION 1        --------------------------------#

def test1():
    print('Question 1\n')

    A = [[10, 17, 13, 28, 23],
         [17, 22, 16, 29, 23],
         [24, 28, 22, 34, 24],
         [11, 13, 6, 17, 7],
         [45, 44, 3, 37, 23],
         [36, 33, 19, 21, 6],
         [75, 66, 51, 53, 34]]

    print('2D Array is :')
    for x in A:
        print(x)

    print()

    ResultB = question1partB(A)

    print('Question 1 Part B\n')
    print('Change element is :\t' + str(ResultB[0]))
    print('Column index is   :\t' + str(ResultB[1]))
    print('Row    index is   :\t' + str(ResultB[2]))
    print()

    A = [[10, 17, 13, 28, 23],
         [17, 22, 16, 29, 23],
         [24, 28, 22, 34, 24],
         [11, 13, 6, 17, 7],
         [45, 44, 32, 37, 23],
         [36, 33, 19, 21, 6],
         [75, 66, 51, 53, 34]]

    print('2D Array is :')
    for x in A:
        print(x)

    print()

    ResultB = question1partB(A)

    print('Question 1 Part B\n')
    print('Change element is :\t' + str(ResultB[0]))
    print('Column index is   :\t' + str(ResultB[1]))
    print('Row    index is   :\t' + str(ResultB[2]))
    print()

    A = [[10, 17, 13, 28, 23],
         [17, 22, 16, 29, 23],
         [24, 28, 22, 34, 24],
         [11, 13, 6, 17, 6],
         [45, 44, 32, 37, 23],
         [36, 33, 19, 21, 6],
         [75, 66, 51, 53, 34]]

    print('2D Array is :')
    for x in A:
        print(x)

    print()

    ResultC = question1partC(A)

    print('Question 1 Part C\n')
    print('Minimum elements are :')
    for mins in ResultC:
        print(mins)
    print('\n')

#----------------------        QUESTION 2        --------------------------------#

def test2():
    print('Question 2\n')

    A = [1, 2, 3, 70, 90]
    B = [2, 4, 6, 8, 10]
    k = 9

    print('First  array A \t:\t' + str(A))
    print('Second array B \t:\t' + str(B))
    print('Searched kth element :\t' + str(k))
    print('Found ' + str(k) + 'th element :\t' + str(question2(A, B, k)))

    print('\n')


#----------------------        QUESTION 3        --------------------------------#

def test3():
    print('Question 3\n')

    A = [5, -6, 6, 7, -6, 7, -4, 3]

    print('Array is \t\t: ' + str(A))
    print('Sum of max sub-array is : ' + str(question3(A)))

    print('\n')


#----------------------        QUESTION 4        --------------------------------#

def test4():
    print('Question 4\n')

    G = [
         [0, 1, 0, 1],
         [1, 0, 1, 0],
         [0, 1, 0, 1],
         [1, 0, 1, 0]
        ]

    print('Graph is : ')
    for i in G:
        print(i)
    print()
    print('Is the Graph bipartite  : ' + str(question4(G)))
    print()

    G = [
         [0, 1, 1, 1],
         [1, 0, 1, 0],
         [0, 1, 0, 1],
         [1, 0, 1, 0]
        ]

    print('Graph is : ')
    for i in G:
        print(i)
    print()
    print('Is the Graph bipartite  : ' + str(question4(G)))


    print('\n')


#----------------------        QUESTION 5        --------------------------------#

def test5():
    print('Question 5\n')

    C = [5, 11, 2, 21, 5, 7, 8, 12, 13, '−']
    P = ['−', 7, 9, 5, 21, 7, 13, 10, 14, 20]

    Result = question5(C, P)

    print('Cost array is  \t: ' + str(C))
    print('Price array is \t: ' + str(P))
    print('Max gain is    \t: ' + str(Result[0]))
    print('Max gain\'s cost day is    : ' + str(Result[1]))

    print('\n')

    C = [5, 11, 2, 21, 5, 7, 8, 12, 13, '−']
    P = ['−']

    Result = question5(C, P)

    print('Cost array is  \t: ' + str(C))
    print('Price array is \t: ' + str(P))
    print('Max gain is    \t: ' + str(Result[0]))
    print('Max gain\'s cost day is    : ' + str(Result[1]))

    print('\n')


##################################################################################

def testAll():
    test1()
    test2()
    test3()
    test4()
    test5()

testAll()

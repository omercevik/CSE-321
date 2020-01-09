'''
    CSE 321
    Introduction to Algorithm Design
    Homework 05
    Omer CEVIK
    161044004
'''
__author__ = 'Omer CEVIK'

#################################################################################
#                          QUESTION    1     BEGIN                              #
#################################################################################

def question1(NY, SF, M):

    NY_costs = [0] * (len(SF)+1)
    SF_costs = [0] * (len(SF)+1)

    for i in range(1,len(SF)+1):

        NY_costs[i] = NY[i-1] + min(NY_costs[i-1], M + SF_costs[i-1])
        SF_costs[i] = SF[i-1] + min(SF_costs[i-1], M + NY_costs[i-1])

    minCost = min(NY_costs[-1], SF_costs[-1])

    return 'Minimum cost is ' + str(minCost)

#################################################################################
#                          QUESTION    1     END                                #
#################################################################################

#-------------------------------------------------------------------------------#

#################################################################################
#                          QUESTION    2     BEGIN                              #
#################################################################################

def question2(sessions):

    sortBubble(sessions)

    n = len(sessions)
    result = [] * n

    i = 0
    result.append(sessions[i])

    for j in range(1,n):
        if sessions[j][0] >= sessions[i][1]:
            result.append(sessions[j])
            i = j

    return result

def sortBubble(sessions):
    for i in range(len(sessions)):
            for j in range(len(sessions)):
                if sessions[i][1] <= sessions[j][1]:
                    sessions[i],sessions[j] = sessions[j],sessions[i]

#################################################################################
#                          QUESTION    2     END                                #
#################################################################################

#-------------------------------------------------------------------------------#

#################################################################################
#                          QUESTION    3     BEGIN                              #
#################################################################################

from itertools import combinations

def question3(S):

    for index in range(len(S)+1):
        for sublist in combinations(S, index):
            if sum(sublist) == 0 and sublist != ():
                return 'Zero sum sub-list is\t' + str(list(sublist))

    return 'No zero sum sub-list found!'



#################################################################################
#                          QUESTION    3     END                                #
#################################################################################

#-------------------------------------------------------------------------------#

#################################################################################
#                          QUESTION    4     BEGIN                              #
#################################################################################

import numpy as np

def question4(sequenceA, sequenceB, match_score, mismatch_score, gap_score):

    MatchTable = np.zeros((len(sequenceB) + 1, len(sequenceA) + 1), np.int)

    matchIndexes = []
    misMatchCounter = 0

    m = n = 1
    for i in range(len(sequenceB)):
        n = 1
        for j in range(len(sequenceA)):
            if sequenceA[j] == sequenceB[i]:
                MatchTable[m][n] = max(MatchTable[m][n - 1], MatchTable[m - 1][n]) + 2
            else:
                neighborMax = max(MatchTable[m][n - 1], MatchTable[m - 1][n])
                MatchTable[m][n] = 0 if neighborMax == 0 else neighborMax - 1
            n += 1
        if max(MatchTable[m]) == 0:
            misMatchCounter += 1
        else:
            maxIndex = 0
            maxValue = MatchTable[m][0]
            for x in range(1,len(MatchTable[m])):
                if MatchTable[m][x] > maxValue and MatchTable[m - 1][x] - 1 != MatchTable[m][x]:
                    maxValue = MatchTable[m][x]
                    maxIndex = x
            matchIndexes.append(maxIndex-1)
        m += 1

    matchCounter = len(matchIndexes)

    counter = 0
    gapCounter = 0

    for i in range(1, max(matchIndexes)):
        if i != matchIndexes[counter]:
            gapCounter += 1
        else:
            counter += 1


    print('Sequence A is ' + str(sequenceA))
    print('Sequence B is ' + str(sequenceB))
    print('Cost = N * match_score + M * mismatch_score + K * gap_score')
    print('Cost = ' + str(matchCounter) + ' * ' + str(match_score) + ' + ' + str(misMatchCounter) + ' * ' + str(mismatch_score) + ' + ' + str(gapCounter) + ' * ' + str(gap_score))
    return 'Cost is ' + str(matchCounter * match_score + misMatchCounter * mismatch_score + gapCounter * gap_score)

#################################################################################
#                          QUESTION    4     END                                #
#################################################################################

#-------------------------------------------------------------------------------#

#################################################################################
#                          QUESTION    5     BEGIN                              #
#################################################################################

def question5(A):

    A.sort()
    sumOfA = A[0]
    sumSize = 0

    for elementOfA in range(1,len(A)):
        sumOfA += A[elementOfA]
        sumSize += sumOfA

    return 'Sum of array is ' + str(sumOfA), 'Sum operation count is ' + str(sumSize)

#################################################################################
#                          QUESTION    5     END                                #
#################################################################################


#-------------------------------------------------------------------------------#


#-----------------------          TESTS         --------------------------------#

#----------------------        QUESTION 1        --------------------------------#

def test1():
    print('Question 1\n')

    NY = [1, 3, 20, 30]
    SF = [50, 20, 2, 4]
    M = 10

    print('NY is\t' + str(NY))
    print('SF is\t' + str(SF))
    print('M is\t' + str(M))
    print(question1(NY,SF,M))

    print('\n')

#----------------------        QUESTION 2        --------------------------------#

def test2():
    print('Question 2\n')

    sessions = [[5, 9],[1, 2],[3, 4],[0, 6],[5, 7],[8, 9]]

    print('[start time, end time]')
    print('Sessions are\t: ' + str(sessions))
    print('You can go on\t: ' + str(question2(sessions)))

    print('\n')


#----------------------        QUESTION 3        --------------------------------#

def test3():
    print('Question 3\n')

    S = [-1, 6, 4, 2, 3, -7, -5]

    print('List is\t\t\t' + str(S))
    print(question3(S))
    print()

    S = [1, 2, 3, 4, 5]

    print('List is\t\t\t' + str(S))
    print(question3(S))

    print('\n')


#----------------------        QUESTION 4        --------------------------------#

def test4():
    print('Question 4\n')

    sequenceA = 'ALIGNMENT'
    sequenceB = 'SLIME'
    match_score = 2
    mismatch_score = -2
    gap_score = -1

    print(question4(sequenceA, sequenceB, match_score, mismatch_score, gap_score))
    print()

    sequenceA = 'ALIGNMENT'
    sequenceB = 'LIME'

    print(question4(sequenceA, sequenceB, match_score, mismatch_score, gap_score))

    print('\n')


#----------------------        QUESTION 5        --------------------------------#

def test5():
    print('Question 5\n')

    A = [1, 5, 4, 9]

    print('Array is\t: ' + str(A))
    print('Sum result is\t: ' + str(question5(A)))

    print('\n')


##################################################################################

def testAll():
    test1()
    test2()
    test3()
    test4()
    test5()

testAll()

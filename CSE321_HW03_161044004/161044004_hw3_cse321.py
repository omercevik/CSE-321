'''
    CSE 321
    Introduction to Algorithm Design
    Homework 03
    Omer CEVIK
    161044004
'''
__author__ = 'Omer CEVIK'

#################################################################################
#                          QUESTION    1     BEGIN                              #
#################################################################################

def question1(A):
    B = []
    decrease_and_conquerQ1(A,B,0,0,len(A)//2,0)
    decrease_and_conquerQ1(A,B,len(A)//2,1,len(A),0)
    return B

def decrease_and_conquerQ1(A,B,indexA,oddEven,lengthOfA,indexB):
    if indexA < lengthOfA:
        B.insert(indexB+oddEven,A[indexA])
        return decrease_and_conquerQ1(A,B,indexA+1,oddEven+1,lengthOfA,indexB+1)
    else:
        return B

#################################################################################
#                          QUESTION    1     END                                #
#################################################################################

#-------------------------------------------------------------------------------#

#################################################################################
#                          QUESTION    2     BEGIN                              #
#################################################################################

import random

def findFakeCoin(array, first, last, sizeOfCoins):
    if sizeOfCoins == 1:
        return first
    elif sizeOfCoins == 2:
        if last != len(array):
            if array[first] > array[last]:
                return last
            elif array[first] < array[last]:
                return first
        else:
            if array[first] > array[last-1]:
                return last-1
            elif array[first] < array[last-1]:
                return first
    else:
        weighbridge = int(sizeOfCoins/3)
        A_Weight = sum(array[first:first+weighbridge])
        B_Weight = sum(array[first+weighbridge:first+2*weighbridge])
        if A_Weight == B_Weight:
            result = findFakeCoin(array, first+2*weighbridge, last, last-(first+2*weighbridge))
        elif A_Weight > B_Weight:
            result = findFakeCoin(array, first+weighbridge, first+2*weighbridge, weighbridge)
        else:
            result = findFakeCoin(array, first, first+weighbridge, weighbridge)
        return result

#################################################################################
#                          QUESTION    2     END                                #
#################################################################################

#-------------------------------------------------------------------------------#

#################################################################################
#                          QUESTION    3     BEGIN                              #
#################################################################################

def quickSortPartition(arr, low, high, swapSize):
    i = low - 1
    pivot = arr[high]

    for j in range(low , high):
        if arr[j] <= pivot:
            i = i+1
            arr[i],arr[j] = arr[j],arr[i]
            swapSize[0] = swapSize[0] + 1

    arr[i+1],arr[high] = arr[high],arr[i+1]
    swapSize[0] = swapSize[0] + 1
    return i+1

def quickSort(arr, low, high, swapSize):
    if low < high:
        pi = quickSortPartition(arr,low,high,swapSize)
        quickSort(arr, low, pi-1, swapSize)
        quickSort(arr, pi+1, high, swapSize)


def insertionSort(arr, swapSize):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j] :
                arr[j+1] = arr[j]
                swapSize[0] = swapSize[0] + 1
                j -= 1

        swapSize[0] = swapSize[0] + 1
        arr[j+1] = key

#################################################################################
#                          QUESTION    3     END                                #
#################################################################################

#-------------------------------------------------------------------------------#

#################################################################################
#                          QUESTION    4     BEGIN                              #
#################################################################################

def question4(A):
    # Decrease and Conquer algorithm Insertion Sort to sort unsorted array.
    for i in range(1, len(A)):
        key = A[i]
        j = i-1
        while j >= 0 and key < A[j] :
                A[j+1] = A[j]
                j -= 1
        A[j+1] = key

    if len(A) % 2 != 0:
        return float(A[len(A) / 2])
    return float((A[int((len(A) - 1) / 2)] + A[int(len(A) / 2)]) / 2.0)

#################################################################################
#                          QUESTION    4     END                                #
#################################################################################

#-------------------------------------------------------------------------------#

#################################################################################
#                          QUESTION    5     BEGIN                              #
#################################################################################

def question5(A):
    B = []
    optimalCondition = (max(A) + min(A))*len(A)/4

    # Sorting just to see the result beauty. Actually not necessary.
    A.sort()

    exhaustiveSearch(A[::-1], 0, [], optimalCondition, B)
    return B[0]

def arrayMultiply(arr):
    m = 1
    for e in arr:
        m = m*e
    return m

def exhaustiveSearch(arr, index, subarr, optimalCondition, result):

    if index == len(arr):
        if sum(subarr) >= optimalCondition:
            if len(result) == 0:
                result.append(subarr)
            else:
                if arrayMultiply(subarr) < arrayMultiply(result[0]):
                    result[0] = subarr
    else:
        exhaustiveSearch(arr, index + 1, subarr, optimalCondition, result)
        exhaustiveSearch(arr, index + 1,subarr+[arr[index]], optimalCondition, result)

#################################################################################
#                          QUESTION    5     END                                #
#################################################################################


#-------------------------------------------------------------------------------#


#-----------------------          TESTS         --------------------------------#

#----------------------        QUESTION 1        --------------------------------#

def test1():
    BOXES_2N = ['BLACK', 'BLACK', 'BLACK', 'BLACK', 'WHITE', 'WHITE', 'WHITE', 'WHITE']

    print('Question 1\n')
    print('Original 2n boxes\t: ' + str(BOXES_2N))
    print('After operation \t: ' + str(question1(BOXES_2N)))
    print('\n')

#----------------------        QUESTION 2        --------------------------------#

def test2():
    print('Question 2\n')

    coins = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    randomIndexForFakeCoin = random.randint(0, 9)
    coins[randomIndexForFakeCoin] = 0
    print('Index of random fake coin is\t: ' + str(randomIndexForFakeCoin))
    print('Coins with fake coin is\t\t: ' + str(coins))
    fakeCoinPosition = findFakeCoin(coins, 0, len(coins), len(coins))
    print('Index of found fake coin is\t: ' + str(fakeCoinPosition))

    if fakeCoinPosition == randomIndexForFakeCoin:
        print('Fake coin found in correct index!')
    else:
        print('Fake coin not found!')

    print('\n')


#----------------------        QUESTION 3        --------------------------------#

def test3():
    print('Question 3\n')

    swapSizeOfQuickSort = [0]
    arrayQuickSort = [10, 7, 8, 9, 1, 5]
    print ('Unsorted array before Quick Sort is\t: ' + str(arrayQuickSort))
    quickSort(arrayQuickSort, 0, len(arrayQuickSort)-1, swapSizeOfQuickSort)

    print ('Quick Sorted array is\t\t\t: ' + str(arrayQuickSort))
    print('Swap Size of Quick Sort is\t\t: ' + str(swapSizeOfQuickSort[0]))
    print()

    swapSizeOfInsertionSort = [0]
    arrayInsertionSort = [10, 7, 8, 9, 1, 5]
    print ('Unsorted array before Insertion Sort is\t: ' + str(arrayInsertionSort))
    insertionSort(arrayInsertionSort, swapSizeOfInsertionSort)

    print ('Insertion Sorted array is\t\t: ' + str(arrayInsertionSort))
    print('Swap Size of Insertion Sort is\t\t: ' + str(swapSizeOfInsertionSort[0]))
    print()

    if swapSizeOfInsertionSort[0] > swapSizeOfQuickSort[0]:
        print('Quick Sort swaps lesser than Insertion Sort!\n')
    elif swapSizeOfInsertionSort[0] < swapSizeOfQuickSort[0]:
        print('Insertion Sort swaps lesser than Quick Sort!\n')
    else:
        print('Insertion Sort swaps equal to Quick Sort!\n')

    print()


#----------------------        QUESTION 4        --------------------------------#

def test4():
    print('Question 4\n')

    A = [1, 3, 4, 2, 7, 5, 8, 6]

    print('Array is\t\t: ' + str(A))
    print('Median of array is\t: ' + str(question4(A)))

    print('\n')


#----------------------        QUESTION 5        --------------------------------#

def test5():
    print('Question 5\n')

    A = [2, 4, 7, 5, 22, 11]
    print('Array is\t\t: ' + str(A))
    print('Optimal Condition is\t: ' + str((max(A) + min(A))*len(A)/4))
    print('Optimal Sub-Array is\t: ' + str(question5(A)))

    print()


##################################################################################

def testAll():
    test1()
    test2()
    test3()
    test4()
    test5()


testAll()

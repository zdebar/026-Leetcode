from typing import List

################ Interview Questions #############
#Question1
def foo(array: List[int]) -> None:
    sum: int = 0
    product: int = 1
    for i in array:
        sum += i
    for i in array:
        product *= i
    print("Sum = "+str(sum)+", Product = "+str(product))

ar1 = [1,2,3,4]
foo(ar1)

#Question2

def printPairs(array: List[int]) -> None:
    for i in array:
        for j in array:
            print(str(i)+","+str(j))


#Question3
def printUnorderedPairs(array: List[int]) -> None:
    for i in range(0, len(array)):
        for j in range(i+1, len(array)):
            print(str(array[i]) + "," + str(array[j]))





#Question4
def printUnorderedPairs2(arrayA: List[int], arrayB: List[int]) -> None:
    for i in range(len(arrayA)):
        for j in range(len(arrayB)):
            if arrayA[i] < arrayB[j]:
                print(str(arrayA[i]) + "," + str(arrayB[j]))

arrayA = [1,2,3,4,5]
arrayB = [2,6,7,8]



#Question5
def printUnorderedPairs3(arrayA: List[int], arrayB: List[int]) -> None:
    for i in range(len(arrayA)):
        for j in range(len(arrayB)):
            for _ in range(0,100000):
                print(str(arrayA[i]) + "," + str(arrayB[j]))

# printUnorderedPairss(arrayA,arrayB)


#Question6
def reverse(array: List[int]) -> None:
    for i in range(0, int(len(array)/2)):
        other: int = len(array) - i - 1
        temp: int = array[i]
        array[i] = array[other]
        array[other] = temp
    print(array)

reverse(arrayA)


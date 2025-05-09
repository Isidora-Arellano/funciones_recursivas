
def addRecursive(array):
    if not array:
        return 0
    else:
        return array[0] + addRecursive(array[1:])

def countTotalNumber(array):
    if not array:
        return 0
    else:
        return 1 + countTotalNumber(array[1:])

def multiNumber(array):
    if not array:
        return 1
    else:
        return array[0]* multiNumber(array[1:])

numbers = [1,2,3,4,5]
result = addRecursive(numbers)
print("Resultado 1: ",result)

numbers3 = [1,2,3,4,3,5]
result3 = multiNumber(numbers3)
print("Resultado 2 :",result3)

numbers2 = [1,2,3,4,5,4,7,1,9,2,3]
result2 = countTotalNumber(numbers2)
print("Resultado",result2)



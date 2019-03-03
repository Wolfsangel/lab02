
def find_reverse(numbers):
    newList = numbers.copy()
    newList.reverse()
    return newList


def find_max(numbers):
    highest = 0
    highest = max(numbers)
    return highest


def find_min(numbers):
    lowest = 0
    lowest = min(numbers)
    return lowest


def find_sum(numbers):
    sum = 0
    for x in numbers:
        sum += x
    return sum


def find_average(numbers):
    sum = 0
    i = 0
    for x in numbers:
        sum += x
        i += 1
    average = sum / i
    return average



def find_descending(numbers):
    toSort = numbers.copy()
    toSort.sort(reverse = True)
    return toSort


def second_smallest(numbers):
    num = 0
    newList = numbers.copy()
    newSet = set(newList)
    newList2 = list(newSet)
    newList2.sort()
    num = newList2[1]
    return num

def kth_smallest(numbers, k):
    num = 0
    newList = numbers.copy()
    newSet = set(newList)
    newList2 = list(newSet)
    newList2.sort()
    num = newList2[k - 1]
    return num


if __name__ == '__main__':
    # If you are testing, place your print statements here
    pass

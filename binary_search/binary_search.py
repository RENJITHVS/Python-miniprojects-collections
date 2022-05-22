import random
import time

def naive_search(l, target):
    for i in range(len(l)):
        if l[i]== target:
            return i

    return -1

def binary_search(l, target, high=None, low=None):
    if low is None:
        low = 0
    if high is None:
        high = len(l)-1

    if high < low:
        return -1

    midpoint = (high + low)//2


    if l[midpoint] == target:
        return f"your target position is {midpoint}"
    elif l[midpoint] < target:
        return binary_search(l, target, high, midpoint+1)
    else:
        return binary_search(l, target, midpoint-1, low )

if __name__ == '__main__':
    # l = [2,5,6,7,12,24,55,67]
    # target = 67
    # print(binary_search(l, target))
    # print(naive_search(l, target))

    length = 10000
    sorted_list = set()
    while len(sorted_list) < length:
        sorted_list.add(random.randint(-3*length, 4*length))
    sorted_list = sorted(list(sorted_list))

    start = time.time()
    for target in sorted_list:
        naive_search(sorted_list, target)
    end = time.time()
    print("Naive search time:", (end-start)/length, 'seconds')
    
    start = time.time()
    for target in sorted_list:
        binary_search(sorted_list, target)
    end = time.time()
    print("Binary search time:", (end-start)/length, 'seconds')
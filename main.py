# Udemy Projects
import random
def in_order(numbers):
    for i in range(len(numbers)-1):
        if numbers[i] > numbers[i+1]:
            return False
    return True

def bogo_sort(numbers):
    while not in_order(numbers):
        random.shuffle(numbers)
    print(numbers)

if __name__ == '__main__':
    print(bogo_sort([1,5,3,2,6]))

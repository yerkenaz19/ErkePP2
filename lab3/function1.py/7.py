def has_33(numbers):
    for i in range(len(numbers)-1):#Это делается потому, что мы сравниваем два соседних элемента
        if(numbers[i]==numbers[i+1]==3):
            return True
    return False
print(has_33([1, 3, 3]))
print(has_33([1, 3, 1, 3]))
print(has_33([3, 1, 3]))
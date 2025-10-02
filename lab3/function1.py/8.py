def spy_game(nums):
    arr = [7, 0, 0]
    for x in nums:
        if arr[-1] == x:# Если текущий элемент списка nums совпадает с последним в arr
            arr.pop()# Удаляем его из arr
        if len(arr) == 0:
            return True
    return False
print(spy_game([1,2,4,0,0,7,5]))
print(spy_game([1,0,2,4,0,5,7]))
print(spy_game([1,7,2,0,4,5,0]))
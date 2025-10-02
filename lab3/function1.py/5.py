from itertools import permutations
def get_permutations():
    string=input()
    perm=permutations(string)
    for x in perm:
        print(''.join(x))
get_permutations()
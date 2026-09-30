from typing import List

def read_integers() -> List[int]:
    numlist = []
    for elem in input().split(","):
        numlist.append(int(elem))
    return numlist


# do not modify the code below
print(read_integers())
print(read_integers())
print(read_integers())

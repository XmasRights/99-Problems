#Solutions to https://sites.google.com/site/prologsite/prolog-problems/1

# 1.01
def getLast(list):
    return list[-1]

# 1.02
def getPenultimate(list):
    return list[2]

# 1.03
def getElementAtIndex(list, index):
    return list[index]

# 1.04
def count(list):
    return len(list)

# 1.05
def reverse(list):
    list.reverse()
    return list

# 1.06
def isPalindrome(list):
    rev = list[:]
    reverse(rev)
    return list == rev

# 1.07
def flatten(nestedList):
    return list(flattenRecursion(nestedList))

def flattenRecursion(container):
    for i in container:
        if isinstance(i, list) or isinstance(i, tuple):
            for j in flattenRecursion(i):
                yield j
        else:
            yield i

# 1.08
def removeConsecutiveDuplicates(list):
    if len(list) <= 0:
        return list

    out = [list[0]]
    for x in list[1:]:
        if x != out[-1]:
            out.append(x)
    return out

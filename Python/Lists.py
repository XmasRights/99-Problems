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

#1.06
def isPalindrome(list):
    rev = list[:]
    reverse(rev)
    return list == rev

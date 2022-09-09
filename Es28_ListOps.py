def append(list1, list2):
    return list1 + list2
def concat(lists):
    list1 = []
    for elem in lists:
        list1 = append(list1,elem)
    return list1
        
def filter(function, list):
    return [elemento for elemento in list if function(elemento)]
def length(list):
    lung = 0
    for elem in list:
        lung += 1
    return lung
def map(function, list):
    return [function(elem) for elem in list]
def foldl(function, list, initial):
    for elem in list:
        initial = function (initial, elem)
    return initial
def foldr(function, list, initial):
    for elem in list[::-1]:
        initial = function(elem, initial)
    return initial
def reverse(list):
    return list[::-1]
def removeDuplicates(tab):
    return list(dict.fromkeys(tab))

tab=[2, 2, 2, 3, 4, 5, 6, 1, 8, 8, 8, 4, 1, 2, 5, 9, 0, 4]
print(tab)
tab=removeDuplicates(tab)
print(tab)
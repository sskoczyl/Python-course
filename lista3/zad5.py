def allSets(tab):
    if len(tab) == 0:
        return [[]]
    first, rest = tab[0], tab[1:]
    return allSets(rest) + list(map(lambda set: [first, *set], allSets(rest)))


tab=[4, 2, 0]
print(allSets(tab))
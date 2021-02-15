tab = [[13,12,115],[32,10,42],[1,19,63]]
for r in tab :
    print(r)

transpozition = [[tab[j][i] for j in range(len(tab))] for i in range(len(tab[0]))]

print("\n")
for r in transpozition:
    print(r)

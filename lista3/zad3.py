def sum_up(path):
    file=open(path,"r")
    tab=[int(line.split(" ")[-1]) for line in file.readlines()]
    return sum(tab)

print(sum_up("./plik.txt"))


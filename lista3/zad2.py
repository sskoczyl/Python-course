def flatten(lst):
    kinds=(list, tuple)
    if isinstance(lst, kinds):
        for x in lst:
            for y in flatten(x):
                yield y
    else:
        yield lst

lst = [[1, 2, ["a", 4, "b", 5, 5, 5]], [4, 5, 6 ], 7, [[9, [123, [[123]]]], 10]]
print(list(flatten(lst)))
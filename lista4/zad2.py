import random


def dfs_walk(node):
    if len(node) > 0:
        yield from check_if_null(node, 1)
        yield check_if_null(node, 0)
        yield from check_if_null(node, 2)
    else:
        pass


def check_if_null(node, i):
    if i != 0:
        return dfs_walk(node[i]) if node[i] is not None else ()
    else:
        return node[i] if node[i] is not None else ()


def bfs_walk(node):
    nodes = [node]
    for subnode in nodes:
        yield subnode[0] if subnode[0] is not None else ()
        nodes.append(subnode[1]) if subnode[1] is not None else ()
        nodes.append(subnode[2]) if subnode[2] is not None else ()


def generator(random_list, quantity):
    return list((random_list[quantity], generator(random_list, 2 * quantity + 1),
                 generator(random_list, 2 * quantity + 2))) if quantity < len(
        random_list) else None


def cnt_nodes(tree_depth):
    nodes_cnt = 0

    for i in range(0, tree_depth + 1):
        nodes_cnt += 2 ** i

    return nodes_cnt


def create_list(max_nodes):
    return random.sample(range(1, max_nodes + 1), max_nodes)


def new_tree(tree_depth):
    random_list = create_list(cnt_nodes(tree_depth))
    return generator(random_list, 0)


print("Podaj wysokosc drzewa: ")
depth = int(input())
tree = new_tree(depth)
print(tree)
print(list(dfs_walk(tree)))
print(list(bfs_walk(tree)))

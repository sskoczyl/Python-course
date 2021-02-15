import random


class Node:
    def __init__(self, value):
        self.value = value
        self.nodes = []

    def get_all_nodes(self):
        return self.nodes

    def add_node(self, child):
        self.nodes.append(child)


def dfs_walk(node):
    if node is not None:
        amount = len(node.get_all_nodes())

        if amount > 0:
            for i in range(0, int(amount / 2 + 1)):
                yield from dfs_walk(node.get_all_nodes()[i])

        yield node.number

        if amount > 0:
            for i in range(int(amount / 2 + 1), amount):
                yield from dfs_walk(node.get_all_nodes()[i])

    else:
        pass


def bfs_walk(node):
    if node is not None:
        nodes = [node]
        for q in nodes:
            if q is not None:
                yield q.number
                for i in q.get_all_nodes():
                    nodes.append(i) if len(q.get_all_nodes()) > 0 else ()
    else:
        pass


def cnt_nodes(tree_depth):
    nodes_cnt = 0

    for i in range(0, tree_depth + 1):
        nodes_cnt += 2 ** i

    return nodes_cnt


def create_list(max_nodes):
    return random.sample(range(1, max_nodes + 1), max_nodes)


def generator(tree_depth, random_list, max_children):
    node = get_new_node(random.choice(random_list))
    how_may_children = random.randrange(0, max_children)

    if tree_depth >= 0:
        for i in range(0, how_may_children):
            node.add_node(generator(tree_depth - 1, random_list, max_children))

        return node
    else:
        pass


def tree_gen(tree_depth, max_children):
    random_list = create_list(1000)

    return generator(tree_depth, random_list, max_children)


def get_new_node(value):
    return Node(value)


print("Podaj wysokosc drzewa: ")
depth = int(input())
"""
tree = Node(1)
n1 = Node(2)
n2 = Node(4)
n3 = Node(5)
tree.insert_child(n1)
tree.insert_child(n2)
tree.insert_child(n3)
n31=Node(10)
n3.insert_child(Node(12))
n2.insert_child(Node(24))
n3.insert_child(n31)
n31.insert_child(Node(123))
n31.insert_child(Node(124))
n31.insert_child(Node(125))
"""

tree = tree_gen(depth, 5)

print(list(dfs_walk(tree)))
print(list(bfs_walk(tree)))

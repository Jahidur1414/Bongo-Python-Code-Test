class Node:
    def __init__(self, value, parent):
        self.value = value
        self.parent = parent


def lca(node1, node2):
    """
    Worst case time complexity: O(n^2).
    Best case time complexity: Ω(1)

    Space complexity: O(n)
    """
    if node1.value == node2.value:
        print(node1.value)
        return

    node1_values = [node1.value]
    node2_values = [node2.value]

    while True:
        if node1.parent:
            node1 = node1.parent
            if node1.value in node2_values:
                print(node1.value)
                return
            node1_values.append(node1.value)

        if node2.parent:
            node2 = node2.parent
            if node2.value in node1_values:
                print(node2.value)
                return
            node2_values.append(node2.value)

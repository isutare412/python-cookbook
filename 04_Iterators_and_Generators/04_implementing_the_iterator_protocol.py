class Node:
    def __init__(self, value):
        self._value = value
        self._children = []

    def __repr__(self):
        return 'Node({!r})'.format(self._value)

    def __iter__(self):
        return iter(self._children)

    def add_child(self, node):
        self._children.append(node)

    def depth_first(self):
        yield self
        for c in self:
            yield from c.depth_first()


class NodeWithoutGenerator(Node):
    def depth_first(self):
        class DepthFirstIterator:
            '''Depth-first traversal'''
            def __init__(self, start_node):
                self._node = start_node
                self._children_iter = None
                self._child_iter = None

            def __iter__(self):
                return self

            def __next__(self):
                if self._children_iter is None:
                    self._children_iter = iter(self._node)
                    return self._node

                elif self._child_iter is not None:
                    try:
                        nextchild = next(self._child_iter)
                        return nextchild
                    except StopIteration:
                        self._child_iter = None
                        return next(self)

                else:
                    self._child_iter = next(self._children_iter).depth_first()
                    return next(self)

        return DepthFirstIterator(self)


if __name__ == '__main__':
    root = Node(0)
    child1 = Node(1)
    child2 = Node(2)
    root.add_child(child1)
    root.add_child(child2)
    child1.add_child(Node(3))
    child1.add_child(Node(4))
    child2.add_child(Node(5))

    for ch in root.depth_first():
        print(ch)
    print()

    root = NodeWithoutGenerator(0)
    child1 = NodeWithoutGenerator(1)
    child2 = NodeWithoutGenerator(2)
    root.add_child(child1)
    root.add_child(child2)
    child1.add_child(NodeWithoutGenerator(3))
    child1.add_child(NodeWithoutGenerator(4))
    child2.add_child(NodeWithoutGenerator(5))

    for ch in root.depth_first():
        print(ch)

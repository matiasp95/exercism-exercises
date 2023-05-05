import unittest
class Record:
    def __init__(self, record_id, parent_id):
        self.record_id = record_id
        self.parent_id = parent_id


class Node:
    def __init__(self, node_id):
        self.node_id = node_id
        self.children = []


def BuildTree(records):
    root = None
    records.sort(key=lambda x: x.record_id)
    ordered_id = [i.record_id for i in records]
    if records:
        if ordered_id[-1] != len(ordered_id) - 1:
            raise ValueError('Record id is invalid or out of order.')
        if ordered_id[0] != 0:
            raise ValueError('invalid')
    trees = []
    parent = {}
    for i in range(len(ordered_id)):
        for j in records:
            if ordered_id[i] == j.record_id:
                if j.record_id == 0:
                    if j.parent_id != 0:
                        raise ValueError("Node parent_id should be smaller than it's record_id.")
                if j.record_id < j.parent_id:
                    raise ValueError("Node parent_id should be smaller than it's record_id.")
                if j.record_id == j.parent_id:
                    if j.record_id != 0:
                        raise ValueError('Only root should have equal record and parent id.')
                trees.append(Node(ordered_id[i]))
    for i in range(len(ordered_id)):
        for j in trees:
            if i == j.node_id:
                parent = j
        for j in records:
            if j.parent_id == i:
                for k in trees:
                    if k.node_id == 0:
                        continue
                    if j.record_id == k.node_id:
                        child = k
                        parent.children.append(child)
    if len(trees) > 0:
        root = trees[0]
    return root


class TreeBuildingTest(unittest.TestCase):
    """
        Record(record_id, parent_id): records given to be processed
        Node(node_id): Node in tree
        BuildTree(records): records as argument and returns tree
        BuildTree should raise ValueError if given records are invalid
    """
    def test_empty_list_input(self):
        records = []
        root = BuildTree(records)
        self.assertIsNone(root)
    def test_one_node(self):
        records = [
            Record(0, 0)
        ]
        root = BuildTree(records)
        self.assert_node_is_leaf(root, node_id=0)
    def test_three_nodes_in_order(self):
        records = [
            Record(0, 0),
            Record(1, 0),
            Record(2, 0)
        ]
        root = BuildTree(records)
        self.assert_node_is_branch(root, node_id=0, children_count=2)
        self.assert_node_is_leaf(root.children[0], node_id=1)
        self.assert_node_is_leaf(root.children[1], node_id=2)
    def test_three_nodes_in_reverse_order(self):
        records = [
            Record(2, 0),
            Record(1, 0),
            Record(0, 0)
        ]
        root = BuildTree(records)
        self.assert_node_is_branch(root, node_id=0, children_count=2)
        self.assert_node_is_leaf(root.children[0], node_id=1)
        self.assert_node_is_leaf(root.children[1], node_id=2)
    def test_more_than_two_children(self):
        records = [
            Record(0, 0),
            Record(1, 0),
            Record(2, 0),
            Record(3, 0)
        ]
        root = BuildTree(records)
        self.assert_node_is_branch(root, node_id=0, children_count=3)
        self.assert_node_is_leaf(root.children[0], node_id=1)
        self.assert_node_is_leaf(root.children[1], node_id=2)
        self.assert_node_is_leaf(root.children[2], node_id=3)
    def test_binary_tree(self):
        records = [
            Record(6, 2),
            Record(0, 0),
            Record(3, 1),
            Record(2, 0),
            Record(4, 1),
            Record(5, 2),
            Record(1, 0)
        ]
        root = BuildTree(records)
        self.assert_node_is_branch(root, 0, 2)
        self.assert_node_is_branch(root.children[0], 1, 2)
        self.assert_node_is_branch(root.children[1], 2, 2)
        self.assert_node_is_leaf(root.children[0].children[0], 3)
        self.assert_node_is_leaf(root.children[0].children[1], 4)
        self.assert_node_is_leaf(root.children[1].children[0], 5)
        self.assert_node_is_leaf(root.children[1].children[1], 6)
    def test_unbalanced_tree(self):
        records = [
            Record(0, 0),
            Record(1, 0),
            Record(2, 0),
            Record(3, 1),
            Record(4, 1),
            Record(5, 1),
            Record(6, 2),
        ]
        root = BuildTree(records)
        self.assert_node_is_branch(root, 0, 2)
        self.assert_node_is_branch(root.children[0], 1, 3)
        self.assert_node_is_branch(root.children[1], 2, 1)
        self.assert_node_is_leaf(root.children[0].children[0], 3)
        self.assert_node_is_leaf(root.children[0].children[1], 4)
        self.assert_node_is_leaf(root.children[0].children[2], 5)
        self.assert_node_is_leaf(root.children[1].children[0], 6)
    def test_root_node_has_parent(self):
        records = [
            Record(0, 1),
            Record(1, 0)
        ]
        # Root parent_id should be equal to record_id(0)
        with self.assertRaises(ValueError) as err:
            BuildTree(records)
        self.assertEqual(type(err.exception), ValueError)
        self.assertEqual(err.exception.args[0], "Node parent_id should be smaller than it's record_id.")
    def test_no_root_node(self):
        records = [
            Record(1, 0),
            Record(2, 0)
        ]
        # Record with record_id 0 (root) is missing
        with self.assertRaises(ValueError) as err:
            BuildTree(records)
        self.assertEqual(type(err.exception), ValueError)
        self.assertEqual(err.exception.args[0], "Record id is invalid or out of order.")
    def test_non_continuous(self):
        records = [
            Record(2, 0),
            Record(4, 2),
            Record(1, 0),
            Record(0, 0)
        ]
        # Record with record_id 3 is missing
        with self.assertRaises(ValueError) as err:
            BuildTree(records)
        self.assertEqual(type(err.exception), ValueError)
        self.assertEqual(err.exception.args[0], "Record id is invalid or out of order.")
    def test_cycle_directly(self):
        records = [
            Record(5, 2),
            Record(3, 2),
            Record(2, 2),
            Record(4, 1),
            Record(1, 0),
            Record(0, 0),
            Record(6, 3)
        ]
        # Cycle caused by Record 2 with parent_id pointing to itself
        with self.assertRaises(ValueError) as err:
            BuildTree(records)
        self.assertEqual(type(err.exception), ValueError)
        self.assertEqual(err.exception.args[0], "Only root should have equal record and parent id.")
    def test_cycle_indirectly(self):
        records = [
            Record(5, 2),
            Record(3, 2),
            Record(2, 6),
            Record(4, 1),
            Record(1, 0),
            Record(0, 0),
            Record(6, 3)
        ]
        # Cycle caused by Record 2 with parent_id(6) greater than record_id(2)
        with self.assertRaises(ValueError) as err:
            BuildTree(records)
        self.assertEqual(type(err.exception), ValueError)
        self.assertEqual(err.exception.args[0], "Node parent_id should be smaller than it's record_id.")
    def test_higher_id_parent_of_lower_id(self):
        records = [
            Record(0, 0),
            Record(2, 0),
            Record(1, 2)
        ]
        # Record 1 have parent_id(2) greater than record_id(1)
        with self.assertRaises(ValueError) as err:
            BuildTree(records)
        self.assertEqual(type(err.exception), ValueError)
        self.assertEqual(err.exception.args[0], "Node parent_id should be smaller than it's record_id.")
    def assert_node_is_branch(self, node, node_id, children_count):
        self.assertEqual(node.node_id, node_id)
        self.assertNotEqual(len(node.children), 0)
        self.assertEqual(len(node.children), children_count)
    def assert_node_is_leaf(self, node, node_id):
        self.assertEqual(node.node_id, node_id)
        self.assertEqual(len(node.children), 0)
    def run_tests(self):
        unittest.main()
TreeBuildingTest().test_unbalanced_tree()
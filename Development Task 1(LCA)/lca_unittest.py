import unittest
from lca import *

class TestLCA(unittest.TestCase):

    def setUp(self):
        pass

    def test_null_graph(self):
        self.assertEqual(-1, findLCA(root, 4, 5)) 
        self.assertEqual(-1, findLCA(root, 2, 7))   

    def test_finding_lca_itself(self):
        root = Node(1)
        self.assertEqual(1, findLCA(root, 1, 1))

    def test_find_lca(self):
        root = Node(1)
        root.left = Node(2)
        root.right = Node(3)
        root.left.left = Node(4)
        root.left.right = Node(5)
        root.right.left = Node(6)
        root.right.right = Node(7)
        self.assertEqual(2, findLCA(root, 4, 5))
        self.assertEqual(1, findLCA(root, 4, 6))
        self.assertEqual(1, findLCA(root, 3, 4))
        self.assertEqual(2, findLCA(root, 2, 4))
        self.assertNotEqual(7, findLCA(root, 3, 4))
        self.assertNotEqual(5, findLCA(root, 2, 4))

    

if __name__ == '__main__':
    unittest.main()
#!/usr/bin/env python3
"""
Comprehensive Test file for maximumvalueinbinarytree.py
Tests the maximum value finding functionality with 30+ test cases
"""
import sys
import os
import unittest

# Add the parent directory to Python path to import Trees package
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)

from Trees.node import Node
from Trees.maximumvalueinbinarytree import max_value_in_binary_tree


class TestMaxValueInBinaryTree(unittest.TestCase):
    """Comprehensive test class for finding maximum value in binary tree"""
    
    # ==================== EDGE CASES ====================
    
    def test_01_empty_tree(self):
        """Test 1: Empty tree (None root) should return -infinity"""
        result = max_value_in_binary_tree(None)
        self.assertEqual(result, float('-inf'), "Empty tree should return negative infinity")
    
    def test_02_single_node_positive(self):
        """Test 2: Single node tree with positive value"""
        root = Node(42)
        result = max_value_in_binary_tree(root)
        self.assertEqual(result, 42, "Single node should return its value")
    
    def test_03_single_node_negative(self):
        """Test 3: Single node tree with negative value"""
        root = Node(-100)
        result = max_value_in_binary_tree(root)
        self.assertEqual(result, -100, "Single negative node should return its value")
    
    def test_04_single_node_zero(self):
        """Test 4: Single node tree with zero value"""
        root = Node(0)
        result = max_value_in_binary_tree(root)
        self.assertEqual(result, 0, "Zero node should return 0")
    
    # ==================== BASIC CASES ====================
    
    def test_05_two_nodes_left_child_greater(self):
        """Test 5: Two nodes with left child greater than root"""
        root = Node(1)
        root.left = Node(10)
        result = max_value_in_binary_tree(root)
        self.assertEqual(result, 10, "Should return left child's value if it's greater")
    
    def test_06_two_nodes_right_child_greater(self):
        """Test 6: Two nodes with right child greater than root"""
        root = Node(1)
        root.right = Node(10)
        result = max_value_in_binary_tree(root)
        self.assertEqual(result, 10, "Should return right child's value if it's greater")
    
    def test_07_two_nodes_root_greater(self):
        """Test 7: Two nodes with root greater than children"""
        root = Node(10)
        root.left = Node(1)
        root.right = Node(5)
        result = max_value_in_binary_tree(root)
        self.assertEqual(result, 10, "Should return root's value if it's the maximum")
    
    def test_08_three_nodes_perfect_tree(self):
        """Test 8: Perfect binary tree with 3 nodes"""
        root = Node(1)
        root.left = Node(2)
        root.right = Node(3)
        result = max_value_in_binary_tree(root)
        self.assertEqual(result, 3, "Should return the maximum value (3)")
    
    def test_09_three_nodes_max_at_root(self):
        """Test 9: Perfect tree with maximum at root"""
        root = Node(10)
        root.left = Node(5)
        root.right = Node(3)
        result = max_value_in_binary_tree(root)
        self.assertEqual(result, 10, "Should return root value as maximum")
    
    def test_10_three_nodes_max_at_left(self):
        """Test 10: Perfect tree with maximum at left child"""
        root = Node(5)
        root.left = Node(10)
        root.right = Node(3)
        result = max_value_in_binary_tree(root)
        self.assertEqual(result, 10, "Should return left child's value as maximum")
    
    # ==================== MEDIUM COMPLEXITY ====================
    
    def test_11_four_nodes_left_skewed(self):
        """Test 11: Left skewed tree with 4 nodes"""
        root = Node(1)
        root.left = Node(2)
        root.left.left = Node(3)
        root.left.left.left = Node(4)
        result = max_value_in_binary_tree(root)
        self.assertEqual(result, 4, "Should return deepest left node's value")
    
    def test_12_four_nodes_right_skewed(self):
        """Test 12: Right skewed tree with 4 nodes"""
        root = Node(1)
        root.right = Node(2)
        root.right.right = Node(3)
        root.right.right.right = Node(4)
        result = max_value_in_binary_tree(root)
        self.assertEqual(result, 4, "Should return deepest right node's value")
    
    def test_13_five_nodes_complete_tree(self):
        """Test 13: Complete binary tree with 5 nodes"""
        root = Node(1)
        root.left = Node(2)
        root.right = Node(3)
        root.left.left = Node(4)
        root.left.right = Node(5)
        result = max_value_in_binary_tree(root)
        self.assertEqual(result, 5, "Should return 5 as maximum")
    
    def test_14_seven_nodes_perfect_tree(self):
        """Test 14: Perfect binary tree with 7 nodes"""
        root = Node(1)
        root.left = Node(2)
        root.right = Node(3)
        root.left.left = Node(4)
        root.left.right = Node(5)
        root.right.left = Node(6)
        root.right.right = Node(7)
        result = max_value_in_binary_tree(root)
        self.assertEqual(result, 7, "Should return 7 as maximum")
    
    def test_15_unbalanced_tree_left_heavy(self):
        """Test 15: Unbalanced tree with larger values on left"""
        root = Node(5)
        root.left = Node(10)
        root.right = Node(3)
        root.left.left = Node(15)
        root.left.right = Node(8)
        result = max_value_in_binary_tree(root)
        self.assertEqual(result, 15, "Should return 15 from left subtree")
    
    def test_16_unbalanced_tree_right_heavy(self):
        """Test 16: Unbalanced tree with larger values on right"""
        root = Node(5)
        root.left = Node(2)
        root.right = Node(10)
        root.right.left = Node(8)
        root.right.right = Node(15)
        result = max_value_in_binary_tree(root)
        self.assertEqual(result, 15, "Should return 15 from right subtree")
    
    def test_17_tree_with_none_children(self):
        """Test 17: Tree with some missing children"""
        root = Node(1)
        root.left = Node(2)
        root.right = Node(3)
        root.left.left = Node(4)
        # root.left.right is None
        root.right.right = Node(7)
        result = max_value_in_binary_tree(root)
        self.assertEqual(result, 7, "Should return 7 as maximum")
    
    def test_18_full_binary_tree(self):
        """Test 18: Full binary tree (every node has 0 or 2 children)"""
        root = Node(10)
        root.left = Node(5)
        root.right = Node(15)
        root.left.left = Node(3)
        root.left.right = Node(7)
        root.right.left = Node(12)
        root.right.right = Node(20)
        result = max_value_in_binary_tree(root)
        self.assertEqual(result, 20, "Should return 20 as maximum")
    
    # ==================== COMPLEX CASES ====================
    
    def test_19_deep_left_skewed(self):
        """Test 19: Deep left skewed tree (10 nodes)"""
        root = Node(1)
        current = root
        for i in range(2, 11):
            current.left = Node(i)
            current = current.left
        result = max_value_in_binary_tree(root)
        self.assertEqual(result, 10, "Should return deepest value (10)")
    
    def test_20_deep_right_skewed(self):
        """Test 20: Deep right skewed tree (10 nodes)"""
        root = Node(1)
        current = root
        for i in range(2, 11):
            current.right = Node(i)
            current = current.right
        result = max_value_in_binary_tree(root)
        self.assertEqual(result, 10, "Should return deepest value (10)")
    
    def test_21_large_complete_tree(self):
        """Test 21: Complete binary tree with 15 nodes (4 levels)"""
        root = Node(1)
        root.left = Node(2)
        root.right = Node(3)
        root.left.left = Node(4)
        root.left.right = Node(5)
        root.right.left = Node(6)
        root.right.right = Node(7)
        root.left.left.left = Node(8)
        root.left.left.right = Node(9)
        root.left.right.left = Node(10)
        root.left.right.right = Node(11)
        root.right.left.left = Node(12)
        root.right.left.right = Node(13)
        root.right.right.left = Node(14)
        root.right.right.right = Node(15)
        result = max_value_in_binary_tree(root)
        self.assertEqual(result, 15, "Should return 15 as maximum")
    
    def test_22_alternating_structure(self):
        """Test 22: Tree with alternating left/right children"""
        root = Node(1)
        root.left = Node(3)
        root.left.left = Node(5)
        root.left.left.left = Node(7)
        result = max_value_in_binary_tree(root)
        self.assertEqual(result, 7, "Should return 7 as maximum")
    
    def test_23_perfect_tree_height_4(self):
        """Test 23: Perfect binary tree with 15 nodes (height 4)"""
        root = Node(1)
        root.left = Node(2)
        root.right = Node(3)
        root.left.left = Node(4)
        root.left.right = Node(5)
        root.right.left = Node(6)
        root.right.right = Node(7)
        root.left.left.left = Node(8)
        root.left.left.right = Node(9)
        root.left.right.left = Node(10)
        root.left.right.right = Node(11)
        root.right.left.left = Node(12)
        root.right.left.right = Node(13)
        root.right.right.left = Node(14)
        root.right.right.right = Node(15)
        result = max_value_in_binary_tree(root)
        self.assertEqual(result, 15, "Should return 15 as maximum")
    
    def test_24_tree_with_missing_branches(self):
        """Test 24: Complex tree with various missing children"""
        root = Node(1)
        root.left = Node(2)
        root.right = Node(3)
        root.left.left = Node(4)
        root.left.right = Node(5)
        root.right.right = Node(7)
        root.left.left.left = Node(8)
        root.left.left.left.left = Node(11)
        result = max_value_in_binary_tree(root)
        self.assertEqual(result, 11, "Should return 11 as maximum")
    
    def test_25_asymmetric_tree(self):
        """Test 25: Highly asymmetric tree"""
        root = Node(1)
        root.left = Node(2)
        root.left.left = Node(3)
        root.left.left.left = Node(4)
        root.left.left.left.left = Node(5)
        result = max_value_in_binary_tree(root)
        self.assertEqual(result, 5, "Should return 5 as maximum")
    
    # ==================== VALUE RANGE TESTS ====================
    
    def test_26_all_negative_values(self):
        """Test 26: Tree with all negative values"""
        root = Node(-1)
        root.left = Node(-2)
        root.right = Node(-3)
        root.left.left = Node(-10)
        root.left.right = Node(-5)
        root.right.left = Node(-7)
        root.right.right = Node(-4)
        result = max_value_in_binary_tree(root)
        self.assertEqual(result, -1, "Should return -1 as maximum (closest to zero)")
    
    def test_27_all_zero_values(self):
        """Test 27: Tree with all zero values"""
        root = Node(0)
        root.left = Node(0)
        root.right = Node(0)
        root.left.left = Node(0)
        root.left.right = Node(0)
        root.right.left = Node(0)
        root.right.right = Node(0)
        result = max_value_in_binary_tree(root)
        self.assertEqual(result, 0, "Should return 0 for all-zero tree")
    
    def test_28_mixed_positive_negative(self):
        """Test 28: Tree with mixed positive and negative values"""
        root = Node(-5)
        root.left = Node(-10)
        root.right = Node(5)
        root.left.left = Node(-20)
        root.left.right = Node(3)
        root.right.left = Node(-3)
        root.right.right = Node(10)
        result = max_value_in_binary_tree(root)
        self.assertEqual(result, 10, "Should return 10 as maximum")
    
    def test_29_duplicate_maximum_values(self):
        """Test 29: Tree with duplicate maximum values"""
        root = Node(5)
        root.left = Node(10)
        root.right = Node(10)
        root.left.left = Node(10)
        root.left.right = Node(8)
        root.right.left = Node(7)
        root.right.right = Node(10)
        result = max_value_in_binary_tree(root)
        self.assertEqual(result, 10, "Should return 10 even with duplicates")
    
    def test_30_large_tree_31_nodes(self):
        """Test 30: Large tree with 31 nodes (5 levels)"""
        root = Node(1)
        nodes = [Node(i) for i in range(1, 32)]
        for i in range(31):
            if 2*i + 1 < 31:
                nodes[i].left = nodes[2*i + 1]
            if 2*i + 2 < 31:
                nodes[i].right = nodes[2*i + 2]
        root = nodes[0]
        result = max_value_in_binary_tree(root)
        self.assertEqual(result, 31, "Should return 31 as maximum in 31-node tree")
    
    def test_31_very_large_tree(self):
        """Test 31: Very large tree with 63 nodes (6 levels)"""
        root = Node(1)
        nodes = [Node(i) for i in range(1, 64)]
        for i in range(63):
            if 2*i + 1 < 63:
                nodes[i].left = nodes[2*i + 1]
            if 2*i + 2 < 63:
                nodes[i].right = nodes[2*i + 2]
        root = nodes[0]
        result = max_value_in_binary_tree(root)
        self.assertEqual(result, 63, "Should return 63 as maximum in 63-node tree")
    
    def test_32_maximum_at_different_depths(self):
        """Test 32: Verify maximum is found at various depths"""
        # Max at depth 0
        root = Node(100)
        root.left = Node(1)
        root.right = Node(2)
        self.assertEqual(max_value_in_binary_tree(root), 100)
        
        # Max at depth 1
        root = Node(5)
        root.left = Node(100)
        root.right = Node(2)
        self.assertEqual(max_value_in_binary_tree(root), 100)
        
        # Max at depth 2
        root = Node(5)
        root.left = Node(3)
        root.right = Node(2)
        root.left.left = Node(100)
        self.assertEqual(max_value_in_binary_tree(root), 100)
        
        # Max at depth 3
        root = Node(5)
        root.left = Node(3)
        root.right = Node(2)
        root.left.left = Node(4)
        root.left.left.left = Node(100)
        self.assertEqual(max_value_in_binary_tree(root), 100)
    
    def test_33_consecutive_values(self):
        """Test 33: Tree with consecutive integer values"""
        root = Node(1)
        root.left = Node(2)
        root.right = Node(3)
        root.left.left = Node(4)
        root.left.right = Node(5)
        root.right.left = Node(6)
        root.right.right = Node(7)
        result = max_value_in_binary_tree(root)
        self.assertEqual(result, 7, "Should return 7 as maximum")
    
    def test_34_decreasing_values(self):
        """Test 34: Tree with decreasing values from root"""
        root = Node(10)
        root.left = Node(9)
        root.right = Node(8)
        root.left.left = Node(7)
        root.left.right = Node(6)
        root.right.left = Node(5)
        root.right.right = Node(4)
        result = max_value_in_binary_tree(root)
        self.assertEqual(result, 10, "Should return 10 (root) as maximum")
    
    def test_35_random_scattered_values(self):
        """Test 35: Tree with random scattered values"""
        root = Node(50)
        root.left = Node(25)
        root.right = Node(75)
        root.left.left = Node(10)
        root.left.right = Node(60)
        root.right.left = Node(5)
        root.right.right = Node(100)
        root.left.right.left = Node(30)
        root.left.right.right = Node(70)
        root.right.right.right = Node(150)
        result = max_value_in_binary_tree(root)
        self.assertEqual(result, 150, "Should return 150 as maximum")
    
    def test_36_minimum_integer_values(self):
        """Test 36: Tree with minimum integer values"""
        root = Node(-2147483648)
        root.left = Node(-2147483648)
        root.right = Node(-2147483648)
        result = max_value_in_binary_tree(root)
        self.assertEqual(result, -2147483648, "Should handle minimum 32-bit integer")
    
    def test_37_maximum_integer_values(self):
        """Test 37: Tree with maximum integer values"""
        root = Node(2147483647)
        root.left = Node(2147483647)
        root.right = Node(2147483647)
        result = max_value_in_binary_tree(root)
        self.assertEqual(result, 2147483647, "Should handle maximum 32-bit integer")
    
    def test_38_tree_depth_1(self):
        """Test 38: Tree with only root and one child"""
        root = Node(10)
        root.left = Node(20)
        result = max_value_in_binary_tree(root)
        self.assertEqual(result, 20, "Should return 20 as maximum")
    
    def test_39_tree_with_one_missing_grandchild(self):
        """Test 39: Tree with some missing grandchildren"""
        root = Node(1)
        root.left = Node(2)
        root.right = Node(3)
        root.left.right = Node(5)
        result = max_value_in_binary_tree(root)
        self.assertEqual(result, 5, "Should return 5 as maximum")
    
    def test_40_same_depth_different_values(self):
        """Test 40: Same depth nodes with different values"""
        root = Node(1)
        root.left = Node(10)
        root.right = Node(20)
        root.left.left = Node(30)
        root.right.right = Node(40)
        result = max_value_in_binary_tree(root)
        self.assertEqual(result, 40, "Should return 40 as maximum")


def run_comprehensive_tests():
    """Run all tests and provide detailed output"""
    print("=" * 80)
    print("COMPREHENSIVE MAX VALUE IN BINARY TREE TEST SUITE")
    print("=" * 80)
    
    # Create test suite
    loader = unittest.TestLoader()
    suite = loader.loadTestsFromTestCase(TestMaxValueInBinaryTree)
    
    # Run tests with verbose output
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    print("=" * 80)
    print("TEST SUMMARY")
    print("=" * 80)
    print(f"Tests run: {result.testsRun}")
    print(f"Failures: {len(result.failures)}")
    print(f"Errors: {len(result.errors)}")
    print(f"Success rate: {((result.testsRun - len(result.failures) - len(result.errors)) / result.testsRun * 100):.1f}%")
    
    if result.failures:
        print("\nFAILURES:")
        for test, traceback in result.failures:
            print(f"- {test}: {traceback}")
    
    if result.errors:
        print("\nERRORS:")
        for test, traceback in result.errors:
            print(f"- {test}: {traceback}")
    
    print("=" * 80)
    
    if result.wasSuccessful():
        print("🎉 ALL TESTS PASSED! 🎉")
        return True
    else:
        print("❌ SOME TESTS FAILED")
        return False


if __name__ == "__main__":
    success = run_comprehensive_tests()
    sys.exit(0 if success else 1)


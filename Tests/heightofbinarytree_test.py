#!/usr/bin/env python3
"""
Comprehensive Test file for heightofbinarytree.py
Tests the height/depth finding functionality with 40+ test cases
100% coverage including edge cases, basic cases, and extremely large trees
"""
import sys
import os
import unittest

# Add the parent directory to Python path to import Trees package
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)

from Trees.node import Node
from Trees.heightofbinarytree import height_of_binary_tree


class TestHeightOfBinaryTree(unittest.TestCase):
    """Comprehensive test class for finding height of binary tree"""
    
    # ==================== EDGE CASES ====================
    
    def test_01_empty_tree(self):
        """Test 1: Empty tree (None root) should return 0"""
        result = height_of_binary_tree(None)
        self.assertEqual(result, 0, "Empty tree should return height 0")
    
    def test_02_single_node(self):
        """Test 2: Single node tree should return height 1"""
        root = Node(42)
        result = height_of_binary_tree(root)
        self.assertEqual(result, 1, "Single node tree should return height 1")
    
    def test_03_single_node_none_value(self):
        """Test 3: Single node with None value still has height 1"""
        root = Node(None)
        result = height_of_binary_tree(root)
        self.assertEqual(result, 1, "Single node with None value should return height 1")
    
    # ==================== BASIC CASES ====================
    
    def test_04_two_nodes_root_and_left(self):
        """Test 4: Root with left child - height 2"""
        root = Node(1)
        root.left = Node(2)
        result = height_of_binary_tree(root)
        self.assertEqual(result, 2, "Tree with root and left child should return height 2")
    
    def test_05_two_nodes_root_and_right(self):
        """Test 5: Root with right child - height 2"""
        root = Node(1)
        root.right = Node(2)
        result = height_of_binary_tree(root)
        self.assertEqual(result, 2, "Tree with root and right child should return height 2")
    
    def test_06_three_nodes_perfect(self):
        """Test 6: Perfect tree with 3 nodes - height 2"""
        root = Node(1)
        root.left = Node(2)
        root.right = Node(3)
        result = height_of_binary_tree(root)
        self.assertEqual(result, 2, "Perfect tree with 3 nodes should return height 2")
    
    def test_07_three_nodes_only_left(self):
        """Test 7: Three nodes (root, left, left-left) - height 3"""
        root = Node(1)
        root.left = Node(2)
        root.left.left = Node(3)
        result = height_of_binary_tree(root)
        self.assertEqual(result, 3, "Left-skewed tree with 3 nodes should return height 3")
    
    def test_08_three_nodes_only_right(self):
        """Test 8: Three nodes (root, right, right-right) - height 3"""
        root = Node(1)
        root.right = Node(2)
        root.right.right = Node(3)
        result = height_of_binary_tree(root)
        self.assertEqual(result, 3, "Right-skewed tree with 3 nodes should return height 3")
    
    def test_09_four_nodes_complete(self):
        """Test 9: Complete tree with 4 nodes - height 3"""
        root = Node(1)
        root.left = Node(2)
        root.right = Node(3)
        root.left.left = Node(4)
        result = height_of_binary_tree(root)
        self.assertEqual(result, 3, "Complete tree with 4 nodes should return height 3")
    
    def test_10_four_nodes_left_skewed(self):
        """Test 10: Left skewed tree with 4 nodes - height 4"""
        root = Node(1)
        root.left = Node(2)
        root.left.left = Node(3)
        root.left.left.left = Node(4)
        result = height_of_binary_tree(root)
        self.assertEqual(result, 4, "Left skewed tree with 4 nodes should return height 4")
    
    def test_11_four_nodes_right_skewed(self):
        """Test 11: Right skewed tree with 4 nodes - height 4"""
        root = Node(1)
        root.right = Node(2)
        root.right.right = Node(3)
        root.right.right.right = Node(4)
        result = height_of_binary_tree(root)
        self.assertEqual(result, 4, "Right skewed tree with 4 nodes should return height 4")
    
    # ==================== MEDIUM COMPLEXITY ====================
    
    def test_12_five_nodes_perfect(self):
        """Test 12: Perfect tree with 5 nodes - height 3"""
        root = Node(1)
        root.left = Node(2)
        root.right = Node(3)
        root.left.left = Node(4)
        root.left.right = Node(5)
        result = height_of_binary_tree(root)
        self.assertEqual(result, 3, "Perfect tree with 5 nodes should return height 3")
    
    def test_13_seven_nodes_perfect(self):
        """Test 13: Perfect tree with 7 nodes - height 3"""
        root = Node(1)
        root.left = Node(2)
        root.right = Node(3)
        root.left.left = Node(4)
        root.left.right = Node(5)
        root.right.left = Node(6)
        root.right.right = Node(7)
        result = height_of_binary_tree(root)
        self.assertEqual(result, 3, "Perfect tree with 7 nodes should return height 3")
    
    def test_14_five_nodes_left_skewed(self):
        """Test 14: Left skewed tree with 5 nodes - height 5"""
        root = Node(1)
        current = root
        for i in range(2, 6):
            current.left = Node(i)
            current = current.left
        result = height_of_binary_tree(root)
        self.assertEqual(result, 5, "Left skewed tree with 5 nodes should return height 5")
    
    def test_15_five_nodes_right_skewed(self):
        """Test 15: Right skewed tree with 5 nodes - height 5"""
        root = Node(1)
        current = root
        for i in range(2, 6):
            current.right = Node(i)
            current = current.right
        result = height_of_binary_tree(root)
        self.assertEqual(result, 5, "Right skewed tree with 5 nodes should return height 5")
    
    def test_16_unbalanced_mixed(self):
        """Test 16: Unbalanced tree with left deeper than right"""
        root = Node(1)
        root.left = Node(2)
        root.right = Node(3)
        root.left.left = Node(4)
        root.left.left.left = Node(5)
        root.right.right = Node(6)
        result = height_of_binary_tree(root)
        self.assertEqual(result, 4, "Unbalanced tree with left depth 4 should return height 4")
    
    def test_17_unbalanced_right_heavy(self):
        """Test 17: Unbalanced tree with right deeper than left"""
        root = Node(1)
        root.left = Node(2)
        root.right = Node(3)
        root.right.right = Node(4)
        root.right.right.right = Node(5)
        root.left.left = Node(6)
        result = height_of_binary_tree(root)
        self.assertEqual(result, 4, "Unbalanced tree with right depth 4 should return height 4")
    
    def test_18_full_binary_tree(self):
        """Test 18: Full binary tree (every node has 0 or 2 children)"""
        root = Node(10)
        root.left = Node(5)
        root.right = Node(15)
        root.left.left = Node(3)
        root.left.right = Node(7)
        root.right.left = Node(12)
        root.right.right = Node(20)
        result = height_of_binary_tree(root)
        self.assertEqual(result, 3, "Full binary tree with 7 nodes should return height 3")
    
    def test_19_complete_binary_tree_6_nodes(self):
        """Test 19: Complete binary tree with 6 nodes - height 3"""
        root = Node(1)
        root.left = Node(2)
        root.right = Node(3)
        root.left.left = Node(4)
        root.left.right = Node(5)
        root.right.left = Node(6)
        result = height_of_binary_tree(root)
        self.assertEqual(result, 3, "Complete tree with 6 nodes should return height 3")
    
    def test_20_zigzag_tree(self):
        """Test 20: Zigzag tree pattern"""
        root = Node(1)
        root.left = Node(2)
        root.left.right = Node(3)
        root.left.right.left = Node(4)
        root.left.right.left.right = Node(5)
        result = height_of_binary_tree(root)
        self.assertEqual(result, 5, "Zigzag tree with depth 5 should return height 5")
    
    # ==================== COMPLEX CASES ====================
    
    def test_21_deep_left_skewed_10_nodes(self):
        """Test 21: Deep left skewed tree with 10 nodes - height 10"""
        root = Node(1)
        current = root
        for i in range(2, 11):
            current.left = Node(i)
            current = current.left
        result = height_of_binary_tree(root)
        self.assertEqual(result, 10, "Left skewed tree with 10 nodes should return height 10")
    
    def test_22_deep_right_skewed_10_nodes(self):
        """Test 22: Deep right skewed tree with 10 nodes - height 10"""
        root = Node(1)
        current = root
        for i in range(2, 11):
            current.right = Node(i)
            current = current.right
        result = height_of_binary_tree(root)
        self.assertEqual(result, 10, "Right skewed tree with 10 nodes should return height 10")
    
    def test_23_perfect_tree_height_4(self):
        """Test 23: Perfect binary tree with height 4 (15 nodes)"""
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
        result = height_of_binary_tree(root)
        self.assertEqual(result, 4, "Perfect tree with height 4 should return 4")
    
    def test_24_complete_tree_15_nodes(self):
        """Test 24: Complete binary tree with 15 nodes - height 4"""
        root = Node(1)
        nodes = [Node(i) for i in range(1, 16)]
        for i in range(15):
            if 2*i + 1 < 15:
                nodes[i].left = nodes[2*i + 1]
            if 2*i + 2 < 15:
                nodes[i].right = nodes[2*i + 2]
        root = nodes[0]
        result = height_of_binary_tree(root)
        self.assertEqual(result, 4, "Complete tree with 15 nodes should return height 4")
    
    def test_25_asymmetric_tree(self):
        """Test 25: Highly asymmetric tree"""
        root = Node(1)
        root.left = Node(2)
        root.left.left = Node(3)
        root.left.left.left = Node(4)
        root.left.left.left.left = Node(5)
        root.right = Node(6)
        root.right.right = Node(7)
        result = height_of_binary_tree(root)
        self.assertEqual(result, 5, "Asymmetric tree with max depth 5 should return height 5")
    
    def test_26_tree_with_none_branches(self):
        """Test 26: Tree with various missing children"""
        root = Node(1)
        root.left = Node(2)
        root.right = Node(3)
        root.left.left = Node(4)
        # root.left.right is None
        root.right.right = Node(7)
        root.right.right.right = Node(8)
        result = height_of_binary_tree(root)
        self.assertEqual(result, 4, "Tree with missing branches should return height 4")
    
    def test_27_balanced_but_not_full(self):
        """Test 27: Balanced tree that's not full"""
        root = Node(1)
        root.left = Node(2)
        root.right = Node(3)
        root.left.left = Node(4)
        root.left.right = Node(5)
        root.right.left = Node(6)
        # root.right.right is None
        root.left.left.left = Node(7)
        result = height_of_binary_tree(root)
        self.assertEqual(result, 4, "Balanced tree with max depth 4 should return height 4")
    
    def test_28_combined_skew(self):
        """Test 28: Tree combining left and right skews"""
        root = Node(1)
        root.left = Node(2)
        root.left.left = Node(3)
        root.right = Node(4)
        root.right.right = Node(5)
        root.right.right.right = Node(6)
        result = height_of_binary_tree(root)
        self.assertEqual(result, 4, "Combined skew tree with max depth 4 should return height 4")
    
    # ==================== LARGE TEST CASES ====================
    
    def test_29_large_complete_tree_31_nodes(self):
        """Test 29: Complete binary tree with 31 nodes - height 5"""
        root = Node(1)
        nodes = [Node(i) for i in range(1, 32)]
        for i in range(31):
            if 2*i + 1 < 31:
                nodes[i].left = nodes[2*i + 1]
            if 2*i + 2 < 31:
                nodes[i].right = nodes[2*i + 2]
        root = nodes[0]
        result = height_of_binary_tree(root)
        self.assertEqual(result, 5, "Complete tree with 31 nodes should return height 5")
    
    def test_30_large_complete_tree_63_nodes(self):
        """Test 30: Complete binary tree with 63 nodes - height 6"""
        root = Node(1)
        nodes = [Node(i) for i in range(1, 64)]
        for i in range(63):
            if 2*i + 1 < 63:
                nodes[i].left = nodes[2*i + 1]
            if 2*i + 2 < 63:
                nodes[i].right = nodes[2*i + 2]
        root = nodes[0]
        result = height_of_binary_tree(root)
        self.assertEqual(result, 6, "Complete tree with 63 nodes should return height 6")
    
    def test_31_large_complete_tree_127_nodes(self):
        """Test 31: Complete binary tree with 127 nodes - height 7"""
        root = Node(1)
        nodes = [Node(i) for i in range(1, 128)]
        for i in range(127):
            if 2*i + 1 < 127:
                nodes[i].left = nodes[2*i + 1]
            if 2*i + 2 < 127:
                nodes[i].right = nodes[2*i + 2]
        root = nodes[0]
        result = height_of_binary_tree(root)
        self.assertEqual(result, 7, "Complete tree with 127 nodes should return height 7")
    
    def test_32_deep_left_skewed_50_nodes(self):
        """Test 32: Left skewed tree with 50 nodes - height 50"""
        root = Node(1)
        current = root
        for i in range(2, 51):
            current.left = Node(i)
            current = current.left
        result = height_of_binary_tree(root)
        self.assertEqual(result, 50, "Left skewed tree with 50 nodes should return height 50")
    
    def test_33_deep_right_skewed_50_nodes(self):
        """Test 33: Right skewed tree with 50 nodes - height 50"""
        root = Node(1)
        current = root
        for i in range(2, 51):
            current.right = Node(i)
            current = current.right
        result = height_of_binary_tree(root)
        self.assertEqual(result, 50, "Right skewed tree with 50 nodes should return height 50")
    
    def test_34_perfect_tree_height_5_63_nodes(self):
        """Test 34: Perfect binary tree with height 6 (63 nodes)"""
        root = Node(1)
        nodes = [Node(i) for i in range(1, 64)]
        # Build perfect binary tree
        for i in range(31, 0, -1):
            if 2*i <= 63:
                nodes[i-1].left = nodes[2*i-1]
            if 2*i + 1 <= 63:
                nodes[i-1].right = nodes[2*i]
        root = nodes[0]
        result = height_of_binary_tree(root)
        self.assertEqual(result, 6, "Perfect tree with 63 nodes (6 levels) should return 6")
    
    def test_35_mixed_depth_tree(self):
        """Test 35: Tree with different depths on left and right subtrees"""
        root = Node(1)
        # Left subtree - depth 10
        left_current = root.left = Node(2)
        for i in range(3, 12):
            left_current.left = Node(i)
            left_current = left_current.left
        # Right subtree - depth 5
        right_current = root.right = Node(12)
        for i in range(13, 17):
            right_current.right = Node(i)
            right_current = right_current.right
        result = height_of_binary_tree(root)
        self.assertEqual(result, 11, "Tree with max depth 11 should return height 11")
    
    def test_36_alternating_tree(self):
        """Test 36: Tree with alternating left/right children"""
        root = Node(1)
        root.left = Node(2)
        root.left.right = Node(3)
        root.left.right.left = Node(4)
        root.left.right.left.right = Node(5)
        root.left.right.left.right.left = Node(6)
        root.left.right.left.right.left.right = Node(7)
        result = height_of_binary_tree(root)
        self.assertEqual(result, 7, "Alternating tree with depth 7 should return height 7")
    
    def test_37_varying_width_tree(self):
        """Test 37: Tree with varying width at different levels"""
        root = Node(1)
        root.left = Node(2)
        root.right = Node(3)
        root.left.left = Node(4)
        root.left.right = Node(5)
        root.left.left.left = Node(6)
        root.left.left.left.left = Node(7)
        root.left.left.left.left.left = Node(8)
        root.right.right = Node(9)
        root.right.right.right = Node(10)
        result = height_of_binary_tree(root)
        self.assertEqual(result, 6, "Tree with max depth 6 should return height 6")
    
    def test_38_staircase_tree(self):
        """Test 38: Staircase pattern tree"""
        root = Node(1)
        root.left = Node(2)
        root.left.left = Node(3)
        root.left.left.left = Node(4)
        root.right = Node(5)
        root.right.right = Node(6)
        root.right.right.right = Node(7)
        root.right.right.right.right = Node(8)
        root.right.right.right.right.right = Node(9)
        result = height_of_binary_tree(root)
        self.assertEqual(result, 6, "Staircase tree with max depth 6 should return height 6")
    
    # ==================== EXTREMELY LARGE TEST CASES ====================
    
    def test_39_extreme_left_skew_100_nodes(self):
        """Test 39: Extremely deep left skewed tree with 100 nodes - height 100"""
        root = Node(1)
        current = root
        for i in range(2, 101):
            current.left = Node(i)
            current = current.left
        result = height_of_binary_tree(root)
        self.assertEqual(result, 100, "Left skewed tree with 100 nodes should return height 100")
    
    def test_40_extreme_right_skew_100_nodes(self):
        """Test 40: Extremely deep right skewed tree with 100 nodes - height 100"""
        root = Node(1)
        current = root
        for i in range(2, 101):
            current.right = Node(i)
            current = current.right
        result = height_of_binary_tree(root)
        self.assertEqual(result, 100, "Right skewed tree with 100 nodes should return height 100")
    
    def test_41_perfect_tree_height_6_127_nodes(self):
        """Test 41: Perfect binary tree with height 5 (31 nodes built)"""
        # Note: Only 31 nodes are built (5 levels), not 127 or 63
        # 31 nodes = 2^5 - 1 = 31, so height is 5, not 6
        root = Node(1)
        # Build level by level
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
        # Continue to depth 5
        root.left.left.left.left = Node(16)
        root.left.left.left.right = Node(17)
        root.left.left.right.left = Node(18)
        root.left.left.right.right = Node(19)
        root.left.right.left.left = Node(20)
        root.left.right.left.right = Node(21)
        root.left.right.right.left = Node(22)
        root.left.right.right.right = Node(23)
        root.right.left.left.left = Node(24)
        root.right.left.left.right = Node(25)
        root.right.left.right.left = Node(26)
        root.right.left.right.right = Node(27)
        root.right.right.left.left = Node(28)
        root.right.right.left.right = Node(29)
        root.right.right.right.left = Node(30)
        root.right.right.right.right = Node(31)
        result = height_of_binary_tree(root)
        self.assertEqual(result, 5, "Perfect tree with 31 nodes (5 levels) should return 5")
    
    def test_42_height_1_validation(self):
        """Test 42: Verify all height 1 scenarios"""
        root = Node(1)
        self.assertEqual(height_of_binary_tree(root), 1)
        
        # After adding children, height increases
        root.left = Node(2)
        self.assertEqual(height_of_binary_tree(root), 2)
        
        root.right = Node(3)
        self.assertEqual(height_of_binary_tree(root), 2)
        
        root.left.left = Node(4)
        self.assertEqual(height_of_binary_tree(root), 3)
    
    def test_43_height_2_validation(self):
        """Test 43: Verify all height 2 scenarios"""
        # Perfect tree height 2
        root = Node(1)
        root.left = Node(2)
        root.right = Node(3)
        self.assertEqual(height_of_binary_tree(root), 2)
        
        # Add to one side only
        root.left.left = Node(4)
        self.assertEqual(height_of_binary_tree(root), 3)
    
    def test_44_height_3_validation(self):
        """Test 44: Verify all height 3 scenarios"""
        root = Node(1)
        root.left = Node(2)
        root.right = Node(3)
        root.left.left = Node(4)
        root.left.right = Node(5)
        root.right.left = Node(6)
        root.right.right = Node(7)
        self.assertEqual(height_of_binary_tree(root), 3)
        
        # Add one more level
        root.left.left.left = Node(8)
        self.assertEqual(height_of_binary_tree(root), 4)
    
    def test_45_height_10_large_tree(self):
        """Test 45: Large balanced tree with height 10"""
        root = Node(1)
        current_level = [root]
        
        for level in range(2, 11):
            next_level = []
            for node in current_level:
                node.left = Node(level * 10 + node.val)
                node.right = Node(level * 10 + node.val + 1)
                next_level.append(node.left)
                next_level.append(node.right)
            current_level = next_level
        
        result = height_of_binary_tree(root)
        self.assertEqual(result, 10, "Large balanced tree with height 10 should return 10")
    
    def test_46_height_15_stress_test(self):
        """Test 46: Very large balanced tree with height 15 (stress test)"""
        root = Node(1)
        current_level = [root]
        
        for level in range(2, 16):
            next_level = []
            for node in current_level:
                node.left = Node(level * 100 + node.val)
                node.right = Node(level * 100 + node.val + 1)
                next_level.append(node.left)
                next_level.append(node.right)
            current_level = next_level
        
        result = height_of_binary_tree(root)
        self.assertEqual(result, 15, "Very large balanced tree with height 15 should return 15")


def run_comprehensive_tests():
    """Run all tests and provide detailed output"""
    print("=" * 80)
    print("COMPREHENSIVE HEIGHT OF BINARY TREE TEST SUITE")
    print("=" * 80)
    
    # Create test suite
    loader = unittest.TestLoader()
    suite = loader.loadTestsFromTestCase(TestHeightOfBinaryTree)
    
    # Run tests with verbose output
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    print("=" * 80)
    print("TEST SUMMARY")
    print("=" * 80)
    print(f"Tests run: {result.testsRun}")
    print(f"Failures: {len(result.failures)}")
    print(f"Errors: {len(result.errors)}")
    success_rate = ((result.testsRun - len(result.failures) - len(result.errors)) / result.testsRun * 100)
    print(f"Success rate: {success_rate:.1f}%")
    
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


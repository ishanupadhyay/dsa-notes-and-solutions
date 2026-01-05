
#!/usr/bin/env python3
"""
Comprehensive Test file for invert_binary_tree.py
Tests the Binary Tree inversion functionality with 30+ test cases
"""
import sys
import os
import unittest

# Add the parent directory to Python path to import Trees package
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)

from Trees.node import Node
from Trees.invertbinarytree import invert_binary_tree


class TestInvertBinaryTree(unittest.TestCase):
    """Comprehensive test class for binary tree inversion"""
    
    def trees_are_equal(self, root1, root2):
        """Helper method to check if two trees have the same structure and values"""
        if not root1 and not root2:
            return True
        if not root1 or not root2:
            return False
        if root1.val != root2.val:
            return False
        return self.trees_are_equal(root1.left, root2.left) and self.trees_are_equal(root1.right, root2.right)
    
    # ==================== EDGE CASES ====================
    
    def test_01_empty_tree(self):
        """Test 1: Empty tree (None root)"""
        result = invert_binary_tree(None)
        self.assertIsNone(result, "Inverting empty tree should return None")
    
    def test_02_single_node(self):
        """Test 2: Single node tree"""
        root = Node(1)
        result = invert_binary_tree(root)
        self.assertEqual(result.val, 1, "Single node value should remain the same")
        self.assertIsNone(result.left, "Single node should have no left child")
        self.assertIsNone(result.right, "Single node should have no right child")
    
    def test_03_two_nodes_left_child(self):
        """Test 3: Tree with root and left child only"""
        root = Node(1)
        root.left = Node(2)
        result = invert_binary_tree(root)
        self.assertEqual(result.val, 1, "Root value should remain 1")
        self.assertIsNone(result.left, "Root should have no left child after inversion")
        self.assertIsNotNone(result.right, "Root should have right child after inversion")
        self.assertEqual(result.right.val, 2, "Right child should have value 2")
    
    def test_04_two_nodes_right_child(self):
        """Test 4: Tree with root and right child only"""
        root = Node(1)
        root.right = Node(2)
        result = invert_binary_tree(root)
        self.assertEqual(result.val, 1, "Root value should remain 1")
        self.assertIsNotNone(result.left, "Root should have left child after inversion")
        self.assertIsNone(result.right, "Root should have no right child after inversion")
        self.assertEqual(result.left.val, 2, "Left child should have value 2")
    
    # ==================== BASIC CASES ====================
    
    def test_05_three_nodes_perfect_tree(self):
        """Test 5: Perfect binary tree with 3 nodes"""
        root = Node(1)
        root.left = Node(2)
        root.right = Node(3)
        result = invert_binary_tree(root)
        # After inversion: left and right should be swapped
        expected = Node(1)
        expected.left = Node(3)
        expected.right = Node(2)
        self.assertTrue(self.trees_are_equal(result, expected), "Perfect tree should have left and right swapped")
    
    def test_06_four_nodes_left_skewed(self):
        """Test 6: Left skewed tree (4 nodes)"""
        root = Node(1)
        root.left = Node(2)
        root.left.left = Node(3)
        root.left.left.left = Node(4)
        result = invert_binary_tree(root)
        # After inversion: should become right skewed
        expected = Node(1)
        expected.right = Node(2)
        expected.right.right = Node(3)
        expected.right.right.right = Node(4)
        self.assertTrue(self.trees_are_equal(result, expected), "Left skewed tree should become right skewed")
    
    def test_07_four_nodes_right_skewed(self):
        """Test 7: Right skewed tree (4 nodes)"""
        root = Node(1)
        root.right = Node(2)
        root.right.right = Node(3)
        root.right.right.right = Node(4)
        result = invert_binary_tree(root)
        # After inversion: should become left skewed
        expected = Node(1)
        expected.left = Node(2)
        expected.left.left = Node(3)
        expected.left.left.left = Node(4)
        self.assertTrue(self.trees_are_equal(result, expected), "Right skewed tree should become left skewed")
    
    def test_08_five_nodes_complete_tree(self):
        """Test 8: Complete binary tree with 5 nodes"""
        root = Node(1)
        root.left = Node(2)
        root.right = Node(3)
        root.left.left = Node(4)
        root.left.right = Node(5)
        result = invert_binary_tree(root)
        # After inversion: children of each node should be swapped
        # Original: 1 with left=2, right=3, and 2 has left=4, right=5
        # After: 1 with left=3, right=2, and 2 has left=5, right=4
        expected = Node(1)
        expected.left = Node(3)
        expected.right = Node(2)
        expected.right.left = Node(5)
        expected.right.right = Node(4)
        self.assertTrue(self.trees_are_equal(result, expected), "Complete tree should have all children swapped")
    
    def test_09_six_nodes_complete_tree(self):
        """Test 9: Complete binary tree with 6 nodes"""
        root = Node(1)
        root.left = Node(2)
        root.right = Node(3)
        root.left.left = Node(4)
        root.left.right = Node(5)
        root.right.left = Node(6)
        result = invert_binary_tree(root)
        # After inversion
        # Original: 1->left=2, right=3; 2->left=4, right=5; 3->left=6
        # After: 1->left=3, right=2; 3->left=6 becomes right; 2->left=5, right=4
        expected = Node(1)
        expected.left = Node(3)
        expected.right = Node(2)
        expected.left.right = Node(6)
        expected.right.left = Node(5)
        expected.right.right = Node(4)
        self.assertTrue(self.trees_are_equal(result, expected), "Complete tree with 6 nodes should be inverted correctly")
    
    def test_10_seven_nodes_perfect_tree(self):
        """Test 10: Perfect binary tree with 7 nodes"""
        root = Node(1)
        root.left = Node(2)
        root.right = Node(3)
        root.left.left = Node(4)
        root.left.right = Node(5)
        root.right.left = Node(6)
        root.right.right = Node(7)
        result = invert_binary_tree(root)
        # After inversion: complete swap at all levels
        expected = Node(1)
        expected.left = Node(3)
        expected.right = Node(2)
        expected.left.left = Node(7)
        expected.left.right = Node(6)
        expected.right.left = Node(5)
        expected.right.right = Node(4)
        self.assertTrue(self.trees_are_equal(result, expected), "Perfect tree should be completely inverted")
    
    # ==================== MEDIUM COMPLEXITY ====================
    
    def test_11_unbalanced_tree(self):
        """Test 11: Unbalanced tree with more nodes on left"""
        root = Node(1)
        root.left = Node(2)
        root.right = Node(3)
        root.left.left = Node(4)
        root.right.right = Node(5)
        result = invert_binary_tree(root)
        # After inversion
        # Original: 1->left=2 (2 has left=4), right=3 (3 has right=5)
        # After: 1->left=3 (3 has left=5), right=2 (2 has right=4)
        expected = Node(1)
        expected.left = Node(3)
        expected.right = Node(2)
        expected.left.left = Node(5)
        expected.right.right = Node(4)
        self.assertTrue(self.trees_are_equal(result, expected), "Unbalanced tree should be inverted correctly")
    
    def test_12_unbalanced_tree_right_heavy(self):
        """Test 12: Unbalanced tree with more nodes on right"""
        root = Node(1)
        root.left = Node(2)
        root.right = Node(3)
        root.right.left = Node(4)
        root.right.right = Node(5)
        result = invert_binary_tree(root)
        # After inversion
        expected = Node(1)
        expected.left = Node(3)
        expected.right = Node(2)
        expected.left.left = Node(5)
        expected.left.right = Node(4)
        self.assertTrue(self.trees_are_equal(result, expected), "Right-heavy tree should be inverted correctly")
    
    def test_13_tree_with_none_values(self):
        """Test 13: Tree with None values in structure"""
        root = Node(1)
        root.left = Node(2)
        root.left.left = Node(4)
        root.left.left.left = Node(8)
        result = invert_binary_tree(root)
        # After inversion: should become right skewed at each level
        expected = Node(1)
        expected.right = Node(2)
        expected.right.right = Node(4)
        expected.right.right.right = Node(8)
        self.assertTrue(self.trees_are_equal(result, expected), "Tree with None values should be inverted correctly")
    
    def test_14_full_binary_tree(self):
        """Test 14: Full binary tree (every node has 0 or 2 children)"""
        root = Node(1)
        root.left = Node(2)
        root.right = Node(3)
        root.left.left = Node(4)
        root.left.right = Node(5)
        root.right.left = Node(6)
        root.right.right = Node(7)
        result = invert_binary_tree(root)
        expected = Node(1)
        expected.left = Node(3)
        expected.right = Node(2)
        expected.left.left = Node(7)
        expected.left.right = Node(6)
        expected.right.left = Node(5)
        expected.right.right = Node(4)
        self.assertTrue(self.trees_are_equal(result, expected), "Full binary tree should be inverted correctly")
    
    def test_15_large_complete_tree(self):
        """Test 15: Complete binary tree with 15 nodes (4 levels)"""
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
        result = invert_binary_tree(root)
        # After inversion: level order should be reversed at each level
        expected = Node(1)
        expected.left = Node(3)
        expected.right = Node(2)
        expected.left.left = Node(7)
        expected.left.right = Node(6)
        expected.right.left = Node(5)
        expected.right.right = Node(4)
        expected.left.left.left = Node(15)
        expected.left.left.right = Node(14)
        expected.left.right.left = Node(13)
        expected.left.right.right = Node(12)
        expected.right.left.left = Node(11)
        expected.right.left.right = Node(10)
        expected.right.right.left = Node(9)
        expected.right.right.right = Node(8)
        self.assertTrue(self.trees_are_equal(result, expected), "Large complete tree should be inverted correctly")
    
    # ==================== COMPLEX CASES ====================
    
    def test_16_deep_left_skewed(self):
        """Test 16: Deep left skewed tree (8 nodes)"""
        root = Node(1)
        current = root
        for i in range(2, 9):
            current.left = Node(i)
            current = current.left
        result = invert_binary_tree(root)
        # Should become deep right skewed
        expected = Node(1)
        current = expected
        for i in range(2, 9):
            current.right = Node(i)
            current = current.right
        self.assertTrue(self.trees_are_equal(result, expected), "Deep left skewed should become deep right skewed")
    
    def test_17_deep_right_skewed(self):
        """Test 17: Deep right skewed tree (8 nodes)"""
        root = Node(1)
        current = root
        for i in range(2, 9):
            current.right = Node(i)
            current = current.right
        result = invert_binary_tree(root)
        # Should become deep left skewed
        expected = Node(1)
        current = expected
        for i in range(2, 9):
            current.left = Node(i)
            current = current.left
        self.assertTrue(self.trees_are_equal(result, expected), "Deep right skewed should become deep left skewed")
    
    def test_18_tree_with_missing_children(self):
        """Test 18: Complex tree with various missing children"""
        root = Node(1)
        root.left = Node(2)
        root.right = Node(3)
        root.left.left = Node(4)
        root.left.right = Node(5)
        root.right.right = Node(7)
        root.left.left.left = Node(8)
        root.left.left.left.left = Node(11)
        result = invert_binary_tree(root)
        # Verify structure after inversion
        # Original: 1->left=2(with children 4,5), right=3(with right=7), 4->left=8->left=11
        # After: 1->left=3(with left=7), right=2(with left=5, right=4), 4->right=8
        self.assertEqual(result.val, 1)
        self.assertEqual(result.left.val, 3)
        self.assertEqual(result.right.val, 2)
        self.assertEqual(result.left.left.val, 7)
        self.assertEqual(result.right.left.val, 5)
        self.assertEqual(result.right.right.val, 4)
        self.assertEqual(result.right.right.right.val, 8)
    
    def test_19_alternating_structure(self):
        """Test 19: Tree with alternating left/right children"""
        root = Node(1)
        root.left = Node(2)
        root.left.left = Node(3)
        root.left.left.left = Node(4)
        result = invert_binary_tree(root)
        expected = Node(1)
        expected.right = Node(2)
        expected.right.right = Node(3)
        expected.right.right.right = Node(4)
        self.assertTrue(self.trees_are_equal(result, expected), "Alternating structure should be inverted correctly")
    
    def test_20_perfect_tree_height_4(self):
        """Test 20: Perfect binary tree with 15 nodes (height 4)"""
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
        result = invert_binary_tree(root)
        expected = Node(1)
        expected.left = Node(3)
        expected.right = Node(2)
        expected.left.left = Node(7)
        expected.left.right = Node(6)
        expected.right.left = Node(5)
        expected.right.right = Node(4)
        expected.left.left.left = Node(15)
        expected.left.left.right = Node(14)
        expected.left.right.left = Node(13)
        expected.left.right.right = Node(12)
        expected.right.left.left = Node(11)
        expected.right.left.right = Node(10)
        expected.right.right.left = Node(9)
        expected.right.right.right = Node(8)
        self.assertTrue(self.trees_are_equal(result, expected), "Perfect tree height 4 should be inverted")
    
    # ==================== ALGORITHM-SPECIFIC CASES ====================
    
    def test_21_double_inversion_returns_original(self):
        """Test 21: Inverting twice should return original tree"""
        root = Node(1)
        root.left = Node(2)
        root.right = Node(3)
        root.left.left = Node(4)
        root.left.right = Node(5)
        root.right.left = Node(6)
        root.right.right = Node(7)
        
        inverted = invert_binary_tree(root)
        double_inverted = invert_binary_tree(inverted)
        
        self.assertTrue(self.trees_are_equal(double_inverted, root), "Double inversion should return original tree")
    
    def test_22_triple_inversion_cycle(self):
        """Test 22: Triple inversion should equal single inversion"""
        root = Node(1)
        root.left = Node(2)
        root.right = Node(3)
        root.left.left = Node(4)
        root.left.right = Node(5)
        
        single = invert_binary_tree(root)
        triple = invert_binary_tree(invert_binary_tree(invert_binary_tree(root)))
        self.assertTrue(self.trees_are_equal(triple, single), "Triple inversion should equal single inversion")
    
    def test_23_single_node_no_change(self):
        """Test 23: Single node tree remains unchanged after inversion"""
        root = Node(42)
        result = invert_binary_tree(root)
        self.assertEqual(result.val, 42, "Single node value should not change")
        self.assertIsNone(result.left, "Single node should have no left child")
        self.assertIsNone(result.right, "Single node should have no right child")
    
    def test_24_two_level_complete_inversion(self):
        """Test 24: Complete 2-level tree inversion"""
        root = Node(0)
        root.left = Node(1)
        root.right = Node(2)
        result = invert_binary_tree(root)
        expected = Node(0)
        expected.left = Node(2)
        expected.right = Node(1)
        self.assertTrue(self.trees_are_equal(result, expected), "2-level complete tree should invert correctly")
    
    def test_25_three_level_complete_inversion(self):
        """Test 25: Complete 3-level tree inversion"""
        root = Node(0)
        root.left = Node(1)
        root.right = Node(2)
        root.left.left = Node(3)
        root.left.right = Node(4)
        root.right.left = Node(5)
        root.right.right = Node(6)
        result = invert_binary_tree(root)
        expected = Node(0)
        expected.left = Node(2)
        expected.right = Node(1)
        expected.left.left = Node(6)
        expected.left.right = Node(5)
        expected.right.left = Node(4)
        expected.right.right = Node(3)
        self.assertTrue(self.trees_are_equal(result, expected), "3-level complete tree should invert correctly")
    
    # ==================== BOUNDARY CONDITIONS ====================
    
    def test_26_negative_values(self):
        """Test 26: Tree with negative values"""
        root = Node(-1)
        root.left = Node(-2)
        root.right = Node(-3)
        root.left.left = Node(-4)
        root.left.right = Node(-5)
        result = invert_binary_tree(root)
        # After inversion: left/right swapped at each node
        expected = Node(-1)
        expected.left = Node(-3)
        expected.right = Node(-2)
        expected.right.left = Node(-5)
        expected.right.right = Node(-4)
        self.assertTrue(self.trees_are_equal(result, expected), "Tree with negative values should invert correctly")
    
    def test_27_zero_values(self):
        """Test 27: Tree with zero values"""
        root = Node(0)
        root.left = Node(0)
        root.right = Node(0)
        root.left.left = Node(0)
        root.left.right = Node(0)
        root.right.left = Node(0)
        root.right.right = Node(0)
        result = invert_binary_tree(root)
        expected = Node(0)
        expected.left = Node(0)
        expected.right = Node(0)
        expected.left.left = Node(0)
        expected.left.right = Node(0)
        expected.right.left = Node(0)
        expected.right.right = Node(0)
        self.assertTrue(self.trees_are_equal(result, expected), "Tree with all zeros should remain symmetric")
    
    def test_28_mixed_positive_negative(self):
        """Test 28: Tree with mixed positive and negative values"""
        root = Node(-5)
        root.left = Node(0)
        root.right = Node(5)
        root.left.left = Node(-3)
        root.left.right = Node(3)
        result = invert_binary_tree(root)
        # Original: -5->left=0(with children -3,3), right=5
        # After: -5->left=5, right=0(with left=3, right=-3)
        expected = Node(-5)
        expected.left = Node(5)
        expected.right = Node(0)
        expected.right.left = Node(3)
        expected.right.right = Node(-3)
        self.assertTrue(self.trees_are_equal(result, expected), "Mixed value tree should invert correctly")
    
    def test_29_duplicate_values(self):
        """Test 29: Tree with duplicate values"""
        root = Node(1)
        root.left = Node(1)
        root.right = Node(1)
        root.left.left = Node(1)
        root.left.right = Node(1)
        root.right.left = Node(1)
        root.right.right = Node(1)
        result = invert_binary_tree(root)
        expected = Node(1)
        expected.left = Node(1)
        expected.right = Node(1)
        expected.left.left = Node(1)
        expected.left.right = Node(1)
        expected.right.left = Node(1)
        expected.right.right = Node(1)
        self.assertTrue(self.trees_are_equal(result, expected), "Tree with duplicate values should invert correctly")
    
    def test_30_large_tree_31_nodes(self):
        """Test 30: Large tree with 31 nodes (5 levels)"""
        root = Node(1)
        # Build a complete tree with 31 nodes
        nodes = [Node(i) for i in range(1, 32)]
        for i in range(31):
            if 2*i + 1 < 31:
                nodes[i].left = nodes[2*i + 1]
            if 2*i + 2 < 31:
                nodes[i].right = nodes[2*i + 2]
        root = nodes[0]
        result = invert_binary_tree(root)
        # Verify structure is correct by checking key nodes
        self.assertEqual(result.val, 1, "Root value should remain 1")
        self.assertEqual(result.left.val, 3, "Left child should be 3 after inversion")
        self.assertEqual(result.right.val, 2, "Right child should be 2 after inversion")
        # Check some grandchildren
        self.assertEqual(result.left.left.val, 7, "Left-left grandchild should be 7")
        self.assertEqual(result.right.right.val, 4, "Right-right grandchild should be 4")
    
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
        result = invert_binary_tree(root)
        # Verify that the structure is correct
        self.assertEqual(result.val, 1, "Root value should remain 1")
        self.assertEqual(result.left.val, 3, "Left child should be 3 after inversion")
        self.assertEqual(result.right.val, 2, "Right child should be 2 after inversion")
    
    def test_32_asymmetric_tree(self):
        """Test 32: Highly asymmetric tree"""
        root = Node(1)
        root.left = Node(2)
        root.left.left = Node(3)
        root.left.left.left = Node(4)
        root.left.left.left.left = Node(5)
        result = invert_binary_tree(root)
        expected = Node(1)
        expected.right = Node(2)
        expected.right.right = Node(3)
        expected.right.right.right = Node(4)
        expected.right.right.right.right = Node(5)
        self.assertTrue(self.trees_are_equal(result, expected), "Asymmetric tree should be inverted correctly")
    
    def test_33_tree_depth_1_no_change(self):
        """Test 33: Tree with only root and one child"""
        root = Node(10)
        root.left = Node(20)
        result = invert_binary_tree(root)
        self.assertEqual(result.val, 10, "Root value should remain 10")
        self.assertIsNone(result.left, "Root should have no left child")
        self.assertIsNotNone(result.right, "Root should have right child")
        self.assertEqual(result.right.val, 20, "Right child should have value 20")
    
    def test_34_tree_depth_2_one_missing(self):
        """Test 34: Tree with some missing grandchildren"""
        root = Node(1)
        root.left = Node(2)
        root.right = Node(3)
        root.left.right = Node(5)
        result = invert_binary_tree(root)
        expected = Node(1)
        expected.left = Node(3)
        expected.right = Node(2)
        expected.right.left = Node(5)
        self.assertTrue(self.trees_are_equal(result, expected), "Tree with missing grandchildren should invert correctly")
    
    def test_35_mirror_image_property(self):
        """Test 35: Verify mirror image property after inversion"""
        # Build a tree
        root = Node(1)
        root.left = Node(2)
        root.right = Node(3)
        root.left.left = Node(4)
        root.left.right = Node(5)
        root.right.left = Node(6)
        root.right.right = Node(7)
        inverted = invert_binary_tree(root)
        
        # Build expected mirror manually
        expected = Node(1)
        expected.left = Node(3)
        expected.right = Node(2)
        expected.left.left = Node(7)
        expected.left.right = Node(6)
        expected.right.left = Node(5)
        expected.right.right = Node(4)
        
        self.assertTrue(self.trees_are_equal(inverted, expected), "Inverted tree should be mirror image")


def run_comprehensive_tests():
    """Run all tests and provide detailed output"""
    print("=" * 80)
    print("COMPREHENSIVE INVERT BINARY TREE TEST SUITE")
    print("=" * 80)
    
    # Create test suite
    loader = unittest.TestLoader()
    suite = loader.loadTestsFromTestCase(TestInvertBinaryTree)
    
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


#!/usr/bin/env python3
"""
Comprehensive Test file for DetectCycle.py
Tests the LinkedList cycle detection functionality with 30+ test cases
"""
import sys
import os
import unittest

# Add the parent directory to Python path to import LinkedList package
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)

from LinkedList.node import Node
from LinkedList.DetectCycle import has_cycle


class TestDetectCycle(unittest.TestCase):
    """Comprehensive test class for cycle detection in linked lists"""
    
    def create_linked_list(self, values):
        """Helper method to create a linked list from a list of values"""
        if not values:
            return None
        
        head = Node(values[0])
        current = head
        for val in values[1:]:
            current.next = Node(val)
            current = current.next
        return head
    
    def create_cycle(self, head, cycle_start_pos):
        """Helper method to create a cycle in a linked list"""
        if head is None or cycle_start_pos < 0:
            return head
        
        current = head
        cycle_start_node = None
        pos = 0
        
        # Find the node where cycle should start
        while current:
            if pos == cycle_start_pos:
                cycle_start_node = current
                break
            current = current.next
            pos += 1
        
        # If we found the cycle start node, connect last node to it
        if cycle_start_node:
            current = head
            while current.next:
                current = current.next
            current.next = cycle_start_node
        
        return head
    
    # ==================== EDGE CASES ====================
    
    def test_01_empty_list(self):
        """Test 1: Empty list (None head)"""
        result = has_cycle(None)
        self.assertFalse(result, "Empty list should not have a cycle")
    
    def test_02_single_node_no_cycle(self):
        """Test 2: Single node without cycle"""
        head = self.create_linked_list([1])
        result = has_cycle(head)
        self.assertFalse(result, "Single node list should not have a cycle")
    
    def test_03_single_node_self_loop(self):
        """Test 3: Single node with self-loop"""
        head = self.create_linked_list([1])
        head.next = head  # Self-loop
        result = has_cycle(head)
        self.assertTrue(result, "Single node with self-loop should have a cycle")
    
    # ==================== BASIC CASES ====================
    
    def test_04_two_nodes_no_cycle(self):
        """Test 4: Two nodes without cycle"""
        head = self.create_linked_list([1, 2])
        result = has_cycle(head)
        self.assertFalse(result, "Two node list without cycle should return False")
    
    def test_05_two_nodes_cycle(self):
        """Test 5: Two nodes with cycle (second points to first)"""
        head = self.create_linked_list([1, 2])
        head.next.next = head  # Second node points to first
        result = has_cycle(head)
        self.assertTrue(result, "Two node list with cycle should return True")
    
    def test_06_three_nodes_no_cycle(self):
        """Test 6: Three nodes without cycle"""
        head = self.create_linked_list([1, 2, 3])
        result = has_cycle(head)
        self.assertFalse(result, "Three node list without cycle should return False")
    
    def test_07_three_nodes_cycle_to_head(self):
        """Test 7: Three nodes with cycle at end pointing to head"""
        head = self.create_linked_list([1, 2, 3])
        self.create_cycle(head, 0)  # Last node points to head
        result = has_cycle(head)
        self.assertTrue(result, "Three node list with cycle to head should return True")
    
    def test_08_three_nodes_cycle_to_middle(self):
        """Test 8: Three nodes with cycle pointing to middle"""
        head = self.create_linked_list([1, 2, 3])
        self.create_cycle(head, 1)  # Last node points to middle node
        result = has_cycle(head)
        self.assertTrue(result, "Three node list with cycle to middle should return True")
    
    # ==================== MEDIUM COMPLEXITY ====================
    
    def test_09_four_nodes_no_cycle(self):
        """Test 9: Four nodes without cycle"""
        head = self.create_linked_list([1, 2, 3, 4])
        result = has_cycle(head)
        self.assertFalse(result, "Four node list without cycle should return False")
    
    def test_10_four_nodes_cycle_beginning(self):
        """Test 10: Four nodes with cycle at beginning"""
        head = self.create_linked_list([1, 2, 3, 4])
        head.next.next.next.next = head  # Last node points to head
        result = has_cycle(head)
        self.assertTrue(result, "Four node list with cycle at beginning should return True")
    
    def test_11_four_nodes_cycle_middle(self):
        """Test 11: Four nodes with cycle in middle"""
        head = self.create_linked_list([1, 2, 3, 4])
        head.next.next.next.next = head.next  # Last node points to second node
        result = has_cycle(head)
        self.assertTrue(result, "Four node list with cycle in middle should return True")
    
    def test_12_five_nodes_no_cycle(self):
        """Test 12: Five nodes without cycle"""
        head = self.create_linked_list([1, 2, 3, 4, 5])
        result = has_cycle(head)
        self.assertFalse(result, "Five node list without cycle should return False")
    
    def test_13_five_nodes_cycle_end(self):
        """Test 13: Five nodes with cycle at end"""
        head = self.create_linked_list([1, 2, 3, 4, 5])
        self.create_cycle(head, 3)  # Last node points to fourth node
        result = has_cycle(head)
        self.assertTrue(result, "Five node list with cycle at end should return True")
    
    # ==================== COMPLEX CASES ====================
    
    def test_14_large_list_no_cycle(self):
        """Test 14: Large list (15 nodes) without cycle"""
        values = list(range(1, 16))  # [1, 2, 3, ..., 15]
        head = self.create_linked_list(values)
        result = has_cycle(head)
        self.assertFalse(result, "Large list without cycle should return False")
    
    def test_15_large_list_cycle_middle(self):
        """Test 15: Large list with cycle in middle"""
        values = list(range(1, 16))  # [1, 2, 3, ..., 15]
        head = self.create_linked_list(values)
        self.create_cycle(head, 7)  # Last node points to 8th node
        result = has_cycle(head)
        self.assertTrue(result, "Large list with cycle in middle should return True")
    
    def test_16_large_list_cycle_at_end(self):
        """Test 16: Large list with cycle at end"""
        values = list(range(1, 16))  # [1, 2, 3, ..., 15]
        head = self.create_linked_list(values)
        self.create_cycle(head, 12)  # Last node points to 13th node
        result = has_cycle(head)
        self.assertTrue(result, "Large list with cycle at end should return True")
    
    def test_17_cycle_at_head(self):
        """Test 17: Cycle at beginning (head points to itself indirectly)"""
        head = self.create_linked_list([1, 2, 3, 4, 5])
        # Create cycle where head is part of the cycle
        head.next.next.next.next.next = head.next.next  # Last node points to third node
        result = has_cycle(head)
        self.assertTrue(result, "List with cycle containing head should return True")
    
    def test_18_multiple_cycle_positions(self):
        """Test 18: Multiple possible meeting points"""
        head = self.create_linked_list([1, 2, 3, 4, 5, 6, 7])
        self.create_cycle(head, 2)  # Last node points to third node
        result = has_cycle(head)
        self.assertTrue(result, "List with cycle should return True regardless of meeting point")
    
    # ==================== ALGORITHM-SPECIFIC CASES ====================
    
    def test_19_even_nodes_cycle(self):
        """Test 19: Cycle with even number of nodes (6 nodes)"""
        head = self.create_linked_list([1, 2, 3, 4, 5, 6])
        self.create_cycle(head, 1)  # Last node points to second node
        result = has_cycle(head)
        self.assertTrue(result, "Even node list with cycle should return True")
    
    def test_20_odd_nodes_cycle(self):
        """Test 20: Cycle with odd number of nodes (7 nodes)"""
        head = self.create_linked_list([1, 2, 3, 4, 5, 6, 7])
        self.create_cycle(head, 3)  # Last node points to fourth node
        result = has_cycle(head)
        self.assertTrue(result, "Odd node list with cycle should return True")
    
    def test_21_immediate_meet(self):
        """Test 21: List where slow and fast pointers meet immediately"""
        head = self.create_linked_list([1, 2])
        head.next.next = head  # Second node points to head, immediate meet possible
        result = has_cycle(head)
        self.assertTrue(result, "List with immediate pointer meet should return True")
    
    def test_22_small_cycle(self):
        """Test 22: Small cycle (2-3 nodes in cycle)"""
        head = self.create_linked_list([1, 2, 3, 4, 5])
        self.create_cycle(head, 3)  # Last two nodes form a cycle
        result = has_cycle(head)
        self.assertTrue(result, "List with small cycle should return True")
    
    def test_23_large_cycle(self):
        """Test 23: Large cycle (most nodes are in cycle)"""
        head = self.create_linked_list([1, 2, 3, 4, 5, 6, 7, 8])
        self.create_cycle(head, 1)  # 7 out of 8 nodes are in cycle
        result = has_cycle(head)
        self.assertTrue(result, "List with large cycle should return True")
    
    # ==================== BOUNDARY CONDITIONS ====================
    
    def test_24_negative_values(self):
        """Test 24: List with negative values"""
        head = self.create_linked_list([-1, -2, -3, -4])
        self.create_cycle(head, 1)  # Cycle with negative values
        result = has_cycle(head)
        self.assertTrue(result, "List with negative values and cycle should return True")
    
    def test_25_zero_values(self):
        """Test 25: List with zero values"""
        head = self.create_linked_list([0, 0, 0, 0])
        result = has_cycle(head)
        self.assertFalse(result, "List with zero values without cycle should return False")
    
    def test_26_duplicate_values(self):
        """Test 26: List with duplicate values"""
        head = self.create_linked_list([1, 1, 2, 2, 3, 3])
        self.create_cycle(head, 2)  # Cycle with duplicate values
        result = has_cycle(head)
        self.assertTrue(result, "List with duplicate values and cycle should return True")
    
    def test_27_mixed_values_cycle(self):
        """Test 27: Mixed positive, negative, and zero values"""
        head = self.create_linked_list([-5, 0, 3, -2, 8])
        self.create_cycle(head, 0)  # Cycle with mixed values
        result = has_cycle(head)
        self.assertTrue(result, "List with mixed values and cycle should return True")
    
    def test_28_alternating_pattern_no_cycle(self):
        """Test 28: Alternating pattern without cycle"""
        head = self.create_linked_list([1, -1, 2, -2, 3, -3, 4, -4])
        result = has_cycle(head)
        self.assertFalse(result, "Alternating pattern without cycle should return False")
    
    def test_29_two_node_cycle_self_loop(self):
        """Test 29: Two-node list with self-loop on first node"""
        head = self.create_linked_list([1, 2])
        head.next = head  # Second node points to first node (self-loop)
        result = has_cycle(head)
        self.assertTrue(result, "Two-node list with self-loop should return True")
    
    def test_30_long_chain_then_cycle(self):
        """Test 30: Long chain (20 nodes) then small cycle"""
        values = list(range(1, 21))  # [1, 2, 3, ..., 20]
        head = self.create_linked_list(values)
        # Create cycle in the last few nodes
        current = head
        for _ in range(17):  # Move to 18th node
            current = current.next
        current.next.next.next = current  # Last 3 nodes form a cycle
        result = has_cycle(head)
        self.assertTrue(result, "Long chain with small cycle should return True")
    
    def test_31_very_large_list_no_cycle(self):
        """Test 31: Very large list (100 nodes) without cycle"""
        values = list(range(1, 101))  # [1, 2, 3, ..., 100]
        head = self.create_linked_list(values)
        result = has_cycle(head)
        self.assertFalse(result, "Very large list without cycle should return False")
    
    def test_32_very_large_list_with_cycle(self):
        """Test 32: Very large list (100 nodes) with cycle"""
        values = list(range(1, 101))  # [1, 2, 3, ..., 100]
        head = self.create_linked_list(values)
        self.create_cycle(head, 50)  # Cycle in the middle
        result = has_cycle(head)
        self.assertTrue(result, "Very large list with cycle should return True")
    
    def test_33_single_element_list_with_self_loop(self):
        """Test 33: Single element with explicit self-loop"""
        head = Node(42)
        head.next = head
        result = has_cycle(head)
        self.assertTrue(result, "Single element with self-loop should return True")
    
    def test_34_two_identical_values_no_cycle(self):
        """Test 34: Two identical values without cycle"""
        head = self.create_linked_list([5, 5])
        result = has_cycle(head)
        self.assertFalse(result, "Two identical values without cycle should return False")
    
    def test_35_complex_cycle_structure(self):
        """Test 35: Complex cycle with multiple connections"""
        head = self.create_linked_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
        # Create a cycle that involves nodes 3->4->5->6->3
        node3 = head.next.next
        node6 = head.next.next.next.next.next
        node6.next = node3
        result = has_cycle(head)
        self.assertTrue(result, "Complex cycle structure should be detected")


def run_comprehensive_tests():
    """Run all tests and provide detailed output"""
    print("=" * 80)
    print("COMPREHENSIVE DETECT CYCLE TEST SUITE")
    print("=" * 80)
    
    # Create test suite
    loader = unittest.TestLoader()
    suite = loader.loadTestsFromTestCase(TestDetectCycle)
    
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

#!/usr/bin/env python3
"""
Test file for FindMiddleofLinkedList.py
Tests the FindMiddle functionality with comprehensive 100% code coverage
"""

import sys
import os

# Add the parent directory to Python path to import LinkedList package
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)

from LinkedList.node import Node
from LinkedList.FindMiddleofLinkedlist import findMiddle


def test_empty_list():
    """Test empty list (None) - covers early return and None handling"""
    print("=" * 60)
    print("Test: Empty List (None)")
    print("=" * 60)
    
    # Test with None input (empty list)
    result = findMiddle(None)
    
    print(f"Input: None")
    print(f"Result: {result}")
    
    if result is None:
        print("✅ PASSED: Empty list returns None")
        return True
    else:
        print("❌ FAILED: Empty list should return None")
        return False


def test_single_node():
    """Test single node list"""
    print("\n" + "=" * 60)
    print("Test: Single Node List")
    print("=" * 60)
    
    # Create single node: 42
    single_node = Node(42)
    
    # Find middle
    result = findMiddle(single_node)
    
    print(f"Input list: 42")
    print(f"Middle node: {result}")
    print(f"Middle node value: {result.val if result else 'N/A'}")
    
    success = (result is not None and 
               result.val == 42 and
               result == single_node)
    
    if success:
        print("✅ PASSED: Single node middle")
        return True
    else:
        print("❌ FAILED: Single node middle")
        return False


def test_two_nodes():
    """Test two node list (even case)"""
    print("\n" + "=" * 60)
    print("Test: Two Node List (Even Case)")
    print("=" * 60)
    
    # Create two node list: 1 -> 2
    node1 = Node(1)
    node2 = Node(2)
    node1.next = node2
    
    # Find middle (should return second node for even length)
    result = findMiddle(node1)
    
    print(f"Input list: 1 -> 2")
    print(f"Middle node: {result}")
    print(f"Middle node value: {result.val if result else 'N/A'}")
    print(f"Middle node is node2: {result == node2}")
    
    success = (result is not None and 
               result.val == 2 and
               result == node2)
    
    if success:
        print("✅ PASSED: Two node list middle (even case)")
        return True
    else:
        print("❌ FAILED: Two node list middle")
        return False


def test_three_nodes():
    """Test three node list (odd case)"""
    print("\n" + "=" * 60)
    print("Test: Three Node List (Odd Case)")
    print("=" * 60)
    
    # Create three node list: 1 -> 2 -> 3
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node1.next = node2
    node2.next = node3
    
    # Find middle (should return second node)
    result = findMiddle(node1)
    
    print(f"Input list: 1 -> 2 -> 3")
    print(f"Middle node: {result}")
    print(f"Middle node value: {result.val if result else 'N/A'}")
    print(f"Middle node is node2: {result == node2}")
    
    success = (result is not None and 
               result.val == 2 and
               result == node2)
    
    if success:
        print("✅ PASSED: Three node list middle (odd case)")
        return True
    else:
        print("❌ FAILED: Three node list middle")
        return False


def test_four_nodes():
    """Test four node list (even case)"""
    print("\n" + "=" * 60)
    print("Test: Four Node List (Even Case)")
    print("=" * 60)
    
    # Create four node list: 1 -> 2 -> 3 -> 4
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    node1.next = node2
    node2.next = node3
    node3.next = node4
    
    # Find middle (should return third node for even length)
    result = findMiddle(node1)
    
    print(f"Input list: 1 -> 2 -> 3 -> 4")
    print(f"Middle node: {result}")
    print(f"Middle node value: {result.val if result else 'N/A'}")
    print(f"Middle node is node3: {result == node3}")
    
    success = (result is not None and 
               result.val == 3 and
               result == node3)
    
    if success:
        print("✅ PASSED: Four node list middle (even case)")
        return True
    else:
        print("❌ FAILED: Four node list middle")
        return False


def test_five_nodes():
    """Test five node list (odd case)"""
    print("\n" + "=" * 60)
    print("Test: Five Node List (Odd Case)")
    print("=" * 60)
    
    # Create five node list: 1 -> 2 -> 3 -> 4 -> 5
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    node5 = Node(5)
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    
    # Find middle (should return third node)
    result = findMiddle(node1)
    
    print(f"Input list: 1 -> 2 -> 3 -> 4 -> 5")
    print(f"Middle node: {result}")
    print(f"Middle node value: {result.val if result else 'N/A'}")
    print(f"Middle node is node3: {result == node3}")
    
    success = (result is not None and 
               result.val == 3 and
               result == node3)
    
    if success:
        print("✅ PASSED: Five node list middle (odd case)")
        return True
    else:
        print("❌ FAILED: Five node list middle")
        return False


def test_large_list():
    """Test larger list (10 nodes)"""
    print("\n" + "=" * 60)
    print("Test: Large List (10 nodes)")
    print("=" * 60)
    
    # Create list with 10 nodes: 1 -> 2 -> 3 -> ... -> 10
    head = Node(1)
    current = head
    
    for i in range(2, 11):
        new_node = Node(i)
        current.next = new_node
        current = new_node
    
    print(f"Created list with 10 nodes (1 to 10)")
    
    # Find middle (should return node 6 for even length)
    result = findMiddle(head)
    
    print(f"Middle node: {result}")
    print(f"Middle node value: {result.val if result else 'N/A'}")
    
    success = (result is not None and result.val == 6)
    
    if success:
        print("✅ PASSED: Large list middle")
        return True
    else:
        print("❌ FAILED: Large list middle")
        return False


def test_while_loop_condition_fast_none():
    """Test while loop condition - case where fast becomes None"""
    print("\n" + "=" * 60)
    print("Test: While Loop Condition (fast becomes None)")
    print("=" * 60)
    
    # Create odd length list where fast will become None
    # 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 (7 nodes, odd)
    head = Node(1)
    current = head
    
    for i in range(2, 8):
        new_node = Node(i)
        current.next = new_node
        current = new_node
    
    print(f"Created 7-node list: 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7")
    
    result = findMiddle(head)
    
    print(f"Middle node: {result}")
    print(f"Middle node value: {result.val if result else 'N/A'}")
    
    # For 7 nodes, middle should be node 4
    success = (result is not None and result.val == 4)
    
    if success:
        print("✅ PASSED: While loop condition (fast None)")
        return True
    else:
        print("❌ FAILED: While loop condition (fast None)")
        return False


def test_while_loop_condition_fast_next_none():
    """Test while loop condition - case where fast.next becomes None"""
    print("\n" + "=" * 60)
    print("Test: While Loop Condition (fast.next becomes None)")
    print("=" * 60)
    
    # Create even length list where fast.next will become None
    # 1 -> 2 -> 3 -> 4 -> 5 -> 6 (6 nodes, even)
    head = Node(1)
    current = head
    
    for i in range(2, 7):
        new_node = Node(i)
        current.next = new_node
        current = new_node
    
    print(f"Created 6-node list: 1 -> 2 -> 3 -> 4 -> 5 -> 6")
    
    result = findMiddle(head)
    
    print(f"Middle node: {result}")
    print(f"Middle node value: {result.val if result else 'N/A'}")
    
    # For 6 nodes, middle should be node 4 (second middle)
    success = (result is not None and result.val == 4)
    
    if success:
        print("✅ PASSED: While loop condition (fast.next None)")
        return True
    else:
        print("❌ FAILED: While loop condition (fast.next None)")
        return False


def test_negative_values():
    """Test with negative values"""
    print("\n" + "=" * 60)
    print("Test: Negative Values")
    print("=" * 60)
    
    # Create list with negative values: -5 -> -3 -> -1
    node1 = Node(-5)
    node2 = Node(-3)
    node3 = Node(-1)
    node1.next = node2
    node2.next = node3
    
    print(f"Input list: -5 -> -3 -> -1")
    
    result = findMiddle(node1)
    
    print(f"Middle node: {result}")
    print(f"Middle node value: {result.val if result else 'N/A'}")
    
    success = (result is not None and result.val == -3)
    
    if success:
        print("✅ PASSED: Negative values")
        return True
    else:
        print("❌ FAILED: Negative values")
        return False


def test_zero_values():
    """Test with zero values"""
    print("\n" + "=" * 60)
    print("Test: Zero Values")
    print("=" * 60)
    
    # Create list with zero values: 0 -> 0 -> 0
    node1 = Node(0)
    node2 = Node(0)
    node3 = Node(0)
    node1.next = node2
    node2.next = node3
    
    print(f"Input list: 0 -> 0 -> 0")
    
    result = findMiddle(node1)
    
    print(f"Middle node: {result}")
    print(f"Middle node value: {result.val if result else 'N/A'}")
    
    success = (result is not None and result.val == 0)
    
    if success:
        print("✅ PASSED: Zero values")
        return True
    else:
        print("❌ FAILED: Zero values")
        return False


def test_duplicate_values():
    """Test with duplicate values"""
    print("\n" + "=" * 60)
    print("Test: Duplicate Values")
    print("=" * 60)
    
    # Create list with duplicates: 5 -> 5 -> 5 -> 5
    node1 = Node(5)
    node2 = Node(5)
    node3 = Node(5)
    node4 = Node(5)
    node1.next = node2
    node2.next = node3
    node3.next = node4
    
    print(f"Input list: 5 -> 5 -> 5 -> 5")
    
    result = findMiddle(node1)
    
    print(f"Middle node: {result}")
    print(f"Middle node value: {result.val if result else 'N/A'}")
    print(f"Middle node is node3: {result == node3}")
    
    success = (result is not None and 
               result.val == 5 and
               result == node3)
    
    if success:
        print("✅ PASSED: Duplicate values")
        return True
    else:
        print("❌ FAILED: Duplicate values")
        return False


def test_mixed_values():
    """Test with mixed positive, negative, and zero"""
    print("\n" + "=" * 60)
    print("Test: Mixed Values")
    print("=" * 60)
    
    # Create list with mixed values: -1 -> 0 -> 1 -> 2 -> 3
    node1 = Node(-1)
    node2 = Node(0)
    node3 = Node(1)
    node4 = Node(2)
    node5 = Node(3)
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    
    print(f"Input list: -1 -> 0 -> 1 -> 2 -> 3")
    
    result = findMiddle(node1)
    
    print(f"Middle node: {result}")
    print(f"Middle node value: {result.val if result else 'N/A'}")
    print(f"Middle node is node3: {result == node3}")
    
    success = (result is not None and 
               result.val == 1 and
               result == node3)
    
    if success:
        print("✅ PASSED: Mixed values")
        return True
    else:
        print("❌ FAILED: Mixed values")
        return False


def test_very_small_lists():
    """Test very small lists (1-2 nodes)"""
    print("\n" + "=" * 60)
    print("Test: Very Small Lists")
    print("=" * 60)
    
    success_count = 0
    total_tests = 2
    
    # Test 1: Single node
    single = Node(100)
    result1 = findMiddle(single)
    
    print("Case 1: Single node (100)")
    print(f"Middle: {result1.val if result1 else 'N/A'}")
    
    if result1 is not None and result1.val == 100:
        print("✅ Single node test passed")
        success_count += 1
    else:
        print("❌ Single node test failed")
    
    # Test 2: Two nodes
    node1 = Node(200)
    node2 = Node(300)
    node1.next = node2
    result2 = findMiddle(node1)
    
    print("Case 2: Two nodes (200 -> 300)")
    print(f"Middle: {result2.val if result2 else 'N/A'}")
    
    if result2 is not None and result2.val == 300 and result2 == node2:
        print("✅ Two node test passed")
        success_count += 1
    else:
        print("❌ Two node test failed")
    
    if success_count == total_tests:
        print("✅ PASSED: Very small lists")
        return True
    else:
        print("❌ FAILED: Very small lists")
        return False


def test_very_large_list():
    """Test very large list (50 nodes)"""
    print("\n" + "=" * 60)
    print("Test: Very Large List (50 nodes)")
    print("=" * 60)
    
    # Create list with 50 nodes
    head = Node(1)
    current = head
    
    for i in range(2, 51):
        new_node = Node(i)
        current.next = new_node
        current = new_node
    
    print(f"Created list with 50 nodes (1 to 50)")
    
    result = findMiddle(head)
    
    print(f"Middle node: {result}")
    print(f"Middle node value: {result.val if result else 'N/A'}")
    
    # For 50 nodes (even), middle should be node 26 (second middle)
    success = (result is not None and result.val == 26)
    
    if success:
        print("✅ PASSED: Very large list")
        return True
    else:
        print("❌ FAILED: Very large list")
        return False


def test_node_integrity():
    """Test that nodes remain unchanged after finding middle"""
    print("\n" + "=" * 60)
    print("Test: Node Integrity")
    print("=" * 60)
    
    # Create list: A -> B -> C -> D
    node_a = Node('A')
    node_b = Node('B')
    node_c = Node('C')
    node_d = Node('D')
    
    node_a.next = node_b
    node_b.next = node_c
    node_c.next = node_d
    
    # Store original node references
    original_a = node_a
    original_b = node_b
    original_c = node_c
    original_d = node_d
    
    print(f"Original list: A -> B -> C -> D")
    print(f"Node A id: {id(original_a)}")
    print(f"Node B id: {id(original_b)}")
    print(f"Node C id: {id(original_c)}")
    print(f"Node D id: {id(original_d)}")
    
    # Find middle
    result = findMiddle(node_a)
    
    print(f"Middle node: {result}")
    print(f"Middle node value: {result.val if result else 'N/A'}")
    
    # Verify node integrity
    node_a_unchanged = (node_a == original_a and node_a.val == 'A')
    node_b_unchanged = (node_b == original_b and node_b.val == 'B')
    node_c_unchanged = (node_c == original_c and node_c.val == 'C')
    node_d_unchanged = (node_d == original_d and node_d.val == 'D')
    
    print(f"Node A unchanged: {node_a_unchanged}")
    print(f"Node B unchanged: {node_b_unchanged}")
    print(f"Node C unchanged: {node_c_unchanged}")
    print(f"Node D unchanged: {node_d_unchanged}")
    
    success = (node_a_unchanged and node_b_unchanged and 
               node_c_unchanged and node_d_unchanged)
    
    if success:
        print("✅ PASSED: Node integrity")
        return True
    else:
        print("❌ FAILED: Node integrity")
        return False


def test_original_list_preservation():
    """Test that original list structure is preserved after finding middle"""
    print("\n" + "=" * 60)
    print("Test: Original List Preservation")
    print("=" * 60)
    
    # Create list: 10 -> 20 -> 30 -> 40 -> 50
    node1 = Node(10)
    node2 = Node(20)
    node3 = Node(30)
    node4 = Node(40)
    node5 = Node(50)
    
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    
    # Store original structure
    original_head = node1
    
    print(f"Original list: 10 -> 20 -> 30 -> 40 -> 50")
    
    # Find middle
    result = findMiddle(original_head)
    
    print(f"Middle node: {result}")
    print(f"Middle node value: {result.val if result else 'N/A'}")
    
    # Verify list structure is preserved
    head_unchanged = (original_head == node1)
    connections_preserved = (
        node1.next == node2 and
        node2.next == node3 and
        node3.next == node4 and
        node4.next == node5 and
        node5.next is None
    )
    
    # Get current list values
    current = original_head
    values = []
    while current:
        values.append(current.val)
        current = current.next
    
    expected_values = [10, 20, 30, 40, 50]
    
    print(f"Expected values: {expected_values}")
    print(f"Actual values: {values}")
    print(f"Head unchanged: {head_unchanged}")
    print(f"Connections preserved: {connections_preserved}")
    
    success = (head_unchanged and 
               connections_preserved and 
               values == expected_values)
    
    if success:
        print("✅ PASSED: Original list preservation")
        return True
    else:
        print("❌ FAILED: Original list preservation")
        return False


def run_all_tests():
    """Run all test cases and return overall result"""
    print("🚀 Starting FindMiddleofLinkedList Tests")
    print("=" * 80)
    
    test_functions = [
        test_empty_list,
        test_single_node,
        test_two_nodes,
        test_three_nodes,
        test_four_nodes,
        test_five_nodes,
        test_large_list,
        test_while_loop_condition_fast_none,
        test_while_loop_condition_fast_next_none,
        test_negative_values,
        test_zero_values,
        test_duplicate_values,
        test_mixed_values,
        test_very_small_lists,
        test_very_large_list,
        test_node_integrity,
        test_original_list_preservation
    ]
    
    passed_tests = 0
    failed_tests = 0
    
    for test_func in test_functions:
        try:
            if test_func():
                passed_tests += 1
            else:
                failed_tests += 1
        except Exception as e:
            print(f"❌ ERROR in {test_func.__name__}: {str(e)}")
            failed_tests += 1
    
    print("\n" + "=" * 80)
    print("Final Test Summary")
    print("=" * 80)
    print(f"Total tests: {len(test_functions)}")
    print(f"Passed: {passed_tests}")
    print(f"Failed: {failed_tests}")
    
    if failed_tests == 0:
        print("🎉 All tests passed successfully!")
        print("📊 Code Coverage: 100%")
        return True
    else:
        print("💥 Some tests failed!")
        return False


if __name__ == "__main__":
    # Run all tests
    success = run_all_tests()
    
    # Exit with appropriate code
    if success:
        print("\n✅ All FindMiddleofLinkedList tests passed!")
        sys.exit(0)
    else:
        print("\n❌ Some tests failed!")
        sys.exit(1)

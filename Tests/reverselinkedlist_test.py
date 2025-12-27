#!/usr/bin/env python3
"""
Test file for ReverseLinkedList.py
Tests the LinkedList reversal functionality with various test cases
"""

import sys
import os

# Add the parent directory to Python path to import LinkedList package
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)

from LinkedList.node import Node
from LinkedList.ReverseLinkedList import reverse_linked_list


def get_linked_list_values(head):
    """Helper function to get values from a linked list"""
    values = []
    current = head
    while current:
        values.append(current.val)
        current = current.next
    return values


def test_reverse_basic_linkedlist():
    """Test basic linked list reversal"""
    print("=" * 60)
    print("Test: Basic LinkedList Reversal")
    print("=" * 60)
    
    # Create linked list: 1 -> 2 -> 3 -> 4 -> 5
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    node5 = Node(5)
    
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    
    original_values = get_linked_list_values(node1)
    print(f"Original list: {original_values}")
    
    # Reverse the linked list
    reversed_head = reverse_linked_list(node1)
    reversed_values = get_linked_list_values(reversed_head)
    
    expected_reversed = [5, 4, 3, 2, 1]
    print(f"Expected reversed: {expected_reversed}")
    print(f"Actual reversed: {reversed_values}")
    
    if reversed_values == expected_reversed:
        print("✅ PASSED: Basic linked list reversal")
        return True
    else:
        print("❌ FAILED: Basic linked list reversal")
        return False


def test_reverse_single_node():
    """Test reversal of single node linked list"""
    print("\n" + "=" * 60)
    print("Test: Single Node LinkedList")
    print("=" * 60)
    
    single_node = Node(42)
    print(f"Original single node: {single_node.val}")
    
    # Reverse the single node
    reversed_head = reverse_linked_list(single_node)
    reversed_values = get_linked_list_values(reversed_head)
    
    expected_reversed = [42]
    print(f"Expected reversed: {expected_reversed}")
    print(f"Actual reversed: {reversed_values}")
    
    if reversed_values == expected_reversed:
        print("✅ PASSED: Single node reversal")
        return True
    else:
        print("❌ FAILED: Single node reversal")
        return False


def test_reverse_empty_linkedlist():
    """Test reversal of empty linked list (None)"""
    print("\n" + "=" * 60)
    print("Test: Empty LinkedList (None)")
    print("=" * 60)
    
    # Test None input
    reversed_head = reverse_linked_list(None)
    reversed_values = get_linked_list_values(reversed_head)
    
    expected_reversed = []
    print(f"Expected reversed: {expected_reversed}")
    print(f"Actual reversed: {reversed_values}")
    
    if reversed_values == expected_reversed:
        print("✅ PASSED: Empty linked list reversal")
        return True
    else:
        print("❌ FAILED: Empty linked list reversal")
        return False


def test_reverse_two_nodes():
    """Test reversal of two node linked list"""
    print("\n" + "=" * 60)
    print("Test: Two Node LinkedList")
    print("=" * 60)
    
    # Create linked list: 10 -> 20
    node1 = Node(10)
    node2 = Node(20)
    node1.next = node2
    
    original_values = get_linked_list_values(node1)
    print(f"Original list: {original_values}")
    
    # Reverse the linked list
    reversed_head = reverse_linked_list(node1)
    reversed_values = get_linked_list_values(reversed_head)
    
    expected_reversed = [20, 10]
    print(f"Expected reversed: {expected_reversed}")
    print(f"Actual reversed: {reversed_values}")
    
    if reversed_values == expected_reversed:
        print("✅ PASSED: Two node reversal")
        return True
    else:
        print("❌ FAILED: Two node reversal")
        return False


def test_reverse_linkedlist_with_duplicates():
    """Test reversal with duplicate values"""
    print("\n" + "=" * 60)
    print("Test: LinkedList with Duplicate Values")
    print("=" * 60)
    
    # Create linked list: 5 -> 5 -> 5 -> 5
    node1 = Node(5)
    node2 = Node(5)
    node3 = Node(5)
    node4 = Node(5)
    
    node1.next = node2
    node2.next = node3
    node3.next = node4
    
    original_values = get_linked_list_values(node1)
    print(f"Original list: {original_values}")
    
    # Reverse the linked list
    reversed_head = reverse_linked_list(node1)
    reversed_values = get_linked_list_values(reversed_head)
    
    expected_reversed = [5, 5, 5, 5]
    print(f"Expected reversed: {expected_reversed}")
    print(f"Actual reversed: {reversed_values}")
    
    if reversed_values == expected_reversed:
        print("✅ PASSED: LinkedList with duplicates reversal")
        return True
    else:
        print("❌ FAILED: LinkedList with duplicates reversal")
        return False


def test_reverse_negative_values():
    """Test reversal with negative values"""
    print("\n" + "=" * 60)
    print("Test: LinkedList with Negative Values")
    print("=" * 60)
    
    # Create linked list: -1 -> -2 -> -3 -> -4
    node1 = Node(-1)
    node2 = Node(-2)
    node3 = Node(-3)
    node4 = Node(-4)
    
    node1.next = node2
    node2.next = node3
    node3.next = node4
    
    original_values = get_linked_list_values(node1)
    print(f"Original list: {original_values}")
    
    # Reverse the linked list
    reversed_head = reverse_linked_list(node1)
    reversed_values = get_linked_list_values(reversed_head)
    
    expected_reversed = [-4, -3, -2, -1]
    print(f"Expected reversed: {expected_reversed}")
    print(f"Actual reversed: {reversed_values}")
    
    if reversed_values == expected_reversed:
        print("✅ PASSED: LinkedList with negative values reversal")
        return True
    else:
        print("❌ FAILED: LinkedList with negative values reversal")
        return False


def test_reverse_mixed_values():
    """Test reversal with mixed positive, negative, and zero"""
    print("\n" + "=" * 60)
    print("Test: LinkedList with Mixed Values")
    print("=" * 60)
    
    # Create linked list: 0 -> -5 -> 10 -> 3 -> -8
    node1 = Node(0)
    node2 = Node(-5)
    node3 = Node(10)
    node4 = Node(3)
    node5 = Node(-8)
    
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    
    original_values = get_linked_list_values(node1)
    print(f"Original list: {original_values}")
    
    # Reverse the linked list
    reversed_head = reverse_linked_list(node1)
    reversed_values = get_linked_list_values(reversed_head)
    
    expected_reversed = [-8, 3, 10, -5, 0]
    print(f"Expected reversed: {expected_reversed}")
    print(f"Actual reversed: {reversed_values}")
    
    if reversed_values == expected_reversed:
        print("✅ PASSED: LinkedList with mixed values reversal")
        return True
    else:
        print("❌ FAILED: LinkedList with mixed values reversal")
        return False


def test_reverse_large_list():
    """Test reversal with larger linked list"""
    print("\n" + "=" * 60)
    print("Test: Large LinkedList (10 nodes)")
    print("=" * 60)
    
    # Create linked list with 10 nodes: 1 -> 2 -> 3 -> ... -> 10
    head = Node(1)
    current = head
    
    for i in range(2, 11):
        new_node = Node(i)
        current.next = new_node
        current = new_node
    
    original_values = get_linked_list_values(head)
    print(f"Original list (first 3 and last 3): ...{original_values[3:-3]}...")
    print(f"Original values: {original_values}")
    
    # Reverse the linked list
    reversed_head = reverse_linked_list(head)
    reversed_values = get_linked_list_values(reversed_head)
    
    expected_reversed = list(range(10, 0, -1))
    print(f"Expected reversed: {expected_reversed}")
    print(f"Actual reversed: {reversed_values}")
    
    if reversed_values == expected_reversed:
        print("✅ PASSED: Large linked list reversal")
        return True
    else:
        print("❌ FAILED: Large linked list reversal")
        return False


def test_reverse_in_place_modification():
    """Test that reversal modifies the list in place"""
    print("\n" + "=" * 60)
    print("Test: In-Place Modification")
    print("=" * 60)
    
    # Create linked list: A -> B -> C -> D
    node1 = Node('A')
    node2 = Node('B')
    node3 = Node('C')
    node4 = Node('D')
    
    node1.next = node2
    node2.next = node3
    node3.next = node4
    
    original_values = get_linked_list_values(node1)
    print(f"Original list: {original_values}")
    
    # Store references to verify they are the same nodes
    original_node4 = node4
    
    # Reverse the linked list
    reversed_head = reverse_linked_list(node1)
    reversed_values = get_linked_list_values(reversed_head)
    
    expected_reversed = ['D', 'C', 'B', 'A']
    print(f"Expected reversed: {expected_reversed}")
    print(f"Actual reversed: {reversed_values}")
    
    # Verify that the original head is now None (list was modified in place)
    original_head_check = node1.next is None
    print(f"Original head (node1) next is None: {original_head_check}")
    
    # Verify that the new head is the old tail
    new_head_is_old_tail = reversed_head is original_node4
    print(f"New head is old tail: {new_head_is_old_tail}")
    
    if (reversed_values == expected_reversed and 
        original_head_check and 
        new_head_is_old_tail):
        print("✅ PASSED: In-place modification verification")
        return True
    else:
        print("❌ FAILED: In-place modification verification")
        return False


def test_node_integrity_after_reversal():
    """Test that nodes maintain their integrity after reversal"""
    print("\n" + "=" * 60)
    print("Test: Node Integrity After Reversal")
    print("=" * 60)
    
    # Create linked list with specific node objects
    node1 = Node(100)
    node2 = Node(200)
    node3 = Node(300)
    
    node1.next = node2
    node2.next = node3
    
    # Store original node references
    original_node1 = node1
    original_node2 = node2
    original_node3 = node3
    
    print(f"Original node1 id: {id(original_node1)}")
    print(f"Original node2 id: {id(original_node2)}")
    print(f"Original node3 id: {id(original_node3)}")
    
    # Reverse the linked list
    reversed_head = reverse_linked_list(node1)
    
    # Verify that the same node objects exist but in reversed order
    reversed_values = get_linked_list_values(reversed_head)
    expected_reversed = [300, 200, 100]
    
    # Check if the same node objects are used
    current = reversed_head
    expected_nodes = [original_node3, original_node2, original_node1]
    
    nodes_match = True
    for i, expected_node in enumerate(expected_nodes):
        if current is not expected_node:
            nodes_match = False
            break
        current = current.next
    
    print(f"Expected reversed: {expected_reversed}")
    print(f"Actual reversed: {reversed_values}")
    print(f"Same node objects used: {nodes_match}")
    
    if reversed_values == expected_reversed and nodes_match:
        print("✅ PASSED: Node integrity after reversal")
        return True
    else:
        print("❌ FAILED: Node integrity after reversal")
        return False


def run_all_tests():
    """Run all test cases and return overall result"""
    print("🚀 Starting Reverse LinkedList Tests")
    print("=" * 80)
    
    test_functions = [
        test_reverse_basic_linkedlist,
        test_reverse_single_node,
        test_reverse_empty_linkedlist,
        test_reverse_two_nodes,
        test_reverse_linkedlist_with_duplicates,
        test_reverse_negative_values,
        test_reverse_mixed_values,
        test_reverse_large_list,
        test_reverse_in_place_modification,
        test_node_integrity_after_reversal
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
        return True
    else:
        print("💥 Some tests failed!")
        return False


if __name__ == "__main__":
    # Run all tests
    success = run_all_tests()
    
    # Exit with appropriate code
    if success:
        print("\n✅ All Reverse LinkedList tests passed!")
        sys.exit(0)
    else:
        print("\n❌ Some tests failed!")
        sys.exit(1)

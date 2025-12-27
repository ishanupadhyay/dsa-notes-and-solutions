#!/usr/bin/env python3
"""
Test file for InsertNodeAtBeginning.py
Tests the InsertNodeAtBeginning functionality with comprehensive coverage
"""

import sys
import os
from io import StringIO
from contextlib import redirect_stdout

# Add the parent directory to Python path to import LinkedList package
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)

from LinkedList.node import Node
from LinkedList.InsertNodeAtBeginning import insert_at_begin


def test_insert_into_empty_list():
    """Test inserting into empty list (None head)"""
    print("=" * 60)
    print("Test: Insert into Empty List (None head)")
    print("=" * 60)
    
    # Test inserting into None
    new_node = Node(100)
    result_head = insert_at_begin(None, new_node)
    
    print(f"Original head: None")
    print(f"New node: {new_node}")
    print(f"Result head: {result_head}")
    print(f"New node.next: {result_head.next if result_head else 'N/A'}")
    
    if result_head == new_node and result_head.next is None:
        print("✅ PASSED: Insert into empty list")
        return True
    else:
        print("❌ FAILED: Insert into empty list")
        return False


def test_insert_into_single_node_list():
    """Test inserting into single node list"""
    print("\n" + "=" * 60)
    print("Test: Insert into Single Node List")
    print("=" * 60)
    
    # Create single node: 5
    existing_node = Node(5)
    
    # Insert new node: 10 at beginning
    new_node = Node(10)
    result_head = insert_at_begin(existing_node, new_node)
    
    print(f"Original head: {existing_node}")
    print(f"New node: {new_node}")
    print(f"Result head: {result_head}")
    print(f"New node.next: {result_head.next}")
    print(f"Original node is now second: {result_head.next == existing_node}")
    
    success = (result_head == new_node and 
               result_head.next == existing_node and
               existing_node.next is None)
    
    if success:
        print("✅ PASSED: Insert into single node list")
        return True
    else:
        print("❌ FAILED: Insert into single node list")
        return False


def test_insert_into_multi_node_list():
    """Test inserting into multi-node list"""
    print("\n" + "=" * 60)
    print("Test: Insert into Multi-Node List")
    print("=" * 60)
    
    # Create linked list: 1 -> 2 -> 3
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    
    node1.next = node2
    node2.next = node3
    
    # Insert new node: 0 at beginning
    new_node = Node(0)
    result_head = insert_at_begin(node1, new_node)
    
    print(f"Original head: {node1}")
    print(f"New node: {new_node}")
    print(f"Result head: {result_head}")
    print(f"New node.next: {result_head.next}")
    print(f"Original node is now second: {result_head.next == node1}")
    
    # Verify the complete structure: 0 -> 1 -> 2 -> 3
    current = result_head
    values = []
    while current:
        values.append(current.val)
        current = current.next
    
    expected_values = [0, 1, 2, 3]
    
    print(f"Expected values: {expected_values}")
    print(f"Actual values: {values}")
    
    success = (result_head == new_node and 
               result_head.next == node1 and
               values == expected_values)
    
    if success:
        print("✅ PASSED: Insert into multi-node list")
        return True
    else:
        print("❌ FAILED: Insert into multi-node list")
        return False


def test_return_value_correctness():
    """Test that function returns correct new head"""
    print("\n" + "=" * 60)
    print("Test: Return Value Correctness")
    print("=" * 60)
    
    # Create list: 100 -> 200
    node1 = Node(100)
    node2 = Node(200)
    node1.next = node2
    
    # Insert new node: 50
    new_node = Node(50)
    result_head = insert_at_begin(node1, new_node)
    
    print(f"New node: {new_node}")
    print(f"Result head: {result_head}")
    print(f"Return value is new node: {result_head == new_node}")
    print(f"Return value is NOT old head: {result_head != node1}")
    
    success = (result_head == new_node and 
               result_head != node1)
    
    if success:
        print("✅ PASSED: Return value correctness")
        return True
    else:
        print("❌ FAILED: Return value correctness")
        return False


def test_node_connections_integrity():
    """Test that node connections are properly maintained"""
    print("\n" + "=" * 60)
    print("Test: Node Connections Integrity")
    print("=" * 60)
    
    # Create list: A -> B -> C -> D
    node_a = Node('A')
    node_b = Node('B')
    node_c = Node('C')
    node_d = Node('D')
    
    node_a.next = node_b
    node_b.next = node_c
    node_c.next = node_d
    
    # Insert new node: 'Z' at beginning
    new_node = Node('Z')
    original_head = node_a
    result_head = insert_at_begin(original_head, new_node)
    
    print(f"Original list: A -> B -> C -> D")
    print(f"Inserting: Z at beginning")
    print(f"Result: {result_head.val} -> {result_head.next.val} -> {result_head.next.next.val} -> {result_head.next.next.next.val} -> {result_head.next.next.next.next}")
    
    # Verify each connection
    connections_correct = (
        result_head == new_node and
        result_head.next == original_head and
        original_head.next == node_b and
        node_b.next == node_c and
        node_c.next == node_d and
        node_d.next is None
    )
    
    if connections_correct:
        print("✅ PASSED: Node connections integrity")
        return True
    else:
        print("❌ FAILED: Node connections integrity")
        return False


def test_multiple_consecutive_insertions():
    """Test multiple consecutive insertions at beginning"""
    print("\n" + "=" * 60)
    print("Test: Multiple Consecutive Insertions")
    print("=" * 60)
    
    # Start with single node: 10
    head = Node(10)
    
    print("Starting with: 10")
    
    # Insert 9 at beginning
    head = insert_at_begin(head, Node(9))
    print("After inserting 9: 9 -> 10")
    
    # Insert 8 at beginning
    head = insert_at_begin(head, Node(8))
    print("After inserting 8: 8 -> 9 -> 10")
    
    # Insert 7 at beginning
    head = insert_at_begin(head, Node(7))
    print("After inserting 7: 7 -> 8 -> 9 -> 10")
    
    # Verify final structure
    current = head
    values = []
    while current:
        values.append(current.val)
        current = current.next
    
    expected_values = [7, 8, 9, 10]
    
    print(f"Expected values: {expected_values}")
    print(f"Actual values: {values}")
    
    if values == expected_values:
        print("✅ PASSED: Multiple consecutive insertions")
        return True
    else:
        print("❌ FAILED: Multiple consecutive insertions")
        return False


def test_insert_with_negative_values():
    """Test inserting with negative values"""
    print("\n" + "=" * 60)
    print("Test: Insert with Negative Values")
    print("=" * 60)
    
    # Create list: -5 -> -3 -> -1
    node1 = Node(-5)
    node2 = Node(-3)
    node3 = Node(-1)
    
    node1.next = node2
    node2.next = node3
    
    # Insert new node: -10 at beginning
    new_node = Node(-10)
    result_head = insert_at_begin(node1, new_node)
    
    print(f"Original list: -5 -> -3 -> -1")
    print(f"Inserting: -10 at beginning")
    
    # Verify values
    current = result_head
    values = []
    while current:
        values.append(current.val)
        current = current.next
    
    expected_values = [-10, -5, -3, -1]
    
    print(f"Expected values: {expected_values}")
    print(f"Actual values: {values}")
    
    if values == expected_values:
        print("✅ PASSED: Insert with negative values")
        return True
    else:
        print("❌ FAILED: Insert with negative values")
        return False


def test_insert_with_zero_and_duplicates():
    """Test inserting with zero and duplicate values"""
    print("\n" + "=" * 60)
    print("Test: Insert with Zero and Duplicates")
    print("=" * 60)
    
    # Create list: 5 -> 0 -> 5
    node1 = Node(5)
    node2 = Node(0)
    node3 = Node(5)
    
    node1.next = node2
    node2.next = node3
    
    # Insert new node: 5 (duplicate) at beginning
    new_node = Node(5)
    result_head = insert_at_begin(node1, new_node)
    
    print(f"Original list: 5 -> 0 -> 5")
    print(f"Inserting: 5 (duplicate) at beginning")
    
    # Verify values
    current = result_head
    values = []
    while current:
        values.append(current.val)
        current = current.next
    
    expected_values = [5, 5, 0, 5]
    
    print(f"Expected values: {expected_values}")
    print(f"Actual values: {values}")
    
    if values == expected_values:
        print("✅ PASSED: Insert with zero and duplicates")
        return True
    else:
        print("❌ FAILED: Insert with zero and duplicates")
        return False


def test_large_list_insertion():
    """Test inserting into larger linked list"""
    print("\n" + "=" * 60)
    print("Test: Large List Insertion")
    print("=" * 60)
    
    # Create large list with 100 nodes (1 -> 2 -> 3 -> ... -> 100)
    head = Node(1)
    current = head
    
    for i in range(2, 101):
        new_node = Node(i)
        current.next = new_node
        current = new_node
    
    print(f"Created list with 100 nodes (1 to 100)")
    
    # Insert 0 at beginning
    new_node = Node(0)
    result_head = insert_at_begin(head, new_node)
    
    print(f"Inserting 0 at beginning")
    
    # Verify first few and last few values
    current = result_head
    values = []
    count = 0
    while current and count < 105:  # Check first 5 and verify structure
        values.append(current.val)
        current = current.next
        count += 1
    
    expected_first_five = [0, 1, 2, 3, 4]
    actual_first_five = values[:5]
    
    print(f"Expected first 5 values: {expected_first_five}")
    print(f"Actual first 5 values: {actual_first_five}")
    print(f"List structure maintained: {len(values) >= 101}")
    
    success = (actual_first_five == expected_first_five and 
               len(values) >= 101)
    
    if success:
        print("✅ PASSED: Large list insertion")
        return True
    else:
        print("❌ FAILED: Large list insertion")
        return False


def test_original_list_preservation():
    """Test that original list structure is preserved after insertion"""
    print("\n" + "=" * 60)
    print("Test: Original List Preservation")
    print("=" * 60)
    
    # Create original list: 10 -> 20 -> 30
    node1 = Node(10)
    node2 = Node(20)
    node3 = Node(30)
    
    node1.next = node2
    node2.next = node3
    
    # Keep reference to original head
    original_head = node1
    
    # Insert new node
    new_node = Node(5)
    result_head = insert_at_begin(original_head, new_node)
    
    print(f"Original head before insertion: {original_head}")
    print(f"New head after insertion: {result_head}")
    
    # Verify original list is still intact
    current = original_head
    original_values = []
    while current:
        original_values.append(current.val)
        current = current.next
    
    expected_original = [10, 20, 30]
    
    print(f"Original list values: {original_values}")
    print(f"Expected original values: {expected_original}")
    
    # Also verify the new list
    current = result_head
    new_list_values = []
    while current:
        new_list_values.append(current.val)
        current = current.next
    
    expected_new_list = [5, 10, 20, 30]
    
    print(f"New list values: {new_list_values}")
    print(f"Expected new list values: {expected_new_list}")
    
    success = (original_values == expected_original and
               new_list_values == expected_new_list)
    
    if success:
        print("✅ PASSED: Original list preservation")
        return True
    else:
        print("❌ FAILED: Original list preservation")
        return False


def run_all_tests():
    """Run all test cases and return overall result"""
    print("🚀 Starting InsertNodeAtBeginning Tests")
    print("=" * 80)
    
    test_functions = [
        test_insert_into_empty_list,
        test_insert_into_single_node_list,
        test_insert_into_multi_node_list,
        test_return_value_correctness,
        test_node_connections_integrity,
        test_multiple_consecutive_insertions,
        test_insert_with_negative_values,
        test_insert_with_zero_and_duplicates,
        test_large_list_insertion,
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
        return True
    else:
        print("💥 Some tests failed!")
        return False


if __name__ == "__main__":
    # Run all tests
    success = run_all_tests()
    
    # Exit with appropriate code
    if success:
        print("\n✅ All InsertNodeAtBeginning tests passed!")
        sys.exit(0)
    else:
        print("\n❌ Some tests failed!")
        sys.exit(1)

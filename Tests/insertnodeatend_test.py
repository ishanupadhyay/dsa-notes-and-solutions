#!/usr/bin/env python3
"""
Test file for InsertNodeAtEnd.py
Tests the InsertNodeAtEnd functionality with comprehensive coverage
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
from LinkedList.InsertNodeAtEnd import insertNodeAtEnd


def test_insert_into_empty_list():
    """Test inserting into empty list (None head)"""
    print("=" * 60)
    print("Test: Insert into Empty List (None head)")
    print("=" * 60)
    
    # Test inserting into None
    new_node = Node(100)
    result_head = insertNodeAtEnd(None, new_node)
    
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
    
    # Insert new node: 10 at end
    new_node = Node(10)
    result_head = insertNodeAtEnd(existing_node, new_node)
    
    print(f"Original head: {existing_node}")
    print(f"New node: {new_node}")
    print(f"Result head: {result_head}")
    print(f"Existing node.next: {result_head.next}")
    print(f"New node.next: {result_head.next.next}")
    
    success = (result_head == existing_node and 
               result_head.next == new_node and
               new_node.next is None)
    
    if success:
        print("✅ PASSED: Insert into single node list")
        return True
    else:
        print("❌ FAILED: Insert into single node list")
        return False


def test_insert_into_two_node_list():
    """Test inserting into two node list"""
    print("\n" + "=" * 60)
    print("Test: Insert into Two Node List")
    print("=" * 60)
    
    # Create two node list: 1 -> 2
    node1 = Node(1)
    node2 = Node(2)
    node1.next = node2
    
    # Insert new node: 3 at end
    new_node = Node(3)
    result_head = insertNodeAtEnd(node1, new_node)
    
    print(f"Original head: {node1}")
    print(f"New node: {new_node}")
    print(f"Result head: {result_head}")
    print(f"Node1.next: {result_head.next}")
    print(f"Node2.next: {result_head.next.next}")
    print(f"New node.next: {result_head.next.next.next}")
    
    # Verify the complete structure: 1 -> 2 -> 3
    current = result_head
    values = []
    while current:
        values.append(current.val)
        current = current.next
    
    expected_values = [1, 2, 3]
    
    print(f"Expected values: {expected_values}")
    print(f"Actual values: {values}")
    
    success = (result_head == node1 and 
               node1.next == node2 and
               node2.next == new_node and
               new_node.next is None and
               values == expected_values)
    
    if success:
        print("✅ PASSED: Insert into two node list")
        return True
    else:
        print("❌ FAILED: Insert into two node list")
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
    
    # Insert new node: 4 at end
    new_node = Node(4)
    result_head = insertNodeAtEnd(node1, new_node)
    
    print(f"Original head: {node1}")
    print(f"New node: {new_node}")
    print(f"Result head: {result_head}")
    
    # Verify the complete structure: 1 -> 2 -> 3 -> 4
    current = result_head
    values = []
    while current:
        values.append(current.val)
        current = current.next
    
    expected_values = [1, 2, 3, 4]
    
    print(f"Expected values: {expected_values}")
    print(f"Actual values: {values}")
    
    success = (result_head == node1 and 
               node1.next == node2 and
               node2.next == node3 and
               node3.next == new_node and
               new_node.next is None and
               values == expected_values)
    
    if success:
        print("✅ PASSED: Insert into multi-node list")
        return True
    else:
        print("❌ FAILED: Insert into multi-node list")
        return False


def test_return_value_correctness():
    """Test that function returns correct head (should remain unchanged)"""
    print("\n" + "=" * 60)
    print("Test: Return Value Correctness")
    print("=" * 60)
    
    # Create list: 100 -> 200
    node1 = Node(100)
    node2 = Node(200)
    node1.next = node2
    
    # Insert new node: 300
    new_node = Node(300)
    result_head = insertNodeAtEnd(node1, new_node)
    
    print(f"Original head: {node1}")
    print(f"New node: {new_node}")
    print(f"Result head: {result_head}")
    print(f"Return value is original head: {result_head == node1}")
    print(f"Return value is NOT new node: {result_head != new_node}")
    
    success = (result_head == node1 and 
               result_head != new_node)
    
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
    
    # Insert new node: 'Z' at end
    new_node = Node('Z')
    original_head = node_a
    result_head = insertNodeAtEnd(original_head, new_node)
    
    print(f"Original list: A -> B -> C -> D")
    print(f"Inserting: Z at end")
    print(f"Result: {result_head.val} -> {result_head.next.val} -> {result_head.next.next.val} -> {result_head.next.next.next.val} -> {result_head.next.next.next.next.val}")
    
    # Verify each connection
    connections_correct = (
        result_head == original_head and
        original_head.next == node_b and
        node_b.next == node_c and
        node_c.next == node_d and
        node_d.next == new_node and
        new_node.next is None
    )
    
    if connections_correct:
        print("✅ PASSED: Node connections integrity")
        return True
    else:
        print("❌ FAILED: Node connections integrity")
        return False


def test_multiple_consecutive_insertions():
    """Test multiple consecutive insertions at end"""
    print("\n" + "=" * 60)
    print("Test: Multiple Consecutive Insertions")
    print("=" * 60)
    
    # Start with single node: 10
    head = Node(10)
    
    print("Starting with: 10")
    
    # Insert 11 at end
    head = insertNodeAtEnd(head, Node(11))
    print("After inserting 11: 10 -> 11")
    
    # Insert 12 at end
    head = insertNodeAtEnd(head, Node(12))
    print("After inserting 12: 10 -> 11 -> 12")
    
    # Insert 13 at end
    head = insertNodeAtEnd(head, Node(13))
    print("After inserting 13: 10 -> 11 -> 12 -> 13")
    
    # Verify final structure
    current = head
    values = []
    while current:
        values.append(current.val)
        current = current.next
    
    expected_values = [10, 11, 12, 13]
    
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
    
    # Insert new node: -10 at end
    new_node = Node(-10)
    result_head = insertNodeAtEnd(node1, new_node)
    
    print(f"Original list: -5 -> -3 -> -1")
    print(f"Inserting: -10 at end")
    
    # Verify values
    current = result_head
    values = []
    while current:
        values.append(current.val)
        current = current.next
    
    expected_values = [-5, -3, -1, -10]
    
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
    
    # Insert new node: 5 (duplicate) at end
    new_node = Node(5)
    result_head = insertNodeAtEnd(node1, new_node)
    
    print(f"Original list: 5 -> 0 -> 5")
    print(f"Inserting: 5 (duplicate) at end")
    
    # Verify values
    current = result_head
    values = []
    while current:
        values.append(current.val)
        current = current.next
    
    expected_values = [5, 0, 5, 5]
    
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
    
    # Insert 101 at end
    new_node = Node(101)
    result_head = insertNodeAtEnd(head, new_node)
    
    print(f"Inserting 101 at end")
    
    # Verify last few values
    current = result_head
    values = []
    while current:
        values.append(current.val)
        current = current.next
    
    expected_first_five = [1, 2, 3, 4, 5]
    expected_last_five = [97, 98, 99, 100, 101]
    actual_first_five = values[:5]
    actual_last_five = values[-5:]
    
    print(f"Expected first 5 values: {expected_first_five}")
    print(f"Actual first 5 values: {actual_first_five}")
    print(f"Expected last 5 values: {expected_last_five}")
    print(f"Actual last 5 values: {actual_last_five}")
    
    success = (actual_first_five == expected_first_five and 
               actual_last_five == expected_last_five and
               len(values) == 101)
    
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
    result_head = insertNodeAtEnd(original_head, new_node)
    
    print(f"Original head before insertion: {original_head}")
    print(f"New head after insertion: {result_head}")
    
    # Since insertNodeAtEnd modifies the list in place, the original_head
    # now points to the modified list. We need to verify that:
    # 1. The head hasn't changed (inserting at end doesn't change head)
    # 2. The structure is correct (new node is at the end)
    
    # Verify head hasn't changed
    head_unchanged = (result_head == original_head)
    
    # Verify the new list structure
    current = result_head
    new_list_values = []
    while current:
        new_list_values.append(current.val)
        current = current.next
    
    expected_new_list = [10, 20, 30, 5]
    
    print(f"New list values: {new_list_values}")
    print(f"Expected new list values: {expected_new_list}")
    print(f"Head unchanged (in-place modification): {head_unchanged}")
    
    # Also verify that individual node connections are preserved
    node1_still_points_to_node2 = (node1.next == node2)
    node2_still_points_to_node3 = (node2.next == node3)
    node3_now_points_to_new_node = (node3.next == new_node)
    new_node_at_end = (new_node.next is None)
    
    print(f"Node1 still points to Node2: {node1_still_points_to_node2}")
    print(f"Node2 still points to Node3: {node2_still_points_to_node3}")
    print(f"Node3 now points to new node: {node3_now_points_to_new_node}")
    print(f"New node is at the end: {new_node_at_end}")
    
    success = (head_unchanged and
               new_list_values == expected_new_list and
               node1_still_points_to_node2 and
               node2_still_points_to_node3 and
               node3_now_points_to_new_node and
               new_node_at_end)
    
    if success:
        print("✅ PASSED: Original list preservation")
        return True
    else:
        print("❌ FAILED: Original list preservation")
        return False


def test_while_loop_condition_coverage():
    """Test while loop condition by ensuring both true and false paths are covered"""
    print("\n" + "=" * 60)
    print("Test: While Loop Condition Coverage")
    print("=" * 60)
    
    # Test case 1: List with multiple nodes (while curr.next will be True at least once)
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node1.next = node2
    node2.next = node3
    
    new_node = Node(4)
    result_head = insertNodeAtEnd(node1, new_node)
    
    print("Case 1: Multi-node list (while loop runs)")
    current = result_head
    values = []
    while current:
        values.append(current.val)
        current = current.next
    expected = [1, 2, 3, 4]
    print(f"Expected: {expected}, Actual: {values}")
    
    success1 = values == expected
    
    # Test case 2: Single node list (while curr.next will be False immediately)
    single_node = Node(100)
    new_single_node = Node(200)
    result_head2 = insertNodeAtEnd(single_node, new_single_node)
    
    print("Case 2: Single node list (while loop condition false immediately)")
    current = result_head2
    values = []
    while current:
        values.append(current.val)
        current = current.next
    expected = [100, 200]
    print(f"Expected: {expected}, Actual: {values}")
    
    success2 = values == expected
    
    if success1 and success2:
        print("✅ PASSED: While loop condition coverage")
        return True
    else:
        print("❌ FAILED: While loop condition coverage")
        return False


def test_traversal_to_end_correctness():
    """Test that traversal reaches the actual end of the list"""
    print("\n" + "=" * 60)
    print("Test: Traversal to End Correctness")
    print("=" * 60)
    
    # Create list: A -> B -> C -> D -> E
    node_a = Node('A')
    node_b = Node('B')
    node_c = Node('C')
    node_d = Node('D')
    node_e = Node('E')
    
    node_a.next = node_b
    node_b.next = node_c
    node_c.next = node_d
    node_d.next = node_e
    
    # Insert 'Z' at end
    new_node = Node('Z')
    result_head = insertNodeAtEnd(node_a, new_node)
    
    print(f"Original list: A -> B -> C -> D -> E")
    print(f"Inserting: Z at end")
    
    # Verify the complete structure: A -> B -> C -> D -> E -> Z
    current = result_head
    values = []
    while current:
        values.append(current.val)
        current = current.next
    
    expected_values = ['A', 'B', 'C', 'D', 'E', 'Z']
    
    print(f"Expected values: {expected_values}")
    print(f"Actual values: {values}")
    
    # Also verify that E is now pointing to Z
    e_to_z = (node_e.next == new_node)
    z_at_end = (new_node.next is None)
    
    print(f"Node E points to Z: {e_to_z}")
    print(f"Z is at the end: {z_at_end}")
    
    success = (values == expected_values and e_to_z and z_at_end)
    
    if success:
        print("✅ PASSED: Traversal to end correctness")
        return True
    else:
        print("❌ FAILED: Traversal to end correctness")
        return False


def run_all_tests():
    """Run all test cases and return overall result"""
    print("🚀 Starting InsertNodeAtEnd Tests")
    print("=" * 80)
    
    test_functions = [
        test_insert_into_empty_list,
        test_insert_into_single_node_list,
        test_insert_into_two_node_list,
        test_insert_into_multi_node_list,
        test_return_value_correctness,
        test_node_connections_integrity,
        test_multiple_consecutive_insertions,
        test_insert_with_negative_values,
        test_insert_with_zero_and_duplicates,
        test_large_list_insertion,
        test_original_list_preservation,
        test_while_loop_condition_coverage,
        test_traversal_to_end_correctness
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
        print("\n✅ All InsertNodeAtEnd tests passed!")
        sys.exit(0)
    else:
        print("\n❌ Some tests failed!")
        sys.exit(1)

#!/usr/bin/env python3
"""
Test file for TraverseLinkedList.py
Tests the LinkedList traversal functionality with various test cases
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
from LinkedList.TraverseLinkedList import traveselinkedlist


def test_traverse_basic_linkedlist():
    """Test basic linked list traversal"""
    print("=" * 60)
    print("Test: Basic LinkedList Traversal")
    print("=" * 60)
    
    # Create linked list: 1 -> 2 -> 3 -> 4
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    
    node1.next = node2
    node2.next = node3
    node3.next = node4
    
    # Capture output
    captured_output = StringIO()
    with redirect_stdout(captured_output):
        traveselinkedlist(node1)
    
    output = captured_output.getvalue().strip()
    expected_output = "1\n2\n3\n4"
    
    print(f"Expected output:\n{expected_output}")
    print(f"Actual output:\n{output}")
    
    if output == expected_output:
        print("✅ PASSED: Basic linked list traversal")
        return True
    else:
        print("❌ FAILED: Basic linked list traversal")
        return False


def test_traverse_single_node():
    """Test traversal of single node linked list"""
    print("\n" + "=" * 60)
    print("Test: Single Node LinkedList")
    print("=" * 60)
    
    single_node = Node(42)
    
    # Capture output
    captured_output = StringIO()
    with redirect_stdout(captured_output):
        traveselinkedlist(single_node)
    
    output = captured_output.getvalue().strip()
    expected_output = "42"
    
    print(f"Expected output: {expected_output}")
    print(f"Actual output: {output}")
    
    if output == expected_output:
        print("✅ PASSED: Single node traversal")
        return True
    else:
        print("❌ FAILED: Single node traversal")
        return False


def test_traverse_empty_linkedlist():
    """Test traversal of empty linked list (None)"""
    print("\n" + "=" * 60)
    print("Test: Empty LinkedList (None)")
    print("=" * 60)
    
    # Capture output for None input
    captured_output = StringIO()
    with redirect_stdout(captured_output):
        traveselinkedlist(None)
    
    output = captured_output.getvalue().strip()
    expected_output = ""  # No output expected for None
    
    print(f"Expected output: '{expected_output}'")
    print(f"Actual output: '{output}'")
    
    if output == expected_output:
        print("✅ PASSED: Empty linked list traversal")
        return True
    else:
        print("❌ FAILED: Empty linked list traversal")
        return False


def test_traverse_linkedlist_with_duplicates():
    """Test traversal with duplicate values"""
    print("\n" + "=" * 60)
    print("Test: LinkedList with Duplicate Values")
    print("=" * 60)
    
    # Create linked list: 5 -> 5 -> 5
    node1 = Node(5)
    node2 = Node(5)
    node3 = Node(5)
    
    node1.next = node2
    node2.next = node3
    
    # Capture output
    captured_output = StringIO()
    with redirect_stdout(captured_output):
        traveselinkedlist(node1)
    
    output = captured_output.getvalue().strip()
    expected_output = "5\n5\n5"
    
    print(f"Expected output:\n{expected_output}")
    print(f"Actual output:\n{output}")
    
    if output == expected_output:
        print("✅ PASSED: LinkedList with duplicates")
        return True
    else:
        print("❌ FAILED: LinkedList with duplicates")
        return False


def test_traverse_negative_values():
    """Test traversal with negative values"""
    print("\n" + "=" * 60)
    print("Test: LinkedList with Negative Values")
    print("=" * 60)
    
    # Create linked list: -1 -> -2 -> -3
    node1 = Node(-1)
    node2 = Node(-2)
    node3 = Node(-3)
    
    node1.next = node2
    node2.next = node3
    
    # Capture output
    captured_output = StringIO()
    with redirect_stdout(captured_output):
        traveselinkedlist(node1)
    
    output = captured_output.getvalue().strip()
    expected_output = "-1\n-2\n-3"
    
    print(f"Expected output:\n{expected_output}")
    print(f"Actual output:\n{output}")
    
    if output == expected_output:
        print("✅ PASSED: LinkedList with negative values")
        return True
    else:
        print("❌ FAILED: LinkedList with negative values")
        return False


def test_traverse_mixed_values():
    """Test traversal with mixed positive, negative, and zero"""
    print("\n" + "=" * 60)
    print("Test: LinkedList with Mixed Values")
    print("=" * 60)
    
    # Create linked list: 0 -> -5 -> 10 -> 0
    node1 = Node(0)
    node2 = Node(-5)
    node3 = Node(10)
    node4 = Node(0)
    
    node1.next = node2
    node2.next = node3
    node3.next = node4
    
    # Capture output
    captured_output = StringIO()
    with redirect_stdout(captured_output):
        traveselinkedlist(node1)
    
    output = captured_output.getvalue().strip()
    expected_output = "0\n-5\n10\n0"
    
    print(f"Expected output:\n{expected_output}")
    print(f"Actual output:\n{output}")
    
    if output == expected_output:
        print("✅ PASSED: LinkedList with mixed values")
        return True
    else:
        print("❌ FAILED: LinkedList with mixed values")
        return False


def test_traverse_large_list():
    """Test traversal with larger linked list"""
    print("\n" + "=" * 60)
    print("Test: Large LinkedList (10 nodes)")
    print("=" * 60)
    
    # Create linked list with 10 nodes
    head = Node(1)
    current = head
    
    for i in range(2, 11):
        new_node = Node(i)
        current.next = new_node
        current = new_node
    
    # Capture output
    captured_output = StringIO()
    with redirect_stdout(captured_output):
        traveselinkedlist(head)
    
    output = captured_output.getvalue().strip()
    expected_output = "\n".join(str(i) for i in range(1, 11))
    
    print(f"Expected output (first 3 and last 3):")
    print("...\n".join(expected_output.split("\n")[:3]) + "\n...\n" + "\n".join(expected_output.split("\n")[-3:]))
    print(f"Actual output (first 3 and last 3):")
    actual_lines = output.split("\n")
    print("...\n".join(actual_lines[:3]) + "\n...\n" + "\n".join(actual_lines[-3:]))
    
    if output == expected_output:
        print("✅ PASSED: Large linked list traversal")
        return True
    else:
        print("❌ FAILED: Large linked list traversal")
        return False


def test_node_string_representation():
    """Test Node class string representation"""
    print("\n" + "=" * 60)
    print("Test: Node String Representation")
    print("=" * 60)
    
    test_node = Node(42)
    expected_repr = "Node(42)"
    actual_repr = repr(test_node)
    
    print(f"Expected representation: {expected_repr}")
    print(f"Actual representation: {actual_repr}")
    
    if actual_repr == expected_repr:
        print("✅ PASSED: Node string representation")
        return True
    else:
        print("❌ FAILED: Node string representation")
        return False


def run_all_tests():
    """Run all test cases and return overall result"""
    print("🚀 Starting LinkedList Traversal Tests")
    print("=" * 80)
    
    test_functions = [
        test_traverse_basic_linkedlist,
        test_traverse_single_node,
        test_traverse_empty_linkedlist,
        test_traverse_linkedlist_with_duplicates,
        test_traverse_negative_values,
        test_traverse_mixed_values,
        test_traverse_large_list,
        test_node_string_representation
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
        print("\n✅ All LinkedList traversal tests passed!")
        sys.exit(0)
    else:
        print("\n❌ Some tests failed!")
        sys.exit(1)

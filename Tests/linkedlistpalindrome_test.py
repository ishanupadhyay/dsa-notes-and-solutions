#!/usr/bin/env python3
"""
Test file for LinkedListPalindrome.py
Tests the palindrome detection functionality with comprehensive coverage
"""

import sys
import os

# Add the parent directory to Python path to import LinkedList package
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)

from LinkedList.node import Node
from LinkedList.LinkedListPalindrome import pallindrome_linked_list, find_middle, reverse_ll


def test_palindrome_odd_length():
    """Test palindrome detection with odd length list"""
    print("=" * 60)
    print("Test: Palindrome with Odd Length (1->2->3->2->1)")
    print("=" * 60)
    
    # Create palindrome: 1 -> 2 -> 3 -> 2 -> 1
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(2)
    node5 = Node(1)
    
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    
    result = pallindrome_linked_list(node1)
    
    print(f"Linked list: 1 -> 2 -> 3 -> 2 -> 1")
    print(f"Is palindrome: {result}")
    
    if result:
        print("✅ PASSED: Odd length palindrome")
        return True
    else:
        print("❌ FAILED: Odd length palindrome")
        return False


def test_palindrome_even_length():
    """Test palindrome detection with even length list"""
    print("\n" + "=" * 60)
    print("Test: Palindrome with Even Length (1->2->2->1)")
    print("=" * 60)
    
    # Create palindrome: 1 -> 2 -> 2 -> 1
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(2)
    node4 = Node(1)
    
    node1.next = node2
    node2.next = node3
    node3.next = node4
    
    result = pallindrome_linked_list(node1)
    
    print(f"Linked list: 1 -> 2 -> 2 -> 1")
    print(f"Is palindrome: {result}")
    
    if result:
        print("✅ PASSED: Even length palindrome")
        return True
    else:
        print("❌ FAILED: Even length palindrome")
        return False


def test_not_palindrome_odd_length():
    """Test non-palindrome with odd length"""
    print("\n" + "=" * 60)
    print("Test: Not Palindrome with Odd Length (1->2->3->4->1)")
    print("=" * 60)
    
    # Create non-palindrome: 1 -> 2 -> 3 -> 4 -> 1
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    node5 = Node(1)
    
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    
    result = pallindrome_linked_list(node1)
    
    print(f"Linked list: 1 -> 2 -> 3 -> 4 -> 1")
    print(f"Is palindrome: {result}")
    
    if not result:
        print("✅ PASSED: Not palindrome with odd length")
        return True
    else:
        print("❌ FAILED: Not palindrome with odd length")
        return False


def test_not_palindrome_even_length():
    """Test non-palindrome with even length"""
    print("\n" + "=" * 60)
    print("Test: Not Palindrome with Even Length (1->2->3->4)")
    print("=" * 60)
    
    # Create non-palindrome: 1 -> 2 -> 3 -> 4
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    
    node1.next = node2
    node2.next = node3
    node3.next = node4
    
    result = pallindrome_linked_list(node1)
    
    print(f"Linked list: 1 -> 2 -> 3 -> 4")
    print(f"Is palindrome: {result}")
    
    if not result:
        print("✅ PASSED: Not palindrome with even length")
        return True
    else:
        print("❌ FAILED: Not palindrome with even length")
        return False


def test_single_node_palindrome():
    """Test single node list (should be palindrome)"""
    print("\n" + "=" * 60)
    print("Test: Single Node Palindrome")
    print("=" * 60)
    
    # Create single node
    single_node = Node(42)
    
    result = pallindrome_linked_list(single_node)
    
    print(f"Linked list: 42 (single node)")
    print(f"Is palindrome: {result}")
    
    if result:
        print("✅ PASSED: Single node palindrome")
        return True
    else:
        print("❌ FAILED: Single node palindrome")
        return False


def test_two_nodes_same_palindrome():
    """Test two nodes with same values (should be palindrome)"""
    print("\n" + "=" * 60)
    print("Test: Two Nodes Same Values (5->5)")
    print("=" * 60)
    
    # Create: 5 -> 5
    node1 = Node(5)
    node2 = Node(5)
    node1.next = node2
    
    result = pallindrome_linked_list(node1)
    
    print(f"Linked list: 5 -> 5")
    print(f"Is palindrome: {result}")
    
    if result:
        print("✅ PASSED: Two nodes same values")
        return True
    else:
        print("❌ FAILED: Two nodes same values")
        return False


def test_two_nodes_different_not_palindrome():
    """Test two nodes with different values (should not be palindrome)"""
    print("\n" + "=" * 60)
    print("Test: Two Nodes Different Values (3->7)")
    print("=" * 60)
    
    # Create: 3 -> 7
    node1 = Node(3)
    node2 = Node(7)
    node1.next = node2
    
    result = pallindrome_linked_list(node1)
    
    print(f"Linked list: 3 -> 7")
    print(f"Is palindrome: {result}")
    
    if not result:
        print("✅ PASSED: Two nodes different values")
        return True
    else:
        print("❌ FAILED: Two nodes different values")
        return False


def test_empty_list_palindrome():
    """Test empty list (None head)"""
    print("\n" + "=" * 60)
    print("Test: Empty List (None)")
    print("=" * 60)
    
    result = pallindrome_linked_list(None)
    
    print(f"Linked list: None (empty)")
    print(f"Is palindrome: {result}")
    
    if result:
        print("✅ PASSED: Empty list palindrome")
        return True
    else:
        print("❌ FAILED: Empty list palindrome")
        return False


def test_negative_values_palindrome():
    """Test palindrome with negative values"""
    print("\n" + "=" * 60)
    print("Test: Palindrome with Negative Values (-1->-2->-3->-2->-1)")
    print("=" * 60)
    
    # Create palindrome with negative values: -1 -> -2 -> -3 -> -2 -> -1
    node1 = Node(-1)
    node2 = Node(-2)
    node3 = Node(-3)
    node4 = Node(-2)
    node5 = Node(-1)
    
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    
    result = pallindrome_linked_list(node1)
    
    print(f"Linked list: -1 -> -2 -> -3 -> -2 -> -1")
    print(f"Is palindrome: {result}")
    
    if result:
        print("✅ PASSED: Negative values palindrome")
        return True
    else:
        print("❌ FAILED: Negative values palindrome")
        return False


def test_mixed_positive_negative_palindrome():
    """Test palindrome with mixed positive and negative values"""
    print("\n" + "=" * 60)
    print("Test: Mixed Positive/Negative Palindrome (1->-2->3->-2->1)")
    print("=" * 60)
    
    # Create palindrome: 1 -> -2 -> 3 -> -2 -> 1
    node1 = Node(1)
    node2 = Node(-2)
    node3 = Node(3)
    node4 = Node(-2)
    node5 = Node(1)
    
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    
    result = pallindrome_linked_list(node1)
    
    print(f"Linked list: 1 -> -2 -> 3 -> -2 -> 1")
    print(f"Is palindrome: {result}")
    
    if result:
        print("✅ PASSED: Mixed positive/negative palindrome")
        return True
    else:
        print("❌ FAILED: Mixed positive/negative palindrome")
        return False


def test_zero_palindrome():
    """Test palindrome with zero values"""
    print("\n" + "=" * 60)
    print("Test: Palindrome with Zero Values (0->0->0)")
    print("=" * 60)
    
    # Create palindrome: 0 -> 0 -> 0
    node1 = Node(0)
    node2 = Node(0)
    node3 = Node(0)
    
    node1.next = node2
    node2.next = node3
    
    result = pallindrome_linked_list(node1)
    
    print(f"Linked list: 0 -> 0 -> 0")
    print(f"Is palindrome: {result}")
    
    if result:
        print("✅ PASSED: Zero values palindrome")
        return True
    else:
        print("❌ FAILED: Zero values palindrome")
        return False


def test_long_palindrome():
    """Test longer palindrome list"""
    print("\n" + "=" * 60)
    print("Test: Long Palindrome (1->2->3->4->5->4->3->2->1)")
    print("=" * 60)
    
    # Create long palindrome: 1 -> 2 -> 3 -> 4 -> 5 -> 4 -> 3 -> 2 -> 1
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    node5 = Node(5)
    node6 = Node(4)
    node7 = Node(3)
    node8 = Node(2)
    node9 = Node(1)
    
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    node5.next = node6
    node6.next = node7
    node7.next = node8
    node8.next = node9
    
    result = pallindrome_linked_list(node1)
    
    print(f"Linked list: 1->2->3->4->5->4->3->2->1 (9 nodes)")
    print(f"Is palindrome: {result}")
    
    if result:
        print("✅ PASSED: Long palindrome")
        return True
    else:
        print("❌ FAILED: Long palindrome")
        return False


def test_character_palindrome():
    """Test palindrome with character values"""
    print("\n" + "=" * 60)
    print("Test: Character Palindrome (a->b->c->b->a)")
    print("=" * 60)
    
    # Create character palindrome: a -> b -> c -> b -> a
    node1 = Node('a')
    node2 = Node('b')
    node3 = Node('c')
    node4 = Node('b')
    node5 = Node('a')
    
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    
    result = pallindrome_linked_list(node1)
    
    print(f"Linked list: a -> b -> c -> b -> a")
    print(f"Is palindrome: {result}")
    
    if result:
        print("✅ PASSED: Character palindrome")
        return True
    else:
        print("❌ FAILED: Character palindrome")
        return False


def test_mismatch_in_first_comparison():
    """Test case where first comparison fails"""
    print("\n" + "=" * 60)
    print("Test: Mismatch in First Comparison (1->2->3->4->5)")
    print("=" * 60)
    
    # Create non-palindrome where first comparison fails
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    node5 = Node(5)
    
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    
    result = pallindrome_linked_list(node1)
    
    print(f"Linked list: 1 -> 2 -> 3 -> 4 -> 5")
    print(f"Is palindrome: {result}")
    
    if not result:
        print("✅ PASSED: Mismatch in first comparison")
        return True
    else:
        print("❌ FAILED: Mismatch in first comparison")
        return False


def test_mismatch_in_last_comparison():
    """Test case where mismatch occurs in later comparison"""
    print("\n" + "=" * 60)
    print("Test: Mismatch in Last Comparison (1->2->3->2->3)")
    print("=" * 60)
    
    # Create non-palindrome where last comparison fails
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(2)
    node5 = Node(3)  # Should be 1 to be palindrome
    
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    
    result = pallindrome_linked_list(node1)
    
    print(f"Linked list: 1 -> 2 -> 3 -> 2 -> 3")
    print(f"Is palindrome: {result}")
    
    if not result:
        print("✅ PASSED: Mismatch in last comparison")
        return True
    else:
        print("❌ FAILED: Mismatch in last comparison")
        return False


# Helper function tests for find_middle and reverse_ll
def test_find_middle_odd_length():
    """Test find_middle with odd length list"""
    print("\n" + "=" * 60)
    print("Test: Find Middle (Odd Length)")
    print("=" * 60)
    
    # Create list: 1 -> 2 -> 3 -> 4 -> 5
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    node5 = Node(5)
    
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    
    middle_node = find_middle(node1)
    
    print(f"Linked list: 1 -> 2 -> 3 -> 4 -> 5")
    print(f"Middle node value: {middle_node.val}")
    print(f"Expected middle: 3")
    
    if middle_node.val == 3:
        print("✅ PASSED: Find middle (odd length)")
        return True
    else:
        print("❌ FAILED: Find middle (odd length)")
        return False


def test_find_middle_even_length():
    """Test find_middle with even length list"""
    print("\n" + "=" * 60)
    print("Test: Find Middle (Even Length)")
    print("=" * 60)
    
    # Create list: 1 -> 2 -> 3 -> 4
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    
    node1.next = node2
    node2.next = node3
    node3.next = node4
    
    middle_node = find_middle(node1)
    
    print(f"Linked list: 1 -> 2 -> 3 -> 4")
    print(f"Middle node value: {middle_node.val}")
    print(f"Expected middle: 3")
    
    if middle_node.val == 3:
        print("✅ PASSED: Find middle (even length)")
        return True
    else:
        print("❌ FAILED: Find middle (even length)")
        return False


def test_find_middle_single_node():
    """Test find_middle with single node"""
    print("\n" + "=" * 60)
    print("Test: Find Middle (Single Node)")
    print("=" * 60)
    
    # Create single node
    node1 = Node(42)
    
    middle_node = find_middle(node1)
    
    print(f"Linked list: 42 (single node)")
    print(f"Middle node value: {middle_node.val}")
    print(f"Expected middle: 42")
    
    if middle_node.val == 42:
        print("✅ PASSED: Find middle (single node)")
        return True
    else:
        print("❌ FAILED: Find middle (single node)")
        return False


def test_find_middle_empty_list():
    """Test find_middle with empty list"""
    print("\n" + "=" * 60)
    print("Test: Find Middle (Empty List)")
    print("=" * 60)
    
    middle_node = find_middle(None)
    
    print(f"Linked list: None (empty)")
    print(f"Middle node: {middle_node}")
    print(f"Expected: None")
    
    if middle_node is None:
        print("✅ PASSED: Find middle (empty list)")
        return True
    else:
        print("❌ FAILED: Find middle (empty list)")
        return False


def test_reverse_linked_list_basic():
    """Test reverse_ll with basic list"""
    print("\n" + "=" * 60)
    print("Test: Reverse Linked List (Basic)")
    print("=" * 60)
    
    # Create list: 1 -> 2 -> 3 -> 4
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    
    node1.next = node2
    node2.next = node3
    node3.next = node4
    
    # Reverse the list
    new_head = reverse_ll(node1)
    
    print(f"Original list: 1 -> 2 -> 3 -> 4")
    print(f"Reversed list values:")
    
    # Traverse reversed list
    current = new_head
    values = []
    while current:
        values.append(current.val)
        current = current.next
    
    expected_values = [4, 3, 2, 1]
    print(f"Expected: {expected_values}")
    print(f"Actual: {values}")
    
    if values == expected_values:
        print("✅ PASSED: Reverse linked list (basic)")
        return True
    else:
        print("❌ FAILED: Reverse linked list (basic)")
        return False


def test_reverse_linked_list_single_node():
    """Test reverse_ll with single node"""
    print("\n" + "=" * 60)
    print("Test: Reverse Linked List (Single Node)")
    print("=" * 60)
    
    # Create single node
    node1 = Node(42)
    
    # Reverse the list
    new_head = reverse_ll(node1)
    
    print(f"Original list: 42 (single node)")
    print(f"Reversed list values:")
    
    # Traverse reversed list
    current = new_head
    values = []
    while current:
        values.append(current.val)
        current = current.next
    
    expected_values = [42]
    print(f"Expected: {expected_values}")
    print(f"Actual: {values}")
    
    if values == expected_values and new_head == node1:
        print("✅ PASSED: Reverse linked list (single node)")
        return True
    else:
        print("❌ FAILED: Reverse linked list (single node)")
        return False


def test_reverse_linked_list_empty():
    """Test reverse_ll with empty list"""
    print("\n" + "=" * 60)
    print("Test: Reverse Linked List (Empty)")
    print("=" * 60)
    
    # Reverse empty list
    new_head = reverse_ll(None)
    
    print(f"Original list: None (empty)")
    print(f"Reversed list: {new_head}")
    print(f"Expected: None")
    
    if new_head is None:
        print("✅ PASSED: Reverse linked list (empty)")
        return True
    else:
        print("❌ FAILED: Reverse linked list (empty)")
        return False


def test_reverse_linked_list_two_nodes():
    """Test reverse_ll with two nodes"""
    print("\n" + "=" * 60)
    print("Test: Reverse Linked List (Two Nodes)")
    print("=" * 60)
    
    # Create list: 10 -> 20
    node1 = Node(10)
    node2 = Node(20)
    node1.next = node2
    
    # Reverse the list
    new_head = reverse_ll(node1)
    
    print(f"Original list: 10 -> 20")
    print(f"Reversed list values:")
    
    # Traverse reversed list
    current = new_head
    values = []
    while current:
        values.append(current.val)
        current = current.next
    
    expected_values = [20, 10]
    print(f"Expected: {expected_values}")
    print(f"Actual: {values}")
    
    if values == expected_values:
        print("✅ PASSED: Reverse linked list (two nodes)")
        return True
    else:
        print("❌ FAILED: Reverse linked list (two nodes)")
        return False


def test_middle_none_condition():
    """Test case that triggers middle is None condition"""
    print("\n" + "=" * 60)
    print("Test: Middle None Condition")
    print("=" * 60)
    
    # Create a list that would result in find_middle returning None
    # This is a theoretical edge case, but let's test it
    try:
        # Test with None (should be handled by empty list check)
        result = pallindrome_linked_list(None)
        print(f"Input: None")
        print(f"Result: {result}")
        print(f"Expected: True")
        
        if result == True:
            print("✅ PASSED: Middle none condition")
            return True
        else:
            print("❌ FAILED: Middle none condition")
            return False
    except Exception as e:
        print(f"❌ ERROR in middle none condition test: {str(e)}")
        return False


def test_main_block_execution():
    """Test the main block execution"""
    print("\n" + "=" * 60)
    print("Test: Main Block Execution")
    print("=" * 60)
    
    # Test that the module can be imported and run
    import subprocess
    import sys
    
    try:
        # Run the module as a script
        result = subprocess.run([sys.executable, 'LinkedList/LinkedListPalindrome.py'], 
                              capture_output=True, text=True, cwd='/Users/ishan/Desktop/git-repos/dsa-notes-and-solutions')
        
        print(f"Script output: {result.stdout.strip()}")
        print(f"Script return code: {result.returncode}")
        
        # The script should output "True"
        expected_output = "True"
        actual_output = result.stdout.strip()
        
        if result.returncode == 0 and actual_output == expected_output:
            print("✅ PASSED: Main block execution")
            return True
        else:
            print("❌ FAILED: Main block execution")
            return False
    except Exception as e:
        print(f"❌ ERROR in main block test: {str(e)}")
        return False


def run_all_tests():
    """Run all test cases and return overall result"""
    print("🚀 Starting LinkedList Palindrome Tests")
    print("=" * 80)
    
    test_functions = [
        # Main palindrome tests
        test_palindrome_odd_length,
        test_palindrome_even_length,
        test_not_palindrome_odd_length,
        test_not_palindrome_even_length,
        test_single_node_palindrome,
        test_two_nodes_same_palindrome,
        test_two_nodes_different_not_palindrome,
        test_empty_list_palindrome,
        test_negative_values_palindrome,
        test_mixed_positive_negative_palindrome,
        test_zero_palindrome,
        test_long_palindrome,
        test_character_palindrome,
        test_mismatch_in_first_comparison,
        test_mismatch_in_last_comparison,
        
        # Helper function tests
        test_find_middle_odd_length,
        test_find_middle_even_length,
        test_find_middle_single_node,
        test_find_middle_empty_list,
        test_reverse_linked_list_basic,
        test_reverse_linked_list_single_node,
        test_reverse_linked_list_empty,
        test_reverse_linked_list_two_nodes,
        
        # Additional coverage tests
        test_middle_none_condition
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
        print("\n✅ All LinkedList palindrome tests passed!")
        sys.exit(0)
    else:
        print("\n❌ Some tests failed!")
        sys.exit(1)

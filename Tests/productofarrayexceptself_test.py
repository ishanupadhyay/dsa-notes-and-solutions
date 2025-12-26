#!/usr/bin/env python3
"""
Test file for productofarrayexceptself.py
Tests the ProductArray class with various test cases
"""

import sys
import os

# Add the current directory to Python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from Arrays.productofarrayexceptself import ProductArray


def test_product_array():
    """Test the ProductArray class with various test cases"""
    
    test_cases = [
        # Test case 1: Basic case
        {
            'input': [1, 2, 3, 4],
            'expected': [24, 12, 8, 6],
            'description': "Basic case: [1, 2, 3, 4] -> [24, 12, 8, 6]"
        },
        # Test case 2: Contains zero
        {
            'input': [0, 1, 2],
            'expected': [2, 0, 0],
            'description': "Zero case: [0, 1, 2] -> [2, 0, 0]"
        },
        # Test case 3: Single element
        {
            'input': [5],
            'expected': [1],
            'description': "Single element: [5] -> [1]"
        },
        # Test case 4: Two elements
        {
            'input': [3, 7],
            'expected': [7, 3],
            'description': "Two elements: [3, 7] -> [7, 3]"
        },
        # Test case 5: Larger numbers
        {
            'input': [2, 3, 4, 5],
            'expected': [60, 40, 30, 24],
            'description': "Larger numbers: [2, 3, 4, 5] -> [60, 40, 30, 24]"
        },
        # Test case 6: Mixed positive/negative (if supported)
        {
            'input': [-1, 3, 4],
            'expected': [12, -4, -3],
            'description': "Negative numbers: [-1, 3, 4] -> [12, -4, -3]"
        }
    ]
    
    print("=" * 60)
    print("Testing ProductArray Class")
    print("=" * 60)
    
    all_passed = True
    passed_tests = 0
    failed_tests = 0
    
    for i, test_case in enumerate(test_cases, 1):
        print(f"\nTest {i}: {test_case['description']}")
        
        try:
            # Create instance and set numbers directly
            product_array = ProductArray()
            product_array.numbers = test_case['input'].copy()
            
            # Get result
            result = product_array.product_of_array()
            
            # Check if result matches expected
            if result == test_case['expected']:
                print(f"  ✅ PASSED: {result}")
                passed_tests += 1
            else:
                print(f"  ❌ FAILED: Expected {test_case['expected']}, got {result}")
                failed_tests += 1
                all_passed = False
                
        except Exception as e:
            print(f"  ❌ ERROR: {str(e)}")
            failed_tests += 1
            all_passed = False
    
    print("\n" + "=" * 60)
    print("Test Summary")
    print("=" * 60)
    print(f"Total tests: {len(test_cases)}")
    print(f"Passed: {passed_tests}")
    print(f"Failed: {failed_tests}")
    
    if all_passed:
        print("🎉 All tests passed!")
        return True
    else:
        print("💥 Some tests failed!")
        return False


def test_manual_input():
    """Test with manual input (original functionality)"""
    print("\n" + "=" * 60)
    print("Manual Input Test")
    print("=" * 60)
    print("This test uses the original interactive input functionality.")
    print("Enter your test case when prompted.")
    
    try:
        n = int(input("\nEnter the number of elements: "))
        productarray = ProductArray()
        productarray.read_array(n)
        result = productarray.product_of_array()
        print(f"Result: {result}")
        return True
    except Exception as e:
        print(f"Error in manual test: {e}")
        return False


if __name__ == "__main__":
    # Run automated tests
    test_result = test_product_array()
    
    # Optionally run manual test (commented out for CI/CD)
    # test_manual_input()
    
    # Exit with appropriate code
    if test_result:
        print("\n✅ All automated tests passed successfully!")
        sys.exit(0)
    else:
        print("\n❌ Some tests failed!")
        sys.exit(1)

# DSA Notes and Solutions

[![CI Pipeline](https://github.com/ishanupadhyay/dsa-notes-and-solutions/workflows/CI%20Pipeline/badge.svg)](https://github.com/ishanupadhyay/dsa-notes-and-solutions/actions)
[![codecov](https://codecov.io/gh/ishanupadhyay/dsa-notes-and-solutions/graph/badge.svg?token=UKAMPEGK1L)](https://codecov.io/gh/ishanupadhyay/dsa-notes-and-solutions)
[![SonarCloud](https://sonarcloud.io/api/project_badges?project=ishanupadhyay_dsa-notes-and-solutions&metric=alert_status)](https://sonarcloud.io/dashboard?id=ishanupadhyay_dsa-notes-and-solutions)

A comprehensive collection of Data Structures and Algorithms (DSA) problems with detailed solutions and explanations, designed to help with coding interview preparation.

## 📋 Table of Contents

- [About](#about)
- [Project Structure](#project-structure)
- [Array Problems](#array-problems)
- [LinkedList Problems](#linkedlist-problems)
- [Getting Started](#getting-started)
- [Running Solutions](#running-solutions)
- [Testing](#testing)
- [Code Quality](#code-quality)
- [Contributing](#contributing)
- [Future Enhancements](#future-enhancements)

## 🎯 About

This repository contains well-documented solutions to common DSA problems frequently asked in technical interviews. Each solution includes:

- Clean, readable Python implementations
- Time and space complexity analysis
- Algorithm explanations
- Interactive input support for practice

**No external dependencies required** - Pure Python implementations using only built-in libraries.

## 📁 Project Structure

```
dsa-notes-and-solutions/
├── Arrays/                     # Array-based problems
│   ├── twosum.py              # Two Sum problem
│   ├── findmax.py             # Find maximum element
│   ├── reverse_inplace.py     # Reverse array in-place
│   ├── remove_duplicates_inplace.py  # Remove duplicates
│   ├── rotate_array_k_steps_to_right.py  # Array rotation
│   ├── Longestsubarray.py     # Longest subarray problem
│   ├── maxsumsubarray.py      # Maximum subarray sum (Kadane's)
│   ├── longestconsecutivesequence.py  # Longest consecutive sequence
│   ├── mergetwosortedarrays.py # Merge sorted arrays
│   ├── productofarrayexceptself.py  # Product except self
│   └── __init__.py
├── LinkedList/                # Linked List problems
│   ├── node.py               # Node class implementation
│   ├── TraverseLinkedList.py # Linked list traversal
│   └── __init__.py
├── Tests/                     # Test files
│   ├── productofarrayexceptself_test.py
│   └── traverselinkedlist_test.py
├── .github/workflows/         # CI/CD configuration
├── requirements.txt           # Dependencies (none required)
└── README.md                 # This file
```

## 📊 Array Problems

### 1. Two Sum (`twosum.py`)
**Problem**: Find two numbers in an array that add up to a target value.

**Algorithm**: Hash Map approach
- **Time Complexity**: O(n)
- **Space Complexity**: O(n)
- **Key Concept**: Use hash map to store complements for O(1) lookup

### 2. Find Maximum (`findmax.py`)
**Problem**: Find the maximum element in an array.

**Algorithm**: Linear scan
- **Time Complexity**: O(n)
- **Space Complexity**: O(1)
- **Key Concept**: Single pass comparison

### 3. Reverse In-Place (`reverse_inplace.py`)
**Problem**: Reverse an array without using extra space.

**Algorithm**: Two-pointer technique
- **Time Complexity**: O(n)
- **Space Complexity**: O(1)
- **Key Concept**: Swap elements from both ends

### 4. Remove Duplicates In-Place (`remove_duplicates_inplace.py`)
**Problem**: Remove duplicates from a sorted array in-place.

**Algorithm**: Two-pointer approach
- **Time Complexity**: O(n)
- **Space Complexity**: O(1)
- **Key Concept**: Fast and slow pointer technique

### 5. Rotate Array (`rotate_array_k_steps_to_right.py`)
**Problem**: Rotate an array to the right by k steps.

**Algorithm**: Reversal algorithm
- **Time Complexity**: O(n)
- **Space Complexity**: O(1)
- **Key Concept**: Three reversals technique

### 6. Longest Subarray (`Longestsubarray.py`)
**Problem**: Find the longest subarray with specific properties.

**Algorithm**: Sliding window or dynamic programming
- **Time Complexity**: O(n)
- **Space Complexity**: O(1) or O(n)
- **Key Concept**: Efficient subarray tracking

### 7. Maximum Subarray Sum (`maxsumsubarray.py`)
**Problem**: Find the contiguous subarray with the largest sum.

**Algorithm**: Kadane's Algorithm
- **Time Complexity**: O(n)
- **Space Complexity**: O(1)
- **Key Concept**: Dynamic programming with running maximum

### 8. Longest Consecutive Sequence (`longestconsecutivesequence.py`)
**Problem**: Find the length of the longest consecutive sequence.

**Algorithm**: Hash Set approach
- **Time Complexity**: O(n)
- **Space Complexity**: O(n)
- **Key Concept**: Find sequence starts and extend

### 9. Merge Two Sorted Arrays (`mergetwosortedarrays.py`)
**Problem**: Merge two sorted arrays into one sorted array.

**Algorithm**: Two-pointer technique
- **Time Complexity**: O(m + n)
- **Space Complexity**: O(1) or O(m + n)
- **Key Concept**: Merge from the end to avoid overwriting

### 10. Product Except Self (`productofarrayexceptself.py`)
**Problem**: Return an array where each element is the product of all other elements.

**Algorithm**: Prefix and suffix products
- **Time Complexity**: O(n)
- **Space Complexity**: O(1) (excluding output array)
- **Key Concept**: Two-pass calculation without division

## 🔗 LinkedList Problems

### 1. Node Implementation (`node.py`)
**Problem**: Basic node class for linked list operations.

**Features**:
- Simple node with value and next pointer
- String representation for debugging
- Foundation for linked list operations

### 2. Traverse LinkedList (`TraverseLinkedList.py`)
**Problem**: Traverse and display linked list elements.

**Algorithm**: Iterative traversal
- **Time Complexity**: O(n)
- **Space Complexity**: O(1)
- **Key Concept**: Node-by-node iteration

**Test Coverage**: Comprehensive test suite (`traverselinkedlist_test.py`) with 8 test cases covering:
- Basic traversal with multiple nodes
- Single node edge case
- Empty list (None) handling
- Duplicate values in list
- Negative values
- Mixed positive/negative/zero values
- Large list performance (10+ nodes)
- Node class string representation

## 🚀 Getting Started

### Prerequisites
- Python 3.6 or higher
- No external dependencies required

### Installation
1. Clone the repository:
```bash
git clone <repository-url>
cd dsa-notes-and-solutions
```

2. No additional installation required - all solutions use Python standard library.

## 🏃‍♂️ Running Solutions

Each solution supports interactive input. Run any problem using:

```bash
# Navigate to the problem directory
cd Arrays  # or LinkedList

# Run the specific problem
python twosum.py           # For Two Sum problem
python findmax.py          # For Find Maximum
# ... and so on
```

### Input Format
Most solutions expect input in the following format:
1. First line: Number of elements (n)
2. Next n lines: Array elements
3. Additional lines: Target values or parameters as needed

### Example Usage
```bash
$ python twosum.py
5
1
4
5
6
9
8
Output: [3, 4]  # Indices of numbers that sum to 8
```

## 🧪 Testing

### Running Tests
```bash
# Run all tests
cd Tests

# Test Array problems
python productofarrayexceptself_test.py

# Test LinkedList problems
python traverselinkedlist_test.py
```

### Test Coverage
- **Current**: Tests for `productofarrayexceptself.py` and `TraverseLinkedList.py`
- **Array Problems**: Product Except Self with comprehensive test cases
- **LinkedList Problems**: LinkedList traversal with 8 different test scenarios including:
  - Basic linked list traversal
  - Single node edge case
  - Empty list handling
  - Duplicate values
  - Negative values
  - Mixed positive/negative/zero values
  - Large list performance
  - Node string representation
- **Future**: Expanding test coverage for all problems

### Test Features
- Automated test cases with expected outputs
- Manual input testing capability
- Comprehensive test reporting

## 🔍 Code Quality

This repository integrates automated code quality analysis through **SonarCloud** to ensure high standards of code quality, security, and maintainability.

### 🔐 SonarCloud Integration

- **Quality Gates**: Automated checks for code quality standards
- **Security Analysis**: Detection of potential security vulnerabilities  
- **Technical Debt**: Identification and tracking of code improvements
- **Coverage Integration**: Combined analysis with test coverage metrics
- **Pull Request Analysis**: Automated quality checks on every PR

### 📊 Quality Metrics Monitored

- **Code Coverage**: Test coverage percentage tracking
- **Maintainability**: Code complexity and readability analysis
- **Reliability**: Bug detection and code quality scoring
- **Security**: Vulnerability scanning and security hotspot detection
- **Duplicated Code**: Detection of code duplication patterns

### 🚀 CI/CD Integration

The SonarCloud analysis runs automatically as part of our GitHub Actions CI pipeline:
- **On Pull Requests**: Quality checks before merging
- **On Main Branch**: Comprehensive analysis on successful merges
- **Quality Gates**: Ensures code meets defined quality standards before deployment

### 📈 Quality Standards

- **Maintainability Rating**: A or higher
- **Reliability Rating**: A or higher  
- **Security Rating**: A or higher
- **Test Coverage**: >80% coverage target
- **Technical Debt**: <5% of development time

### 🔧 Setup Instructions

To set up SonarCloud for your own fork:

1. **Create SonarCloud Account**: Sign up at [sonarcloud.io](https://sonarcloud.io)
2. **Import GitHub Repository**: Connect your GitHub account and import this repository
3. **Generate Token**: Create a new project and generate a SonarCloud token
4. **Configure GitHub Secrets**: Add `SONAR_TOKEN` to your repository secrets
5. **Update Configuration**: Replace `your-github-username` in `sonar-project.properties` with your actual username

### 📋 Quality Reports

Quality reports are automatically generated and available in:
- **SonarCloud Dashboard**: Comprehensive project analysis
- **Pull Request Comments**: Inline quality feedback
- **GitHub Checks**: Integration with GitHub's native checks system

*This ensures that all code contributions maintain the highest standards of quality and security.*

## 🤝 Contributing

We welcome contributions! Here's how you can help:

### Adding New Problems
1. Create a new Python file in the appropriate directory (`Arrays/` or `LinkedList/`)
2. Include:
   - Clear problem description in comments
   - Efficient algorithm implementation
   - Time and space complexity analysis
   - Interactive input support
3. Add corresponding test file if applicable

### Improving Existing Solutions
- Optimize algorithms for better performance
- Add more detailed explanations
- Improve code readability and documentation
- Add edge case handling

### Code Standards
- Follow PEP 8 Python style guidelines
- Add comprehensive comments explaining the algorithm
- Include time/space complexity in comments
- Make solutions interactive for practice

## 🔮 Future Enhancements

### Planned Features
- [ ] **More Data Structures**: Trees, Graphs, Hash Tables
- [ ] **Advanced Algorithms**: Dynamic Programming, Greedy Algorithms
- [x] **Comprehensive Test Suite**: Unit tests for all problems ✅ *In Progress*
  - ✅ Product Except Self test implemented
  - ✅ LinkedList Traversal test with 8 comprehensive test cases
  - [ ] Expand test coverage to remaining Array problems
- [ ] **Performance Benchmarks**: Timing and memory usage analysis
- [ ] **Visualizations**: Algorithm animations and diagrams
- [ ] **Interview Question Categories**: Problems grouped by company
- [ ] **Solution Variations**: Multiple approaches for the same problem

### Data Structures Roadmap
- [ ] Binary Trees
- [ ] Binary Search Trees
- [ ] Graphs (BFS, DFS)
- [ ] Heaps and Priority Queues
- [ ] Stacks and Queues
- [ ] Tries

### Algorithm Categories
- [ ] Sorting Algorithms
- [ ] Searching Algorithms
- [ ] Dynamic Programming
- [ ] Greedy Algorithms
- [ ] Divide and Conquer
- [ ] Backtracking

## 📞 Support

If you encounter any issues or have questions:
1. Check the existing test files for usage examples
2. Review the algorithm comments in each file
3. Create an issue for bugs or feature requests

## 📄 License

This project is open source and available under the MIT License.

---

## 🏗️ Architecture & Workflow

### 📊 UML Diagrams

#### 1. Class Diagram - Core Components

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                                 CORE CLASSES                                │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  ┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐        │
│  │    TwoSum       │    │  ProductArray   │    │      Node       │        │
│  ├─────────────────┤    ├─────────────────┤    ├─────────────────┤        │
│  │ - numbers[]     │    │ - numbers[]     │    │ - val           │        │
│  ├─────────────────┤    ├─────────────────┤    │ - next: Node    │        │
│  │ + read_array()  │    │ + read_array()  │    ├─────────────────┤        │
│  │ + two_sum()     │    │ + product_      │    │ + __repr__()    │        │
│  └─────────────────┘    │   of_array()    │    └─────────────────┘        │
│                         └─────────────────┘             │                  │
│         ┌─────────────────────────┬─────────────────────┘                  │
│         │                         │                                          │
│  ┌──────▼──────────┐    ┌─────────▼──────────┐                              │
│  │   Test Suite    │    │   LinkedList Ops   │                              │
│  ├─────────────────┤    ├────────────────────┤                              │
│  │ + test cases    │    │ + traveselinkedlist│                              │
│  │ + assertions    │    │ + node creation    │                              │
│  │ + validation    │    └────────────────────┘                              │
│  └─────────────────┘                                                       │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

#### 2. Activity Diagram - Algorithm Workflow

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                           ALGORITHM EXECUTION FLOW                          │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  ┌─────────────┐    ┌─────────────┐    ┌─────────────┐    ┌─────────────┐ │
│  │ Start User  │───▶│ Read Input  │───▶│ Validate    │───▶│ Execute     │ │
│  │ Interaction │    │ (n, array,  │    │ Input       │    │ Algorithm   │ │
│  └─────────────┘    │ params)     │    │             │    │             │ │
│                     └─────────────┘    └─────────────┘    └──────┬────────┘ │
│                                                                     │         │
│                               ┌─────────────────────────────────────┘         │
│                               │                                             │
│  ┌─────────────┐    ┌─────────▼──────────┐    ┌─────────────┐              │
│  │ Show Result │◀───│ Format & Display  │◀───│ Test        │              │
│  │             │    │ Output            │    │ Validation  │              │
│  └─────────────┘    └───────────────────┘    └─────────────┘              │
│                                │                    │                       │
│                                ▼                    ▼                       │
│                       ┌─────────────────┐   ┌─────────────┐                 │
│                       │ Automated Tests │   │ CI/CD       │                 │
│                       │ (Optional)      │   │ Pipeline    │                 │
│                       └─────────────────┘   └─────────────┘                 │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

#### 3. Component Diagram - Package Architecture

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                             PACKAGE STRUCTURE                               │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  ┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐        │
│  │   Arrays/       │    │  LinkedList/    │    │     Tests/      │        │
│  │   Package       │    │   Package       │    │   Package       │        │
│  ├─────────────────┤    ├─────────────────┤    ├─────────────────┤        │
│  │                 │    │                 │    │                 │        │
│  │ • twosum.py     │    │ • node.py       │    │ • *_test.py     │        │
│  │ • findmax.py    │    │ • traverse.py   │    │ • test_runner   │        │
│  │ • reverse.py    │    │ • reverse.py    │    │ • validation    │        │
│  │ • duplicates.py │    │                 │    │                 │        │
│  │ • rotate.py     │    │                 │    │                 │        │
│  │ • longestsub.py │    │                 │    │                 │        │
│  │ • maxsum.py     │    │                 │    │                 │        │
│  │ • consecutive.py│    │                 │    │                 │        │
│  │ • merge.py      │    │                 │    │                 │        │
│  │ • product.py    │    │                 │    │                 │        │
│  │                 │    │                 │    │                 │        │
│  └─────────────────┘    └─────────────────┘    └─────────────────┘        │
│           │                       │                       │               │
│           └───────────────────────┼───────────────────────┘               │
│                                   │                                       │
│                        ┌─────────────────┐                                 │
│                        │  Core Python   │                                 │
│                        │   Runtime      │                                 │
│                        │  (3.6+ only)   │                                 │
│                        └─────────────────┘                                 │
│                                                                             │
│  ┌─────────────────────────────────────────────────────────────────────────┐
│  │                    CI/CD Pipeline (.github/workflows/)                   │
│  │  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐    │
│  │  │   GitHub    │▶ │   Run Tests │▶ │ Validate    │▶ │    Report   │    │
│  │  │  Trigger    │  │   (pytest)  │  │ Results     │  │   Status    │    │
│  │  └─────────────┘  └─────────────┘  └─────────────┘  └─────────────┘    │
│  └─────────────────────────────────────────────────────────────────────────┘
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

#### 4. Data Flow Diagram - Input/Output Process

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                             DATA FLOW PROCESS                               │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  User Input ───┐                                                                │
│  ┌─────────────┐│                                                                │
│  │ n (size)    ││                                                                │
│  │ elements[]  ││                                                                │
│  │ target/     ││                                                                │
│  │ parameters  ││                                                                │
│  └─────────────┘│                                                                │
│                ▼                                                                 │
│  ┌─────────────────────────────────────────────────────────────────────────┐ │
│  │                      Algorithm Classes                                   │ │
│  │  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐    │ │
│  │  │ read_array()│  │  process()  │  │ validate()  │  │  output()   │    │ │
│  │  └─────────────┘  └─────────────┘  └─────────────┘  └─────────────┘    │ │
│  └─────────────────────────────────────────────────────────────────────────┘ │
│                ▼                                                                 │
│  ┌─────────────────────────────────────────────────────────────────────────┐ │
│  │                         Results                                          │ │
│  │  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐    │ │
│  │  │  Indices    │  │  Values     │  │  Modified   │  │  Success/   │    │ │
│  │  │             │  │             │  │  Array      │  │  Error      │    │ │
│  │  └─────────────┘  └─────────────┘  └─────────────┘  └─────────────┘    │ │
│  └─────────────────────────────────────────────────────────────────────────┘ │
│                                                                             │
│                           Validation & Testing                              │
│  ┌─────────────────────────────────────────────────────────────────────────┐ │
│  │  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐    │ │
│  │  │ Unit Tests  │  │ Integration │  │ Performance │  │ Code        │    │ │
│  │  │             │  │ Tests       │  │ Tests       │  │ Coverage    │    │ │
│  │  └─────────────┘  └─────────────┘  └─────────────┘  └─────────────┘    │ │
│  └─────────────────────────────────────────────────────────────────────────┘ │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

### 🔄 Workflow Explanation

#### Algorithm Execution Flow:
1. **Input Phase**: User provides input through interactive prompts
   - Array size and elements
   - Target values or parameters
   - Algorithm-specific inputs

2. **Processing Phase**: Algorithm classes process the data
   - Data validation and preprocessing
   - Algorithm execution with optimized complexity
   - Result computation and storage

3. **Output Phase**: Results are displayed in user-friendly format
   - Console output with clear formatting
   - Return values for integration
   - Error handling and edge cases

#### Testing Architecture:
- **Automated Tests**: Comprehensive test suites with multiple test cases
- **Manual Testing**: Interactive input validation
- **CI/CD Integration**: GitHub Actions pipeline for continuous testing
- **Coverage**: Unit tests, integration tests, and performance validation

#### Key Design Patterns:
- **Consistent Interface**: All algorithms follow similar input/output patterns
- **Modular Design**: Clear separation between data structures and algorithms
- **Test-Driven**: Comprehensive test coverage for reliability
- **Documentation**: Inline comments and complexity analysis

**Happy Coding! 🎉**

*Master the fundamentals, practice consistently, and ace your coding interviews!*

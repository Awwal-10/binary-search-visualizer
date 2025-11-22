# Binary Search Algorithm Visualizer

## Demo
*Live demo available at this Hugging Face Space*

## Problem Breakdown & Computational Thinking

### Algorithm Choice
I chose **Binary Search** because it's an efficient O(log n) algorithm that demonstrates the "divide and conquer" approach perfectly. It's ideal for visualization as each step clearly shows the search space halving.

### Decomposition
1. Take sorted array and target value as input
2. Initialize low pointer to 0 and high pointer to len(array)-1
3. Calculate mid index: (low + high) // 2
4. Compare array[mid] with target value
5. If equal → target found, return success
6. If target > array[mid] → search right half (low = mid + 1)
7. If target < array[mid] → search left half (high = mid - 1)
8. Repeat steps 3-7 until found or search space exhausted

### Pattern Recognition
- The search space halves each iteration (logarithmic behavior)
- Repeated compare-and-divide pattern
- Consistent O(log n) time complexity regardless of data size

### Abstraction
- **User sees**: Color-coded array visualization, step-by-step explanations, current low/high/mid pointers, comparison results
- **Hidden**: Internal index calculations, loop mechanics, temporary variables

### Algorithm Design
**Input**: Sorted comma-separated numbers, target integer  

**Process**: 

WHILE low <= high:

mid = (low + high) // 2

IF array[mid] == target: RETURN FOUND

ELSE IF array[mid] < target: low = mid + 1

ELSE: high = mid - 1

RETURN NOT FOUND

**Output**: Visual step-by-step demonstration with color-coded array and final result

### Flowchart
Start → Input sorted array & target → Initialize low=0, high=len-1

↓

While low <= high

↓

mid = (low + high) // 2

↓

Compare array[mid] with target

↓

If equal → Found! → End

↓

If target > array[mid] → low = mid + 1

↓

If target < array[mid] → high = mid - 1

↓

If low > high → Not Found → End


## Steps to Run
1. Enter sorted numbers (e.g., "1,3,5,7,9") in the first box
2. Enter target number (e.g., "5") in the second box  
3. View the step-by-step visualization

## Testing & Verification
Thoroughly tested with normal cases, edge cases, error handling, and large arrays. All tests passed.

## Author & Acknowledgment
**Awwal** - CISC 121 Project

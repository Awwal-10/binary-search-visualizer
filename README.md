# Binary Search Algorithm Visualizer

## Live Demo
[My Hugging Face Space](https://huggingface.co/spaces/Awwal-10/binary-search-visualizer)

[My Github Repo should go here](link)


## 📸 Demo Screenshots
## 🎥 Demo Videos (Hosted on Imgur)

### Test 1: Simple Example
[![Watch](https://img.shields.io/badge/▶️_Watch_Simple_Example-blue)](https://imgur.com/a/klnbAlb)

### Test 2: Best Case  
[![Watch](https://img.shields.io/badge/▶️_Watch_Best_Case-green)](https://imgur.com/a/FZdWvme)

### Test 3: Average Case
[![Watch](https://img.shields.io/badge/▶️_Watch_Worst_Case-orange)](https://imgur.com/a/AVtmYLv)

### Test 4: Worst Case
[![Watch](https://img.shields.io/badge/▶️_Watch_Worst_Case-orange)](https://imgur.com/a/Bw3Sgac)

### Test 5: Custom Input
[![Watch](https://img.shields.io/badge/▶️_Watch_Custom_Input-purple)](https://imgur.com/a/PiFwcAE)

### Test 6: Unsorted Error
[![Watch](https://img.shields.io/badge/▶️_Watch_Unsorted_Error-red)](https://imgur.com/a/pwbiigG)

### Test 7: Empty Error  
[![Watch](https://img.shields.io/badge/▶️_Watch_Empty_Error-red)](https://imgur.com/a/GcSbpdd)
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

## 🛠️ Features & Usage

### Two Learning Modes:
1. **🚀 Quick Start**: Pre-made examples to learn from:
   - *Simple Example*: Easy to follow demonstration
   - *Best Case*: Target in middle (1 step)
   - *Average Case*: Target exists in array
   - *Worst Case*: Target not found

2. **🎯 Custom Search**: Enter your own sorted array and target

### How to Use:
1. Select an example from **Quick Start** OR check **"Use my own numbers"**
2. Enter sorted numbers (comma-separated) and target
3. Click **"Run Binary Search"** to see the algorithm work step-by-step
4. Watch the color-coded visualization and learn how binary search works

## 🚀 Deployment

### Local Setup

git clone https://github.com/Awwal-10/binary-search-visualizer.git
cd binary-search-visualizer
pip install -r requirements.txt
python app.py

### Author Acknoledgement
Awwal Ahmed - CISC 121 Project

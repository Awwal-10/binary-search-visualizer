# binary-search-project/app.py
# binary-search-project/app.py

import gradio as gr

def binary_search_steps(arr, target):
    """
    Binary search implementation that tracks each step of the algorithm.
    Returns both the search steps and whether the target was found.
    """
    steps = []  # Stores each step's state for visualization
    low = 0  # Starting index of current search space
    high = len(arr) - 1  # Ending index of current search space

    # Continue searching while there are elements to check
    while low <= high:
        mid = (low + high) // 2  # Calculate middle index using integer division
        # Record current state for visualization
        steps.append({
            "low": low,
            "high": high,
            "mid": mid,
            "mid_value": arr[mid]  # Value being compared with target
        })
        # Compare middle element with target
        if arr[mid] == target:
            return steps, True  # Target found at middle index
        # Target is in right half, so adjust search space
        elif arr[mid] < target:
            low = mid + 1  # Discard left half including mid
        # Target is in left half, so adjust search space  
        else:
            high = mid - 1  # Discard right half including mid
    return steps, False  # Target not found in array

def run_binary_search(array_input, target_input):
    """
    Processes user input, validates data, runs binary search, and formats output.
    Handles error cases and creates visual step-by-step explanation.
    """
    # Convert comma-separated string to list of integers
    try:
        arr = [int(x.strip()) for x in array_input.split(",")]
    except:
        return "Error: Please enter numbers separated by commas (e.g., '1,2,3').", ""

    # Validate input array
    if not arr:
        return "Error: The array cannot be empty.", ""
    # Binary search requires sorted input for correct operation
    if arr != sorted(arr):
        return "Error: Please enter a sorted array in ascending order.", ""

    # Validate target input
    try:
        target = int(target_input)
    except:
        return "Error: Please enter a single integer for the target.", ""

    # Execute binary search algorithm
    steps, found = binary_search_steps(arr, target)

    # Generate visual step-by-step explanation
    visual_output = ""
    for i, step in enumerate(steps):
        visual_output += f"<div style='margin-bottom: 20px; padding: 10px; border: 1px solid #ccc; border-radius: 5px;'>"
        visual_output += f"<h3>🎯 Step {i+1}</h3>"
        
        # Create visual array representation with color coding
        visual_output += "<div style='display: flex; gap: 5px; margin: 10px 0;'>"
        for idx, value in enumerate(arr):
            style = "padding: 8px 12px; border: 2px solid; border-radius: 4px; font-weight: bold;"
            # Color coding helps users understand algorithm state:
            if idx == step['mid']:
                style += " background: #4CAF50; color: white; border-color: #45a049;"  # Green: current comparison element
            elif idx == step['low']:
                style += " background: #2196F3; color: white; border-color: #0b7dda;"  # Blue: search space lower bound
            elif idx == step['high']:
                style += " background: #ff9800; color: white; border-color: #e68a00;"  # Orange: search space upper bound
            else:
                style += " background: #f1f1f1; border-color: #ddd;"  # Gray: elements outside current search space
            
            visual_output += f"<div style='{style}'>{value}</div>"
        visual_output += "</div>"
        
        # Explain what's happening in this step
        visual_output += f"<p><b>Search Space:</b> indices {step['low']} to {step['high']}</p>"
        visual_output += f"<p><b>Checking Middle:</b> arr[{step['mid']}] = {step['mid_value']}</p>"
        visual_output += f"<p><b>Comparison:</b> Is {step['mid_value']} == {target}? <span style='color: {'green' if step['mid_value'] == target else 'red'}'>{'✅ Match found!' if step['mid_value'] == target else '❌ No match'}</span></p>"
        
        # Explain algorithm decision
        if step['mid_value'] == target:
            visual_output += "<p><b>Algorithm Decision:</b> Target found! Search complete.</p>"
        elif step['mid_value'] < target:
            visual_output += "<p><b>Algorithm Decision:</b> Target is larger, so search right half (low = mid + 1)</p>"
        else:
            visual_output += "<p><b>Algorithm Decision:</b> Target is smaller, so search left half (high = mid - 1)</p>"
            
        visual_output += "</div>"

    # Display final result
    result = f"<h2 style='color: {'green' if found else 'red'}; padding: 10px; text-align: center;'>🎊 Final Result: Target {target} was {'FOUND! ✅' if found else 'NOT FOUND ❌'}</h2>"
    return result, visual_output

# Create Gradio interface for user interaction
demo = gr.Interface(
    fn=run_binary_search,  # Function to call when user clicks button
    inputs=[
        gr.Textbox(label="Sorted Array", value="1, 3, 5, 7, 9, 11, 13", placeholder="Enter numbers separated by commas..."),
        gr.Textbox(label="Target Number", value="7", placeholder="Enter the number to find...")
    ],
    outputs=[
        gr.HTML(label="Final Result"),  # Use HTML for rich formatting
        gr.HTML(label="Step-by-Step Visualization")  # Show algorithm progression
    ],
    title="Binary Search Algorithm Visualizer",
    description="Enter a sorted list of numbers and a target to see how the Binary Search algorithm works step-by-step. The algorithm has O(log n) time complexity because it halves the search space each iteration."
)

# Launch the web application
if __name__ == "__main__":
    demo.launch(share=True)  # share=True creates public URL for easy access

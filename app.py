# binary-search-project/app.py

import gradio as gr

def binary_search_steps(arr, target):
    """
    Performs binary search on a sorted list and returns a list of each step.
    """
    steps = []  # This will store the state at each step
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        # Save the current state (low, high, mid, value at mid)
        steps.append({
            "low": low,
            "high": high,
            "mid": mid,
            "mid_value": arr[mid]
        })
        # Check if we found the target
        if arr[mid] == target:
            return steps, True  # Found it!
        # If target is greater, ignore left half
        elif arr[mid] < target:
            low = mid + 1
        # If target is smaller, ignore right half
        else:
            high = mid - 1
    return steps, False  # Target is not in the array

def run_binary_search(array_input, target_input):
    """
    Takes input from the Gradio UI, runs the search, and formats the output.
    """
    # Convert the string input "1,2,3" into a list of integers [1,2,3]
    try:
        arr = [int(x.strip()) for x in array_input.split(",")]
    except:
        return "Error: Please enter numbers separated by commas (e.g., '1,2,3').", ""

    # Basic validation
    if not arr:
        return "Error: The array cannot be empty.", ""
    if arr != sorted(arr):
        return "Error: Please enter a sorted array in ascending order.", ""

    try:
        target = int(target_input)
    except:
        return "Error: Please enter a single integer for the target.", ""

    # Run the binary search algorithm
    steps, found = binary_search_steps(arr, target)

    # Create VISUAL output with HTML styling
    visual_output = ""
    for i, step in enumerate(steps):
        visual_output += f"<div style='margin-bottom: 20px; padding: 10px; border: 1px solid #ccc; border-radius: 5px;'>"
        visual_output += f"<h3>🎯 Step {i+1}</h3>"
        
        # Create visual array representation
        visual_output += "<div style='display: flex; gap: 5px; margin: 10px 0;'>"
        for idx, value in enumerate(arr):
            style = "padding: 8px 12px; border: 2px solid; border-radius: 4px; font-weight: bold;"
            if idx == step['mid']:
                style += " background: #4CAF50; color: white; border-color: #45a049;"  # Green for mid
            elif idx == step['low']:
                style += " background: #2196F3; color: white; border-color: #0b7dda;"  # Blue for low
            elif idx == step['high']:
                style += " background: #ff9800; color: white; border-color: #e68a00;"  # Orange for high
            else:
                style += " background: #f1f1f1; border-color: #ddd;"
            
            visual_output += f"<div style='{style}'>{value}</div>"
        visual_output += "</div>"
        
        # Add step details
        visual_output += f"<p><b>Low:</b> index {step['low']} | <b>High:</b> index {step['high']} | <b>Mid:</b> index {step['mid']}</p>"
        visual_output += f"<p><b>Checking:</b> arr[{step['mid']}] = {step['mid_value']}</p>"
        visual_output += f"<p><b>Comparison:</b> Is {step['mid_value']} == {target}? <span style='color: {'green' if step['mid_value'] == target else 'red'}'>{'✅ YES! Found it!' if step['mid_value'] == target else '❌ No'}</span></p>"
        visual_output += "</div>"

    result = f"<h2 style='color: {'green' if found else 'red'}; padding: 10px; text-align: center;'>🎊 Final Result: Target {target} was {'FOUND! ✅' if found else 'NOT FOUND ❌'}</h2>"
    return result, visual_output

# Create the Gradio interface
demo = gr.Interface(
    fn=run_binary_search,
    inputs=[
        gr.Textbox(label="Sorted Array", value="1, 3, 5, 7, 9, 11, 13", placeholder="Enter numbers separated by commas..."),
        gr.Textbox(label="Target Number", value="7", placeholder="Enter the number to find...")
    ],
    outputs=[
        gr.HTML(label="Final Result"),
        gr.HTML(label="Step-by-Step Visualization")
    ],
    title="Binary Search Algorithm Visualizer",
    description="Enter a sorted list of numbers and a target to see how the Binary Search algorithm works step-by-step. The algorithm has O(log n) time complexity."
)

# Launch the app
if __name__ == "__main__":
    demo.launch(share=True)
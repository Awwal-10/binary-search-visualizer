# binary-search-project/app.py

import gradio as gr

def binary_search_steps(arr, target):
    """
    I implemented the binary search algorithm here to demonstrate how it works step by step.
    This function takes a sorted array and target value, then returns each search step for visualization.
    """
    steps = []  # I'll store each step of the search process here to show the user later
    low = 0  # Starting from the first index
    high = len(arr) - 1  # And ending at the last index

    # I keep searching while there's still a valid search space
    while low <= high:
        mid = (low + high) // 2  # I calculate the middle index to check
        # I save the current state to show the user what's happening
        steps.append({
            "low": low,
            "high": high,
            "mid": mid,
            "mid_value": arr[mid]  # The actual value at the middle position
        })
        # Now I check if we found what we're looking for
        if arr[mid] == target:
            return steps, True  # Success! Target found
        # If the target is bigger, I know it must be in the right half
        elif arr[mid] < target:
            low = mid + 1  # So I move the low pointer up
        # If the target is smaller, it must be in the left half
        else:
            high = mid - 1  # So I move the high pointer down
    return steps, False  # If we get here, the target isn't in the array

def run_binary_search(array_input, target_input):
    """
    This function handles the user input from the Gradio interface and processes it.
    I added error checking to make sure the user enters valid data.
    """
    # First, I convert the user's comma-separated string into a list of integers
    try:
        arr = [int(x.strip()) for x in array_input.split(",")]
    except:
        return "Error: Please enter numbers separated by commas (e.g., '1,2,3').", ""

    # I check if the array is empty
    if not arr:
        return "Error: The array cannot be empty.", ""
    # Binary search only works on sorted arrays, so I validate that
    if arr != sorted(arr):
        return "Error: Please enter a sorted array in ascending order.", ""

    # I make sure the target is a valid integer
    try:
        target = int(target_input)
    except:
        return "Error: Please enter a single integer for the target.", ""

    # Now I run my binary search algorithm to get all the steps
    steps, found = binary_search_steps(arr, target)

    # I create a visual representation using HTML to make it easy to understand
    visual_output = ""
    for i, step in enumerate(steps):
        # I create a container for each step with clear visual separation
        visual_output += f"<div style='margin-bottom: 20px; padding: 10px; border: 1px solid #ccc; border-radius: 5px;'>"
        visual_output += f"<h3>🎯 Step {i+1}</h3>"
        
        # I build a visual array where users can see the current pointers
        visual_output += "<div style='display: flex; gap: 5px; margin: 10px 0;'>"
        for idx, value in enumerate(arr):
            # I use different colors to highlight the important indices
            style = "padding: 8px 12px; border: 2px solid; border-radius: 4px; font-weight: bold;"
            if idx == step['mid']:
                style += " background: #4CAF50; color: white; border-color: #45a049;"  # Green for the middle element we're checking
            elif idx == step['low']:
                style += " background: #2196F3; color: white; border-color: #0b7dda;"  # Blue for the low boundary
            elif idx == step['high']:
                style += " background: #ff9800; color: white; border-color: #e68a00;"  # Orange for the high boundary
            else:
                style += " background: #f1f1f1; border-color: #ddd;"  # Gray for other elements
            
            visual_output += f"<div style='{style}'>{value}</div>"
        visual_output += "</div>"
        
        # I add descriptive text to explain what's happening in this step
        visual_output += f"<p><b>Low:</b> index {step['low']} | <b>High:</b> index {step['high']} | <b>Mid:</b> index {step['mid']}</p>"
        visual_output += f"<p><b>Checking:</b> arr[{step['mid']}] = {step['mid_value']}</p>"
        visual_output += f"<p><b>Comparison:</b> Is {step['mid_value']} == {target}? <span style='color: {'green' if step['mid_value'] == target else 'red'}'>{'✅ YES! Found it!' if step['mid_value'] == target else '❌ No'}</span></p>"
        visual_output += "</div>"

    # I create a clear final result message
    result = f"<h2 style='color: {'green' if found else 'red'}; padding: 10px; text-align: center;'>🎊 Final Result: Target {target} was {'FOUND! ✅' if found else 'NOT FOUND ❌'}</h2>"
    return result, visual_output

# I set up the Gradio interface to make it user-friendly
demo = gr.Interface(
    fn=run_binary_search,  # This connects the interface to my function
    inputs=[
        gr.Textbox(label="Sorted Array", value="1, 3, 5, 7, 9, 11, 13", placeholder="Enter numbers separated by commas..."),
        gr.Textbox(label="Target Number", value="7", placeholder="Enter the number to find...")
    ],
    outputs=[
        gr.HTML(label="Final Result"),  # I use HTML for better formatting
        gr.HTML(label="Step-by-Step Visualization")  # And here for the visual steps
    ],
    title="Binary Search Algorithm Visualizer",
    description="Enter a sorted list of numbers and a target to see how the Binary Search algorithm works step-by-step. The algorithm has O(log n) time complexity."
)

# Finally, I launch the application so users can interact with it
if __name__ == "__main__":
    demo.launch(share=True)  # I use share=True to create a public link for easy access

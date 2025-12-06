# Name: Awwal Ahmed
# December 6th 2025

# binary-search-project/app.py

import gradio as gr
import random

def binary_search_steps(arr, target):
    """
    Binary search algorithm that returns each step for visualization.
    Efficient O(log n) algorithm that halves search space each iteration.
    """
    steps = []  # Track algorithm progression
    low = 0
    high = len(arr) - 1
    step_count = 0

    # Continue while search space exists
    while low <= high:
        step_count += 1
        mid = (low + high) // 2  # Divide search space
        
        # Record current state for visualization
        steps.append({
            "low": low,
            "high": high,
            "mid": mid,
            "mid_value": arr[mid],
            "step_count": step_count
        })
        
        # Core algorithm decision
        if arr[mid] == target:
            return steps, True, step_count  # Found target
        elif arr[mid] < target:
            low = mid + 1  # Search right half
        else:
            high = mid - 1  # Search left half
            
    return steps, False, step_count  # Target not found

def generate_sample_array(case_type, size=10):
    """Generate examples to demonstrate different algorithm behaviors."""
    if case_type == "Best Case":
        arr = sorted(random.sample(range(1, 50), size))
        target = arr[len(arr)//2]
        return arr, target, "Best Case: Target in middle (fastest)"
    
    elif case_type == "Average Case":
        arr = sorted(random.sample(range(1, 50), size))
        target = random.choice(arr)
        return arr, target, "Average Case: Target exists in array"
    
    elif case_type == "Worst Case":
        arr = sorted(random.sample(range(1, 50), size))
        target = 99  # Guaranteed not in array
        return arr, target, "Worst Case: Target not found"
    
    else:  # Simple Example
        arr = [2, 5, 8, 12, 16, 23, 38, 45, 67, 89]
        target = 23
        return arr, target, "Simple Example: Easy to follow"

def run_binary_search(quick_case, use_custom, custom_array, custom_target):
    """
    Main function that processes input and generates visualization.
    Handles both sample cases and custom user input.
    """
    if use_custom:
        case_description = "Your Custom Search"
        # Process and validate custom input
        try:
            arr = [int(x.strip()) for x in custom_array.split(",")]
        except:
            return case_description, "Please enter numbers like: 1, 3, 5, 7, 9", ""
        
        # Binary search requires sorted input
        if not arr:
            return case_description, "Array cannot be empty", ""
        if arr != sorted(arr):
            return case_description, "Array must be sorted in ascending order", ""

        try:
            target = int(custom_target)
        except:
            return case_description, "Target must be a single number", ""
    else:
        # Use pre-made educational example
        case_type = quick_case
        arr, target, case_description = generate_sample_array(case_type)

    # Execute binary search
    steps, found, total_steps = binary_search_steps(arr, target)

    # Display search information
    case_info = f"""
    <div style='
        background: linear-gradient(135deg, #1976D2, #42A5F5);
        color: white;
        padding: 20px;
        border-radius: 12px;
        margin-bottom: 25px;
        box-shadow: 0 4px 12px rgba(25, 118, 210, 0.3);
    '>
        <h2 style='margin: 0 0 10px 0; text-align: center;'>🔍 {case_description}</h2>
        <div style='
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 15px;
            margin-top: 15px;
            background: rgba(255,255,255,0.1);
            padding: 15px;
            border-radius: 8px;
        '>
            <div><strong>Array Size:</strong> {len(arr)} numbers</div>
            <div><strong>Target Value:</strong> {target}</div>
            <div><strong>Steps Taken:</strong> {total_steps}</div>
            <div><strong>Time Complexity:</strong> O(log n)</div>
        </div>
    </div>
    """

    # Generate step-by-step visualization
    visual_output = case_info
    
    for i, step in enumerate(steps):
        visual_output += f"""
        <div style='
            margin-bottom: 25px;
            padding: 20px;
            border: 2px solid #E3F2FD;
            border-radius: 12px;
            background: white;
            box-shadow: 0 2px 8px rgba(0,0,0,0.1);
        '>
            <div style='
                display: flex;
                justify-content: space-between;
                align-items: center;
                margin-bottom: 20px;
                padding-bottom: 15px;
                border-bottom: 2px solid #E3F2FD;
            '>
                <h3 style='margin: 0; color: #1976D2; font-size: 20px;'>Step {step['step_count']}</h3>
                <span style='
                    background: #FF5722;
                    color: white;
                    padding: 8px 16px;
                    border-radius: 20px;
                    font-size: 14px;
                    font-weight: bold;
                '>
                    Search Space: {step['high'] - step['low'] + 1} elements
                </span>
            </div>
        """
        
        # Visual array with color coding
        visual_output += "<div style='display: flex; gap: 8px; margin: 20px 0; flex-wrap: wrap; justify-content: center;'>"
        for idx, value in enumerate(arr):
            style = """
                padding: 12px 16px;
                border: 2px solid;
                border-radius: 8px;
                font-weight: bold;
                text-align: center;
                min-width: 50px;
                font-size: 14px;
                box-shadow: 0 2px 4px rgba(0,0,0,0.1);
            """
            
            # Color coding for algorithm visualization
            if idx == step['mid']:
                style += " background: #4CAF50; color: white; border-color: #45a049; transform: scale(1.05);"  # Current element
            elif idx == step['low']:
                style += " background: #2196F3; color: white; border-color: #1976D2;"  # Low boundary
            elif idx == step['high']:
                style += " background: #2196F3; color: white; border-color: #1976D2;"  # High boundary
            elif step['low'] <= idx <= step['high']:
                style += " background: #E3F2FD; border-color: #90CAF9; color: #1976D2;"  # Active search area
            else:
                style += " background: #F5F5F5; border-color: #E0E0E0; color: #9E9E9E;"  # Eliminated elements
            
            visual_output += f"<div style='{style}'>{value}</div>"
        visual_output += "</div>"
        
        # Step explanation
        visual_output += f"""
        <div style='
            background: #F3F8FF;
            padding: 18px;
            border-radius: 10px;
            margin: 20px 0;
            border-left: 4px solid #2196F3;
        '>
            <div style='display: grid; gap: 12px;'>
                <div><strong>Low Pointer:</strong> index {step['low']} (value: {arr[step['low']]})</div>
                <div><strong>High Pointer:</strong> index {step['high']} (value: {arr[step['high']]})</div>
                <div><strong>Checking:</strong> index {step['mid']} = {step['mid_value']}</div>
                <div><strong>Comparison:</strong> Is {step['mid_value']} = {target}?</div>
            </div>
        </div>
        
        <div style='
            background: {'#E8F5E8' if step['mid_value'] == target else '#FFF8E1'}; 
            padding: 16px;
            border-radius: 8px;
            text-align: center;
            border: 2px solid {'#4CAF50' if step['mid_value'] == target else '#FFA000'};
            margin: 15px 0;
        '>
            <strong style='color: {'#2E7D32' if step['mid_value'] == target else '#E65100'}; font-size: 16px;'>
        """
        
        if step['mid_value'] == target:
            visual_output += "🎯 Target found!"
        elif step['mid_value'] < target:
            visual_output += f"➡️ Target > {step['mid_value']} → Search RIGHT half"
        else:
            visual_output += f"⬅️ Target < {step['mid_value']} → Search LEFT half"
            
        visual_output += "</strong></div></div>"

    # Final result display
    if found:
        result = f"""
        <div style='
            background: linear-gradient(135deg, #4CAF50, #66BB6A);
            color: white;
            padding: 30px;
            border-radius: 15px;
            text-align: center;
            margin: 25px 0;
        '>
            <h2 style='margin: 0 0 15px 0; font-size: 28px;'>🎉 Target Found</h2>
            <p style='margin: 0; font-size: 20px;'>Found {target} in {total_steps} steps</p>
        </div>
        """
    else:
        result = f"""
        <div style='
            background: linear-gradient(135deg, #F44336, #EF5350);
            color: white;
            padding: 30px;
            border-radius: 15px;
            text-align: center;
            margin: 25px 0;
        '>
            <h2 style='margin: 0 0 15px 0; font-size: 28px;'>🔍 Target Not Found</h2>
            <p style='margin: 0; font-size: 20px;'>{target} not in array</p>
        </div>
        """
    
    return case_description, result, visual_output

# Gradio interface
with gr.Blocks() as demo:
    
    gr.Markdown("""
    <div style='
        background: linear-gradient(135deg, #1976D2, #42A5F5);
        color: white;
        padding: 40px 20px;
        border-radius: 0 0 20px 20px;
        text-align: center;
        margin-bottom: 30px;
    '>
        <h1 style='margin: 0 0 10px 0; font-size: 2.5em;'>Binary Search Visualizer</h1>
        <p style='margin: 0; font-size: 1.2em;'>Visualize the O(log n) search algorithm</p>
    </div>
    """)
    
    with gr.Row():
        with gr.Column(scale=1):
            gr.Markdown("### 🚀 Quick Start")
            quick_case = gr.Radio(
                choices=["Simple Example", "Best Case", "Average Case", "Worst Case"],
                value="Simple Example",
                label="Select example:"
            )
            
            gr.Markdown("### 🎯 Custom Search")
            use_custom = gr.Checkbox(
                label="Use my own numbers",
                value=False
            )
            
            custom_array = gr.Textbox(
                label="Sorted Numbers",
                placeholder="e.g., 1, 3, 5, 7, 9, 11, 13",
                visible=False
            )
            
            custom_target = gr.Textbox(
                label="Target Number",
                placeholder="e.g., 7",
                visible=False
            )
            
            search_btn = gr.Button("Run Binary Search", variant="primary")
            
            gr.Markdown("""
            ### 💡 How to Use
            1. Select example OR check "Use my own numbers"
            2. Enter sorted numbers (comma-separated)
            3. Click Run to see algorithm steps
            """)
        
        with gr.Column(scale=2):
            case_info = gr.Textbox(label="Search Details", interactive=False)
            result_output = gr.HTML(label="Result")
            visual_output = gr.HTML(label="Step-by-Step Visualization")
    
    # Show/hide custom inputs
    def toggle_custom_inputs(use_custom):
        if use_custom:
            return gr.update(visible=True), gr.update(visible=True)
        else:
            return gr.update(visible=False), gr.update(visible=False)
    
    use_custom.change(toggle_custom_inputs, inputs=use_custom, outputs=[custom_array, custom_target])
    
    # Connect search button
    search_btn.click(
        fn=run_binary_search,
        inputs=[quick_case, use_custom, custom_array, custom_target],
        outputs=[case_info, result_output, visual_output]
    )

# Launch app
if __name__ == "__main__":
    demo.launch(share=True)

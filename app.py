import gradio as gr
        
def calculator(x,y,operation):
    if operation == "Addition":
        return x + y
    elif operation == "Subtraction":
        return x - y
    elif operation == "Division":
        return x/y
    elif operation == "Multiplication":
        return x * y
        
    
app = gr.Interface(calculator,
                   inputs = [gr.Number(label = "First Number"),
                             gr.Number(label = "Second Number"),
                             gr.Radio(["Addition","Subtraction","Division","Multiplication"],label = "Choose Operation")], 
                   theme = gr.themes.Soft(),
                   analytics_enabled=True,
                   outputs = gr.Number(label = "Calculation Result"), 
                   title = "Calculator")

app.launch()
                                
                  

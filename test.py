import tkinter as tk

def evaluate_expression(expression):
    try:
        result = str(eval(expression))
        entry_var.set(result)
        return result
    except Exception as e:
        entry_var.set("Error")
        return str(e)

def on_button_click(value):
    current_text = entry_var.get()
    if value == "=":
        evaluate_expression(current_text)
    elif value == "C":
        entry_var.set("")
    else:
        entry_var.set(current_text + str(value))

# Create main window
root = tk.Tk()
root.title("Simple Calculator")

# Entry widget for displaying and entering the expression
entry_var = tk.StringVar()
entry = tk.Entry(root, textvariable=entry_var, font=('Arial', 14), justify='right')
entry.grid(row=0, column=0, columnspan=4)

# Buttons
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+',
    'C'
]

row_val = 1
col_val = 0

for button in buttons:
    tk.Button(root, text=button, padx=20, pady=20, font=('Arial', 14),
              command=lambda b=button: on_button_click(b)).grid(row=row_val, column=col_val)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

# Run the Tkinter main loop
root.mainloop()

# gui_calculator.py

import tkinter as tk
from operations import add, subtract, multiply, divide
from logger import log_operation

def calculate():
    try:
        a = float(entry1.get())
        b = float(entry2.get())
        op = operator_var.get()

        if op == '+':
            result = add(a, b)
        elif op == '-':
            result = subtract(a, b)
        elif op == '*':
            result = multiply(a, b)
        elif op == '/':
            result = divide(a, b)
        else:
            result_label.config(text="Invalid operator")
            return

        result_label.config(text=f"Result: {result}")
        log_operation(op, a, b, result)

    except ValueError as ve:
        result_label.config(text=f"Error: {ve}")

# GUI Setup
root = tk.Tk()
root.title("Simple Calculator")


# Entry fields
tk.Label(root, text="First Number").grid(row=0, column=0)
entry1 = tk.Entry(root)
entry1.grid(row=0, column=1)

tk.Label(root, text="Second Number").grid(row=1, column=0)
entry2 = tk.Entry(root)
entry2.grid(row=1, column=1)

# Operator selection
tk.Label(root, text="Operation").grid(row=2, column=0)
operator_var = tk.StringVar(root)
operator_var.set('+')  # default value
operators = tk.OptionMenu(root, operator_var, '+', '-', '*', '/')
operators.grid(row=2, column=1)

# Calculate button
calculate_btn = tk.Button(root, text="Calculate", command=calculate)
calculate_btn.grid(row=3, column=0, columnspan=2)

# Result label
result_label = tk.Label(root, text="Result: ")
result_label.grid(row=4, column=0, columnspan=2)

root.mainloop()

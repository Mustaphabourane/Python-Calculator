import tkinter as tk
import math

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")
        
        self.entry = tk.Entry(root, width=30, font=("Arial", 12))
        self.entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10, ipady=10)
        
        buttons = [
            ("7", "#E0E0E0"), ("8", "#E0E0E0"), ("9", "#E0E0E0"), ("/", "#FF9800"),
            ("4", "#E0E0E0"), ("5", "#E0E0E0"), ("6", "#E0E0E0"), ("*", "#FF9800"),
            ("1", "#E0E0E0"), ("2", "#E0E0E0"), ("3", "#E0E0E0"), ("-", "#FF9800"),
            ("0", "#E0E0E0"), (".", "#E0E0E0"), ("=", "#FF9800"), ("+", "#FF9800")
        ]
        
        row = 1
        col = 0
        
        for button in buttons:
            tk.Button(root, text=button[0], width=5, height=2, bg=button[1], fg="#000000", font=("Arial", 12, "bold"),
                      command=lambda button=button[0]: self.button_click(button)).grid(row=row, column=col, padx=5, pady=5)
            col += 1
            if col > 3:
                col = 0
                row += 1
    
    def button_click(self, button):
        current = self.entry.get()
        
        if button == "=":
            try:
                result = eval(current)
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, str(result))
            except:
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, "Error")
        else:
            self.entry.insert(tk.END, button)

root = tk.Tk()
calculator = Calculator(root)
root.mainloop()
import pandas as pd
import tkinter as tk
from tkinter import filedialog, Label, Entry, Button, Text, Scrollbar

def browse_file():
    global excel_file
    excel_file = filedialog.askopenfilename(filetypes=[("Excel Files", "*.xlsx")])
    file_label.config(text=excel_file)

def filter_data():
    filter_column = column_entry.get()
    filter_value = value_entry.get()
    
    df = pd.read_excel(excel_file)
    filtered_df = df[df[filter_column] == filter_value]

    output_text.delete(1.0, tk.END)  # Clear previous output
    output_text.insert(tk.END, "Available Columns:\n")
    output_text.insert(tk.END, str(df.columns.to_list()))  # Convert columns to a string list
    output_text.insert(tk.END, "\n\nFiltered Data:\n")
    output_text.insert(tk.END, filtered_df.to_string(index=False))

window = tk.Tk()
window.title("Exel sheet filter by hrishi")

browse_button = Button(window, text="select Excel File", command=browse_file)
file_label = Label(window, text="select something")
column_label = Label(window, text="Enter the column name:")
column_entry = Entry(window)
value_label = Label(window, text="Enter the value to filter by:")
value_entry = Entry(window)
filter_button = Button(window, text="Filter Data", command=filter_data)
output_text = Text(window, height=40, width=190)
output_scrollbar = Scrollbar(window, command=output_text.yview)
output_text.config(yscrollcommand=output_scrollbar.set)

browse_button.pack(pady=5)
file_label.pack()
column_label.pack(pady=5)
column_entry.pack()
value_label.pack(pady=5)
value_entry.pack()
filter_button.pack(pady=5)
output_text.pack(pady=10)
output_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# Start the GUI main loop
window.mainloop()

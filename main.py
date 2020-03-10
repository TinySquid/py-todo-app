import tkinter as tk
import webbrowser as browser

# My todoItem module
from todoItem import TodoItem

# Open browser and navigate to source repo
def browse_to_repo(e):
    browser.open("https://github.com/TinySquid/py-todo-app", new=2)


# Create list to hold todo items
todos = {}


def add_todo():
    # Add new todo item
    todos[len(todos.keys())] = TodoItem(todo_list_frame, new_todo_title_input.get())
    # Clear Entry box text
    new_todo_title_input.delete(0, tk.END)


# Create main window & set title
main_window = tk.Tk()
main_window.title("Todo App")

# Create attribution label & setup onClick functionality
owner_label = tk.Label(main_window, text="Written in Python by Michael Nunes")
owner_label.pack(side=tk.BOTTOM)
owner_label.bind("<Button-1>", browse_to_repo)

# Create UI frames for todo items and controls
todo_list_frame = tk.Frame(main_window)
new_todo_frame = tk.Frame(main_window)
controls_frame = tk.Frame(main_window)

# Add frames to UI
todo_list_frame.pack()
new_todo_frame.pack()
controls_frame.pack(side=tk.BOTTOM)

# Create dummy todo items
todo_a = TodoItem(todo_list_frame, "Make dinner")
todo_b = TodoItem(todo_list_frame, "Take out the trash")
todo_c = TodoItem(todo_list_frame, "Code...")

# Append to list
todos.update({1: todo_a, 2: todo_b, 3: todo_c})

new_todo_title_input = tk.Entry(new_todo_frame, width=40)
new_todo_title_input.pack(side=tk.LEFT)

add_todo_btn = tk.Button(new_todo_frame, text="(+)", width=10, command=add_todo)
add_todo_btn.pack(side=tk.RIGHT)

# Setup clear button
clear_btn = tk.Button(controls_frame, text="Clear Completed", width=50, command=None)
clear_btn.pack(side=tk.BOTTOM)

# Enter GUI loop
main_window.mainloop()


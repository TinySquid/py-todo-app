import tkinter as tk
import webbrowser as browser


# Open browser and navigate to source repo
def browse_to_repo(e):
    browser.open("https://github.com/TinySquid/py-todo-app", new=2)


# Create main window & set title
main_window = tk.Tk()
main_window.title("Todo App")

# Create attribution label & setup onClick functionality
owner_label = tk.Label(main_window, text="Created in Python 3.8 by Michael Nunes")
owner_label.pack(side=tk.BOTTOM)
owner_label.bind("<Button-1>", browse_to_repo)

# Create UI frames for todo items and controls
todo_list_frame = tk.Frame(main_window)
controls_frame = tk.Frame(main_window)

# Add frames to UI
todo_list_frame.pack()
controls_frame.pack(side=tk.BOTTOM)


# Setup clear button
clear_btn = tk.Button(controls_frame, text="Clear Completed", width=50, command=None)
clear_btn.pack(side=tk.BOTTOM)

# Enter GUI loop
main_window.mainloop()


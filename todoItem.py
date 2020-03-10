import tkinter as tk


class TodoItem:
    def __init__(self, master, title):
        self.title = title
        self.check_state = tk.IntVar()
        self.widget = tk.Checkbutton(
            master,
            text=title,
            variable=self.check_state,
            command=self.toggle,
            width=50,
        )
        self.widget.pack()

    # https://stackoverflow.com/a/25244576 for strike example
    def toggle(self):
        # Set strikethrough or clear it depending on checkbox state
        if self.check_state.get() == 0:
            self.widget.configure(text=self.title)
        else:
            strike_text = ""

            for char in self.title:
                strike_text = strike_text + char + "\u0336"
            # Update text
            self.widget.configure(text=strike_text)
        # Update GUI item
        self.widget.update()

    def get_state(self):
        return self.check_state.get()

    def destroy(self):
        self.widget.destroy()

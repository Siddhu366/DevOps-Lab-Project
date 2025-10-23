# src/lotto_game/gui.py
import tkinter as tk
from tkinter import messagebox, simpledialog
from lotto_game.core import draw_lotto, save_history, load_history
import os

HISTORY_PATH = "lotto_history.json"

class LottoApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Lotto Style Game")
        self.geometry("360x300")
        self.history = []
        if os.path.exists(HISTORY_PATH):
            try:
                self.history = load_history(HISTORY_PATH)
            except Exception:
                self.history = []

        self.create_widgets()

    def create_widgets(self):
        frm = tk.Frame(self)
        frm.pack(pady=10)

        tk.Label(frm, text="Pick count:").grid(row=0, column=0, sticky="e")
        self.pick_spin = tk.Spinbox(frm, from_=1, to=10, width=5)
        self.pick_spin.delete(0, "end")
        self.pick_spin.insert(0, "6")
        self.pick_spin.grid(row=0, column=1)

        tk.Button(self, text="Draw", command=self.on_draw).pack(pady=10)

        tk.Label(self, text="Result:").pack()
        self.result_var = tk.StringVar(value="")
        tk.Label(self, textvariable=self.result_var, font=("Helvetica", 14)).pack(pady=5)

        tk.Button(self, text="Show History", command=self.show_history).pack(pady=5)

    def on_draw(self):
        try:
            pick_count = int(self.pick_spin.get())
            nums = draw_lotto(49, pick_count)
            self.result_var.set(", ".join(map(str, nums)))
            self.history.insert(0, nums)
            save_history(HISTORY_PATH, self.history[:50])  # keep last 50
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def show_history(self):
        htext = "\n".join(", ".join(map(str, h)) for h in self.history[:10])
        messagebox.showinfo("History (last 10)", htext or "No history yet.")

def run():
    app = LottoApp()
    app.mainloop()

if __name__ == "__main__":
    run()

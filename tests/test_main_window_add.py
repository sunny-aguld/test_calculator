import tkinter as tk
from GUI.main_window import calculate_add

def test_calculate_add():
    root = tk.Tk()
    root.withdraw()

    entry_input1 = tk.Entry(root)
    entry_input2 = tk.Entry(root)
    entry_result = tk.Entry(root)

    entry_input1.insert(0, "3")
    entry_input2.insert(0, "4")

    calculate_add(entry_input1, entry_input2, entry_result)

    assert entry_result.get() == "7.0"

    root.destroy()

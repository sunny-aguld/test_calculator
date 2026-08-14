import tkinter as tk
from APP.add import add
def create_main_window()-> tk.Tk:
    # -----------------------------------------------------
    # メインウィンドウ
    # -----------------------------------------------------
    root = tk.Tk()
    root.title("計算機")
    root.geometry("500x250")
    
    # -----------------------------------------------------
    # 全体をまとめるFrame
    # -----------------------------------------------------
    frame_main = tk.Frame(root)
    frame_main.pack(padx=20, pady=20)
    
    # -----------------------------------------------------
    # 入力1
    # -----------------------------------------------------
    label_input1 = tk.Label(frame_main, text="入力1:")
    label_input1.grid(row=0, column=0, padx=5, pady=10)
    entry_input1 = tk.Entry(frame_main, width=10)
    entry_input1.grid(row=0, column=1, padx=5, pady=10)
    
    # -----------------------------------------------------
    # 入力2 
    # -----------------------------------------------------
    label_input2 = tk.Label(frame_main, text="入力2:")
    label_input2.grid(row=0, column=2, padx=5, pady=10)
    entry_input2 = tk.Entry(frame_main, width=10)
    entry_input2.grid(row=0, column=3, padx=5, pady=10)

    # -----------------------------------------------------
    # 計算結果
    # -----------------------------------------------------
    label_result = tk.Label(frame_main, text="計算結果:")
    label_result.grid(row=1, column=2, padx=5, pady=20)
    entry_result = tk.Entry(frame_main, width=30)
    entry_result.grid(row=1, column=3, padx=5, pady=20)

    # -----------------------------------------------------
    # 計算ボタン
    # -----------------------------------------------------
    button_add = tk.Button(frame_main, text="加算", width=8, command=lambda: calculate_add(entry_input1, entry_input2, entry_result))
    button_add.grid(row=2, column=0, padx=5, pady=10)
    
    button_subtract = tk.Button(frame_main, text="減算", width=8)
    button_subtract.grid(row=2, column=1, padx=5, pady=10)
    
    button_mul = tk.Button(frame_main, text="乗算", width=8)
    button_mul.grid(row=2, column=2, padx=5, pady=10)
    
    button_dev = tk.Button(frame_main, text="除算", width=8)
    button_dev.grid(row=2, column=3, padx=5, pady=10)

    return root

def calculate_add(entry_input1, entry_input2, entry_result):
    result = add(float(entry_input1.get()), float(entry_input2.get()))
    update_result(entry_result, result)

def update_result(entry_widget, result):
    entry_widget.delete(0, tk.END)
    entry_widget.insert(0, str(result))

def start():
    app = create_main_window()
    app.mainloop()

from GUI.main_window import create_main_window

def test_create_app_returns_tk_root():
    """
    create_main_window()がTk()のインスタンスを返すことを確認する
    remarks:
      Tk()を作ったら最後にdestroy()する
      そうしないとテスト後にリソースが残ることがある
    """
    app = create_main_window()
    try:
        assert app is not None
        assert app.winfo_exists() == 1
        assert app.title() == "計算機"
    finally:
        app.destroy()

from unittest.mock import MagicMock, patch

from GUI.main_window import create_main_window

def test_create_app_returns_tk_root():
    """
    create_main_window()がTk()のインスタンスを返すことを確認する
    remarks:
      Tk()を作ったら最後にdestroy()する
      そうしないとテスト後にリソースが残ることがある
    """
    root = MagicMock()
    root.winfo_exists.return_value = 1

    with patch("GUI.main_window.tk.Tk", return_value=root), \
         patch("GUI.main_window.tk.Frame", return_value=MagicMock()), \
         patch("GUI.main_window.tk.Label", return_value=MagicMock()), \
         patch("GUI.main_window.tk.Entry", return_value=MagicMock()), \
         patch("GUI.main_window.tk.Button", return_value=MagicMock()):
        app = create_main_window()

    assert app is root
    assert app.winfo_exists() == 1
    root.title.assert_called_once_with("計算機")

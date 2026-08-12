from unittest.mock import MagicMock, patch
from GUI import main_window

def test_start_calls_mainloop():
    """
    start() が create_app() を呼ぶ
    返ってきた app に対して mainloop() を実行する
    →「GUI起動処理の最後まで到達している」と確認している

    remarks:
      本当に mainloop() を回すとテストが止まるので、create_app() が返すオブジェクトをモック
    """
    mock_app = MagicMock()

    with patch("GUI.main_window.create_main_window", return_value=mock_app):
        main_window.start()

    mock_app.mainloop.assert_called_once()

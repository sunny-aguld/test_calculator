from unittest.mock import patch
import run

def test_main_calls_start():
    """
    run.main()を実行した
    その結果start()が1回呼ばれた
    """
    with patch('run.start') as mock_start:
        run.main()
        mock_start.assert_called_once()

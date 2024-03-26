# test_minimal.py
def test_simple_mock(mocker):
    mock_function = mocker.patch("builtins.print", autospec=True)
    print("Hello, world!")
    mock_function.assert_called_once_with("Hello, world!")

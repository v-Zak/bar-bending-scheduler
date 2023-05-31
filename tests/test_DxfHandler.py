from DxfHandler import DxfHandler

def test_get_text_as_list() -> None:
    """
    Tests the get_text_as_list() function

    """
    test_file_path = "text_test.dxf"
    dxf_handler = DxfHandler()
    results = dxf_handler.get_text_as_list(test_file_path)
    assert results == ["test1", "test2", "test3"]
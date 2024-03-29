from DxfHandler import DxfHandler
from Logger import Logger

def test_get_all_mtext_text() -> None:
    """
    Tests the get_all_mtext_text() function

    """
    test_file_path = "tests/dxf_samples/text_test_3.dxf" #path relative to root 
    logger = Logger()
    dxf_handler = DxfHandler(logger)
    results = dxf_handler.get_all_mtext_text(test_file_path)
    assert results == ['8H16-02\\P4T1 4B1', '8H16-01\\P4T1 4B1', '8H16-02\\P4T1 4B1']
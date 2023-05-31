from DxfHandler import DxfHandler 


if __name__ == "__main__":
    dxf_handler = DxfHandler()
    all_text = dxf_handler.get_all_mtext_text("tests/dxf_samples/text_test_3.dxf")
    print(all_text)
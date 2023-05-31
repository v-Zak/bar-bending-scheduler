from DxfHandler import DxfHandler 


if __name__ == "__main__":
    dxf_handler = DxfHandler()
    all_text = dxf_handler.get_text_as_list("test.dxf")
    print(all_text)
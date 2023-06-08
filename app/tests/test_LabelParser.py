from LabelParser import LabelParser

def test_get_bars() -> None:
    """
    Tests the get_bars() function

    """
    test_input = ['8H16-02\\P4T1 4B1', '8H16-01\\P4T1 4B1', '8H16-02\\P4T1 4B1', '16H20-500', 'aaH20-500', '16h20-500', '16H20500']
    label_parser = LabelParser()
    results = label_parser.get_bars(test_input)
    assert results == [{'bar_mark': '02', 'type': 'H', 'size': 16, 'quantity': 8}, 
                       {'bar_mark': '01', 'type': 'H', 'size': 16, 'quantity': 8}, 
                       {'bar_mark': '02', 'type': 'H', 'size': 16, 'quantity': 8},
                       {'bar_mark': '500', 'type': 'H', 'size': 20, 'quantity': 16}]

def test_filter_strings_with_pattern() -> None:
    """
    Tests the filter_strings_with_pattern() function

    """
    strings = ['8H16-02\\P4T1 4B1', '8H16-01\\P4T1 4B1', '8H16-02\\P4T1 4B1', '16H20-500', 'aaH20-500', '16h20-500', '16H20500']
    pattern =  r'\d+H\d+-\d+'
    label_parser = LabelParser()
    results = label_parser.filter_strings_with_pattern(strings, pattern)
    assert results == ['8H16-02', '8H16-01', '8H16-02', '16H20-500']
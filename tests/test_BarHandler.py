from BarHandler import BarHandler

def test_get_bar_set() -> None:
    """
    Tests the get_bar_set() function

    """
    bars = [{'bar_mark': '02', 'type': 'H', 'size': 16, 'quantity': 8}, 
            {'bar_mark': '01', 'type': 'H', 'size': 16, 'quantity': 8}, 
            {'bar_mark': '02', 'type': 'H', 'size': 16, 'quantity': 8},
            {'bar_mark': '500', 'type': 'H', 'size': 20, 'quantity': 16}]
    bar_handler = BarHandler()
    results = bar_handler.get_bar_set(bars)
    assert results == [ {'bar_mark': '02', 'type': 'H', 'size': 16, 'quantity': [8,8]}, 
                        {'bar_mark': '01', 'type': 'H', 'size': 16, 'quantity': [8]}, 
                        {'bar_mark': '500', 'type': 'H', 'size': 20, 'quantity': [16]}]
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


def test_are_elements_equal() -> None:
    """
    Tests the are_elements_equal() function

    """
    input = [[1,1,1,1,1], [10,10,9,10], ["a", "a", "a"], ["a", "b", "a"]]
    results = []
    bar_handler = BarHandler()
    for bars in input:
        results.append(bar_handler.are_elements_equal(bars))
    assert results == [True, False, True, False]
    

def test_sum_quantities() -> None:
    """
    Tests the sum_quantities() function

    """
    bars = [{'bar_mark': '02', 'type': 'H', 'size': 16, 'quantity': [8, 8]},
            {'bar_mark': '01', 'type': 'H', 'size': 16, 'quantity': [8]},
            {'bar_mark': '500', 'type': 'H', 'size': 20, 'quantity': [16]}]
    bar_handler = BarHandler()
    results = bar_handler.sum_quantities(bars)
    assert results == [ {'bar_mark': '02', 'type': 'H', 'size': 16, 'quantity': [8, 8], 'number_of_members': 2, 'number_of_bars_in_each': 8},
                        {'bar_mark': '01', 'type': 'H', 'size': 16, 'quantity': [8], 'number_of_members': 1, 'number_of_bars_in_each': 8},
                        {'bar_mark': '500', 'type': 'H', 'size':20, 'quantity': [16], 'number_of_members': 1, 'number_of_bars_in_each': 16}]
    



    

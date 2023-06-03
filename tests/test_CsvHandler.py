from CsvHandler import CsvHandler
import csv
import os

def test_dict_list_to_csv() -> None:
    """
    Tests the dict_list_to_csv() & csv_to_dict_list() functions

    """
    # test with no keys
    file_path = "test.csv"
    list_to_csv = [{'bar_mark': '02', 'type': 'H', 'size': 16, 'quantity': [8, 8], 'number_of_members': 2, 'number_of_bars_in_each': 8},
                   {'bar_mark': '01', 'type': 'H', 'size': 16, 'quantity': [8], 'number_of_members': 1, 'number_of_bars_in_each': 8}]
    csv_handler = CsvHandler()
    csv_handler.dict_list_to_csv(list_to_csv, csv_file_path = file_path)

    results = csv_handler.csv_to_dict_list(file_path)    
    assert results == [{'bar_mark': '02', 'type': 'H', 'size': '16', 'quantity': '[8, 8]', 'number_of_members': '2', 'number_of_bars_in_each': '8'},
                   {'bar_mark': '01', 'type': 'H', 'size': '16', 'quantity': '[8]', 'number_of_members': '1', 'number_of_bars_in_each': '8'}]
    
    # test with keys
    keys = ['bar_mark', 'type', 'size', 'number_of_members', 'number_of_bars_in_each']
    csv_handler.dict_list_to_csv(list_to_csv, keys = keys, csv_file_path = file_path)
    results = csv_handler.csv_to_dict_list(file_path)
    
    assert results == [{'bar_mark': '02', 'type': 'H', 'size': '16', 'number_of_members': '2', 'number_of_bars_in_each': '8'},
                   {'bar_mark': '01', 'type': 'H', 'size': '16', 'number_of_members': '1', 'number_of_bars_in_each': '8'}]

    # delete test file
    os.remove(file_path)
    
    
    


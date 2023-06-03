from DxfHandler import DxfHandler 
from LabelParser import LabelParser
from BarHandler import BarHandler
from CsvHandler import CsvHandler

if __name__ == "__main__":

    #dxf_path = input("Enter a DXF File Path (include .dxf): ")
    dxf_path = "tests/dxf_samples/text_test_3.dxf"

    output_path = dxf_path[0:-4] + '-BBS-output.csv'

    print('Reading...')
    dxf_handler = DxfHandler()   
    all_text = dxf_handler.get_all_mtext_text(dxf_path) # get text

    print('Parsing...')
    label_parser = LabelParser()
    bars = label_parser.get_bars(all_text) # get bars as dicts

    print('Creating Bars...')
    bar_handler = BarHandler()
    bars_unique = bar_handler.get_bar_set(bars) # get unique set of bar marks
    bars_summed = bar_handler.sum_quantities(bars_unique) # get the bbs formatted set

    print('Exporting...')
    csv_handler = CsvHandler()
    csv_handler.dict_list_to_csv(bars_summed, keys = ['bar_mark', 'type', 'size', 'number_of_members', 'number_of_bars_in_each'], csv_file_path = output_path)

    print('Done...')
    print(f'File saved to: {output_path}')






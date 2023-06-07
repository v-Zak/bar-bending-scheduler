from DxfHandler import DxfHandler 
from LabelParser import LabelParser
from BarHandler import BarHandler
from CsvHandler import CsvHandler

class BarBendingScheduler:
    """
    A class which handles the creation of a BBS (CSV) based on a given DXF file

    """
    def __init__(self):
        pass
    
    def createBarQuantitiesCsv(self, dxf_path, csv_path = None):
        """
        creates a BBS in CSV format based on a given DXF file

        Parameters
        ----------
        dxf_path : string
            The path to the DXF to read
        csv_path : string
            The path to save the CSV (default is '{dxf_path}-BBS-output.csv')
    
        """
        try:
            if csv_path == None:            
                csv_path = dxf_path[0:-4] + '-BBS-output.csv'

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
            csv_handler.dict_list_to_csv(   list_to_csv = bars_summed, 
                                            keys = [   'bar_mark', 'type', 
                                                    'size', 'number_of_members',
                                                    'number_of_bars_in_each'
                                                ],
                                            csv_file_path = csv_path)

            print('Done...')
            print(f'File saved to: {csv_path}')
        except ValueError as err:
            print(err.args)
